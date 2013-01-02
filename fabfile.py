from fabric.operations import sudo, local

__author__ = 'steven'


def install_system_local():
    local('sudo su -c "createdb -T template_postgis crimemonitor" postgres')
    local('sudo su -c "psql -f init_db.sql" postgres')