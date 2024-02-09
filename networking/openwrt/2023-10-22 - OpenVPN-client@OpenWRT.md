# create *.ovpn config file on server side (i.e. with 'pivpn add nopass' command in PiVPN)

in OpenWRT, open WebUI:

LuCi, System, Software, search and install packages:
```
openvpn-openssl
luci-app-openvpn
```
When done, navigate to:
LuCi, VPN
import *.ovpns config file, [x] enable and [Save and Apply], [Start]

ref
```
https://openwrt.org/docs/guide-user/services/vpn/openvpn/client-luci
```