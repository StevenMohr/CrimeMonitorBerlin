## Postgres/PostGIS-only

UPDATE crime_main_district SET way=ST_Transform(subquery.way, 4326) FROM (SELECT planet_osm_line.way, planet_osm_line.osm_id from planet_osm_line INNER JOIN crime_main_district on (planet_osm_line.osm_id = crime_main_district.area_id)) AS subquery WHERE crime_main_district.area_id = subquery.osm_id;
