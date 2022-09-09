## CISCO ASA 5505
ciscoasa# show version

# factory defaults
? configure factory-default
confreg 0x2040
relo

# reset password
# on console, during boot, hit ESC, enter ROMMON mode
confreg 0x41
boot

# disable rebooting to normal state again
ciscoasa(config)# config-register 0x1

# after reboot, password is empty, set enable's password
# (very strong password, use different admin user to process changes)
enable password (password)

# set hostname, print label, attach to device
hostname (hostname)

# enter config mode
enable
configure terminal

# no callhome, please
(config)# clear configure call-home
(config)# no service call-home

# set clock
ciscoasa# show clock
ciscoasa# clock set 07:29:00 May 06 2019
ciscoasa(config)# clock timezone UTC +3
# if DST presents
ciscoasa(config)# clock summer-time MST recurring 1 Sunday April 2:00 last Sunday October 2:00

# set NTP
# ntp server ip_address [ key key_id ] [ source interface_name ] [ prefer ]
hostname(config)# ntp server 10.1.1.1 key 1 prefer
sh ntp associations
sh ntp status

# configure DNS
#  Enables the ASA to send DNS requests to a DNS server to perform a name lookup for supported commands.
# dns domain-lookup interface_name
hostname(config)# dns domain-lookup inside

# Specifies the DNS server group that the ASA uses for outgoing requests.
# dns server-group DefaultDNS
hostname(config)# dns server-group DefaultDNS

# Specifies one or more DNS servers. You can enter all six IP addresses in the same command, separated by spaces,
# name-server ip_address [ip_address2] [...] [ip_address6]
hostname(config-dns-server-group)# name-server 10.1.1.5 192.168.1.67 209.165.201.6


# disable call-home function

# Enable Management Access with ASDM
# [Location of ASDM image on the ASA]
ASA(config)# asdm image disk0:/asdm-647.bin
# [Enable the http server on the device ]
ASA(config)# http server enable
# [Tell the device which IP addresses are allowed to connect with HTTP (ASDM)]
ASA(config)# http 10.10.10.0 255.255.255.0 inside
# [Configure user/pass to login with ASDM]
ASA(config)# username admin password adminpass


# DHCP (Assign IP addresses to computers from the ASA device)
# [Create a DHCP address pool to assign to clients. This address pool must be on the same subnet as the ASA interface]
ciscoasa(config)# dhcpd address 192.168.1.101-192.168.1.110 inside
# [The DNS servers to assign to clients via DHCP]
ciscoasa(config)# dhcpd dns 8.8.8.8 8.8.8.8
# [Enable the DHCP server on the inside interface]
ciscoasa(config)# dhcpd enable inside


# Permit Traffic Between Same Security Levels
# [Permits communication between different interfaces that have the same security level.]
ciscoasa(config)# same-security-traffic permit inter-interface
# [Permits traffic to enter and exit the same interface.]
ciscoasa(config)# same-security-traffic permit intra-interface


# Useful Verification and Troubleshooting Commands
# [Shows hit-counts on ACL with name “OUTSIDE-IN”. It shows how many hits each entry has on the ACL]
ciscoasa# show access-list OUTSIDE-IN
Sample output:
access-list OUTSIDE-IN line 1 extended permit tcp 100.100.100.0 255.255.255.0 10.10.10.0 255.255.255.0 eq telnet (hitcnt=15) 0xca10ca21

# [The show conn command displays the number of active TCP and UDP connections, and provides information about connections of various types.]
ciscoasa# show conn
# [Shows all the connections through the appliance]
ciscoasa# show conn all
# [Shows HTTP GET, H323, and SIP connections that are in the “up” state]
ciscoasa# show conn state up,http_get,h323,sip
# [Shows overall connection counts]
ciscoasa# show conn count
54 in use, 123 most used

# [show CPU utilization]
ciscoasa# show cpu usage

# [List the contents of the internal flash disk of the ASA]
ciscoasa# show disk

