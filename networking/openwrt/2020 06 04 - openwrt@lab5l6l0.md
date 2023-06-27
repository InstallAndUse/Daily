http://192.168.1.1
manual config
Linksys config panel, pass: admin
connectivity, flash firmware
https://downloads.openwrt.org/releases/19.07.2/targets/ipq40xx/generic/openwrt-19.07.2-ipq40xx-generic-linksys_ea6350v3-squashfs-factory.bin
http://192.168.1.1
LuCi, pass: admin
system
	system
		general
			sync time from browser
			hostname: xxxx
			timezone: xxxx
			[save]
		time synchronization
			[x] enable NTP client
			NTP server: xxxx
	administration
		router pass: set pass
		ssh access, check that enabled


network
	interfaces:
		LAN:
			general:
				static:
					192.168.5.1/255.255.255.0
				[disable] IPv6 assignment length
			advanced:
				[ ] ipv6 management
				[ ] force link
			DHCP-server:
				IPv6: disable everything
[save&apply]
[unsaved changed, apply&restart]
quickly reconnect ethernet cable, renew DHCP
login to apply settings (otherwise they will be reverted)
http://192.168.5.1


network
	wireless
		radio0, Generic 802.11bgn, scan
		(tablet-ssid)
			[x] replace wireless configuration
			name: wwan
			[x] lock to BSSID
			Create/assign firewall-zone: wan
		check:
			general
				mode: client
				ESSID: (tablet-ssid)
				network: wwan
[save]
[save&apply]

status
	overview
		check that connected

network
	wireless
		remove "openwrt"
		radio1, Generic 802.11nac, scan for free channel
		radio1, Generic 802.11nac, add
			general
				set channel
				mode: access point
				ESSID: xxx
				network: LAN
			wireless security
				encryption: WPA2-PSK
				cipher: auto
				key: wlan pass
[save]
[save&apply]








#
# softflowd
#
system
	software
		update lists
		filter: softflowd, install
