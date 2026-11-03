"""Smooth photo-traced fairways in course.svg (run in the course folder, before surrounds.py).
OSM fairways are kept as mapped. Traced pieces near each hole line are joined across tree shadows
(closing), cleared of blobs (opening), then Chaikin-smoothed, and clipped off greens, tees and bunkers."""
import re, sys, numpy as np
sys.path.insert(0, "/home/claude/moorpark")
import coursekit as ck
import xml.etree.ElementTree as ET
from pyproj import Transformer
from shapely.geometry import Polygon, LineString
from shapely.ops import unary_union
c = ck.load_cfg(); S = int(c["size"])
holes, yv, _ = ck.hole_data(c)
svg = open("course.svg").read()
def polys(label):
    i0 = svg.find('inkscape:label="%s"' % label); blk = svg[i0:svg.find("</g>", i0)]; out = []
    for d in re.findall(r' d="([^"]+)"', blk):
        rings = []
        for sp in re.split(r"(?=M )", d.strip()):
            n = [float(v) for v in re.findall(r"-?\d+\.?\d*", sp)]
            pts = [(n[k], S - n[k + 1]) for k in range(0, len(n) - 1, 2)]
            if len(pts) > 2: rings.append(Polygon(pts).buffer(0))
        if rings:
            rings.sort(key=lambda p: -p.area); g = rings[0]
            for r in rings[1:]: g = g.symmetric_difference(r)
            out.append(g)
    return unary_union(out)
t = Transformer.from_crs("EPSG:4326", "EPSG:%d" % c["epsg"], always_xy=True)
r = ET.parse("map.osm").getroot()
N = {}
for nd in r.iter("node"):
    e, n = t.transform(float(nd.get("lon")), float(nd.get("lat"))); N[nd.get("id")] = (e - c["sw_e"], n - c["sw_n"])
osm_fw = []
for w in r.findall("way"):
    tg = {q.get("k"): q.get("v") for q in w.findall("tag")}
    p = [N[q.get("ref")] for q in w.findall("nd") if q.get("ref") in N]
    if tg.get("golf") == "fairway" and len(p) > 3: osm_fw.append(Polygon(p).buffer(0))
osm_fw = unary_union(osm_fw)
G, T, B, W = polys("Green"), polys("Tee"), polys("Bunker"), polys("Water")
traced = polys("Fairway").difference(osm_fw.buffer(1))
def chaikin(ring, it=3):
    p = np.array(ring.coords)[:-1]
    for _ in range(it):
        q = np.roll(p, -1, 0); p = np.vstack([np.c_[.75 * p + .25 * q], np.c_[.25 * p + .75 * q]]).reshape(-1, 2, order="F") if False else np.ravel(np.stack([.75 * p + .25 * q, .25 * p + .75 * q], 1)).reshape(-1, 2)
    return p
def smooth(poly):
    ext = Polygon(chaikin(poly.exterior, 4))
    for i in poly.interiors:
        if Polygon(i).area > 40: ext = ext.difference(Polygon(chaikin(i)))
    return ext.buffer(0)
out = []
for h in holes:
    line = LineString(np.vstack([h["line"][0]] + h["path"] + [h["green"]]))
    near = traced.intersection(line.buffer(45))
    if near.is_empty: continue
    f = near.buffer(12, join_style=1).buffer(-12, join_style=1)          # bridge tree shadows
    f = f.buffer(-7, join_style=1).buffer(7, join_style=1)              # drop blobs and spurs
    f = f.simplify(2.0)
    parts = [smooth(p) for p in getattr(f, "geoms", [f]) if p.area > 250]
    out += parts
fw = unary_union(out + [osm_fw]).difference(unary_union([G.buffer(0.5), T.buffer(1), B.buffer(0.5), W.buffer(0.5)]))
fw = unary_union([p for p in getattr(fw, "geoms", [fw]) if p.area > 100])
rough = polys("Rough")
rough = unary_union([rough, polys("Fairway")]).difference(fw)     # whatever fairway was dropped becomes rough
print("Fairway %.2f ha (OSM %.2f ha + smoothed trace), was %.2f ha" % (fw.area / 1e4, osm_fw.area / 1e4, polys("Fairway").area / 1e4))
def d_of(p):
    return " ".join("M " + " L ".join("%.3f,%.3f" % (a, S - b) for a, b in list(rg.coords)[:-1]) + " Z" for rg in [p.exterior] + list(p.interiors))
def put(svg, label, geom, pid, col):
    gs = [g.simplify(0.15) for g in getattr(geom, "geoms", [geom]) if g.area > 1]
    paths = "\n".join('<path id="%s_%d" style="fill:%s;fill-opacity:1;fill-rule:evenodd;stroke:none" d="%s"/>' % (pid, n, col, d_of(g)) for n, g in enumerate(gs))
    i0 = svg.find('inkscape:label="%s"' % label); a = svg.find(">", i0) + 1; b = svg.find("</g>", i0)
    return svg[:a] + "\n" + paths + "\n" + svg[b:]
svg = put(svg, "Fairway", fw, "fairway", "#43E561")
svg = put(svg, "Rough", rough.buffer(0), "rough", "#278438")
open("course.svg", "w").write(svg)
