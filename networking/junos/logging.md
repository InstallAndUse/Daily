

observing logs:
```
show log messages.0.gz
```



saving logs

to ftp
```
sh log messages.0.gz | no-more | save ftp://username:password@A.B.C.D/directory/messages.0.txt
```



downloading logs over scp
```
scp (user)@(junos-host):/var/log/* .
```
or more specific:
```
scp (user)@(junos-host):/var/log/messages .
```



more:
https://supportportal.juniper.net/s/article/EX-QFX-How-to-collect-logs-and-files-from-standalone-and-Virtual-Chassis-VCF-devices?language=en_US
