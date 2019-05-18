# Handling

Syntax   try-Except-Else
```python

try:
    you do your operation here;
    ..........................
except ExceptionI:
    if there is ExceptionI, then execute this block.
except ExceptionII:     
    if there is ExceptionII, then execute this block.
    .........................
else:if there is Exception, then execute this block.

```

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