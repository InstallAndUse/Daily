# 2022 03 19  + published on https://github.com/InstallAndUse/Daily /A

disappointed
consider using alternatives, TablePlus is good.

### # #
# prepare
### # #

# get repo for distro
https://yum.postgresql.org/repopackages.php
https://download.postgresql.org/pub/repos/yum/11/fedora/fedora-28-x86_64/pgdg-fedora11-11-2.noarch.rpm
rpm -ivh pgdg-fedora11-11-2.noarch.rpm

# install (will install httpd)
yum install pgadmin4

# add extra configs location to apache
vi /etc/httpd/conf/httpd.conf
:$
IncludeOptional /data/www/conf/*.conf

# conf virtual conf file
mkdir -p /data/www/conf
cp /etc/httpd/conf.d/pgadmin4.conf.sample /data/www/conf/01-pgadmin.conf
vi /data/www/conf/01-pgadmin.conf

# SElinux
#(not needed, yet)semanage fcontext -a -t httpd_sys_content_t "/data/www(/.*)?"
semanage fcontext -a -t httpd_config_t      "/data/www/conf(/.*)?"
semanage fcontext -l | grep /data/www
restorecon -R -v /data/www

# when logs are clear, connect
http://localhost/pgadmin4




https://linuxhint.com/install-pgadmin4-ubuntu/
http://yallalabs.com/linux/how-to-install-pgadmin-4-in-server-mode-on-ubuntu-16-04-lts/


Books:
- [Anton's bookshelf](https://og2k.com/books/)
