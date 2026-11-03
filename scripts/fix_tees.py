"""Move any tee that sits more than 7 m off its card yardage along the line of play until it matches the card,
and set Tierra's approved course defaults. Run in the course folder after coursekit card."""
import json, csv, sys, numpy as np
sys.path.insert(0, "/home/claude/moorpark")
import coursekit as ck
c = ck.load_cfg(); holes, yv, _ = ck.hole_data(c)
card = ck.read_card("card.csv")
slot = {"Black": "Black", "Blue": "Blue", "White": "White", "Combo": "Green", "Yellow": "Yellow"}
yards = {slot[t["name"]]: t["yards"] for t in card["tees"]}
d = json.load(open("Harding.GKD"))
moved = []
for h in d["Holes"]:
    n = h["HoleNumber"]
    by = {t["TeeType"]: t for t in h["Tees"] if t.get("Position")}
    target = by.get("AimPoint1", by["GreenCenterPoint"])["Position"]
    green = by["GreenCenterPoint"]["Position"]
    for s, ys in yards.items():
        t = by.get(s)
        if not t: continue
        p = np.array([t["Position"]["x"], t["Position"]["z"]])
        a = np.array([target["x"], target["z"]]); g = np.array([green["x"], green["z"]])
        cur = np.hypot(*(a - p)) + (np.hypot(*(g - a)) if "AimPoint1" in by else 0)
        # measured along tee -> aim1 -> (aim2) -> green like coursekit; use the tee's own Distance when present
        cur = t.get("Distance") or cur
        dev = ys[n - 1] * 0.9144 - cur
        if abs(dev) > 7:
            u = (a - p) / np.hypot(*(a - p))
            q = p - u * dev
            t["Position"] = {"x": round(float(q[0]), 3), "y": round(float(yv(q)), 3), "z": round(float(q[1]), 3)}
            t["Distance"] = round(ys[n - 1] * 0.9144, 3)
            moved.append("%d %s %+.0f yds" % (n, s, dev / 0.9144))
d.update({"KeywordMountain": False, "KeywordParkland": True, "KeywordsString": "Parkland,Historic", "KeywordHistoric": True,
          "DefaultStimp": 2, "MaxStimp": 5, "FairwayFirmnessDefault": 0, "GreenFirmnessDefault": 0})   # Tierra's approved values
json.dump(d, open("Harding.GKD", "w"))
print("moved:", ", ".join(moved) or "none")
