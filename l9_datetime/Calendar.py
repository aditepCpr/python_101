import calendar
from  calendar import TextCalendar
from  calendar import HTMLCalendar

c = TextCalendar(calendar.MONDAY) # วันที่เริ่มต้น
# c = TextCalendar(calendar.SUNDAY)
c.pryear(2019)
print("#"*30)
c.prmonth(2019,5)
print("#"*30)

h = HTMLCalendar(calendar.SUNDAY)
print(h.formatmonth(2019,8))

file = open("cal.html",'w')
file.write(h.formatyear(2019,3))
file.close()
print("#"*30)

for m in c.itermonthdays(2019,5) :
    print(m)

for m in c.itermonthdates(2019,5) :
    print(m)
print("#"*3)

for mn in calendar.month_name :
    print(mn)
print("#"*3)
for mn in calendar.day_name :
    print(mn)