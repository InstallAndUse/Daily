#!/usr/local/bin/python3

#
# this script will show time and date in different locations
# Author: Anton TETERIN
# web:    https://2dz.fi
#

# 2024-04-28  * init /A

from datetime import datetime
import pytz

ts_utc = pytz.utc

zones = [
    "UTC",
    "Europe/Dublin",
    "Europe/Madrid",
    "Europe/Paris",
    "Europe/Helsinki",
    "Europe/Moscow",
    "Asia/Riyadh",
    "Asia/Dubai",
    "Asia/Sakhalin"
]

for zone in zones:
  ts = pytz.timezone(zone)
  print ( "  ", datetime.now(ts).strftime("%Y-%m-%d %H:%M:%S"), " in ", ts )
