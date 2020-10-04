#!/usr/bin/env python3
# coding=utf-8

__appname__ = 'weekly_date.py'
__version__ = '0.01'
__date__    = '2020/10/02'

#  -- Values --  #
CHARACTER_CODE  = "utf-8"
#CHARACTER_CODE  = "shift_jis"
#  ------------  #

from datetime import datetime
from datetime import timedelta

# '%Y-%m-%d' で指定された日付を含む週のプチカレンダーを print
class WeeklyDate(object):

    def __init__(self, datestr):
        self.skeleton = """
**yyyy年 weeknum週 (startdate - enddate)**

```
startdate - enddate
★
mo tu we th fr sa su    start=
d1 d2 d3 d4 d5 d6 d7    end  =





---
[完了]


```
"""
        self.datetime = datetime.strptime(datestr, '%Y-%m-%d')
        year_weeknum_day = self.datetime.isocalendar()
        self.year = year_weeknum_day[0]
        self.week_num = year_weeknum_day[1]
        self.day_of_the_week = year_weeknum_day[2]
        self.weekly_todo_str = self.skeleton
        self.weekly_dates_list = []
        for i in range(1,8):
            tdatetime = self.datetime
            tdatetime +=timedelta(days=-(self.day_of_the_week - i))
            self.weekly_dates_list.append(tdatetime.strftime("%Y/%m/%d"))
        self.weekly_todo_str = self.weekly_todo_str.replace("d1", self.weekly_dates_list[0].split("/")[2], 1)
        self.weekly_todo_str = self.weekly_todo_str.replace("d2", self.weekly_dates_list[1].split("/")[2], 1)
        self.weekly_todo_str = self.weekly_todo_str.replace("d3", self.weekly_dates_list[2].split("/")[2], 1)
        self.weekly_todo_str = self.weekly_todo_str.replace("d4", self.weekly_dates_list[3].split("/")[2], 1)
        self.weekly_todo_str = self.weekly_todo_str.replace("d5", self.weekly_dates_list[4].split("/")[2], 1)
        self.weekly_todo_str = self.weekly_todo_str.replace("d6", self.weekly_dates_list[5].split("/")[2], 1)
        self.weekly_todo_str = self.weekly_todo_str.replace("d7", self.weekly_dates_list[6].split("/")[2], 1)
        self.weekly_todo_str = self.weekly_todo_str.replace("startdate", self.weekly_dates_list[0], 2)
        self.weekly_todo_str = self.weekly_todo_str.replace("enddate", self.weekly_dates_list[6], 2)
        self.weekly_todo_str = self.weekly_todo_str.replace("weeknum", str(self.week_num), 1)
        self.weekly_todo_str = self.weekly_todo_str.replace("yyyy", str(self.year), 1)

    def print(self):
        print(self.weekly_todo_str)


def retreive_args():
    import argparse
    parser = argparse.ArgumentParser(description="This script is trello program.")
    parser.add_argument("startdate", help="specify start date.")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = retreive_args()
    weeklydate = WeeklyDate(args.startdate)
    weeklydate.print()
