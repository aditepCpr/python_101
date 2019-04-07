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
