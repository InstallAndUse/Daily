# 2022 03 19  + published on https://github.com/InstallAndUse/Daily /A

# assumed that evolution is installed and working properly


### ## #
# openpgp
### ## #

evolution, edit, preferences,
mail accounts,
select account, edit (double click)
security, Pretty Good Privacy (OpenPGP)
OpenPGP Key Id: (insert fingerprint here, without spaces)
select signing algorithm: default

# recipient has several email addresses in keypair,
# evolution refuses to send
# set keypair trust
gpg2 --edit-key BB8F40F041619xxxx47754xxxx8A11 trust
# 5 = I trust ultimately


### ## #
# p12 MIME
### ## #

evolution, edit, preferences,
certificates, your certificates, import
(pass),
mail accounts,
select account, edit (double click)
security, Secure MIME,
  signing certificate, [select], select cert, [ok]
  encryption certificate, [select], select cert, [ok]
select signing algorithm: default



Evolution issue:
Could not create message.
you may need to select different mail options.
Detailed error: Peer's Certificate issuer is not recognized. (-8179) - Cannot add SMIMEEncKeyPrefs attribute

https://askubuntu.com/questions/36300/error-when-sending-signed-mail-in-evolution
edit, [x] trust this ca to identify email users

# if you did not found your issuer in list, list certs
certutil -d sql:$HOME/.pki/nssdb -L

# find your certs nickname, set as trusted
certutil -d sql:$HOME/.pki/nssdb -M -n "(nickname)" -t Pu,Pu,Pu

# verify
certutil -d sql:$HOME/.pki/nssdb -L

# restart evolution



Books:
- [Anton's bookshelf](https://og2k.com/books/)
