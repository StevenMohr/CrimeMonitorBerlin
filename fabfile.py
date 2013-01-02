from fabric.context_managers import lcd
from fabric.operations import sudo, local

__author__ = 'steven'


def install_system_local():
    local('sudo su -c "createdb -T template_postgis crimemonitor" postgres')
    local('sudo su -c "psql -f init_db.sql" postgres')
    local('python manage.py syncdb')
    with lcd('/tmp/'):
        local('wget http://download.geofabrik.de/openstreetmap/europe/germany/berlin.osm.bz2')
        local('osm2pgsql -d crimemonitor -U crime -W -s berlin.osm.bz2')
    local('sudo su -c "psql -f crime_main/sql/district_.sql  crimemonitor" postgres')