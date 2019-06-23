# Decorator

``` การออกแบบ function เพื่อไปลดข้อจำกัดบางอย่าง ```


``` 
Powerful Function 
ไม่สนใจว่าใครจะเปลี่ยนชื่อ  Function

```
```
- Template function
- Loose Coupling อิสระ
- Function independent 

```
### Non_decorate pattern
```python
def non_decorate_message(site_name):
    return ('welcome to '+ site(site_name))

def site(site_name):
    return site_name;
msg = non_decorate_message("Thailand")
print(msg)

```

### decorate pattern
```python

def decorate_message(fun):
    def addWelcome(site_name):
        return "welcome to " + fun(site_name)
    return addWelcome

def site(site_name):
    return site_name

site = decorate_message(site)
print(site("Thailand"))

```

## Decorator with Pie ( @ )
`function ที่เป็น Decorator ต้องถูก design ในรูปแบบประกาศ nested function และ return ข้างใน `
#### Simple Decorator
```python
# Adds a welcome message the string
# returned by fun(). Takes fun() as
# parameter and return welcome().

def decorate_message(fun):
    
    # Nested function
    def addWelcome(site_name):
        return "welcome to "+ fun(site_name)
       
    # Decorator returns a function
    return  addWelcome
    
@decorate_message
def site(site_name):
    return site_name

# Driver code

# this call is equivalent to call to
# decorate_message() with function
# site("GeeksforGeeks") as parameter
print(site("GeeksforGeeeks"))

```

```python
def decorate_message(fun): 
    def addWelcome(site_name):
        return "welcome to " + fun(site_name)
    return addWelcome

@decorate_message # เรียกใช้ decorate_message เป็น decorator
def site(site_name) : # function หลัก
    return site_name

print(site('Thailand'))

```
```python
def decor(func):
    def wrap():
        print("$$$$$$$$$$$$$$$")
        func()
        print("$$$$$$$$$$$$$$$")
    return wrap
    
def sayhello():
    print("Hello")
    
newfunc=decor(sayhello)
newfunc()

```

```python
# A decorator function to attach
# data to func

def attach_date(func):
    func.date = 3
    return func

@attach_date
def add (x,y):
    return x + y

# Thai call is equivalent to attach_date()
# with add() as parameter
print("2+3 = ",add(2,3))
print("Add Data",add.date)

```

## Decorator With Parameters

```python
# Decorators with Parameters in Python
def decorator(*args,**kwargs): # args = list  , kwargs = map
    def inner(func):
        print(func(),kwargs['name'])
        return func
    return inner

@decorator(name = "Tony Stark")
def sayHello():
    return "Hello"

sayHello()
     

```