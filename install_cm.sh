apt-get install postgresql-9.1 postgres-server-dev-9.1 libxml2-dev build-essential g++ binutils python-psycopg2 python-imaging python-pip
pip install -r requirements.txt
cp init_db.sql /tmp
cd /tmp

su -c "psql -f init_db.sql" postgres 

./osm2pgsql -d crimemonitor -U crime -W -s -C 200 ../Downloads/berlin.osm
echo "Change user auth method from PEER to md5 in pg_hba.conf"
echo "Patch GeoDjango with fix for proper creation with PostGIS 2.0 (see JIRA REG-2)"
