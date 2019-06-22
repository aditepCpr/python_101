class Car:
    # class attribute
    wheel = 4
    color = "unset"
    engine = "ivtech"

    # constructor
    def __init__(self, wheel=None,color=None,engine=None):
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


# instantiate the Car object

honda = Car(4, "White", "ivtec")
Jazz = Car(4, "ivtec")
crv = Car('black')

# access the instance attributes
print(crv.wheel)
print(crv.color)
print(crv.engine)
print(type(honda))
