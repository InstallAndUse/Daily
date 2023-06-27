# 2022 03 19  + published on https://github.com/InstallAndUse/Daily /A

```
c_rehash .fetchmail_certs/
mkdir -p .fetchmail/ssl
echo | openssl s_client -connect (server):993 -showcerts 2>/dev/null | sed -ne '/BEGIN CERT/,/END CERT/p' > .fetchmail/ssl/avaruus.pem
openssl x509 -in .fetchmail/ssl/avaruus.pem -noout -md5 -fingerprint
```


Books:
- [Anton's bookshelf](https://og2k.com/books/)
