# cisco switch

# users
show user-account
show running-config | include username

enter config mode
```
confugure terminal
```

create users
```
username (user) privilege 15 password (encrypted-password)
username (user) privilege 15 password 0 (plain-password)

username (user) role network-admin
username (user) password (pass)
```

remove user
```
#no username (user)
```

remember to save settings
```
#copy running-config startup-config
```

#
# interfaces
#

show int desc
show int stats
show int status
show vlanico  ne



conf term


# remove interfaces
default interface (if)
interface (if)
shutdown
exit

# enable interface
int gi0/7
  sw access vlan 777
  no shut
  desc (description)
exit
C+z

# configuring several
interface ethernet 4/17, ethernet 4/19, ethernet 4/21, ethernet 4/23

# save config
write mem
copy running-config startup-config
copy run start





How to recover/set/change enable password ?

Unplug the power cable to the switch.

Step 4: Press and hold the MODE button on the front of the switch and plug the power cable back into the switch at the same. After the power cable has been plugged in, wait a couple of seconds and then release the MODE button.

Step 5: Your display on your HyperTerminal should look like this… switch:

Step 6: Enter these commands into the switch
```
switch: flash_init
# switch: load_helper
# switch: dir flash:
```
Directory of flash:
```
13 drwx   192 Mar 01 1993 22:30:48 c2960-mz-124-0.0.53
11 -rwx   5825 Mar 01 1993 22:31:59 config.text
18 -rwx   720 Mar 01 1993 02:21:30 vlan.da

switch: rename flash:config.text flash:config.text.old
switch: boot
```
Step 7: Once the switch reboots, answer NO to “Would you like to enter system configuration dialog? [Yes/No]:

Step 8: Get into the privilege prompt.
```
Switch>enable
# Switch#rename flash:config.text.old flash:config.text
Switch#copy flash:config.text.original system:running-config
# Switch#copy flash:config.text system:running-config
Source filename [config.text]?
Destination filename [running-config]?
Press Enter to copy
```
Step 9: Get into global configuration
```
Switch#conf t
Switch (config)#enable secret password
```
Enter the password you would like

Step 10: Return to Privilege mode and save your config

```
Switch (config)#exit
Switch#copy run start
```

Step 11: reload switch
```
reload
```
