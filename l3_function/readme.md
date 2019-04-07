# Python Function
## Syntax
```python

def function_name(parameters):
    """docstring"""
    statement(s)
        
```

### docstring

        ` print(hello.__doc__) `
        
```python

def hello(name):
"""This function say hello follow by name """
print("Hello,", name)
    
print(hello.__doc__)
hello('top')

 ```
 #### Output
 ```
This function say hello follow by name 
Hello, top
 ```
 ## Return
 ```python

def function_name(parameters):
    """docstring"""
    statement(s)
    return [expression]

 ```
 ```python
def hello(name):
    """This function say hello follow by name """
    return 'Hello,'+name
print(hello('Jack'))
 ```
 #### Output
 ```
Hello,Jack
 ```
