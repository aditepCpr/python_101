# Python Function
##### Syntax
```python

def function_name(parameters):
    """docstring"""
    statement(s)
        
```

## docstring
##### Syntax
        ` print(hello.__doc__) `
 
##### EX
```python

def hello(name):
"""This function say hello follow by name """
print("Hello,", name)
    
print(hello.__doc__)
hello('top')

 ```
 ##### Output
 ```
This function say hello follow by name 
Hello, top
 ```
 ## Return
 ##### Syntax
 ```python

def function_name(parameters):
    """docstring"""
    statement(s)
    return [expression]

 ```
 ##### EX
 ```python
def hello(name):
    """This function say hello follow by name """
    return 'Hello,'+name
print(hello('Jack'))
 ```
 ##### Output
 ```
Hello,Jack
 ```
 
 ## Function Arguments
 
   - Requird arguments
   - Keyword arguments
   - Default arguments
   - Variable-length arguments
   
   ### - Requird arguments
   ```python
   
def hello(name):
    """This function say hello follow by name """
    return 'Hello,'+name
    
print(hello('Jack'))

print(hello()) #Error
   
   ```
   ### - Keyword arguments
   ```python
   
def hello(name):
    """This function say hello follow by name """
    return 'Hello,'+name

print(hello('Jack'))
print(hello(name='top')) # Keyword
print(hello(name2='Jack')) #Error
   ```
   ### - Default arguments
```python
def hello(name='None'): #Default arguments
    """This function say hello follow by name """
    return 'Hello,'+name

print(hello())
print(hello('Jack'))
print(hello(name='top'))
```
   ### - Variable-length arguments
   ```python
   def hello(name='None',*word): # ' * ' *word = Tuple
    """This function say hello follow by name """
    text=''
    for w in word :
        text+=str(w)
    return 'Hello,'+name+' '+text

print(hello('top','How','are you')) # Hello,top Howare you
print(hello('Tony',1,2,3)) # Hello,Tony 123

# print(hello(name='top','How','are you')) #Erroe
# n* arguments
   
   ```
   ## Anonymous Functions
   ### Lambda
```python
    
    lamba arguments: expression
    
```
```python
sum = lambda n1,n2 : n1+n2
sub = lambda n1,n2 : n1-n2
div = lambda n1,n2 : n1/n2
mul = lambda n1,n2 : n1*n2

print(sum(20,10)) #30
print(sub(20,10)) #10
print(div(20,10)) #2.0
print(mul(20,10)) #200

```
   ### - Lambda Functions
```python
   
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))  ##22
print(mytripler(11))  ##33
   ```
## Scope
- local
- Global
### - local
```python
def foo():
    y = 'local'
    print(y)
foo()  #local
print(y) #Error

```
### - Global
```python
x = 'outer'

def foo():
    print('x inside :',x)
    
foo()
print('x outside :',x)

#x inside : outer
#x outside : outer
```
#### Ex

```python
x = 'Global'

def foo():
    x = x * 2  #Error x = null  :  cant *2
    print(x)
foo()
```
```python
x = 'global'

def foo():
    global x  # x = 'global'
    y = 'local'
    x = x * 2
    print(x)
    print(y)
foo()
print(x)

```
## ypes of Functions
- Build-in
- user-Define
### - Build-in Functions
```python
abs() delattr() hash() memoryview() set() all() dict() help() min() setattr() any() dir() hex() next() slice() ascii() divmod() id() object() sorted() bin() enumerate() input() oct() staticmethod() bool() eval() int() open() str() breakpoint() exec() isinstance() ord() sum() bytearray() filter() issubclass() pow() super() bytes() float() iter() print() tuple() callable() format() len() property() type() chr() frozenset() list() range() vars() classmethod() getattr() locals() repr() zip() compile() globals() map() reversed() import() complex() hasattr() max() round()

```
