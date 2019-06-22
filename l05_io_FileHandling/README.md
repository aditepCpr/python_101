# I/O

python build-in


## print , input
```python
# printing to the screen
print()   
# reading input
input()
```
```python
import sys
x= 5
y = 5
print(sys.stderr)
print((x,y)) # print function
```
```python
num = input() # str type
print('you enter',num)
print(int(num)+5) ## convert types   str --> int,float
```

# Read write file
```python
open()
read()
write()
close()
```
## open()
` open('file-path','mode')`

```

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

 binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)


Create a New File

"x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist

``` f = open("myfile.txt", "x") ```

```

```python
file = open('D:tmp/test/hello.txt','r')
f = open("demofile", "rt")
# recommended
# '/'
```
##### PATH
1. absolute path
ex.
```python
D:tmp/test/hello.txt
```

2. Relative Path
 
 ex.
 `` /math/proj1 ``
 
 ##### mode()
 ```
  r = read
  w = write
  a = appending
```
## read()
```python
read()
read(limit)
readline(limit)
readlines(limit)
``` 
```python
print(file.read(8))
print(file.read())

print(file.readline())
print(file.readline(5))

for f in file :
    print(f)
    
lines = file.readlines()
for l in lines :
    print(1)    
```
## write()
```python
write(text)
writeline(line)
```
```  CSV , JSON , XML ```
```python
Write to an Existing File

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content

```
```python
file.write('Todat is Monday')
file.write('Time to go school')

data ['today is monday','time to go school\n','abc\n','def\n']
file.writelines(data)

file.close()
```

```python
rename()
remove()
mkdir()
chdir()
getcwd()
rmdir()
```
