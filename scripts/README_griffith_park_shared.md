# Griffith Park shared frame (Wilson + Harding)

- 2000 m square, centre 34.1405, -118.28425. EPSG:6340 (NAD83(2011) UTM 11N) SW corner 380594.21 E, 3777479.33 N.
- Unity x = metres east of SW corner, z = metres north, y = elevation - 120 m (y_offset in course.json).
- `heightmap_2049.raw`: 2049 x 2049, 16-bit, Windows byte order. Unity Terrain 2000 x 227 x 2000. Ground 121.0 to 345.8 m.
- LiDAR: USGS 3DEP `CA_LosAngeles_1_B23` (QL1, flown 2023-24) from the EPT copy on AWS: 95.4 M points, 23.9 per m2, noise removed.
  `points.npz` (770 MB, coursekit format) is here once the copy finishes. Rebuild: `python coursekit.py lidar --ept CA_LosAngeles_1_B23`.
  `USGS_LPC_CA_LosAngeles_2016_LAS_2018` (QL2) also covers the park.
- `map_export_original.osm`: BoJa's OSM export of both courses. Its bbox stops at lat 34.14655, so the tees for Harding 13 and 18 (and a green and 2 bunkers) were missing.
  `map.osm` = the export plus those polygons from Overture 2026-09-23.0 (`scripts/fill_osm.py`).
- `scripts/split_osm.py map.osm "Harding Golf Course" out.osm scripts/griffith_golf.geojson` keeps one course's golf features (Wilson: "Wilson Golf Course").
- Satellite: NAIP hosts are blocked from the cloud session; to be fetched on the Mac (`coursekit.py satellite` in a folder holding this course.json).
