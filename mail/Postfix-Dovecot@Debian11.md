= Dovecot =
Install IMAP Server - Dovecot:
```bash
apt install dovecot-core dovecot-imapd
```


Configure mail storage to use Maildir (if needed)
```bash
vi /etc/dovecot/conf.d/10-mail.conf
```
```bash
mail_location = maildir:~/Maildir
```

Enable service and check
```bash
systemctl enable --now dovecot
systemctl restart dovecot
systemctl status dovecot
ss -ntap | grep dovecot
```


Make first connection with remote mail client, Maildir directory will be created
```bash
anton@gcp1mx1:~/Maildir$ ls -la
total 52
drwx------ 7 anton anton 4096 Feb  2 06:38 .
drwx------ 4 anton anton 4096 Feb  2 06:38 ..
drwx------ 5 anton anton 4096 Feb  2 06:38 .Drafts
drwx------ 5 anton anton 4096 Feb  2 06:38 .Trash
drwx------ 2 anton anton 4096 Feb  2 06:38 cur
-rw------- 1 anton anton   51 Feb  2 06:38 dovecot-uidlist
-rw------- 1 anton anton    8 Feb  2 06:38 dovecot-uidvalidity
-r--r--r-- 1 anton anton    0 Feb  2 06:38 dovecot-uidvalidity.65bc8dda
-rw------- 1 anton anton  320 Feb  2 06:38 dovecot.index.log
-rw------- 1 anton anton 2392 Feb  2 06:38 dovecot.list.index.log
-rw------- 1 anton anton   48 Feb  2 06:38 dovecot.mailbox.log
-rw------- 1 anton anton    0 Feb  2 06:38 maildirfolder
drwx------ 2 anton anton 4096 Feb  2 06:38 new
-rw------- 1 anton anton   18 Feb  2 06:38 subscriptions
drwx------ 2 anton anton 4096 Feb  2 06:38 tmp
```


Install CLI mail client compatible with Maildir - Mutt :
```bash
apt install mutt
```
Configure Mutt to use Maildir:
```bash
su - (user)
mutt
# 'E' exit greeting and exit
vi .muttrc
```
```bash
set mbox_type=Maildir
set spoolfile="~/Maildir/"
set folder="~/Maildir/"
set mask=".*"
set record="+.Sent"
set postponed="+.Drafts"

# Generate mailboxes for each maildir subdir
mailboxes ! + `\
for file in ~/Maildir/.*; do \
  box=$(basename "$file"); \
  if [ ! "$box" = '.' -a ! "$box" = '..' -a ! "$box" = '.customflags' \
      -a ! "$box" = '.subscriptions' ]; then \
   echo -n "\"+$box\" "; \
  fi; \
done`

# Marcos to display folder list when changing maildir folders
macro index c "<change-folder>?<toggle-mailboxes>" "open a different folder"
macro pager c "<change-folder>?<toggle-mailboxes>" "open a different folder"

# Macros to display folder list when copying/moving messages
macro index C "<copy-message>?<toggle-mailboxes>" "copy a message to a mailbox"
macro index M "<save-message>?<toggle-mailboxes>" "move a message to a mailbox"
```



= Postfix =
```bash
apt install postfix
dpkg-reconfigure postfix
```
Configuration
```bash
Internet Site
postmaster
domain: "mail.(your-domain), (your-domain), localhost, (others if needed)"
No
127.0.0.0/8 \[::ffff:127.0.0.0\]/104 \[::1\]/128 (trusted networks, i.e. 192.168.0.0/24 or 10.166.0.0/20)
0
+
all (or IPv4 only)
```

Service is enabled automatically, check it is running and listening
```bash
systemctl status postfix
ss -ntap | grep master
ss -lnpt | grep master
```


Configure Maildir mailbox format (if needed)
```bash
postconf -e 'home_mailbox = Maildir/'
```

Configure SMTP authentication (referring to dovecot's auth method)
```bash
postconf -e 'smtpd_sasl_type = dovecot'
postconf -e 'smtpd_sasl_path = private/auth'
postconf -e 'smtpd_sasl_local_domain ='
postconf -e 'smtpd_sasl_security_options = noanonymous,noplaintext'
postconf -e 'smtpd_sasl_tls_security_options = noanonymous'
postconf -e 'broken_sasl_auth_clients = yes'
postconf -e 'smtpd_sasl_auth_enable = yes'
postconf -e 'smtpd_recipient_restrictions = permit_sasl_authenticated,permit_mynetworks,reject_unauth_destination'
postconf -e 'smtpd_relay_restrictions = permit_mynetworks,permit_sasl_authenticated,defer_unauth_destination'
```

Configure TLS (secure connection to SMTP server)
```bash
postconf -e 'smtp_tls_security_level = may'
postconf -e 'smtpd_tls_security_level = may'
postconf -e 'smtp_tls_note_starttls_offer = yes'
# postconf -e 'smtpd_tls_key_file = /etc/ssl/private/server.key'
# postconf -e 'smtpd_tls_cert_file = /etc/ssl/certs/server.crt'
# we shall used already generated cert-key pait on the system
postconf -e 'smtpd_tls_key_file = /etc/ssl/private/ssl-cert-snakeoil.key'
postconf -e 'smtpd_tls_cert_file = /etc/ssl/certs/ssl-cert-snakeoil.pem'

# Enable for troubleshooting
#postconf -e 'smtpd_tls_loglevel = 1'
postconf -e 'smtpd_tls_received_header = yes'
postconf -e 'myhostname = (hostname)'
```



if own CA, then
```bash
postconf -e 'smtpd_tls_CAfile = /etc/ssl/certs/cacert.pem'
```

Restart and check Postfix
```bash
systemctl restart postfix
systemctl status postfix
```


Configure SASL
```bash
vi /etc/dovecot/conf.d/10-master.conf
```
```bash
  # Postfix smtp-auth
  unix_listener /var/spool/postfix/private/auth {
    mode = 0660
    user = postfix
    group = postfix
  }
```
```bash
vi /etc/dovecot/conf.d/10-auth.conf
```
```bash
auth_mechanisms = plain login
```
Restart Dovecot
```bash
systemctl restart dovecot
```

Test environment
```bash
apt install telnet
telnet 127.0.0.1 25
# CTRL+] to get 'Escape character is '^]'.' and type 'quit'
```

---todo---
Enabling SMTPS
```bash
vi /etc/postfix/master.cf
```
---todo---



Install Mail utils
```bash
apt install mailutils
```

Setting up defaults for system to use Maildir
```bash
echo 'export MAIL=~/Maildir' | sudo tee -a /etc/bash.bashrc | sudo tee -a /etc/profile.d/mail.sh
vi /etc/s-nail.rc

```
