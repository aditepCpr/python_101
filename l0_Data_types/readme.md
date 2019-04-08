# Data Types
# Contents

[Python Numbers](#Python-Numbers)

[Python Casting](#Python-Casting)

[Python Strings](#Python-Strings)

[Python Collections](#Python-Collections)

[-List[]](#List)
    
[-Tuple()](#Tuple)
    
[-Set{}](#Set)
    
[-Dictionary{K:'values'}](#Dictionary{k:'v'})
    
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
```
## Python Collections (Arrays)
    - List[] 
    - Tuple()
    - Set{}
    - Dictionary{key:'value'}
### [List[]](https://github.com/topkoka/python_101/blob/master/l0_Data_types/List.ipynb)

```python 
thislist = ["apple", "banana", "cherry"]
```
- List[]
    - Change Item Value
    - Loop Through a List
    - List Length
        - len()
    - Add Items
        - append()
        - insert()
    - Remove Item
        - remove() 
        - pop()
        - del
    - Copy a List
        - copy() 
        - list()
        
### [Tuple()](https://github.com/topkoka/python_101/blob/master/l0_Data_types/Tuples.ipynb)

```python
thistuple = ("apple", "banana", "cherry")
```
- Tuple() 
    - fixed size
        - cannot add items
        - cannot change values
        - cannot remove items
    - Loop Through a Tuple
    - Check if Item Exists
    - Tuple Length
        - len()
    - Remove 
        - del
        
### set{}
### Dictionary{k:'v'}
