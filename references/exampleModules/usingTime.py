"""
Using the Time module.

Created on Sat Aug 29 10:01:06 2020.

@author: omgitskuei
"""
# -*- coding: utf-8 -*-

import time

"""
[time.time()] returns number of seconds since Jan 1, 1970

For example, to find out how long parts of your program take to run, you
can record the time at the beginning and end, and compare the values.
"""
print(time.time())
# 1598771533.3746486


def lots_of_numbers(max):
    """
    Print how much time the function took.

    Parameters
    ----------
    max : int
        A number for how many times to run the for-loop.

    Returns
    -------
    None.

    """
    t1 = time.time()
    for x in range(0, max):
        print(x)
    t2 = time.time()
    print('It took %s seconds' % (t2-t1))


lots_of_numbers(8)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# It took 0.0009996891021728516 seconds


"""
[time.asctime()] function returns current datetime in a readable format

It can take a tuple (aka. immutable list) as a parameter - if no t is
provided, time.localtime() is used by default.
"""
print(time.asctime())
# Sun Aug 30 15:21:14 2020
print(time.asctime(time.localtime()))
# Sun Aug 30 15:21:14 2020

# (year, month, day, hour, min, sec, weekday, yearday, daylightsavings)
t = (2020, 2, 23, 10, 30, 48, 4, 2, 0)
print(time.asctime(t))
# Sun Feb 23 10:30:48 2020


"""
[time.localtime()] returns current datetime AS AN OBJECT Tuple

(year, month, day, hour, minute, sec, weekday, yearday, daylightsavings*)

* tm_isdst may be set to 1 when daylight savings time is in effect, and 0
when it is not. A value of -1 indicates that this is not known, and will
usually result in the correct state being filled in.

When a tuple with an incorrect length is passed to a function expecting a
struct_time, or having elements of the wrong type, a TypeError is raised.
"""
localTime = time.localtime()
print(localTime)
# time.struct_time(tm_year=2020, tm_mon=2, tm_mday=23, tm_hour=22,
# tm_min=18, tm_sec=39, tm_wday=0, tm_yday=73, tm_isdst=0)
year = localTime[0]
month = localTime[1]
day = localTime[2]
hour = localTime[3]
minute = localTime[4]
sec = localTime[5]
weekday = localTime[6]
# tm_wday: 0 (Monday) to 6 (Sunday)
yearday = localTime[7]
# tm_yday: 1 to 366
daylightsavings = localTime[8]
# tm_isdst: daylight savings time 1 true, 0 false, -1 unknown autofill

# Convert to readible date
print(time.asctime(time.localtime()))
# Sun Aug 30 15:21:14 2020


"""
[time.sleep(x)] delays program execution by x seconds.
"""
# print 1 to 10, with 1 sec delay between each number
for x in range(1, 11):
    print(x)
    time.sleep(1)
