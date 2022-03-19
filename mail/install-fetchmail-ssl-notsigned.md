# 2022 03 19  + published on https://github.com/InstallAndUse/Daily /A

(you)@lab2:~$ c_rehash .fetchmail_certs/
(you)@lab2:~$ mkdir -p .fetchmail/ssl
(you)@lab2:~$ echo | openssl s_client -connect (server):993 -showcerts 2>/dev/null | sed -ne '/BEGIN CERT/,/END CERT/p' > .fetchmail/ssl/avaruus.pem
(you)@lab2:~$ openssl x509 -in .fetchmail/ssl/avaruus.pem -noout -md5 -fingerprint
