****# Datetime

## date

```python
date.today()
date(y,m,d)
date.fromtimestamp(int) # เอาไว้ใช้คำนวณ เริ่มจาก 0.0.0 1/11970  ค่าเป็น ms มิลิเซก

```

### data.today()
```python
date.today() # ปัจจุบัน
today.weakday()
# Monday  0  , Tuesday 1 , Wednesday 2 , Thursday 3 , Friday 4 , Saturday 5 , Sunday 6 

wd = date.weakday(today)

date.year
date.month
date.day

```

## time
```python
time()
time(h,m,s)
time(h,m,s,ms)
```

## datetime

```python
datetime(y,m,d)
datetime(y,m,d,h,m,s,ms)

datetime.now()
datetime.year
datetime.hour
datetime.minut
datetime.timestamp()
```

## Format Date & Time

```python
strftime() # output , datetime object to string   # today = dt.datetime.now() # print(today.strftime("%Y-%m-%d")) 
strptime() # input , string to datetime

```
#### strftime()
```
%y = 19, %Y = 2019  :: Year
%a = Thu, %A = Thursday :: Weakday
%b = 6, %B = June :: Month
%d =  20     day of month
%s = second
("%Y-%B-%d-%A")) =  2019-June-20-Thursday

%c local Date&Time
%x local Date
%X  local Time
```
#### strptime() 
```
now.strptime("String","%Y")

```

### timedelta
```python
+,-    >,< 

timedelta.days
timedelta.seconds
timedelta.milliseconds
timedelta.total_seconds() #ใช่ไปแล้วกี่วินาที

```

# calendar
```python
import calendar
tc= calendar.TextCalendar(firstweekday=0)
print(tc.formatmonth(2016, 5))

```