# 2022 03 19  + published on https://github.com/InstallAndUse/Daily /A


## DATABASES
SHOW DATABASES;


## USERS
# list users
USE mysql;
SELECT * FROM user \G;

# create user
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';

# change password of another user
ALTER USER 'olduser'@'hostname' IDENTIFIED BY 'newpassword';

# for older than 5.7.5
USE mysql;
SET PASSWORD FOR 'user-name-here'@'hostname' = PASSWORD('new-password');
# or
UPDATE mysql.user SET Password=PASSWORD('new-password-here') WHERE User='user-name-here' AND Host='host-name-here';


## PRIVILEGES
# GRANT privileges
```
GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'localhost';
GRANT type_of_permission ON database_name.table_name TO ‘username’@'localhost’;
```

# REVOKE privileges
REVOKE type_of_permission ON database_name.table_name FROM ‘username’@‘localhost’;

Remember to flush priveleges after GRANT/REVOKE functions!
```
FLUSH PRIVILEGES;
```

# show, who has privileges to specific database
??

# show, to which databases user has privileges to
```
SHOW GRANTS FOR 'xxxx'@'xxx.xxx.xx.xx'
```

## TABLES




## REPLICATION
on old mariadb
```

```

on newer mariadb
```
GRANT REPLICATION SLAVE ON *.* TO 'replication'@'%';
```
can not perform only for specific table, need to dump and restore
```
GRANT REPLICATION SLAVE ON db.table TO 'user'@'host';
```

# Replication via file
mysqldump --host 11.22.33.44 -u username -ppassword --master-data=2 \
--quick --hex-blob --add-drop-table --create-options --extended-insert \
--disable-keys --allow-keywords mydatabase mytable myview > mdump.sql



# Set new pass for root
stop manually started service
```
mysqld_safe --skip-grant-tables --skip-networking &
systemctl stop mariadb
mysql -u root

FLUSH PRIVILEGES;
SET PASSWORD FOR 'root'@'localhost' = PASSWORD('pass');
```
