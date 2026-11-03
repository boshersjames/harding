# Flyover gate (data pass)

Inputs: GKD `Harding.GKD`, signs `progress/hole_signs.json`, trees `trees.csv`, greens `course.svg`, heightmap `heightmap_2049.raw`, pin index 0.

Pass = yaw and pitch under 5 deg in every 1 s window, opening camera clear of crowns with the sign in frame and unhidden, terrain clearance 5 m+, crown clearance 1.5 m+ on the whole path, no part of the green cut off ahead or to the side in the end frame (the part under the camera is reported, not failed), pin in frame and not behind a crown.

| Hole | s | yaw/1s | pitch/1s | end pitch (target) | end h / short (used) | terrain min (after rise) | crown min (tree, frame), lift rise/flight | first: crown / sight / in frame | green: in / under cam / cut off (pull-back to fit) | pin | result | opening move |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 21.3 | 0.0 | 4.5 | -29.2 (-29.2) | 14.5 / 24.0 | 14.4 | 3.7 (1165, f0), 0.0 / 0.0 | 3.7 / 3.8 / yes | 99% / 1 / 0 (0 m) | in, sight 6.6 | **OK** |  |
| 2 | 18.4 | 1.1 | 4.5 | -30.2 (-30.2) | 12.7 / 21.0 | 12.7 | 2.7 (796, f56), 0.0 / 0.0 | 4.3 / 4.4 / yes | 100% / 0 / 0 (0 m) | in, sight 11.6 | **OK** |  |
| 3 | 20.3 | 0.9 | 4.5 | -29.7 (-29.7) | 16.3 / 27.5 | 16.2 | 4.5 (211, f68), 0.0 / 0.0 | 8.4 / 8.5 / yes | 93% / 6 / 0 (0 m) | in, sight 8.6 | **OK** |  |
| 4 | 17.7 | 1.7 | 4.5 | -29.6 (-29.6) | 12.8 / 21.0 | 12.8 | 2.2 (358, f328), 0.0 / 6.0 | 10.0 / 10.0 / yes | 100% / 0 / 0 (0 m) | in, sight 4.9 | **OK** |  |
| 5 | 12.7 | 4.5 | 4.3 | -28.1 (-28.1) | 16.1 / 29.5 | 16.0 | 13.1 (217, f184), 0.0 / 0.0 | 14.4 / 14.9 / yes | 100% / 0 / 0 (0 m) | in, sight 7.9 | **OK** |  |
| 6 | 25.6 | 0.5 | 4.5 | -29.0 (-29.0) | 14.0 / 24.0 | 14.0 | 8.4 (15, f212), 0.0 / 0.0 | 15.3 / 14.2 / yes | 94% / 4 / 0 (0 m) | in, sight 9.7 | **OK** |  |
| 7 | 23.6 | 1.3 | 4.5 | -29.9 (-29.9) | 13.4 / 23.0 | 13.4 | 5.1 (16, f264), 0.0 / 0.0 | 23.9 / 23.9 / yes | 100% / 0 / 0 (0 m) | in, sight 15.6 | **OK** |  |
| 8 | 20.5 | 2.8 | 4.5 | -29.2 (-29.2) | 12.3 / 21.0 | 12.3 | 5.0 (21, f82), 0.0 / 0.0 | 12.2 / 12.2 / yes | 100% / 0 / 0 (0 m) | in, sight 11.1 | **OK** |  |
| 9 | 20.9 | 0.2 | 4.5 | -26.4 (-26.4) | 16.0 / 30.5 | 16.0 | 4.3 (885, f56), 0.0 / 0.0 | 5.9 / 5.9 / yes | 100% / 0 / 0 (0 m) | in, sight 13.3 | **OK** |  |
| 10 | 19.0 | 2.7 | 4.5 | -29.2 (-29.2) | 13.4 / 22.0 | 13.4 | 4.0 (719, f70), 0.0 / 0.0 | 9.0 / 6.8 / yes | 100% / 0 / 0 (0 m) | in, sight 22.0 | **OK** |  |
| 11 | 20.2 | 1.0 | 4.5 | -29.6 (-29.6) | 14.8 / 25.0 | 14.8 | 5.6 (319, f410), 0.0 / 0.0 | 6.5 / 6.5 / yes | 96% / 3 / 0 (0 m) | in, sight 9.8 | **OK** |  |
| 12 | 19.8 | 0.9 | 4.5 | -29.1 (-29.1) | 14.3 / 24.0 | 14.3 | 3.3 (294, f392), 0.0 / 0.0 | 16.3 / 14.4 / yes | 98% / 1 / 0 (0 m) | in, sight 9.2 | **OK** |  |
| 13 | 12.7 | 4.5 | 3.2 | -12.3 (-12.3) | 16.2 / 64.0 | 16.2 | 11.0 (720, f254), 0.0 / 0.0 | 11.5 / 11.8 / yes | 82% / 0 / 12 (6 m) | in, sight 7.0 | **FAIL** |  |
| 14 | 19.5 | 1.9 | 4.5 | -29.5 (-29.5) | 12.0 / 20.5 | 12.0 | 7.4 (126, f208), 0.0 / 0.0 | 13.0 / 11.5 / yes | 100% / 0 / 0 (0 m) | in, sight 12.0 | **OK** |  |
| 15 | 12.7 | 4.5 | 3.8 | -15.2 (-15.2) | 16.2 / 55.5 | 16.2 | 3.4 (957, f52), 0.0 / 0.0 | 4.3 / 4.3 / yes | 72% / 0 / 16 (5 m) | in, sight 6.1 | **FAIL** |  |
| 16 | 19.4 | 2.5 | 4.5 | -29.0 (-29.0) | 13.5 / 23.0 | 13.5 | 5.1 (726, f52), 0.0 / 0.0 | 5.9 / 6.1 / yes | 100% / 0 / 0 (0 m) | in, sight 7.6 | **OK** |  |
| 17 | 18.6 | 1.2 | 4.5 | -22.2 (-22.2) | 16.1 / 37.0 | 16.1 | 0.1 (1078, f66), 0.0 / 4.8 | 3.8 / 3.9 / yes | 100% / 0 / 0 (0 m) | in, sight 7.9 | **FAIL** | opening NOT fixed within 6 m (crown 3.8 m, sign sightline 3.9 m, sign in frame True, rise 0.1 m from crown of tree 1078) |
| 18 | 23.5 | 1.1 | 4.5 | -29.2 (-29.2) | 16.5 / 27.5 | 16.1 | 2.2 (1152, f60), 0.0 / 0.0 | 5.6 / 5.5 / yes | 93% / 6 / 0 (0 m) | in, sight 6.4 | **OK** |  |

End spot: 12 m short of the pin, 8 m over the ground (v4 default 12 / 8), pulled back per hole until the green fits (--end-fit).

Failed holes: 13, 15, 17

Poster frames (first / rise / mid / approach / end) per hole are in flyover_gate.json; shots for the PC render in flyover_shots.json (8655 frames).
