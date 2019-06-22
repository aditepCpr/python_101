# Regular

## syntax
### match()
```python

re.match (patrerr, string, flags=0)

```

```python

import re
#input ข้อควา่ม
line = "Cats are smarter than dogs"

# match ข้อความ ที่ มี are ตรงกลาง และ เริ่มต้นด้วย r
match0bj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

if match0bj:
    print("match0j.grouo() :", match0bj.group()) #เอามาโชว์ทั้งหมด
    print("match0bj.group(1) :", match0bj.group(1)) # โชว์แค่ กลุ่ม 1 'Cats'
    print("match0bj.group(2) :", match0bj.group(2)) # โชว์แค่ กลุ่ม 2 'smarter' 
else:
    print("No match!!")

```

### search()
```python

re.search (patrerr, string, flags=0)
```
```python
search0bj = re.search(r'(.*) are (.*?) .*', line, re.M|re.I)

if search0bj:
    print("match0j.grouo() :", search0bj.group())
    print("match0bj.group(1) :", search0bj.group(1))
    print("match0bj.group(2) :", search0bj.group(2))
else:
    print("No match!!")

```

#### Search & Replace

##### syntax
```python

re.sub(pattern.repl,string ,max=0)
```
```python

# re.sup() การ replaces ค่าต่างๆ ด้วย pattern ที่เรากำหนด

import re
phone = "2004-959-599 # This is Phone Number"

#Delete Python-style comments
num = re.sub(r'#.*$',"",phone)
print('Phone Num :',num)

#Remove anything other than digits
num = re.sub(r'\D',"",phone)
print('Phone Num :',num)

```





```
r'^ $'

# ^ เริ่มต้น
# $ จบ
# . 1 character
# [...] ex. [abc] หมายถึงตัวไหนก็ได้ a b c
# [^...] ex. [^def] หมายถึงตัวไหนก็ได้ที่ไม่ใช้  d e f
# re*  ตั้งแต่ 0 ถึง n
# re+  มีอย่างน้อย 1 char
# re?  อย่างน้อย 0 หรือ 1
# re{n} ex. a{3} ระบุจำนวนชัดเจน
# re{n,} ex. a{3,} ตั้งแต่ 3 เป็นต้นไป
# re(n,m) ex. a{3,5} 

# \w  เป็ย word char
# \W เป็น noword char 
# \s whitespace
# \S nonwhitespace
# \d digits[0-9]
# \D nondigits

# (?=.*[0-9]) กี่ตัวกอักษรก็ได้ เลข 0 - 9
# (?:.{8,}) ต้องมีตัวอักษร 8 ตัวขึ้นไป
# passRE ต้องมี ทั้งตัวเลข ตัว uppercase และ lowercase  8 ตัวอักษรขึ้นไป
passRE = r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?:.{8,})$'

# ขึ้นต้อนด้วย 08 ตัวเลข - ตัวเลช 3 ตัว - ตัวเลช 4 ตัว
telRE = r'^08\d-\d{3}-\d{4}$'

python  = 'python'
[Pp]ython  = 'Python' or 'pythop'
rub[ye] = 'ruby' or 'rube'
[aeiou] = lowercase vowel
[0-9] = digit [0123456789]
[a-z] = lowercase ASCII
[A-Z] = uppercase ASCII
[a-zA-Z0-9] = รวมกันได้
[^aeiou]
[^0-9] = nondigit

rubyM = rub or ruby
\d{3} = 3 digits
\d{3,} = 3 เป็นต้นไป
\d{3,5} = 3-5

<.*> = ภายใต้มากกว่าน้อยกว่ามี กี่ char ก็ได้ "<python>perl>""
<.*?> = matches "<python>" in "<python>perl>"

\D\d+ = (no group)ขึ้นต้อนด้วยตัวเลข  ที่เหลือไม่ใช่ตัวเลข
(\D\d)+ = (Grouped)  ขึ้นต้อนด้วยตัวเลข  ที่เหลือไม่ใช่ตัวเลข แบบเป็นกลุ่ม
([Pp]ython(,)?)+ = match "Python","Python,python,python",etc.
```

```python
import re
year = '19416556446546546546546545'
try :
    find = re.match(r'\d{4}',year)
    print(find.group())
except :
    print("Invalid")
```
```python
import re
number = '0801953333'
try :
    find = re.match(r'^08\d{8}$',number)
    print(find.group())
except :
    print("Invalid")
```
```python
import re
number = '1234-4567-1574-6547'
try :
    find = re.match(r'^\d{4}-\d{4}-\d{4}-\d{4}$',number)
    print(find.group())
except :
    print("Invalid")
```