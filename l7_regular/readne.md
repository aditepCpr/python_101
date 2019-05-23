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