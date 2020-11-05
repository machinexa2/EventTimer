from lib.ColoredObject import Color
from lib.TimeFunctions import seconds_from_time
# Note: For GMT only if event occurs in GMT+2 then subtract 2 hour, i.e if sth start in 17:00:00 GMT +2 then, set 15:00:00 with timeformat GMT

event_1 = {
    "event_name":"Pentesterlab Subscription Ends",
    "event_date":"2020-12-01",
    "event_time":"18:28:00",
    "event_timeformat":"GMT",
    "event_description":"For personal use!",
}

event_2 = {
    "event_name":"None",
    "event_date":"2030-01-01",
    "event_time":"12:00:00",
    "event_timeformat":"GMT",
    "event_description":"None",
}

event_3 = {
    "event_name":"None",
    "event_date":"2030-01-01",
    "event_time":"12:00:00",
    "event_timeformat":"GMT",
    "event_description":"None"
}
event_4 = {
    "event_name":"None",
    "event_date":"2030-01-01",
    "event_time":"12:00:00",
    "event_timeformat":"GMT",
    "event_description":"None"
}
"""
"""

# Anything having 5:45:00 is GMT +5:45 (timezone for Nepal)
pacific_to_ktm = seconds_from_time('00:45:00')
gmt_to_ktm = seconds_from_time('05:45:00')
est_to_ktm = seconds_from_time('04:00:00')
est_to_ktm += seconds_from_time('05:45:00')
cest_to_ktm = seconds_from_time('05:45:00')
cest_to_ktm -= seconds_from_time('02:00:00')

ColorObj = Color()
