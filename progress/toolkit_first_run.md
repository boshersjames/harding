# First headless toolkit run (2026-11-03)

Run from the course folder, course-build at 02dcbcb Skills: additive Tools section in all 23 (exact toolkit commands, rule keys, and 'no tool yet' gaps); no existing text changed.

## doctor.py

```
ok   course.json                            /home/user/harding/course.json
ok   paths.toolkit                          /home/user/course-build
ok   heightmap size                         8396802 bytes (= 2049^2 x 2)
ok   gkd parses                             Harding - Griffith Park: 18 holes, 18 enabled
ok   svg greens match gkd                   18 outlines, 18 of 18 enabled holes matched
ok   paths.satellite                        /home/user/harding/satellite.jpg
ok   paths.trees_csv                        /home/user/harding/trees.csv
WARN paths.signs                            missing (/home/user/harding/progress/hole_signs.json)
WARN paths.photos_root                      missing (/home/user/harding/course_photos)
ok   python numpy                           
ok   python scipy                           
ok   python matplotlib                      
ok   python PIL                             
ok   python pyproj                          
ok   python laspy                           
ok   python pillow_heif                     
ok   tool git                               
ok   tool git-lfs                           
ok   tool ffmpeg                            
ok   tool yt-dlp                            
info unity_project                          C:/GSP/Harding_Project not on this machine
info automation latest run                  none here

0 FAIL, 2 WARN
[exit 0]
```

## gkd_tools.py check

```
25 checks, 0 failing
[exit 0]
```

## green_report.py --smooth 0.6

```
# Green report (Harding, surface: course heightmap order 3, low-pass sigma 0.6 m)

Rules: pin area <= 1.7 deg over 17 points, pins >= 3 m from the edge, >= 4 valid areas >= 3 m apart; internal slope 1-3%.

| hole | area m2 | relief m | slope mean/p90 % | >3% | pins fail | pin angles | usable % | areas | flag | pass |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 560 | 0.53 | 2.0 / 3.4 | 19 | 0/4 | Thu:1.2 Fri:1.6 Sat:1.0 Sun:1.2 | 84 | 48 |  | PASS |
| 2 | 447 | 0.49 | 1.8 / 3.9 | 18 | 0/4 | Thu:0.4 Fri:0.7 Sat:0.9 Sun:0.5 | 80 | 35 |  | PASS |
| 3 | 602 | 0.98 | 3.1 / 4.8 | 48 | 0/4 | Thu:1.0 Fri:1.0 Sat:1.3 Sun:1.3 | 45 | 31 | steep >3% | PASS |
| 4 | 351 | 1.05 | 4.0 / 6.8 | 56 | 1/4 | Thu:1.6 Fri:1.6 Sat:1.4 Sun:3.3 | 40 | 16 | steep >3% | FAIL |
| 5 | 286 | 1.02 | 4.5 / 5.4 | 95 | 4/4 | Thu:2.5 Fri:2.5 Sat:2.8 Sun:3.0 | 0 | 0 | steep >3% | FAIL |
| 6 | 484 | 0.61 | 2.1 / 3.6 | 18 | 0/4 | Thu:1.3 Fri:1.1 Sat:1.0 Sun:1.3 | 80 | 36 |  | PASS |
| 7 | 596 | 0.50 | 2.3 / 4.6 | 20 | 0/4 | Thu:0.7 Fri:0.9 Sat:0.8 Sun:1.1 | 74 | 46 |  | PASS |
| 8 | 409 | 0.88 | 4.1 / 7.2 | 64 | 2/4 | Thu:1.3 Fri:1.8 Sat:2.0 Sun:1.2 | 35 | 19 | steep >3% | FAIL |
| 9 | 367 | 0.95 | 3.7 / 7.5 | 48 | 4/4 | Thu:4.5 Fri:1.4 Sat:5.5 Sun:4.2 | 50 | 21 | steep >3% | FAIL |
| 10 | 301 | 0.57 | 2.5 / 3.3 | 19 | 0/4 | Thu:1.3 Fri:1.4 Sat:1.2 Sun:1.1 | 75 | 21 |  | PASS |
| 11 | 683 | 1.70 | 6.2 / 12.5 | 86 | 3/4 | Thu:2.2 Fri:2.3 Sat:3.2 Sun:1.3 | 10 | 9 | steep >3% | FAIL |
| 12 | 323 | 0.88 | 3.2 / 4.2 | 66 | 4/4 | Thu:2.3 Fri:2.4 Sat:2.0 Sun:1.9 | 34 | 15 | steep >3% | FAIL |
| 13 | 565 | 1.73 | 5.1 / 9.9 | 74 | 2/4 | Thu:1.3 Fri:3.4 Sat:1.1 Sun:2.4 | 25 | 19 | steep >3% | FAIL |
| 14 | 408 | 0.42 | 2.0 / 3.3 | 14 | 0/4 | Thu:0.8 Fri:1.0 Sat:1.7 Sun:1.3 | 82 | 34 |  | PASS |
| 15 | 405 | 0.87 | 3.4 / 6.0 | 46 | 2/4 | Thu:1.5 Fri:1.8 Sat:6.0 Sun:1.2 | 56 | 26 | steep >3% | FAIL |
| 16 | 382 | 0.74 | 3.6 / 5.0 | 71 | 4/4 | Thu:2.5 Fri:2.5 Sat:2.2 Sun:1.9 | 18 | 10 | steep >3% | FAIL |
| 17 | 566 | 1.50 | 3.7 / 5.6 | 68 | 4/4 | Thu:2.2 Fri:2.7 Sat:1.9 Sun:2.0 | 32 | 23 | steep >3% | FAIL |
| 18 | 396 | 1.13 | 4.4 / 7.2 | 76 | 3/4 | Thu:1.6 Fri:2.5 Sat:2.7 Sun:2.6 | 21 | 11 | steep >3% | FAIL |
wrote progress/green_report
[exit 0]
```