# [Displays operating information about hardware system components such as CPU, fans, power supply, temperature etc]
ciscoasa# show environment

# [Displays maximum physical memory and current free memory]
ciscoasa# show memory

# [Displays information about Active/Standby failover status] (ERROR: Command requires failover license)
ciscoasa# show failover

# [Shows information about Interfaces, such as line status, packets received/sent, IP address etc]
ciscoasa# show interface

# [Displays the network states of local hosts. A local-host is created for any host that forwards traffic to, or through, the ASA.]
ciscoasa# show local-host

# [Displays the routing table]
ciscoasa# show route

# [Displays information about NAT sessions]
ciscoasa# show xlate


# show configs
ciscoasa# show startup-config
ciscoasa# show running-config

# save configs to memory
ciscoasa# copy run start
Source filename [running-config] ?
# [enter] to confirm
# or (will not ask source)
ciscoasa# write memory

# enable logging
ASA(config)# logging enable
ASA(config)# logging timestamp
ASA(config)# logging buffer-size 65536
ASA(config)# logging buffered warnings
ASA(config)# logging asdm errors
# send to syslog, if needed
ASA(config)# logging host inside 192.168.1.30
ASA(config)# logging trap errors

# permit local aaa
hostname(config)# aaa authorization exec authentication-server

# add user
username (username) nopassword

# list users

# change password of user
username (username) password (password)

# delete user

# give user privileges
username (username) password (password) privilege 15
username (username) attributes
ciscoasa(config-username)# service-type admin
ciscoasa(config-username)# service-type nas-prompt
ciscoasa(config-username)# service-type remote-access
ciscoasa(config-username)# exit


# add ssh access
ASA#configure terminal
ASA(config)#domain-name local.local
     ASA(config)#aaa authentication ssh console LOCAL
ciscoasa(config)#aaa authentication ssh console LOCAL
                 aaa authentication ssh console LOCAL
ciscoasa(config)#crypto key generate rsa modulus 2048
     ASA(config)#crypto key generate rsa general-keys modulus 1024
ASA(config)#ssh 192.168.1.10 255.255.255.255 inside
ASA(config)#ssh 0.0.0.0 0.0.0.0 OUTSIDE
# verify which encryptions are enabled

# connect via ssh (some routers use SSH1)
show ssh

# Image Software Management
# [Copy image file from TFTP to Flash of ASA]
ciscoasa# copy tftp flash


# copy file to USB
# download file (firmware, config) from device

# upload file
# copy file from USB

# upgrade firmware
# [At next reboot, the firewall will use the software image “asa911-k8.bin” from flash]
ciscoasa(config)# boot system flash:/asa911-k8.bin

# show interfaces
show interface ip brief
show switch vlan

# set up interfaces for VLAN interfaces (example: outside-inside)
ciscoasa(config)# interface Vlan 10
ciscoasa(config-if)# nameif outside
ciscoasa(config-if)# security-level 80
ciscoasa(config-if)# ip address 192.168.100.77 255.225.255.0
ciscoasa(config-if)# no shutdown
ciscoasa(config-if)# exit

ciscoasa(config)# interface Vlan 20
ciscoasa(config-if)# nameif lab5
ciscoasa(config-if)# security-level 90
ciscoasa(config-if)# ip address 192.168.2.1 255.225.255.0
ciscoasa(config-if)# no shutdown
ciscoasa(config-if)# exit

ciscoasa(config)# interface Ethernet 0/0
ciscoasa(config-if)# no nameif
ciscoasa(config-if)# no security-level
ciscoasa(config-if)# no ip address
ciscoasa(config-if)# switchport access vlan 10
ciscoasa(config-if)# no shutdown
ciscoasa(config-if)# exit

# (same for 0/6 PoE, deskphone)
ciscoasa(config)# interface Ethernet 0/6

