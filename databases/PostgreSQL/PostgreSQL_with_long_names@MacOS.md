#
# postgres with columns's longnames 512-bit
#
# 2022 03 19  + published on https://github.com/InstallAndUse/Daily /A



# download stable source from https://www.postgresql.org/ftp/source/
cd Downloads
tar -xzvf postgresql-12.4.tar.gz
vi src/include/pg_config_manual.h
    #define NAMEDATALEN 512
./configure
# download and install xcode
make
su
make install

/usr/sbin/sysadminctl -addUser postgres
mkdir /usr/local/pgsql/data
chown postgres /usr/local/pgsql/data
su - postgres
/usr/local/pgsql/bin/initdb -D /usr/local/pgsql/data
/usr/local/pgsql/bin/pg_ctl -D /usr/local/pgsql/data -l logfile start

# console
/usr/local/pgsql/bin/psql

# create user (match OS's username) and give rights
CREATE USER (you)

# from another terminal, should work
/usr/local/pgsql/bin/psql -U postgres postgres

# include into PATHs
su
vi /etc/paths
    /usr/local/pgsql/bin
