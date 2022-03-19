# 2022 03 19  + published on https://github.com/InstallAndUse/Daily /A

https://www.howtoforge.com/how-to-install-and-configure-mailman-with-postfix-on-debian-squeeze
https://help.ubuntu.com/community/Mailman

installing mailman

sudo apt-get install mailman
select ALL languages (english as well)
select default language
sudo newlist mailman
sudo service mailman start

sudo nano /etc/mailman/mm_cfg.py
sudo /usr/lib/mailman/bin/genaliases

sudo postconf -e 'relay_domains = lists.(domain)'
sudo postconf -e 'transport_maps = hash:/etc/postfix/transport'
sudo postconf -e 'mailman_destination_recipient_limit = 1'
sudo postconf -e 'alias_maps = hash:/etc/aliases, hash:/var/lib/mailman/data/aliases'

check:
sudo nano /etc/postfix/master.cf

    mailman   unix  -       n       n       -       -       pipe
      flags=FR user=list argv=/usr/lib/mailman/bin/postfix-to-mailman.py
      ${nexthop} ${user}

sudo nano /etc/postfix/transport
    lists.(domain) mailman:

sudo postmap -v /etc/postfix/transport

sudo nano /etc/aliases
    mailman:              "|/var/lib/mailman/mail/mailman post mailman"
    mailman-admin:        "|/var/lib/mailman/mail/mailman admin mailman"
    mailman-bounces:      "|/var/lib/mailman/mail/mailman bounces mailman"
    mailman-confirm:      "|/var/lib/mailman/mail/mailman confirm mailman"
    mailman-join:         "|/var/lib/mailman/mail/mailman join mailman"
    mailman-leave:        "|/var/lib/mailman/mail/mailman leave mailman"
    mailman-owner:        "|/var/lib/mailman/mail/mailman owner mailman"
    mailman-request:      "|/var/lib/mailman/mail/mailman request mailman"
    mailman-subscribe:    "|/var/lib/mailman/mail/mailman subscribe mailman"
    mailman-unsubscribe:  "|/var/lib/mailman/mail/mailman unsubscribe mailman"

sudo chown root:list /var/lib/mailman/data/aliases
sudo chown root:list /etc/aliases
sudo newaliases
sudo service postfix restart
sudo service mailman restart

testing:
sudo apt-get install mutt
nano .muttrc
    set mbox_type=Maildir
    set folder="~/Maildir"
    set mask="!^\\.[^.]"
    set mbox="~/Maildir"
    set record="+.Sent"
    set postponed="+.Drafts"
    set spoolfile="~/Maildir"
mutt


sudo cp /etc/mailman/apache.conf /etc/apache2/sites-available/mailman.conf
sudo nano /etc/apache2/sites-available/mailman.conf
  uncomment <VirtualHost>, check
sudo mkdir /var/www/lists
sudo a2ensite mailman.conf
sudo service apache2 restart

sudo nano /etc/mailman/mm_cfg.py
    DEFAULT_URL_PATTERN = 'http://%s/'

sudo a2enmod cgid


sudo newlist trac-(domain)
sudo list_lists

echo "(you)@(domain)" | sudo add_members -r - trac-(domain)
sudo list_members trac-(domain)




mailman.conf


<VirtualHost *>
    ServerName (domain)
    DocumentRoot /var/www/
    ErrorLog /var/log/apache2/lists-error.log
    CustomLog /var/log/apache2/lists-access.log combined

    <Directory /var/lib/mailman/archives/>
        Options FollowSymLinks
        AllowOverride None
    </Directory>

    Alias /pipermail/ /var/lib/mailman/archives/public/
    Alias /images/mailman/ /usr/share/images/mailman/
    ScriptAlias /admin /usr/lib/cgi-bin/mailman/admin
    ScriptAlias /admindb /usr/lib/cgi-bin/mailman/admindb
    ScriptAlias /confirm /usr/lib/cgi-bin/mailman/confirm
    ScriptAlias /create /usr/lib/cgi-bin/mailman/create
    ScriptAlias /edithtml /usr/lib/cgi-bin/mailman/edithtml
    ScriptAlias /listinfo /usr/lib/cgi-bin/mailman/listinfo
    ScriptAlias /options /usr/lib/cgi-bin/mailman/options
    ScriptAlias /private /usr/lib/cgi-bin/mailman/private
    ScriptAlias /rmlist /usr/lib/cgi-bin/mailman/rmlist
    ScriptAlias /roster /usr/lib/cgi-bin/mailman/roster
    ScriptAlias /subscribe /usr/lib/cgi-bin/mailman/subscribe
    ScriptAlias /mailman/ /usr/lib/cgi-bin/mailman/
</VirtualHost>


(you)@(domain):~/temp-mailman$ sudo nano fix_url.py
    DEFAULT_URL_PATTERN = 'https://%s/mailman/'
(you)@(domain):~/temp-mailman$ sudo withlist -l -r fix_url mailman