# Step 5: Configure PAT on the outside interface
ASA5505(config)# global (outside) 1 interface
ASA5505(config)# nat (inside) 1 0.0.0.0 0.0.0.0

# for ASA 8.3 and later:
object network obj_any
subnet 0.0.0.0 0.0.0.0
nat (inside,outside) dynamic interface

# to check PoE status
show power inline

# configure interface to use DHCP client and set default route provided
ciscoasa(config-if)# ip address dhcp setroute

show nameif

# trunk port
show interfaces trunk
(config-if)#interface gigabitEthernet 0/23
(config-if)#description Trunk port to (host)
(config-if)#switchport mode trunk
(config-if)#switchport trunk allowed vlan all
(config-if)#switchport trunk allowed vlan 2-4094
no shutdown

# access port
(config)#interface gigabitEthernet 0/23
(config-if)#description (host)
(config-if)#switchport mode access
(config-if)#switchport access vlan 128
(config-if)#no shutdown
# or
ciscoasa(config)# interface Ethernet 0/1
ciscoasa(config-if)# no nameif
ciscoasa(config-if)# no security-level
ciscoasa(config-if)# no ip address
ciscoasa(config-if)# switchport access 20
ciscoasa(config-if)# no shutdown
ciscoasa(config-if)# exit




# Static and Default Routes
# MORE READING:  Cisco ASA Firewall in Transparent Layer2 Mode
# [Configure a default route via the “outside” interface with gateway IP of 100.1.1.1 ]
ciscoasa(config)# route outside 0.0.0.0 0.0.0.0 100.1.1.1

# routing (traffic to modem of ISP)
ciscoasa(config-if)# route outside 0.0.0.0 0.0.0.0 192.168.100.1 1

# [Configure a static route via the “inside” interface. To reach network 192.168.2.0/24 go via gateway IP 192.168.1.1 ]
ciscoasa(config)# route inside 192.168.2.0 255.255.255.0 192.168.1.1

# same level security traffic
hostname(config)# same-security-traffic permit inter-interface




# The absolutely necessary Interface Sub-commands that you need to configure in order for the interface to pass traffic are the following:
# Assigns a name to an interface
nameif “interface name”
# Assigns an IP address to the interface
ip address “ip_address” “subnet_mask”
# Assigns a security level to the interface
security-level “number 0 to 100”
# By default all interfaces are shut down, so enable them.
no shutdown



# Network Address Translation (NAT)
[Configure PAT for internal LAN (192.168.1.0/24) to access the Internet using the outside interface]
ciscoasa(config)# object network internal_lan
ciscoasa(config-network-object)# subnet 192.168.1.0 255.255.255.0
ciscoasa(config-network-object)# nat (inside,outside) dynamic interface

# [Configure PAT for all (“any”) networks to access the Internet using the outside interface]
ciscoasa(config)# object network obj_any
ciscoasa(config-network-object)# subnet 0.0.0.0 0.0.0.0
ciscoasa(config-network-object)# nat  (any,outside) dynamic interface

# [Configure static NAT. The private IP 192.168.1.1 in DMZ will be mapped statically to public IP 100.1.1.1 in outside zone]
ciscoasa(config)# object network web_server_static
ciscoasa(config-network-object)# host 192.168.1.1
ciscoasa(config-network-object)# nat (DMZ , outside) static 100.1.1.1

# [Configure static Port NAT. The private IP 192.168.1.1 in DMZ will be mapped statically to public IP 100.1.1.1 in outside zone only for port 80]
ciscoasa(config)# object network web_server_static
ciscoasa(config-network-object)# host 192.168.1.1
ciscoasa(config-network-object)# nat (DMZ , outside) static 100.1.1.1 service tcp 80 80










# FIREWALL
# Access Control Lists (ACL)

# show
show run access-list (host)
show access-list (host)

# [Apply the ACL above at the “outside” interface for traffic coming “in” the interface]
ciscoasa(config)# access-group OUTSIDE_IN in interface outside
ciscoasa(config)# access-group INSIDE_IN in interface inside

