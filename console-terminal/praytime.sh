### ## #
#
# show Islamic prayer times
#
# 2018 10 08  + initial /A
# 2019 12 14  * fix /A
# 2019 03 17  * updated installation instructions /A
# 2020 12 24  * updated /A
# 2024-02-11  * updated for Debian 11.8 /A
#
### ## #

## Fedora 29,31
# yum install libitl
# from link get the latest package
#    http://www.rpm-find.net/linux/rpm2html/search.php?query=itools
# and install it
#    rpm -ivh itools-1.0-7.fc15.x86_64.rpm
# or
#    dnf install itools-1.0-6.fc14.x86_64.rpm

## Debian 11.8
#    apt install itools

echo "---------------------------------------------------------"
echo "Now is:"
date
echo ""
echo "For Riyadh, KSA:"
ipraytime --brief -lat 24.4827 -lon 46.3945 -u 3 -a 6 -h24
echo ""

echo "For Mersin, Turkey:"
ipraytime --brief -lat 36.63890968272466 -lon 34.36292102081904 -u 3 -a 1 -h24
echo "---------------------------------------------------------"