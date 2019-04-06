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
* Looping Statements

``` for loop, while loop ```

* Orther

``` Break , Continue , Pass ```
