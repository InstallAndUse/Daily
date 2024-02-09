Connect to router and update OS before installation (that will request a build)
```bash
ssh root@(router)
opkg update
opkg install auc
auc
```

Output:
```bash
Are you sure you want to continue the upgrade process? [N/y] y
Requesting build........................................................................
Downloading image from https://sysupgrade.openwrt.org/store/c0445c2842532e39e98efeede77b6731/openwrt-22.03.5-4deda7068699-ipq40xx-generic-linksys_ea6350v3-squashfs-sysupgrade.bin
Writing to 'openwrt-22.03.5-4deda7068699-ipq40xx-generic-linksys_ea6350v3-squashfs-sysupgrade.bin'
image verification succeeded
invoking sysupgrade

client_loop: send disconnect: Broken pipe

anton-pvt@ant1mbp3 ~ % ssh root@(router)
root@(router)'s password:


BusyBox v1.35.0 (2023-09-24 19:31:42 UTC) built-in shell (ash)

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 -----------------------------------------------------
 OpenWrt 22.03.5, r20134-5f15225c1e
 -----------------------------------------------------
root@(router):~#
```

Update opkg DB and install AdHomeGuard
```bash
opkg update
opkg install adguardhome
Installing adguardhome (0.107.21-1) to root...
Downloading https://downloads.openwrt.org/releases/22.03.5/packages/arm_cortex-a7_neon-vfpv4/packages/adguardhome_0.107.21-1_arm_cortex-a7_neon-vfpv4.ipk
Configuring adguardhome.
```

Checking does it runs and which port
```bash
netstat -ntap | grep AdGuardHome
tcp        0      0 :::3000                 :::*                    LISTEN      2885/AdGuardHome
```


Open WebUI in browser (beware, it is HTTP, not HTTPS by default)
```
http://(router):3000
```


Initial instructions
```
http://192.168.71.1:3000/install.html
Step 1/5
[Get Started]

Step 2/5
Admin Web Interface - 'All Interfaces' (Recommended: change to internal one, if you would like to limit access only from inside of network)
Choose a port other than 80 (which may be used already by another process, probably by LuCi)
```
'br-lan 192.168.71.1' port '1080'
```

At this point, it is important to understand what you are doing:
settings up additional DNS server aside with current running one, replacing it and reconfiguring it might effect name resolution and access to Internet.

There are instructions how to replace current running DNS, but that is solution, I would not advice, because OS's own name resolution might be effected.
The main idea is that, we are enabling DNS resolution for end clients, not for OS router itself.
I advice to set up AdGuardHome DNS server running on different port: for example, 1053 and point a name resolution traffic to it.

Listening interface: (Recommended: change to internal one, if you would like to limit access only from inside of network)
```
'br-lan 192.168.71.1' port '1053'
```

Static IP Address
AdGuard Home is a server so it needs a static IP address to function properly. Otherwise, at some point, your router may assign a different IP address to this device.
AdGuard Home cannot configure it automatically for this network interface. Please look for an instruction on how to do this manually.
[avoiding this message for now]


Step 3/5
Creating admin credentials

Step 4,5/5
read and confirm

```


Check processes are running and listening for incoming traffic
```
netstat -ntap | grep AdGuardHome
tcp        0      0 192.168.71.1:1080       0.0.0.0:*               LISTEN      2885/AdGuardHome    <--- dashboard
tcp        0      0 192.168.71.1:1053       0.0.0.0:*               LISTEN      2885/AdGuardHome    <--- DNS server
[...]
```

Change OpenWRT default DNS listening port to something other that 53
```
https://192.168.71.1/cgi-bin/luci/admin/network/dhcp
DHCP and DNS
Dnsmasq is a lightweight DHCP server and DNS forwarder.
"Advanced Settings" tab
Set "DNS server port" to 2053
[Save & Apply]
```