## flyover_gate.py --end-fit --no-plots

```
no signs file at /home/user/harding/progress/hole_signs.json: provisional sign spots from the back tees
hole  1: 532 frames  21.3 s (x1.00) yaw/1s 0.02 pitch/1s 4.50 | end pitch -29.2 (pin -29.2) h 14.5 m, 24.0 m short | terrain 14.4 m crown 3.7 m (tree 1165, lift 0.0/0.0) | first: crown 3.7 sight 3.8 in-frame True | green 99% (cut off 0, pull-back 0.0) pin True sight 6.6 -> OK
hole  2: 459 frames  18.4 s (x1.00) yaw/1s 1.07 pitch/1s 4.50 | end pitch -30.2 (pin -30.2) h 12.7 m, 21.0 m short | terrain 12.7 m crown 2.7 m (tree 796, lift 0.0/0.0) | first: crown 4.3 sight 4.4 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 11.6 -> OK
hole  3: 507 frames  20.3 s (x1.00) yaw/1s 0.87 pitch/1s 4.50 | end pitch -29.7 (pin -29.7) h 16.3 m, 27.5 m short | terrain 16.2 m crown 4.5 m (tree 211, lift 0.0/0.0) | first: crown 8.4 sight 8.5 in-frame True | green 93% (cut off 0, pull-back 0.0) pin True sight 8.6 -> OK
hole  4: 442 frames  17.7 s (x1.00) yaw/1s 1.66 pitch/1s 4.50 | end pitch -29.6 (pin -29.6) h 12.8 m, 21.0 m short | terrain 12.8 m crown 2.2 m (tree 358, lift 0.0/6.0) | first: crown 10.0 sight 10.0 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 4.9 -> OK
hole  5: 317 frames  12.7 s (x1.00) yaw/1s 4.50 pitch/1s 4.29 | end pitch -28.1 (pin -28.1) h 16.1 m, 29.5 m short | terrain 16.0 m crown 13.1 m (tree 217, lift 0.0/0.0) | first: crown 14.4 sight 14.9 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 7.9 -> OK
hole  6: 641 frames  25.6 s (x1.00) yaw/1s 0.54 pitch/1s 4.50 | end pitch -29.0 (pin -29.0) h 14.0 m, 24.0 m short | terrain 14.0 m crown 8.4 m (tree 15, lift 0.0/0.0) | first: crown 15.3 sight 14.2 in-frame True | green 94% (cut off 0, pull-back 0.0) pin True sight 9.7 -> OK
hole  7: 590 frames  23.6 s (x1.00) yaw/1s 1.28 pitch/1s 4.50 | end pitch -29.9 (pin -29.9) h 13.4 m, 23.0 m short | terrain 13.4 m crown 5.1 m (tree 16, lift 0.0/0.0) | first: crown 23.9 sight 23.9 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 15.6 -> OK
hole  8: 512 frames  20.5 s (x1.00) yaw/1s 2.78 pitch/1s 4.50 | end pitch -29.2 (pin -29.2) h 12.3 m, 21.0 m short | terrain 12.3 m crown 5.0 m (tree 21, lift 0.0/0.0) | first: crown 12.2 sight 12.2 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 11.1 -> OK
hole  9: 523 frames  20.9 s (x1.00) yaw/1s 0.21 pitch/1s 4.50 | end pitch -26.4 (pin -26.4) h 16.0 m, 30.5 m short | terrain 16.0 m crown 4.3 m (tree 885, lift 0.0/0.0) | first: crown 5.9 sight 5.9 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 13.3 -> OK
hole 10: 474 frames  19.0 s (x1.00) yaw/1s 2.70 pitch/1s 4.50 | end pitch -29.2 (pin -29.2) h 13.4 m, 22.0 m short | terrain 13.4 m crown 4.0 m (tree 719, lift 0.0/0.0) | first: crown 9.0 sight 6.8 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 22.0 -> OK
hole 11: 505 frames  20.2 s (x1.00) yaw/1s 0.99 pitch/1s 4.50 | end pitch -29.6 (pin -29.6) h 14.8 m, 25.0 m short | terrain 14.8 m crown 5.6 m (tree 319, lift 0.0/0.0) | first: crown 6.5 sight 6.5 in-frame True | green 96% (cut off 0, pull-back 0.0) pin True sight 9.8 -> OK
hole 12: 495 frames  19.8 s (x1.00) yaw/1s 0.93 pitch/1s 4.50 | end pitch -29.1 (pin -29.1) h 14.3 m, 24.0 m short | terrain 14.3 m crown 3.3 m (tree 294, lift 0.0/0.0) | first: crown 16.3 sight 14.4 in-frame True | green 98% (cut off 0, pull-back 0.0) pin True sight 9.2 -> OK
hole 13: 317 frames  12.7 s (x1.00) yaw/1s 4.50 pitch/1s 3.25 | end pitch -12.3 (pin -12.3) h 16.2 m, 64.0 m short | terrain 16.2 m crown 11.0 m (tree 720, lift 0.0/0.0) | first: crown 11.5 sight 11.8 in-frame True | green 82% (cut off 12, pull-back 6.0) pin True sight 7.0 -> FAIL
hole 14: 487 frames  19.5 s (x1.00) yaw/1s 1.95 pitch/1s 4.50 | end pitch -29.5 (pin -29.5) h 12.0 m, 20.5 m short | terrain 12.0 m crown 7.4 m (tree 126, lift 0.0/0.0) | first: crown 13.0 sight 11.5 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 12.0 -> OK
hole 15: 317 frames  12.7 s (x1.00) yaw/1s 4.50 pitch/1s 3.77 | end pitch -15.2 (pin -15.2) h 16.2 m, 55.5 m short | terrain 16.2 m crown 3.4 m (tree 957, lift 0.0/0.0) | first: crown 4.3 sight 4.3 in-frame True | green 72% (cut off 16, pull-back 5.0) pin True sight 6.1 -> FAIL
hole 16: 485 frames  19.4 s (x1.00) yaw/1s 2.47 pitch/1s 4.50 | end pitch -29.0 (pin -29.0) h 13.5 m, 23.0 m short | terrain 13.5 m crown 5.1 m (tree 726, lift 0.0/0.0) | first: crown 5.9 sight 6.1 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 7.6 -> OK
hole 17: 465 frames  18.6 s (x1.00) yaw/1s 1.20 pitch/1s 4.50 | end pitch -22.2 (pin -22.2) h 16.1 m, 37.0 m short | terrain 16.1 m crown 0.1 m (tree 1078, lift 0.0/4.8) | first: crown 3.8 sight 3.9 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 7.9 -> FAIL  [opening NOT fixed within 6 m (crown 3.8 m, sign sightline 3.9 m, sign in frame True, rise 0.1 m from crown of tree 1078)]
hole 18: 587 frames  23.5 s (x1.00) yaw/1s 1.06 pitch/1s 4.50 | end pitch -29.2 (pin -29.2) h 16.5 m, 27.5 m short | terrain 16.1 m crown 2.2 m (tree 1152, lift 0.0/0.0) | first: crown 5.6 sight 5.5 in-frame True | green 93% (cut off 0, pull-back 0.0) pin True sight 6.4 -> OK
Failed holes: 13, 15, 17

Poster frames (first / rise / mid / approach / end) per hole are in flyover_gate.json; shots for the PC render in flyover_shots.json (8655 frames).
[exit 1]
```

