CREATE DATABASE crimemonitor;
CREATE DATABASE test_crimemonitor;
\c crimemonitor;
Create USER crime PASSWORD 'crime';
CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;
grant ALL on DATABASE crimemonitor to crime;
ALTER TABLE layer  OWNER TO crime;
ALTER TABLE topology  OWNER TO crime;
ALTER TABLE spatial_ref_sys OWNER TO crime;
ALTER TABLE geometry_columns OWNER TO crime;
\c test_crimemonitor;
CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;
grant ALL on DATABASE test_crimemonitor to crime;
ALTER TABLE layer  OWNER TO crime;
ALTER TABLE topology  OWNER TO crime;
ALTER TABLE spatial_ref_sys OWNER TO crime;
ALTER TABLE geometry_columns OWNER TO crime;

\q
