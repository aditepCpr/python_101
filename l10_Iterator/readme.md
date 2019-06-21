#  Iterator

``` an object that contains a countable number of values.```

``` 
String, Lists, Tuples, dictionaries, and all iterable objects
```

an object which implement the iterator protocol, which consist of the methods

```python 
next()   __next__()
iter()   __iter__()
```
```python
list = [12,3,4,5,6,7,78]

for index in range(len(list)):
    print(list[index])

# implement Iterator
for index in list :
    print(index)

```
``` 
object implement Iterator  ->  iterable
iter(iterble) ฟังก์ชั่นส่งไปให้ iter_obj  เรียกว่า Iterator Object
iter_obj จะสามารถใช้ next(iter_obj) ได้

```
```python
# create an iterator object fom that iterable
iter_obj = iter(iterable)

#infinite loop
while True:
    try:
        # get the nrxt item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        breaks
```

```python

for element in iterable:   
    # do something with element

```

## iterator vs iterable
``` 
Iterator

next()
hasNext()
```
```python
b = PowTwo(9)
while(b.hasNext()):
    print(b.hext())
```
```python
for x in b.iterator() :
    print(x)

```
```
b.next()  = oop
next(b)   = python
```