Check from process is changed listening port
```
root@hlm1gw:~# netstat -ntap | grep dnsmasq
tcp        0      0 127.0.0.1:2053          0.0.0.0:*               LISTEN      3206/dnsmasq
tcp        0      0 192.168.1.100:2053      0.0.0.0:*               LISTEN      3206/dnsmasq
tcp        0      0 192.168.71.1:2053       0.0.0.0:*               LISTEN      3206/dnsmasq
tcp        0      0 ::1:2053                :::*                    LISTEN      3206/dnsmasq
tcp        0      0 fe80::6238:e0ff:fe9b:984a:2053 :::*                    LISTEN      3206/dnsmasq
tcp        0      0 fd98:4463:7c5a::1:2053  :::*                    LISTEN      3206/dnsmasq
tcp        0      0 fe80::6238:e0ff:fe9b:984b:2053 :::*                    LISTEN      3206/dnsmasq
tcp        0      0 fe80::6238:e0ff:fe9b:984c:2053 :::*                    LISTEN      3206/dnsmasq
tcp        0      0 fe80::6238:e0ff:fe9b:984d:2053 :::*                    LISTEN      3206/dnsmasq
```

Change AdHomeGuard's DNS listening port to 53.
```bash
root@hlm1gw:~# vi /etc/adguardhome.yaml
change bind port for DNS server
service  adguardhome restart
```


Disable dnsmasq on OpenWRT
```
https://192.168.71.1/cgi-bin/luci/admin/system/startup
Startup, dnsmasq, [Disabled], [Stop]
```


Point local traffic to AdHome Guard
do not edit ```/etc/resolv.conf```, it will be overwritten on reboot
```
https://192.168.71.1/cgi-bin/luci/admin/network/network
Interfaces >> wan, "Advanced Settings":
Uncheck [ ] "Use DNS servers advertised by peer"
Set "Use custom DNS servers" to "192.168.71.1"
```

Reboot OpenWRT to validate setup
```
System > Reboot
```




# to forward DNS requests to specific servers by doing:
uci add_list dhcp.@dnsmasq[0].server="192.168.71.1"
uci commit dhcp


uci set network.wan.peerdns="0"
uci set network.wan6.peerdns="0"
uci -q delete network.wan.dns
uci -q delete network.wan6.dns
uci add_list network.wan.dns="192.168.71.1"
uci commit network
service network reload


# as long, as /etc/resolv.conf is used by many system tools, DNS resolver must be listening there:
```bash
cat /etc/resolv.conf
search lan
nameserver 127.0.0.1
nameserver ::1

netstat -ntap | grep 53
tcp        0      0 127.0.0.1:2053          0.0.0.0:*               LISTEN      4405/dnsmasq
tcp        0      0 192.168.1.100:2053      0.0.0.0:*               LISTEN      4405/dnsmasq
tcp        0      0 192.168.71.1:2053       0.0.0.0:*               LISTEN      4405/dnsmasq
tcp        0      0 192.168.71.1:53         0.0.0.0:*               LISTEN      1128/AdGuardHome
tcp        0      0 192.168.71.1:22         192.168.71.106:53246    ESTABLISHED 3810/dropbear
```

# fix issue with OpenWRT local DNS resolution by binding AdGuardHome to localhost, as well

```bash
vi /etc/adguardhome.yaml
---edit---
dns:
  bind_hosts:
    - 192.168.71.1
    # add localhost below
    - 127.0.0.1
---edit---


service adguardhome restart

root@hlm1gw:~# netstat -ntap | grep 53
tcp        0      0 127.0.0.1:2053          0.0.0.0:*               LISTEN      4405/dnsmasq
tcp        0      0 192.168.1.100:2053      0.0.0.0:*               LISTEN      4405/dnsmasq
tcp        0      0 192.168.71.1:2053       0.0.0.0:*               LISTEN      4405/dnsmasq
tcp        0      0 127.0.0.1:53            0.0.0.0:*               LISTEN      5093/AdGuardHome <<
tcp        0      0 192.168.71.1:53         0.0.0.0:*               LISTEN      5093/AdGuardHome
tcp        0      0 192.168.71.1:22         192.168.71.106:53246    ESTABLISHED 3810/dropbear
```



ref:
```
https://openwrt.org/docs/guide-user/base-system/dhcp_configuration
```