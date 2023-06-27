# JUNIPER FIREWALLS

configuration overview
```
show configuration
show configuration | display set | match
show | display set | include
show ethernet-switching interface brief
```

global navigation
```
up
top
```

modification
```
set
replace pattern A with B
rename object to object
delete
```


enabling SSH, generate keys
```
set system services ssh
set system services ssh root-login deny
set system services ssh protocol-version v2
set system services ssh client-alive-count-max 5
set system services ssh client-alive-interval 12
? set system services ssh ciphers 3des-cbc
```


## USERS AND PASSWORDS
show users
```
show system login | display set
```

create new user and give a role
```
set system login user (username) full-name (FULL_username)
set system login user (username) class super-user/operator
```

create permission class and add user (i.e. 'rancid' to fetch configuration)
```
set system login class rancid permissions view
set system login class rancid permissions view-configuration
set system login user rancid class rancid
set system login user rancid authentication plain-text-password
New password: (enter pass)
```
if authentication with keys, then
```
set system login user rancid authentication ssh-ecdsa (plain_password)
```
in addition to user rancid user creation, on rancid host, configure new network device:
(on rancid server, add host to. do not use ";"c for commenting)
```
vi router.db
su - rancid
```
add key and check that rancid can login
```
ssh-keygen -R xxx.xxx.196.155
ssh rancid@(new-device)
vi ./cloginrc
bin/clogin (host)
```

set password, when already encrypted (copying pass from one switch to another"
```
set system login user (username) authentication encrypted-password "(crypted_pass)"
```

when entering in _plain_text_, pass will be prompted and encrypted
```
set system login user (username) authentication plain-text-password
New password: (enter new pass)
```

## NTERFACES

list interfaces
```
show interfaces descriptions
show interfaces terse
```

disable interface (=clean conf + administatively down)
```
delete interfaces (interface)
set interfaces (interface) disable
```

set interfaces ge-0/0/44 unit 0 family inet address xxx.xxx.196.159/26
```
set interface ge-0/0/34 description "(host)"
set routing-options static route default next-hop xxx.xxx.196.129
```

trunk port
```
set interfaces ge-0/0/44 unit 0 family ethernet-switching interface-mode trunk
set interfaces ge-0/0/44 unit 0 family ethernet-switching vlan members mgmt (128)
```

access port
```
set interfaces ge-0/0/44 unit 0 family ethernet-switching interface-mode access
set interfaces ge-0/0/44 unit 0 family ethernet-switching vlan members mgmt (128)
```

VLANs
```
show ethernet-switching interface
set vlans mgmt vlan-id 128
set interfaces xe-0/0/44 unit 0 family ethernet-switching vlan members mgmt
set interfaces vlan unit 128 enable
set interfaces irb unit 40 family inet
set interfaces irb unit 40 family inet address xxx.xxx.196.159/26
set vlans (vlan name) vlan-id 96 l3-interface irb.96
set interfaces irb unit 96
set interfaces ge-0/0/46 unit 0 family ethernet-switching vlan members [ vlan1 vlan2 ]
set interface vlan unit 96 enable
```



# CONFIGURING RULES

search for matched rules in existing config
```
show configuration | display set | match (ip)    
```

configure mode
```
configure
run show configuration | display set | match (ip)
run show configuration | display set | match TCP_Port_(number)    
run show configuration security policies from-zone untrust to-zone (zone) policy (policy-name) | display set
```

add new rule
```
set security policies from-zone (zone) to-zone (zone) policy (number) match source-address Host_(ip)         
set security policies from-zone (zone) to-zone (zone) policy (number) match destination-address (ip)    
set security policies from-zone (zone) to-zone (zone) policy (number) match application TCP_Port_(number)/(name of app)
set security policies from-zone (zone) to-zone (zone) policy (number) then permit    
```

add new application (port)
```
set applications application TCP_Port_(number) destination-port (number)
set applications application TCP_Port_(number) protocol tcp          
```

add new host to set of hosts in address book
```
set security zones security-zone (zone) address-book address-set (name_of_hosts) address Host_(ip)
set security zones security-zone (zone) address-book address Host_(ip) (ip)/32
set security zones security-zone (zone) address-book address Host_(ip) (ip)/32
```

checking that security policy applies
```
show security flow session source-prefix xxx.xxx.xxx.244 application smtp | refresh 3
show security match-policies from-zone mgmt to-zone untrust source-ip xxx.xxx.xxx.244 source-port 12345 destination-ip xxx.xxx.xxx.90 destination-port 25 protocol tcp
```


checking and commiting
```
show | compare
commit check
commit
```

committing with failover
```
TODO
```



show history of commits
```
request system software rollback
```

checking that policy is in use
```
show security policies hit-count | match (number)    
```


## MAINTENANCE

backup/restore configuration to file
stop commit server, that somebody will not commit config
```
request system commit server pause
```

delete old, save rescue configuration, check timestamp
```
request system configuration rescue delete
request system configuration rescue save
show system configuration rescue
show system rollback 0
```

at this point, configuration could be restored with "rollback" command
```
?? request system software rollback
```

save config, check
```
save dhcp-security-snoop config.dhcp-security-snoop.2019073
save dhcp-snooping config.dhcp-snooping.20190731.1024
    error: the ethernet-switching subsystem is not running
save dhcpv6-security-snoop config.dhcpv6-security-snoop.20190731.1025
file list detail
```

resume commit server, when ready
```
request system commit server pause start
```

copy from switch to usb memory
```
TODO
```
scp from switch
save scp://user@hostname/path/filename routing-instance instance-name source-address address
```

copy from ftp to switch
```
file copy ftp://anonymous:geg@test.jnpr.net/pub/junos/7.5R2.8/jinstall-7.5R2.8-domestic-signed.tgz /var/tmp/
```

copy from usb memory to switch
```
TODO
```


scp from local host to switch
```
TODO
```


restore configuration file
```
test configuration (file)
load (filename)
```

insert configuration into terminal, finish with C-D
```
test configuration terminal
```



## JUNOS UPGRADE

```
show version status
show version
show chassis firmware
```

attach USB and take a snapshot (flash will be repartitioned and content of USB memory will be erased)
```
request system snapshot
```

upload from usb memory
```
start shell user root
mkdir /var/tmp/usb
mkdir /var/tmp/downloads
```

connect usb
```
ls /dev/da*
mount_msdosfs /dev/da0s1 /var/tmp/usb
cp /var/tmp/usb(new-file) /var/tmp/downloads
umount /var/tmp/usb
```


upload via scp
```
TODO
```

validate package first
```
request system software validate /var/tmp/(new-filename)
```

applying new version
```
request system software add /var/tmp/(new-filename) validate
```

at this point last change to cancel upgrade by deleting install, otherwise reboot
request system reboot
