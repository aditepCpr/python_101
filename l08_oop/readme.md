# OOP Concept

- Object
- method # Function
- Attribute # Variables
- Class
- Encapsulation # hiding private
- Inheritance # สืบทอด,ประหยัด code
- Polymorphism #common Operation # Abstraction # Function ที่สร้างขึ้นมาหลายบริบทได้่
- Abstraction # Flexible


# Class 

```
มีคุณสมบัติอะไรบ้าง 
    - มี attribute อะไรบ้าง
    - มี Method อะไรบ้าง

Car (,,,) # Constructor

```

```python
class Car:
    # class attribute
    wheel = 4
    color = "unset"
    engine = "ivtech"
    
    # constructor
    def __init__(self,wheel, color,engine):
        self.wheel = wheel
        self.color = color
        self.engine = engine

# instantiate the Car object

honda = Car(4,"White","ivtec")
Jazz = Car(4,"Blue","ivtec")
crv = Car(5,"White","super ivtec")

# access the instance attributes
print(crv.wheel)
print(crv.color)
print(crv.engine)

```

## Overloading

```python
# constructor
def __init__(self, wheel=None,color=None,engine=None)
    if(wheel is not None and color is not None and engine is not None) :
        self.wheel = wheel
        self.color=color
        self.engine=engine
    elif (wheel is not None and engine is not None):
        self.wheel = wheel
        self.color = "white"
        self.engine = engine
    elif (wheel is not None):
        self.wheel = wheel
        self.color = "white"
        self.engine = "ivtech"
    else:
        self.wheel = 4
        self.color = "white"
        self.engine = "ivtech"

```
## Encapsulation
``` hiding,private```
```python

    def info(self):
        print(self.wheel)
        print(self.color)
        print(self.engine)

```
## Inheritance
``` สืบทอด  ```
```python
class CRV(Car) :
    def __init__(self,color):
    # call super() function
        super().__init__(5,color,"super ivtech")
```
## Polymorphism
``` 
 Polymorphism =  Inheritance + Encapsulation
```
```python
import l8_oop.Class.polymorphism.Carpoly as poly
# Polymorphic arguments
def info(Car):
    Car.info()


crv = poly.CRV('red')

info(crv)

```

## Overriding

```python
class Car:
    # class attribute
    wheel = 4
    color = "unset"
    engine = "ivtech"

    # constructor
    def __init__(self, wheel, color, engine):
        self.wheel = wheel
        self.color = color
        self.engine = engine
    # info superClass
    def info(self):
        print(self.wheel)
        print(self.color)
        print(self.engine)


class CRV(Car):
    def __init__(self, color ,ai):
        self.ai = ai
        # call super() function
        super().__init__(5, color, "super invtech")
    #Overriding
    # info subclass
    def info(self):
        print(self.wheel)
        print(self.color)
        print("CRV Engin :",self.engine)
        print(self.ai)


def info(Car):
    Car.info()


crv = CRV('red','AI')
crv = carover.CRV('red','AI')
honda = carover.Car(2,'black','Ivtech')

# info CRV subclass
info(crv)
# info CRV superclass
info(honda)

```