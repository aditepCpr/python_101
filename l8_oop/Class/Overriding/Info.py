import l8_oop.Class.Overriding.Caroverri as carover

# Polymorphic arguments
def info(Car):
    Car.info()


crv = carover.CRV('red','AI')
honda = carover.Car(2,'black','Ivtech')
info(crv)
info(honda)
