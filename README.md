# Harding Golf Course, Griffith Park (Los Angeles)

4730 Crystal Springs Dr, Los Angeles, CA 90027. City of LA municipal course, opened 1923 (credited to William H. Johnson, William P. Bell, George C. Thomas Jr. and Willie Watson). Par 72, 6,714 yds from the Black tees. Shares Griffith Park with Wilson.
Sources: golfpass.com course 183 (Harding at Griffith Park), courses.opengolfapi.org. Yardages and handicaps confirmed against the club scorecard BoJa sent (2026-10-28); `card.csv` holds it.

## Tees
| Tee | Yards | Rating/Slope (M) | Rating/Slope (W) |
|---|---|---|---|
| Black | 6,714 | 71.4/121 | 78.1/134 |
| Blue | 6,423 | 70.0/118 | 76.4/130 |
| White | 6,168 | 68.7/115 | 75.0/126 |
| White/Yellow combo | 5,811 | 67.0/111 | n/a (golfpass repeats Yellow's) |
| Yellow | 4,946 | 63.0/101 | 68.2/113 |

## Hole by hole
| Hole | Par | M HCP | W HCP | Black | Blue | White | Combo |
|---|---|---|---|---|---|---|---|
| 1 | 4 | 5 | 9 | 430 | 417 | 404 | 333 |
| 2 | 4 | 17 | 15 | 346 | 333 | 314 | 314 |
| 3 | 4 | 1 | 3 | 405 | 395 | 386 | 386 |
| 4 | 4 | 11 | 13 | 330 | 320 | 310 | 310 |
| 5 | 3 | 13 | 17 | 185 | 174 | 162 | 162 |
| 6 | 5 | 15 | 1 | 555 | 543 | 531 | 415 |
| 7 | 5 | 9 | 5 | 498 | 471 | 449 | 449 |
| 8 | 4 | 7 | 7 | 399 | 371 | 360 | 298 |
| 9 | 4 | 3 | 11 | 427 | 414 | 403 | 403 |
| Out | 37 | | | 3,575 | 3,438 | 3,319 | 3,070 |
| 10 | 4 | 8 | 4 | 360 | 351 | 343 | 343 |
| 11 | 4 | 2 | 2 | 401 | 391 | 381 | 338 |
| 12 | 4 | 12 | 10 | 388 | 366 | 347 | 347 |
| 13 | 3 | 4 | 14 | 201 | 183 | 172 | 134 |
| 14 | 4 | 18 | 12 | 374 | 353 | 337 | 337 |
| 15 | 3 | 10 | 18 | 179 | 168 | 154 | 154 |
| 16 | 4 | 6 | 8 | 377 | 359 | 348 | 348 |
| 17 | 4 | 16 | 16 | 363 | 335 | 300 | 300 |
| 18 | 5 | 14 | 6 | 496 | 479 | 467 | 440 |
| In | 35 | | | 3,139 | 2,985 | 2,849 | 2,741 |
| Total | 72 | | | 6,714 | 6,423 | 6,168 | 5,811 |

Yellow (club card): 333 262 295 249 119 415 360 298 233 / 271 338 287 134 269 135 276 232 440 = 2,564 + 2,382 = 4,946. Women's par on 9 is 5 (women's par 73). The club card has no Combo row; Combo comes from golfpass.
Possible GSPro slots (same idea as Wilson/Tierra): Black→Black, Blue→Blue, White→White, Combo→Green, Yellow→Yellow.

## Map data
OSM (Overture 2026-09-23.0) has a `Harding Golf Course` golf_course polygon (lon -118.28905 to -118.27889, lat 34.13591 to 34.14792, centroid 34.14312, -118.28299) and the `Harding Golf Course Driving Range` to the west. Griffith Park has ~61 tees, 40 greens, 35 fairways, 47 bunkers and 4 water hazards mapped across both courses.

## Shared Griffith Park frame (Wilson + Harding)
- 2000 m square, centre 34.1405, -118.28425. EPSG:6340 SW corner 380594.21 E, 3777479.33 N. Unity x = m east, z = m north.
- Every mapped golf feature of both courses is at least 172 m inside the square.

