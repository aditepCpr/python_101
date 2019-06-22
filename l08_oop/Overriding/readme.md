# Overriding
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