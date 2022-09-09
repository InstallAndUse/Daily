# 2022 03 19  + published on https://github.com/InstallAndUse/Daily /A

howto: sending mail using apache/php mail() via msmtp

(you)@lab2:~$ echo -e "From: alice@example.com \n\
> To: bob@domain.com \n\
> Subject: Hello World \n\
> \n\
> This email was sent using MSMTP via Gmail/Yahoo." >> sample_email.txt
(you)@lab2:~$ emacs sample_email.txt
(you)@lab2:~$ cat sample_email.txt
From: alice@example.com
To: (sender)@(host).com
Subject: Hello World

This email was sent using MSMTP via Gmail/Yahoo.

(you)@lab2:~$ cat sample_email.txt | msmtp --debug -a (domain) (sender)@(host).com
(you)@lab2:~$ sudo cp -p .msmtprc /etc/php5/apache2/.msmtp_php
(you)@lab2:~$ sudo chown www-data:www-data /etc/php5/apache2/.msmtp_php

(you)@lab2:~$ sudo pico /etc/php5/apache2/php.ini
    sendmail_path = "/usr/bin/msmtp -C /etc/php5/apache2/.msmtp_php --logfile /var/log/msmtp.log -a (domain) -t"


(you)@lab2:~$ sudo touch /var/log/msmtp.log
(you)@lab2:~$ sudo chown www-data:www-data /var/log/msmtp.log



Books:
- [Anton's bookshelf](https://og2k.com/books/)
