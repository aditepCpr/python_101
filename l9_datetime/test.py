import datetime as dt
import calendar

print(dt.date.today())
print(dt.time())
today = dt.datetime.now()
year = dt.datetime.timestamp(today)
print(today.strftime("%Y-%B-%d-%A-%d"))

tc= calendar.TextCalendar(firstweekday=0)
print(tc.formatmonth(2016, 5))