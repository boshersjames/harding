"""Harding PC on-surface check (Oct 28): every GKD tee must stand on a Tee mesh and off cart paths.
1. Tees within 3 m of a cart path slide sideways (across the line of play) until clear.
2. Every GKD tee not on a Tee polygon gets a flat 7 x 9 m pad (long side toward the green) in course.svg's Tee layer,
   with a 2 m first cut (fairway pulled back from it). Listed in tee_pads.csv.
3. Terrain under those pads is levelled in heightmap_2049.raw (blended over 3 m) and the GKD tee heights set to match.
4. Trees whose crown x 1.3 reaches a bunker are moved off it (up to 4 m), else dropped (trees.csv, trees_removed_bunkers.csv)."""
import re, csv, json, math, sys, numpy as np
from shapely.geometry import Polygon, Point, LineString
from shapely.ops import unary_union
from shapely import affinity
c = json.load(open("course.json")); S = int(c["size"]); TH = c["terrain_height"]
d = json.load(open("Harding.GKD", encoding="utf-8-sig"))
svg = open("course.svg").read()
def layer(label):
    i0 = svg.find('inkscape:label="%s"' % label); blk = svg[i0:svg.find("</g>", i0)]; out = []
    for dd in re.findall(r' d="([^"]+)"', blk):
        rings = []
        for sp in re.split(r"(?=M )", dd.strip()):
            n = [float(v) for v in re.findall(r"-?\d+\.?\d*", sp)]
            pts = [(n[k], S - n[k + 1]) for k in range(0, len(n) - 1, 2)]
            if len(pts) > 2: rings.append(Polygon(pts).buffer(0))
        if rings:
            rings.sort(key=lambda p: -p.area); g = rings[0]
            for r in rings[1:]: g = g.symmetric_difference(r)
            out.append(g)
    return unary_union(out)
T, B, G, W, FW = layer("Tee"), layer("Bunker"), layer("Green"), layer("Water"), layer("Fairway")
paths = []
for r in csv.DictReader(open("cartpaths.csv")):
    paths.append(r)
# cartpaths.csv: one row per vertex with path id
by = {}
for r in paths:
    k = r["segment"]
    by.setdefault(k, []).append((float(r["x"]), float(r["z"])))
cart = unary_union([LineString(p).buffer(1.2) for p in by.values() if len(p) > 1])
hm = np.fromfile("heightmap_2049.raw", "<u2").reshape(2049, 2049).astype(np.float64) * TH / 65535
cell = S / 2048
def height(x, z):
    i, j = z / cell, x / cell; i0, j0 = int(i), int(j); fi, fj = i - i0, j - j0
    return float(hm[i0, j0] * (1 - fi) * (1 - fj) + hm[i0 + 1, j0] * fi * (1 - fj) + hm[i0, j0 + 1] * (1 - fi) * fj + hm[i0 + 1, j0 + 1] * fi * fj)
COL = ("Black", "Blue", "White", "Green", "Yellow")
log, pads = [], []
for h in d["Holes"]:
    X = {t["TeeType"]: t for t in h["Tees"]}
    gc = X["GreenCenterPoint"]["Position"]
    tgt = X["AimPoint1"]["Position"] if X.get("AimPoint1") and X["AimPoint1"].get("Enabled") and X["AimPoint1"].get("Position") and h["Par"] > 3 else gc
    for name in COL:
        t = X.get(name)
        if not t or not t["Enabled"] or not t["Position"]: continue
        p = t["Position"]; ux, uz = tgt["x"] - p["x"], tgt["z"] - p["z"]; L = math.hypot(ux, uz); ux, uz = ux / L, uz / L
        if cart.buffer(1.8).contains(Point(p["x"], p["z"])):          # 1. off the cart path
            best = None
            for s in np.arange(1, 15.5, 0.5):
                for sg in (1, -1):
                    q = (p["x"] - sg * s * uz, p["z"] + sg * s * ux)
                    if not cart.buffer(4.5).contains(Point(q)) and not B.buffer(2).contains(Point(q)) and not W.contains(Point(q)):
                        best = q; break
                if best: break
            log.append("hole %d %s moved %.1f m sideways off the cart path" % (h["HoleNumber"], name, s))
            p.update(x=round(best[0], 3), z=round(best[1], 3), y=round(height(*best), 3))
        if T.buffer(0.5).contains(Point(p["x"], p["z"])): continue    # 2. already on a mapped tee box
        pad = Polygon([(-4.5, -3.5), (4.5, -3.5), (4.5, 3.5), (-4.5, 3.5)])
        pad = affinity.rotate(pad, math.degrees(math.atan2(uz, ux)), origin=(0, 0))
        pad = affinity.translate(pad, p["x"], p["z"]).difference(cart.buffer(0.5))
        pads.append((h["HoleNumber"], name, p["x"], p["z"], pad))
newT = unary_union([T] + [q[4] for q in pads])
lip = newT.buffer(2).difference(newT)
FW2 = FW.difference(newT.buffer(2))                                  # 2 m first cut of rough round every pad
def d_of(p):
    return " ".join("M " + " L ".join("%.3f,%.3f" % (a, S - b) for a, b in list(rg.coords)[:-1]) + " Z" for rg in [p.exterior] + list(p.interiors))
