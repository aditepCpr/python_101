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
    def info(self):
        print(self.wheel)
        print(self.color)
        print("CRV Engin :",self.engine)
        print(self.ai)