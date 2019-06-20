from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

###   Get Current Date
print("Get Current Date")
print(date.today())
print(datetime.now()) # แนะนำให่้ใช้ datetime ไปเลย
print(datetime.today())
print("*"*30)

### Get Spacific Date & time
print("Get Spacific Date & time")
print(date(2019,5,5))
print(time())
print(time(12,20,20))
print(time(12,20,20,234566))
print(datetime(2019,5,9))
print(datetime(2019,5,9,12,20,20,234566))
print("*"*30)

### Get Date from Timestamp
print("Get Date from Timestamp")
print(date.fromtimestamp(1561001111))
print("*"*30)

### Get each filed of date & time
print('Get each filed of date & time')
dt = datetime(2019,5,9,12,20,20,234566)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)
print("*"*30)

### Apply Code
td = date.today()
dayOfWeek =["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
print(dayOfWeek[td.weekday()]) ## แนะนำ
print(dayOfWeek[date.weekday(td)])
print("*"*30)

print(td.strftime("%Y"))
print(td.strftime("%y"))
print(td.strftime("%d-%b-%y"))
print(td.strftime("%d-%B-%Y"))
print(dt.strftime("%d-%B %Y"))
print("*"*30)



strDate = "11-May-2019"
dt2 = dt.strptime(strDate,"%d-%B-%Y")
print(dt2)
print(dt2.year)
print(type(dt2))
print("*"*30)

delta = timedelta(days=365,hours=8,minutes=15)
print(delta)
print("*"*30)

today = datetime.now()
print(type(today))
print("this Year :",today)
print("*"*30)

nextYear = today+delta
print(type(nextYear))
print("Next Year :",nextYear)
print("*"*30)

nextWeek = today+timedelta(weeks=1)
print(nextWeek)
print("#"*30)

##How Many days pass the new Year
td = date.today()
newYear = date(2019,1,1)

if newYear<td :
    print((td-newYear).days)
else:
    print((newYear-td).days)

print((td-newYear).total_seconds())

