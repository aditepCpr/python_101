# python_101_ubuntu


# Types of Operators

* Arithmetic 

``` +,-,*,/ ```
* Comparison 

``` <,>,<=,>= ```
* Logical    

``` and,or,not ```
* Assignment

``` +=,-=,*=,/=,%= ```
* bitwise    

``` &,|,~,^,>>,<< ```

#### new python

* identity   

``` is , is not ```
* member     

``` in , not in ```

# Flow Control

* Decision Statements

``` if , if - else , if - elif - else ```
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

* Looping Statements

``` for loop, while loop ```

* Orther

``` Break , Continue , Pass ```
