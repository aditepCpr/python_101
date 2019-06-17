import l8_oop.Class.polymorphism.Carpoly as poly

# Polymorphic arguments
def info(Car):
    Car.info()


crv = poly.CRV('red')

info(crv)
