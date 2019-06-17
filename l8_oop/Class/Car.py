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


# instantiate the Car object

honda = Car(4, "White", "ivtec")
Jazz = Car(4, "Blue", "ivtec")
crv = Car(5, "White", "super ivtec")

# access the instance attributes
print(crv.wheel)
print(crv.color)
print(crv.engine)
print(type(honda))