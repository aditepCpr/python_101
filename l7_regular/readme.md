# Regular

## syntax
### match()
```python

re.match (patrerr, string, flags=0)

```

```python

import re

line = "Cats are smarter than dogs"

match0bj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

if match0bj:
    print("match0j.grouo() :", match0bj.group())
    print("match0bj.group(1) :", match0bj.group(1))
    print("match0bj.group(2) :", match0bj.group(2))
else:
    print("No match!!")

```

### search()
```python

re.search (patrerr, string, flags=0)
```
```python
import re
#input ข้อความ
line = "Cats are smarter than dogs"

# match ข้อความที่มี are ตรงกลาง และ เริ่มต้นด้วย r
match0bj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

if match0bj:
    print("match0j.grouo() :", match0bj.group()) #เอามาโชว์ทั้งหมด
    print("match0bj.group(1) :", match0bj.group(1)) # โชว์แค่ กลุ่ม 1 'Cats'
    print("match0bj.group(2) :", match0bj.group(2)) # โชว์แค่ กลุ่ม 2 'smarter' 
else:
    print("No match!!")

```

#### Search & Replace

##### syntax
```python

re.sub(pattern.repl,string ,max=0)
```