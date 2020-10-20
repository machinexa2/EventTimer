from termcolor import colored

from lib.Globals import ColorObj
from lib.TimeFunctions import seconds_from_time, time_from_seconds

def print_from_seconds(second, edict):
    gmt_diff, india_diff = seconds_from_time('05:45:00'), seconds_from_time('00:15:00')
    nepal = colored(time_from_seconds(second), color='cyan')
    india = colored(time_from_seconds(second-india_diff), color='yellow')
    universal = colored(time_from_seconds(second-gmt_diff), color='red')
    if 'event_description' in edict.keys():
        print(f"{ColorObj.information} Event {colored(edict['event_name'], color='green', attrs=['bold'])}: {edict['event_description']}")
    else:
        print(f"{ColorObj.information} Event: {colored(edict['event_name'], color='green', attrs=['bold'])}")
    print(f"{ColorObj.good} Universal/UTC Time: {universal}, Nepali Time: {nepal}, Indian Time: {india} ")
    print("")
    return True
