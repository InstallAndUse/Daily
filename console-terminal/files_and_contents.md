# 2022 03 19  + published on https://github.com/InstallAndUse/Daily /A

locate readme

# find where what
find / -type f -name readme
find ./ -type d -exec chmod 0550 {} \;


# grep what where
fgrep -irl ldap *
fgrep -rl "class Anon" *
