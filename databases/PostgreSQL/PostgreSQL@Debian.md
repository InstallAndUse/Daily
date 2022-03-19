# 2022 03 19  + published on https://github.com/InstallAndUse/Daily /A


(you)@(domain):/etc$ sudo -u postgres psql postgres
    postgres=# SHOW hba_file;
    postgres=# SHOW config_file;

(you)@(domain):/etc$ sudo nano /etc/postgresql/9.3/main/pg_hba.conf

    # "local" is for Unix domain socket connections only
    #local   all             all                                     peer
    local   all             all                                     ident


    # IPv4 local connections:
    host    all             all             127.0.0.1/32            md5      
    host    all             all             0.0.0.0/0               md5
    hostssl all             all             0.0.0.0/0               md5

    # IPv6 local connections:
    host    all             all             ::1/128                 md5

(you)@(domain):/etc$ sudo nano /etc/postgresql/9.3/main/postgresql.conf
    #listen_addresses = 'localhost'         # what IP address(es) to listen on;
    listen_addresses = '*'         # what IP address(es) to listen on;


(you)@lab:~$ psql -h (domain) (domain) postgres
Password for user postgres:
psql (9.3.9)
SSL connection (cipher: DHE-RSA-AES256-GCM-SHA384, bits: 256)
Type "help" for help.

(domain)=#


adding users:

list users:
\du

list databases:
\l

list database roles:
\dg  

log:
(you)@(domain):~$ sudo tail -f /var/log/postgresql/postgresql-9.3-main.log

(you)@(domain):~$ sudo service postgresql restart

(you)@(domain):~$ sudo -u postgres psql postgres
psql (9.3.9)
Type "help" for help.

postgres=# CREATE USER ksr WITH PASSWORD 'ksr123ksr123';
CREATE ROLE
postgres=# GRANT ALL PRIVILEGES ON DATABASE (domain) TO ksr;
GRANT


postgres=# CREATE USER "(user)" WITH PASSWORD '(pass)';
CREATE ROLE
postgres=# GRANT ALL PRIVILEGES ON DATABASE "(domain)-current" TO "www-data";
GRANT
postgres=#

$ sudo apt-get install php5-pgsql  

postgres=# REVOKE ALL PRIVILEGES ON DATABASE (domain) FROM wwwdata;
postgres=# DROP USER wwwdata;

postgres=# CREATE DATABASE "(domain)-current" WITH OWNER=(user);
    CREATE DATABASE
postgres=# \l
                                    List of databases
      Name      |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
----------------+----------+----------+-------------+-------------+-----------------------
 (d)            | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =Tc/postgres         +
                |          |          |             |             | postgres=CTc/postgres+
                |          |          |             |             | (you)=CTc/postgres   +
                |          |          |             |             | xxx=CTc/postgres
 (d)-current    | xxx      | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
 postgres       | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
 template0      | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
                |          |          |             |             | postgres=CTc/postgres
 template1      | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
                |          |          |             |             | postgres=CTc/postgres
(5 rows)

postgres=#
(domain)-current=# GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO "www-data";
(domain)-current=# GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO "www-data";

//connect to DB
\c (domain)

// list tables
\dt
