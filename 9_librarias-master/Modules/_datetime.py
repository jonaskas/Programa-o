"""
datetime
See: http://strftime.org/ 
"""

import datetime

data1 = datetime.date(2017, 6, 10)
data2 = datetime.datetime(2017, 6, 10, 11, 30, 0)

print(data1)

print(data2)
print(data2.year)
print(data2.month)
print(data2.day)
print(data2.hour)
print(data2.minute)
print(data2.second)

current_date = datetime.date.today()
print(current_date)

print(current_date.strftime("%d/%m/%y")) # str from date
print(current_date.strftime("%Y %b %d %a"))
print(current_date.strftime("%Y %B %A"))

date = input("Insert date [%d/%m/%y]: ")
date = datetime.datetime.strptime(date, "%d/%m/%y") # date from string
print(date.strftime("%Y %b %d %a"))

diff = current_date - date.date()

print(diff)
print(diff.days)

now = datetime.datetime.now()
print(now.hour)
print(now.minute)
print(now.second)

print(now.strftime("%d/%m/%y %H:%M:%S %I%p"))