def put(svg, label, geom, pid, col):
    gs = [g for g in getattr(geom, "geoms", [geom]) if g.area > 1]
    pth = "\n".join('<path id="%s_%d" style="fill:%s;fill-opacity:1;fill-rule:evenodd;stroke:none" d="%s"/>' % (pid, n, col, d_of(g)) for n, g in enumerate(gs))
    i0 = svg.find('inkscape:label="%s"' % label); a = svg.find(">", i0) + 1; b = svg.find("</g>", i0)
    return svg[:a] + "\n" + pth + "\n" + svg[b:]
svg = put(svg, "Tee", newT, "tee", "#A0E5B8")
svg = put(svg, "Fairway", FW2, "fairway", "#43E561")
# rough layer: add back what fairway gave up (the first cut) minus the pads
RO = layer("Rough"); RO = unary_union([RO, FW.difference(FW2)]).difference(newT)
svg = put(svg, "Rough", RO.buffer(0), "rough", "#278438")
open("course.svg", "w").write(svg)
with open("tee_pads.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["hole", "tee", "x", "z"]); w.writerows([(a, b, "%.2f" % x, "%.2f" % z) for a, b, x, z, _ in pads])
# 3. level the terrain under the new pads
zz, xx = np.mgrid[0:2049, 0:2049] * cell
for hole, name, px, pz, pad in pads:
    h = d["Holes"][hole - 1]; X = {t["TeeType"]: t for t in h["Tees"]}; t = X[name]
    gc = X["GreenCenterPoint"]["Position"]; ux, uz = gc["x"] - px, gc["z"] - pz; L = math.hypot(ux, uz); ux, uz = ux / L, uz / L
    r0 = slice(max(0, int((pz - 12) / cell)), int((pz + 12) / cell) + 1); c0 = slice(max(0, int((px - 12) / cell)), int((px + 12) / cell) + 1)
    a = (xx[r0, c0] - px) * ux + (zz[r0, c0] - pz) * uz; b = -(xx[r0, c0] - px) * uz + (zz[r0, c0] - pz) * ux
    out = np.sqrt(np.maximum(np.abs(a) - 4.5, 0) ** 2 + np.maximum(np.abs(b) - 3.5, 0) ** 2)
    sub = hm[r0, c0]; level = float(sub[out == 0].mean()); wgt = np.clip(1 - out / 3.0, 0, 1)
    hm[r0, c0] = sub * (1 - wgt) + level * wgt
    t["Position"]["y"] = round(level, 3)
np.round(np.clip(hm / TH, 0, 1) * 65535).astype("<u2").tofile("heightmap_2049.raw")
# keep tee distances honest after the cart-path moves
for h in d["Holes"]:
    X = {t["TeeType"]: t for t in h["Tees"]}; gc = X["GreenCenterPoint"]["Position"]
    aims = [X[a]["Position"] for a in ("AimPoint1", "AimPoint2") if X.get(a) and X[a].get("Enabled") and X[a].get("Position")] if h["Par"] > 3 else []
    for name in COL:
        t = X.get(name)
        if t and t["Enabled"] and t["Position"]:
            pts = [t["Position"]] + aims + [gc]
            t["Distance"] = round(sum(math.hypot(p["x"] - q["x"], p["z"] - q["z"]) for p, q in zip(pts, pts[1:])), 3)
json.dump(d, open("Harding.GKD", "w", encoding="utf-8"), indent=1)
# 4. trees off the bunkers (rendered crowns come out ~1.3x the LiDAR radius)
keep, gone, moved = [], [], 0
rows = list(csv.DictReader(open("trees.csv")))
for r in rows:
    x, z, cr = float(r["x"]), float(r["z"]), float(r["crown_radius_m"]) * 1.3
    dist = B.distance(Point(x, z)) if not B.contains(Point(x, z)) else 0
    if dist >= cr: keep.append(r); continue
    if dist > 0:
        nearest = B.boundary.interpolate(B.boundary.project(Point(x, z)))
        vx, vz = x - nearest.x, z - nearest.y; L = math.hypot(vx, vz)
        need = cr - dist
        q = (x + vx / L * need, z + vz / L * need)
        if need <= 4 and not (G.buffer(2).contains(Point(q)) or newT.buffer(1).contains(Point(q)) or cart.contains(Point(q)) or B.distance(Point(q)) < cr - 0.05):
            r = dict(r, x="%.2f" % q[0], z="%.2f" % q[1], y="%.2f" % (height(*q) - 0)); keep.append(r); moved += 1; continue
    gone.append(r)
with open("trees.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(keep)
with open("trees_removed_bunkers.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(gone)
print("\n".join(log))
print("%d tee pads added (7 x 9 m, levelled): %s" % (len(pads), ", ".join("%d %s" % (a, b) for a, b, *_ in pads)))
print("trees: %d moved off bunkers, %d removed (crown x1.3 over sand), %d kept" % (moved, len(gone), len(keep)))
