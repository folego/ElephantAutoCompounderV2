import datetime
import math

def log(text, sameline=True):
    now = datetime.datetime.now()
    if sameline: linecontrol = '\r'
    else: linecontrol = '\n'
    print(now.strftime("%Y%m%d %H:%M:%S") + '> ' + text, end=linecontrol)


intervals = (
    ('weeks', 604800),  # 60 * 60 * 24 * 7
    ('days', 86400),    # 60 * 60 * 24
    ('hours', 3600),    # 60 * 60 
    ('minutes', 60),
    ('seconds', 1),
)
def display_friendly_time(seconds, granularity=2):
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(math.floor(value), name))
    return ', '.join(result[:granularity])    

def get_current_time_of_the_day():
    now = datetime.datetime.now()
    return int(now.strftime("%H"))

def get_current_day():
    return int(datetime.datetime.now().strftime("%d"))

def get_current_week_day():
    return datetime.datetime.now().weekday()