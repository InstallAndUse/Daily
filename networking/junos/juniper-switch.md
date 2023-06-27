# JUNIPER SWITCH


# global navigatoin
show | display set

up

# modification
set
replace pattern A with B
delete

# USERS AND PASSWORDS
# show users
show system login | display set

# create new user and give a role
set system login user (username) full-name (FULL_username)
set system login user (username) class super-user/operator

# set password, when already encrypted (copying pass from one switch to another"
set system login user (username) authentication encrypted-password "(crypted_pass)"

# when entering in _plain_text_, pass will be asked and encrypted
set system login user (username) authentication plain-text-password
New password: (enter new pass)

# enabling SSH, generate keys
set system services ssh
set system services ssh root-login deny
set system services ssh protocol-version v2
set system services ssh client-alive-count-max 5
set system services ssh client-alive-interval 12
? set system services ssh ciphers 3des-cbc

# add A record on DNS servers

# add rancid user
set system login class rancid permissions view
set system login class rancid permissions view-configuration
set system login user rancid class rancid
set system login user rancid authentication plain-text-password
New password: (enter pass)
# if authentication with keys, then
set system login user rancid authentication ssh-ecdsa (plain_password)

## on rancid server, add host to
## do not use ";"c for commenting
vi router.db
su - rancid
# add key and check that rancid can login
ssh-keygen -R xxx.xxx.196.155
ssh rancid@(new-device)
vi ./cloginrc
bin/clogin (host)


# show configuration
show configuration | display set | match
show ethernet-switching interface brief

# INTERFACES

# list interfaces
show interfaces descriptions
show interfaces terse

# disable interface (=clean conf + administatively down)
delete interfaces (interface)
set interfaces (interface) disable

# set interfaces ge-0/0/44 unit 0 family inet address xxx.xxx.196.159/26
set routing-options static route default next-hop xxx.xxx.196.129
set interface ge-0/0/34 description "(host)"

# trunk port
set interfaces ge-0/0/44 unit 0 family ethernet-switching interface-mode trunk
set interfaces ge-0/0/44 unit 0 family ethernet-switching vlan members mgmt (128)

# access port
set interfaces ge-0/0/44 unit 0 family ethernet-switching interface-mode access
set interfaces ge-0/0/44 unit 0 family ethernet-switching vlan members mgmt (128)

# VLANs
show ethernet-switching interface
set vlans mgmt vlan-id 128
##set interfaces xe-0/0/44 unit  0s family ethernet-switching vlan members mgmt
set interfaces vlan unit 128 enable
set interfaces irb unit 40 family inet
set interfaces irb unit 40 family inet address xxx.xxx.196.159/26
set vlans (vlan name) vlan-id 96 l3-interface irb.96
set interfaces irb unit 96
set interfaces ge-0/0/46 unit 0 family ethernet-switching vlan members [ vlan1 vlan2 ]
set interface vlan unit 96 enable




# checking and commiting
show | compare
commit check
commit

# show history of commits
request system software rollback

# checking that policy is in use
show security policies hit-count | match (number)    



## MAINTENANCE

# backup/restore configuration to file
# stop commit server, that somebody will not commit config
request system commit server pause

# delete old, save rescue configuration, check timestamp
request system configuration rescue delete
request system configuration rescue save
show system configuration rescue
show system rollback 0

# at this point, configuration could be restored with "rollback" command
?? request system software rollback

# save config, check
save dhcp-security-snoop config.dhcp-security-snoop.2019073
save dhcp-snooping config.dhcp-snooping.20190731.1024
    error: the ethernet-switching subsystem is not running
save dhcpv6-security-snoop config.dhcpv6-security-snoop.20190731.1025
file list detail

# resume commit server, when ready
request system commit server pause start

## copy from switch to usb memory

## scp from switch
save scp://user@hostname/path/filename routing-instance instance-name source-address address

## copy from ftp to switch
file copy ftp://anonymous:geg@test.jnpr.net/pub/junos/7.5R2.8/jinstall-7.5R2.8-domestic-signed.tgz /var/tmp/

## copy from usb memory to switch

## scp from local host to switch

## restore configuration file
test configuration (file)
load (filename)

# insert configuration into terminal, finish with C-D
test configuration terminal




# JUNOS UPGRADE

## show version status
show version
show chassis firmware

# attach USB and take a snapshot (flash will be repartitioned and content of USB memory will be erased)
request system snapshot

## upload from usb memory
start shell user root
mkdir /var/tmp/usb
mkdir /var/tmp/downloads
## connect usb
ls /dev/da*
mount_msdosfs /dev/da0s1 /var/tmp/usb
cp /var/tmp/usb(new-file) /var/tmp/downloads
umount /var/tmp/usb

## upload via scp

## validate package first
request system software validate /var/tmp/(new-filename)

## applying new version
request system software add /var/tmp/(new-filename) validate

## at this point last change to cancel upgrade by deliting jinstall, otherwise reboot
request system reboot
