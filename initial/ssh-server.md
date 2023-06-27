= openSuSE =

sudo su
zypper install openssh
systemctl start sshd
systemctl status sshd
systemctl enable sshd
firewall-cmd --permanent --add-service=ssh
firewall-cmd --reload