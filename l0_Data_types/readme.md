# Data Types

## Python Numbers
    - int
    - float
    - complex

```python
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))
```
## Python Casting
    - int()
    - float()
    - str() 
```python     
x = int(2.8)     # x will be 2
y = float("3")   # y will be 3.0
z = str(3.0)     # z will be '3.0'
```
## Python Strings

'hello' is the same as "hello"
```python
a = "Hello, World!"

print(a[1]) # e
print(a[2:5]) #llo
print(a.strip()) # " Hello, World! " returns "Hello, World!"
print(len(a)) # 13
print(a.lower()) #hello, world!
print(a.upper()) #HELLO, WORLD!
print(a.replace("H", "J")) #Jello, World!
b = a.split(",") # returns ['Hello', ' World!'] <class 'list'>
