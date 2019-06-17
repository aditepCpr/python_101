class Car:
    # Fields     # Attributes
    color = "white"
    wheel = 4
    engine = 'normal'

    # Constructor #Initiailization
    def __init__(self, color=None, wheel=None, engine=None):

        if(color is not None and wheel is not None and engine is not None) :
            self.color = color
            self.wheel = wheel
            self.engine = engine
        elif(color is not None) :
            self.color = color
        else:
            pass

    def info(self):
        print(self.color)
        print(self.wheel)
        print(self.engine)