## gate_report.py

```
# Gate report: Harding (18 holes)

Sources: flyover, lidar-proxy. Missing: Unity CourseGreenChecks (checks/greens_all18.csv): run Course Checks > Greens on the PC.

GKD checks: all pass

| hole | source | step cm | lip cm | col dy | tiers | crown m | pins fail | usable % | areas | fall dir | flyover | result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 13 | lidar-proxy+flyover | - | - | - | - | - | 2 | 25 | 19 | - | FAIL | **FAIL** flyover warn: pins(lidar) |
| 15 | lidar-proxy+flyover | - | - | - | - | - | 2 | 56 | 26 | - | FAIL | **FAIL** flyover warn: pins(lidar) |
| 17 | lidar-proxy+flyover | - | - | - | - | - | 4 | 32 | 23 | - | FAIL | **FAIL** flyover warn: pins(lidar) |
| 1 | lidar-proxy+flyover | - | - | - | - | - | 0 | 84 | 48 | - | PASS | PASS |
| 2 | lidar-proxy+flyover | - | - | - | - | - | 0 | 80 | 35 | - | PASS | PASS |
| 3 | lidar-proxy+flyover | - | - | - | - | - | 0 | 45 | 31 | - | PASS | PASS |
| 4 | lidar-proxy+flyover | - | - | - | - | - | 1 | 40 | 16 | - | PASS | PASS warn: pins(lidar) |
| 5 | lidar-proxy+flyover | - | - | - | - | - | 4 | 0 | 0 | - | PASS | PASS warn: pins(lidar),areas(lidar) |
| 6 | lidar-proxy+flyover | - | - | - | - | - | 0 | 80 | 36 | - | PASS | PASS |
| 7 | lidar-proxy+flyover | - | - | - | - | - | 0 | 74 | 46 | - | PASS | PASS |
| 8 | lidar-proxy+flyover | - | - | - | - | - | 2 | 35 | 19 | - | PASS | PASS warn: pins(lidar) |
| 9 | lidar-proxy+flyover | - | - | - | - | - | 4 | 50 | 21 | - | PASS | PASS warn: pins(lidar) |
| 10 | lidar-proxy+flyover | - | - | - | - | - | 0 | 75 | 21 | - | PASS | PASS |
| 11 | lidar-proxy+flyover | - | - | - | - | - | 3 | 10 | 9 | - | PASS | PASS warn: pins(lidar) |
| 12 | lidar-proxy+flyover | - | - | - | - | - | 4 | 34 | 15 | - | PASS | PASS warn: pins(lidar) |
| 14 | lidar-proxy+flyover | - | - | - | - | - | 0 | 82 | 34 | - | PASS | PASS |
| 16 | lidar-proxy+flyover | - | - | - | - | - | 4 | 18 | 10 | - | PASS | PASS warn: pins(lidar) |
| 18 | lidar-proxy+flyover | - | - | - | - | - | 3 | 21 | 11 | - | PASS | PASS warn: pins(lidar) |
wrote progress/gate_report
[exit 1]
```
