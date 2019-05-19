# Handling

# try-Except-Else
#### Syntax   try-Except-Else
```python

try:
    you do your operation here;
    ..........................
except ExceptionI:
    if there is ExceptionI, then execute this block.
except ExceptionII:     
    if there is ExceptionII, then execute this block.
    .........................
else:
    if there is no Exception, then execute this block.

```
#### No Exception
```python

try:
    you do your operation here;
    ..........................
except :
    if there is any Exception, then execute this block.
    .........................
else:
    if there is no Exception, then execute this block.

```
#### Multiple Exceptions
```python

try:
    you do your operation here;
    ..........................
except (Exception1[, Exception2[,..... ExceptionN]]):
    if there is any Exception, from the given exception list, thne execute this block.
    .........................
else:
    if there is no Exception, then execute this block.

```



##### EX

```python

try:
    fh = open("testfile","w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t fing file or read data")
else:
    print("Written content in the file successfully")
    fh.close()

```

##### output
```

Written content in the file successfully

```

# Try-Finally

#### syntax

```python
try:
    you do yuor operations here;
    ................................
    Due to any exception. this may be skipped.
finally:
    This would always be executed.
    .............................
```

## Argument of Exception

#### syntax

```python
try:
    you do your openrations here;
    .........................
excrpt ExceptionType  as Argument:
    you can print value of Argument here..

```
```python

def temp_convert(var):
    try:
        return int(var)
    except ValueError as e:
        print("the argument does cantain number\n",e.args)

temp_convert("xyz")

```