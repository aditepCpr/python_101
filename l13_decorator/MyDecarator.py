def decor(func):
    def wrap():
        print("$$$$$$$$$$$$$$$")
        func()
        print("$$$$$$$$$$$$$$$")

    return wrap

@decor
def sayhello():
    print("Hello")

sayhello()
# newfunc = decor(sayhello)
# newfunc()

print("*"*30)

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

print("*"*30)

# Decorators with Parameters in Python
def decorator(*args,**kwargs): # args = tuple  , kwargs = map
    def inner(func):
        print(func(),kwargs['name'])
        return func
    return inner

@decorator(name = "Tony Stark")
def sayHello():
    return "Hello"

sayHello()

print("*"*30)

def decor1(func):
    def wrap():
        print('$$$$$$$$$$')
        func()
        print('$$$$$$$$$$')
    return wrap

def decor2(func):
    def wrap():
        print('#'*10)
        func()
        print('#'*10)
    return wrap

@decor1 #  ทำงานที่หลัง
@decor2 #  ทำงานก่อน
def sayhello():
    print("Hello")

sayhello()