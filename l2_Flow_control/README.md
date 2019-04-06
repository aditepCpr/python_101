# python_101 
# Flow Control - Looping Statements
` for loop, while loop , Break , Continue , Pass `
## Contents
[For loop](#For-loop)

[While Loop](#While-Loop)

[Break](#Break)

[Continue](#Continue)

[Pass](#Pass)


## For loop
![Image](https://github.com/topkoka/python_101_ubuntu/blob/master/pic/flow%20control/python_for_loop.jpg?raw=true)

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
### For loop else
```python
## for loop else
numbers = []

for i in numbers:
    print(i)
else:
    print('No item left')
```
## While Loop
![image](https://github.com/topkoka/python_101_ubuntu/blob/master/pic/flow%20control/python_while_loop.jpg?raw=true)
### While Loop
#### Statement syntax
```python
while test_expression :
      Body of while
```
```python
n = 10

sum = 0
i = 1

while i <= n:
    sum += i
    i+=1
    print(sum)
print('The sum is', sum)
```
### While Loop Else
#### Statement syntax
```python
while test_expression :
      Body of while
else:
      statements
```
```python
counter = 0

while counter < 10:
    print('No.',counter)
    counter += 1
else:
    print('Done.')
```
* Orther

``` Break , Continue , Pass ```
## Break
![image](https://github.com/topkoka/python_101_ubuntu/blob/master/pic/flow%20control/r-break-flowchart.jpg?raw=true)
![image](https://github.com/topkoka/python_101_ubuntu/blob/master/pic/flow%20control/break.jpeg?raw=true)

### for loop break
```python
## for loop break
for val in "hello world":
    if val == 'o':
        break
    print(val)
print('The End')

```
#### output
```output
h
e
l
l
The End
```
### whlie loop break
```python
n = 10
sum = 0 
i = 1

while i <= n:
    sum += i
    i+=1
    print(sum)
    if sum == 36:
        print('sum = 36 :: Break')
        break
print('The sum is', sum)

```
#### output
```output

1
3
6
10
15
21
28
36
sum = 36 :: Break
The sum is 36

```
## Continue
![image](https://github.com/topkoka/python_101_ubuntu/blob/master/pic/flow%20control/continue.jpeg?raw=true)
![image](https://github.com/topkoka/python_101_ubuntu/blob/master/pic/flow%20control/continue2.jpeg?raw=true)

#### For loop continue

```python

for val in "hello world":
    if val == 'o':
        continue
    print(val)
print('The End')

```
#### output
```output

h
e
l
l
 
w
r
l
d
The End
```
## Pass
```python

sequence = ['h','i','l','o']
for val in sequence:
    if(val=='i') :
        pass
    print(val)
```
#### Output
```output
h
i
l
o
```
