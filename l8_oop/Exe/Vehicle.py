class Car:
    # Fields     # Attributes
    color = "white"
    wheel = 4
    engine = 'normal'

    # Constructor #Initiailization
    def __init__(self, color=None, wheel=None, engine=None):

        if (color is not None and wheel is not None and engine is not None):
            self.color = color
            self.wheel = wheel
            self.engine = engine
        elif (color is not None):
            self.color = color
        else:
            pass

    def info(self):
        print(self.color)
        print(self.wheel)
        print(self.engine)


class Owner:
    # Fields
    id = '0'
    name = 'unset'
    # car = Car() # composite
    cars = []  # aggregate

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def buyCar(self, car):
        self.cars.append(car)

    def getInfo(self):
        print("Owner is", self.name)
        for c in self.cars :
            print(type(c))
            c.info()


class Jazz(Car):
    # Attributes
    ai = "normal"

    def __init__(self, color=None, wheel=None, engine=None, ai=None):

        if (color is not None and wheel is not None and engine is not None and ai is not None):
            super().__init__(color,wheel,engine)
            self.ai = ai
        elif (color is not None):
            self.color = color
        else:
            pass

    def info(self):
        super().info()
        print(self.ai)

class CRV(Car):
    # Attributes
    abc = "abc"

    def __init__(self, color=None, wheel=None, engine=None, abc=None):

        if (color is not None and wheel is not None and engine is not None and abc is not None):
            super().__init__(color,wheel,engine)
            self.abc =abc
        elif (color is not None):
            self.color = color
        else:
            pass

    def info(self):
        super().info()
        print(self.abc)