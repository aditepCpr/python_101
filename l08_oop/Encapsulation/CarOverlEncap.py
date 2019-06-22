class Car:
    # class attribute
    wheel = 4
    color = "unset"
    engine = "ivtech"

    # constructor Overloading
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

    def info(self):
        print(self.wheel)
        print(self.color)
        print(self.engine)

# instantiate the Car object

honda = Car(4, "White", "ivtec")
jazz = Car(4, "ivtec")
crv = Car('black')

# access the instance attributes
honda.info()
jazz.info()
crv.info()