## LiDAR
EPT index lists two surveys over the course, and both really have points there (checked in the EPT hierarchy, unlike Tierra's false positives):
- **CA_LosAngeles_1_B23** (QL1, flown 2023-24): used.
- USGS_LPC_CA_LosAngeles_2016_LAS_2018 (QL2): fallback / comparison.

## Build status (2026-10-28)
Shared frame data in `../griffith-park/` (heightmap, points, OSM, satellite.jpg, scripts). Here:
- `map.osm`: Harding-only golf features (18 holes, 23 tees, 18 greens, 22 bunkers, 3 water hazards, 26 cart paths).
- `holes.csv`, `tees.csv`: OSM hole lines measure within a few yards of the Black card on almost every hole.
- `Harding.GKD` (draft, Moorpark GKD as template): Black, Blue, White, Combo->Green, Yellow; greens, aim points at the widest fairway on 15 holes, 4 pins per green; altitude 445 ft, Parkland.
  OB draft: pOOB 396 points around the Harding boundary, 3 interior OB patches, 3 water hazards; every tee, aim point and pin checked in bounds.
  Forward tees with no mapped box were put on the hole line at the card yardage (mostly Yellow, plus White/Combo on 8, 12, 13, 15, 17). Pin real spots in `tee_pins.csv` (hole,label,lat,lon) if needed.
  Card vs mapped box mismatches to check: 16 Black (card 377, box 361), 14 White/Combo (337 vs 354), 18 Combo/Yellow (440 vs 462), 8 Blue (371 vs 385), 12 Blue (366 vs 380).
- Vegetation run with the new `--parkland` flag (coursekit): the whole mapped course is turf, because Harding's rough runs under trees between holes and the default SoCal canyon rules painted it as scrub. Scrub/golden grass only on the natural park hillsides outside the course. `terrain_masks/`, `shrubs_clean.csv` (88 LiDAR + 303 edge shrubs).
- `trees.csv`: 1,256 LiDAR trees (satellite green-share filter on). Mostly pines, eucalyptus, sycamores and oaks on the photo; check the flyover.
- `course.svg`: Rough 43.4 ha, Fairway 10.5 ha (3.2 ha from OSM, rest traced from the photo: check in Inkscape), Tee, Green, Bunker, Water from OSM. Preview `course_svg_preview.png`.
- Wilson (next door) is not in Harding's meshes; it shows as satellite-textured terrain in this scene.

## Flyover video
https://youtu.be/l-k2b8OmybI (from BoJa). Skip the city views at the start; hole 1 tee is at about 0:42. Use for tree species, bunker shapes, OB fences and landmarks.

## Bunkers and green surrounds (Tierra play-test lessons, Oct 28)
Applied with `../surrounds.py` (from Penmar, plus an uphill-bank rule):
- No fairway or rough polygon overlaps sand (0 m2), so the Bunker mesh is the only surface there: no fairway physics in the sand.
- 2 m first-cut rough lip around every bunker.
- Fairway-height collar around every green (3 m sides, about 5 m at the back) so balls just off the green roll out. Where the ground rises more than 0.6 m above the green within 6 m (uphill banks) the collar is left as rough: 411 m2 dropped.
- `bunkers.csv`: 22 bunkers with the Tierra BunkerDepth profile: depth 0.25 m under 60 m2, 0.35 m for 60-150 m2, 0.5 m above; flat floor (< 3 deg), face 25-30 deg toward the green (face_toward_x/z), entry < 12 deg.
- In Unity: every Bunker mesh must get the sand physics material (check in the collider sweep that none reports fairway).
- Vegetation re-run with both courses in map.osm (`--parkland`), so Wilson's holes are turf in Harding's scene, and with the LA River no longer treated as water.

## Fairways smoothed (Oct 28, after BoJa's Inkscape check)
The photo trace was blotchy. `../smooth_fairways.py` keeps the 3.1 ha of OSM fairways as mapped and, per hole, joins the traced pieces across tree shadows (12 m closing), drops blobs (7 m opening) and Chaikin-smooths the edges, then clips off greens, tees, bunkers and water. Dropped bits become rough. Then `../surrounds.py` re-adds collars and bunker lips. Fairway 11.3 ha with collars. Layer preview `course_svg_layers.png`.
Rebuild order: `coursekit.py svg` -> `smooth_fairways.py` -> `surrounds.py` -> `coursekit.py card ... --ob`.

## Checked against BOJA_FEEDBACK_CHECKLIST.md (Oct 28)
Data-side items done (rebuild order: svg -> smooth_fairways.py -> surrounds.py -> coursekit card --ob -> fix_tees.py -> apply_checklist_harding.py):
- Tees: card mismatches moved along the line (8 Blue -14, 12 Blue -14, 14 White/Combo -17, 16 Black +16 (back), 18 Combo/Yellow -22 yds).
  Combo shares the White or Yellow box on every hole, so the later colour sits 3.5 m to the side (never stacked). All tees in bounds.
- Par 3s (5, 13, 15) aim at the green centre.
- OB: dropped 2 bogus interior OB slivers (a tree by a path on 9/10, a gap between trees by 18). Kept one 1.5 ha interior OB on the wooded knoll between 1, 17 and 18 as a draft: **ask BoJa if the knoll is OB or play-it-as-it-lies.** No drop zones.
- GKD: Parkland + Historic (Mountain off), Tierra's stimp/firmness defaults, name "Harding - Griffith Park", designer George C. Thomas Jr. and William P. Bell (1923), altitude 445 ft.
- Trees line up with the satellite crowns (checked on the overlay).
- Green slopes (`green_slopes.csv`, fitted plane / 90th pct local): flagged for review 4, 5, 8, 9, 11, 12, 13, 15, 16, 17, 18. Steepest: 11 (5.4 % overall, 13.5 % local, probably a bank in the outline), 5 (4.5 %), 13 (3.6 %). Harding's old greens do tilt back to front, so check these in Unity rather than flatten blindly.
Still Unity-side (PC): sand physics on every bunker + BunkerDepth from bunkers.csv, tree LOD/billboards, canopy colliders, cart path colour/lift, keep the Griffith Park hills backdrop, extend terrain with fog, own Unity project C:\GSP\Harding_Project.

## PC on-surface fixes (Oct 28, from the Unity build check)
`../tee_pads_harding.py` (run after apply_checklist_harding.py):
- (superseded below) 37 GKD tees had no mapped box: each now has a flat 7 x 9 m pad in course.svg's Tee layer (long side to the green) with a 2 m first cut; listed in `tee_pads.csv`.
- **Use `harding/heightmap_2049.raw` from now on**: same as `../heightmap_2049.raw` but levelled under those pads (blended over 3 m); GKD tee heights match it.
- Hole 17 White and Combo (Green slot) were on cart path 22: moved 8 m sideways off it (yardage unchanged, 301/300). Hole 7 Yellow also moved 6 m off a path.
- Trees: crowns x 1.3 kept off the sand: 6 trees nudged away from bunkers, none removed.

## Shared-box tees (Oct 29, PC rebuild: 1 and 3 Yellow landed on rough)
A colour pushed sideways off a shared mapped box got a pad that merged with the box into a jagged shape, which OPCD left as rough.
`../fix_box_tees.py Harding.GKD <pre-pad heightmap>` (from the Wilson thread) now runs before `../tee_pads_harding.py`: it puts every colour that shares a mapped box onto the box, at least 3 m from the other colour and 1.2 m inside the edge (1 Yellow, 3 Yellow, 7 Green, 16 Green, 17 Black moved; yardages within 3 of the card).
Pads were then rebuilt from the pre-pad svg and heightmap: 35 pads, none within 6 m of a mapped box. No tee is stacked or near a box edge.
Rebuild order: svg -> smooth_fairways.py -> surrounds.py -> coursekit card --ob -> fix_tees.py -> apply_checklist_harding.py -> fix_box_tees.py -> tee_pads_harding.py.

## Repo note (2026-11-03)
This folder is now its own repo (split out of the moorpark branch `claude/project-thread-a6haj8`, `griffith-park/harding`) wired to the course-build toolkit via `course.json`.
- `heightmap_2049.raw` is harding's own (levelled under the tee pads), not the griffith-park shared one.
- `satellite.jpg` was copied from the shared `griffith-park/satellite.jpg` (harding/ had none of its own).
- The sibling scripts from `griffith-park/` (tee_pads_harding.py, surrounds.py, smooth_fairways.py, fix_tees.py, fix_box_tees.py, apply_checklist_harding.py) are in `scripts/`; they were written to run from `griffith-park/` with `harding/...` paths.
