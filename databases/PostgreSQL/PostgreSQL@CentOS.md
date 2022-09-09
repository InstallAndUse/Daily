# 2022 03 19  + published on https://github.com/InstallAndUse/Daily /A

# INSTALL
yum install postgresql-server
systemctl enable postgresql
postgresql-setup initdb
systemctl start postgresql


# CONFIG
vi /var/lib/pgsql/data/pg_hba.conf
su - postgres
psql
\password postgres

# make (user) administrator in database (create databases, roles, grant)
CREATE USER (user);
?? GRANT ALL ON DATABASE postgres TO (user);
\q
logout

# allow authorization by internal roles of database
vi /var/lib/pgsql/data/pg_hba.conf
# insert !!! before 'ident' method in local ipv4
host    all             all             127.0.0.1/32            md5
# allow network connections
host    all             all             0.0.0.0/32              md5
host    all             all             ::1/128                 md5

# open firewall (system dependent)
tcp/5432

# connect to database, using local ident
psql postgres

# connect to database, using other ident (via network)
psql -h 0 --username=(user) postgres


# USERS
\du               list users:
\password (user)  change password
ALTER USER (user) PASSWORD '(pass)';
# add user
CREATE USER (user) WITH PASSWORD '(user)123';

# DATABASES
\l  list
\c  connect
\dg list database roles:
# create db
# in naming, avoid usage of hyphen ("-"), otherwise use quotes ("")
CREATE DATABASE "(dbname)" OWNER (user;
# GRANT ALL PRIVILEGES ON DATABASE "(domain)-local" TO (user);
GRANT ALL ON DATABASE "(db)" TO (user);





# TABLES
\d         show tables
\d $table  show columns of table
# create table
CREATE TABLE events();
# add column
ALTER TABLE events ADD COLUMN event_id bigint PRIMARY KEY;
# delete column
ALTER TABLE events DROP COLUMN timestamp_start;


# BACKUP
pg_dump --verbose -h 0 --username (user) -s -f (localfile-schema) "(dbname)"
pg_dump --verbose -h 0 --username (user) "(dbname)" >> (localfile-data).backup


# RESTORE
psql -h 0 --username (user) "(dbname)" < (dbname).backup





# add column with coordinates
# https://www.postgresql.org/docs/9.1/static/earthdistance.html
# or
# http://epsg.io/4326
# https://postgis.net/docs/manual-2.1/using_postgis_dbmanagement.html#PostGIS_GeographyVSGeometry
# https://postgis.net/docs/manual-2.1/PostGIS_Special_Functions_Index.html#PostGIS_GeographyFunctions
https://fedoraproject.org/wiki/PostgreSQL


?????
//   (domain)=# GRANT SELECT ON users TO PUBLIC;


Books:
- [Anton's bookshelf](https://og2k.com/books/)
