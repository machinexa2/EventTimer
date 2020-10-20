#!/usr/bin/python3
from os import system
from time import sleep
from datetime import date, datetime

from lib.TimeFunctions import seconds_from_time
from lib.PrintFunctions import print_from_seconds
from lib.DateFunctions import seconds_from_date, date_from_seconds
from lib.Globals import gmt_to_ktm, est_to_ktm, cest_to_ktm, pacific_to_ktm, ColorObj
from lib.Globals import *

current_time = seconds_from_time(datetime.now().strftime("%H:%M:%S"))
current_date = seconds_from_date(date.today().isoformat())
current_seconds = current_time + current_date

system('clear')

def EventSeconds(edict: dict):
    if edict["event_timeformat"] == "GMT" or edict["event_timeformat"] == "UTC":
        event_seconds = int(seconds_from_date(edict["event_date"])) + int(seconds_from_time(edict["event_time"])) + int(gmt_to_ktm)
    elif edict["event_timeformat"] == "PCT":
        event_seconds = int(seconds_from_date(edict["event_date"])) + int(seconds_from_time(edict["event_time"])) +int(pacific_to_ktm)
    elif edict["event_timeformat"] == "EST":
        event_seconds = int(seconds_from_date(edict["event_date"])) + int(seconds_from_time(edict["event_time"])) + int(est_to_ktm)
    elif edict["event_timeformat"] == "CEST":
        event_seconds = int(seconds_from_date(edict["event_date"])) + int(seconds_from_time(edict["event_time"])) + int(cest_to_ktm)
    return event_seconds

def CounterSeconds(edict):
    global current_seconds
    event_seconds = EventSeconds(edict)
    cdate, seconds = date_from_seconds(event_seconds-current_seconds)
    counter_seconds = seconds_from_date(cdate) + int(seconds)
    return counter_seconds

if __name__ == '__main__':
    counter_1 = CounterSeconds(event_1)
    #counter_2 = CounterSeconds(event_2)
    #counter_3 = CounterSeconds(event_3)
    #counter_4 = CounterSeconds(event_4)

    try:
        while True:
            print("\x1b[%d;%dH" % (1, 1), end="")
            print_from_seconds(counter_1, event_1)
            #print_from_seconds(counter_2, event_2)
            #print_from_seconds(counter_3, event_3)
            #print_from_seconds(counter_4, event_4)
            counter_1 -= 1
            #counter_2 -= 1
            #counter_3 -= 1
            #counter_4 -= 1
            sleep(1)
    except KeyboardInterrupt:
        print(f"{ColorObj.bad} Exiting")
        import sys
        sys.exit()
