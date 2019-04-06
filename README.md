# python_101_ubuntu


# Types of Operators

* Arithmetic 

``` +,-,*,/,% ```
```python
a = 5
b = 6
print(a+b) # 11
print(a-b)
print(a*b)
print(a/b)
print(a%b)

```
* Comparison 

``` <,>,<=,>= ```
```python
a=6
b=5
if a>5:
    print('hi')
elif a<5:
    print('low')   
```
* Logical    

``` and,or,not ```
```python
a=6
b=5
c= True
if a>5 and b>4:
    print('hi')
elif a<5 or b<6:
    print('low')   
print(not c) # !True = False
```
* Assignment

``` +=,-=,*=,/=,%= ```
```python
a = 5
b = 5

b += a #10
b -= a #5`
b *= a #25
b /= a #5.0
b %= a #0.0

```
* bitwise    

``` &,|,~,^,>>,<< ```

#### new python

* identity   

``` is , is not ```
* member     

``` in , not in ```

# Flow Control

* Decision Statements

``` if , if - else , if - elif - else , nested if ```
## if
![Image](https://github.com/topkoka/python_101_ubuntu/blob/master/pic/flow%20control/if.jpeg?raw=true)
#### Statement syntax
```python 
if test expression:
    ststement(s) 
```
#### Statement example
```python
a = 2
if a<3:
  print (a)
if a>3:
  print('hi')
```
#### output
``` 
2 
```
    

## if - else
![Image](https://github.com/topkoka/python_101_ubuntu/blob/master/pic/flow%20control/if-else.png?raw=true)
#### Statement syntax
```python 
if test_expression:
  statements
else:
  statements
```
####  Statement example
```python
x = 5
if x<10:
  print('Condition is TRUE')
else:
  print('Condition is FALSE')
```
#### Output
```
Condition is True
```
## if-elif-else
![Image](https://github.com/topkoka/python_101_ubuntu/blob/master/pic/flow%20control/Python-if-elif-else-statement.jpg?raw=true)
#### Statement syntax
```python
if test expression:
    Body of if
elif test expression :
    Body of elif
else:
    Body of else
```
####  Statement example
```python
num = 3.4

if num > 0:
    print('Positive number')
elif num == 0:
    print('Zero')
else:
    print('Negative number')
```
#### output
``` 
Positive number
```
## Nested if
```python 
if test_expression:
    if test_expression:
        statements
    else:
        statements
else:
  statements
```
#### Statement syntax
#### Statement example
# Looping Statements

``` for loop, while loop ```

## For loop

```python
# For loop
numbers = [7,4,1,2,5,8,9,4,11]
print('numbers =',type(numbers),numbers)
sum = 0
for val in numbers:
        print('val = ',val,type(val))
        sum += val
        print('sum =',sum)
print('end loop sum =',sum)

```
### For loop in range
```python
# For loop in range

numbers = [1,2,3,4,5,6,7,8,9,10]
print('numbers =',type(numbers),numbers)
sum = 0
for val in range(1,11):  # 11-1 = 10 ,  1 -> 10
        print('val = ',val,type(val)) 
        sum += val
        print('sum =',sum)
print('end loop sum =',sum)

# range(10)
# range(1,10)
# range(1,10,2)
# range(begin,end,step)

```
```python
genre = ['pop','rock','jazz']

# range()
for i in range(len(genre)):
    print('i like',genre[i])

# list
for g in genre :
    print('i like',g)
```
## For loop else
```python
## for loop else
numbers = []

for i in numbers:
    print(i)
else:
    print('No item left')
```
* Orther

``` Break , Continue , Pass ```
