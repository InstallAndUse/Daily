#!/usr/local/bin/python3

#
# this script will show time and date in different locations
# Author: Anton TETERIN
# web:    https://2dz.fi

#
# list of zones:
# >>> from pytz import country_names, country_timezones
# >>> all_timezones = [country_timezones.get(country) for country in country_names]
# >>> all_timezones
#

# 2024-04-28  * init /A
# 2024-05-22  + doc to list timezones /A

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
    "Asia/Ho_Chi_Minh",
    "Asia/Bangkok",
    "Asia/Sakhalin",
]

for zone in zones:
  ts = pytz.timezone(zone)
  print ( "  ", datetime.now(ts).strftime("%Y-%m-%d %H:%M:%S"), " in ", ts )
