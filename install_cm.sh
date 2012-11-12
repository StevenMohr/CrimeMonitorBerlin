apt-get install postgresql-9.1 postgres-server-dev-9.1 libxml2-dev build-essential g++ binutils python-psycopg2 python-imaging python-pip
pip install django geopy django_nose feedparser
cp init_db.sql /tmp
cd /tmp

wget http://download.osgeo.org/geos/geos-3.3.5.tar.bz2
tar xjf geos-3.3.5.tar.bz2
cd geos-3.3.5
./configure
make
make install
ldconfig
cd ..

wget http://download.osgeo.org/proj/proj-4.8.0.tar.gz
wget http://download.osgeo.org/proj/proj-datumgrid-1.5.tar.gz
tar xzf proj-4.8.0.tar.gz
cd proj-4.8.0/nad
tar xzf ../../proj-datumgrid-1.5.tar.gz
cd ..
./configure
make
make install
ldconfig
cd ..

wget http://download.osgeo.org/gdal/gdal-1.9.1.tar.gz
tar xzf gdal-1.9.1.tar.gz
cd gdal-1.9.1

./configure
make # Go get some coffee, this takes a while.
make install
ldconfig
cd ..

wget http://postgis.refractions.net/download/postgis-2.0.1.tar.gz
tar xzf postgis-2.0.1.tar.gz
cd postgis-2.0.1
./configure
make
make install
ldconfig
cd ..

su -c "psql -f init_db.sql" postgres 

./osm2pgsql -d crimemonitor -U crime -W -s -C 200 ../Downloads/berlin.osm
echo "Change user auth method from PEER to md5 in pg_hba.conf"
echo "Patch GeoDjango with fix for proper creation with PostGIS 2.0 (see JIRA REG-2)"
