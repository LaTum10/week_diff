# -*- coding: utf-8 -*-
#day1 is assumed to be normally before day2
import datetime

def diff_weeks(day1, day2):
  monday1 = (day1 - datetime.timedelta(days=day1.weekday()))

  monday2 = (day2 - datetime.timedelta(days=day2.weekday()))
  
  

  diff_in_days=(monday2 - monday1).days

  diff_in_weeks=0
  remainder_in_days=0

  if day2.weekday()<day1.weekday():
    diff_in_weeks=diff_in_days/7-1
    remainder_in_days=(7-day1.weekday())+day2.weekday()
  else:
    diff_in_weeks=diff_in_days/7
    remainder_in_days=day2.weekday()-day1.weekday()

  return [int(diff_in_weeks),remainder_in_days]

def format_date(date):
    return date.strftime('%Y-%m-%d')
