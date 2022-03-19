# 2022 03 19  + published on https://github.com/InstallAndUse/Daily /A

# prepare
yum install \
  postgresql-server \
  postgresql-contrib

# init
postgresql-setup initdb

# enable and start
systemctl enable postgresql
systemctl start postgresql

# connect
sudo -u postgres psql postgres

# set password for user "postgres"
\password postgres
# re-login

# show config files
postgres=# SHOW hba_file;
 /var/lib/pgsql/data/pg_hba.conf
postgres=# SHOW config_file;
 /var/lib/pgsql/data/postgresql.conf

# enable connections
vi  /var/lib/pgsql/data/pg_hba.conf
# comment everything!.
# for local access add only ipv4 with md5 password (just created)
  host    all             all             127.0.0.1/32            md5

# check connection
psql -h 127.0.0.1 -U postgres


# FIREWALL
$ # make it last after reboot
$ firewall-cmd --permanent --add-port=5432/tcp
$ # change runtime configuration
$ firewall-cmd --add-port=5432/tcp


# SELinux (if DB location changes)
$ semanage fcontext -a -t postgresql_db_t "/my/new/location(/.*)?"
$ semanage port -a -t postgresql_port_t -p tcp 5433
# setsebool -P httpd_can_network_connect_db on
















sudo nano /etc/postgresql/9.3/main/pg_hba.conf
    # "local" is for Unix domain socket connections only
    #local   all             all                                     peer
    local   all             all                                     ident

    # IPv4 local connections:
    host    all             all             127.0.0.1/32            md5
    host    all             all             0.0.0.0/0               md5
    hostssl all             all             0.0.0.0/0               md5

    # IPv6 local connections:
    host    all             all             ::1/128                 md5

sudo nano /etc/postgresql/9.3/main/postgresql.conf
    #listen_addresses = 'localhost'         # what IP address(es) to listen on;
    listen_addresses = '*'         # what IP address(es) to listen on;

(you)@lab:~$ psql -h (domain) (domain) postgres