# [Create an ACL to allow TCP access from “any” source IP to host 192.168.1.1 port 80]
ciscoasa(config)# access-list OUTSIDE_IN extended permit tcp any host 192.168.1.1 eq 80

# [Create an ACL to deny all traffic from host 192.168.1.1 to any destination and allow everything else. This ACL is then applied at the “inside” interface for traffic coming “in” the interface]
ciscoasa(config)# access-list INSIDE_IN extended deny ip host 192.168.1.1 any
ciscoasa(config)# access-list INSIDE_IN extended permit ip any any


# Object Groups
# [Create a network group having two hosts (192.168.1.1 and 192.168.1.2). This group can be used in other configuration commands such as ACLs]
ciscoasa(config)# object-group network WEB_SRV
ciscoasa(config-network)# network-object host 192.168.1.1
ciscoasa(config-network)# network-object host 192.168.1.2

# [Create a network group having two subnets (10.1.1.0/24 and 10.2.2.0/24). This group can be used in other configuration commands such as ACLs]
ciscoasa(config)# object-group network DMZ_SUBNETS
ciscoasa(config-network)# network-object 10.1.1.0 255.255.255.0
ciscoasa(config-network)# network-object 10.2.2.0 255.255.255.0

# [Create a service group having several ports. This group can be used in other configuration commands such as ACLs]
ciscoasa(config)# object-group service DMZ_SERVICES tcp
ciscoasa(config-service)# port-object eq http
ciscoasa(config-service)# port-object eq https
ciscoasa(config-service)# port-object range 21 23

# [Example of using object groups in ACLs]
ciscoasa(config)# access-list OUTSIDE-IN extended permit tcp any object-group DMZ_SUBNETS object-group DMZ_SERVICES

# create group
(config)# object-group network (hostgroup)

# add object into group
(config-network-object-group)# network-object object (newhost)

# show objects
show object-group network
exit

# edit objects
object network (newhost)
host (ip)





# CISCO FIREWALL:

# enable SSH
https://www.opentechguides.com/how-to/article/cisco/39/Cisco-configure-ssh.html

# CHECKING EXISTING
show running-config | include (ip-from)
show running-config | include (ip-to)
show access-list outside_in
show run | include (ip)
show (ip)

# interfaces
show interfaces status

# access-groups
show configuration | include access-group
ip access-group access-list-name {in | out}
no ip access-group access-list-name {in | out}

# let host out:
access-list (zone) extended permit udp host (ip) host (ip) eq (port)
access-list (zone) extended permit tcp host (ip) host (ip) eq (port)
access-list (zone) extended permit tcp any4 host (ip) eq https

# write configuration
wr (copy running-config startup-config)
wr
write mem

# capturing
capture capin interface outside match tcp host (host) host (host) eq (port)
show capture
show capture capin

# general commands
show run | include route

# enable unsupported tranceiver
service unsupported-transceiver
no errdisable detect cause gbic-invalid



# save (commit)
write mem


# set up VPN
# [show details about IPSEC VPNs like packets encrypted/decrypted, tunnel peers etc]
ciscoasa# show crypto ipsec sa
# [show details if an IPSEC VPN tunnel is up or not. MM_ACTIVE means the tunnel is up]
ciscoasa# show crypto isakmp sa







### sources:
https://www.cisco.com/c/en/us/td/docs/security/asa/asa82/configuration/guide/config.html
https://www.cisco.com/c/en/us/td/docs/security/asa/asa82/configuration/guide/config/access_aaa.html

https://www.cisco.com/c/en/us/td/docs/security/asa/asa92/configuration/general/asa-general-cli/interface-basic-5505.pdf
https://www.cisco.com/c/en/us/td/docs/security/asa/asa91/configuration/general/asa_91_general_config/route_static.pdf




Books:
- [Anton's bookshelf](https://og2k.com/books/)
