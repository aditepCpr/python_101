from l8_oop.Exe.Vehicle import *

honda = Car('red', 4, "IVTech")
crv = Car('silver', 5, 'IVTech')
toyota = Car('black')

print(type(honda))
print(type(crv))

honda.info()
crv.info()
toyota.info()
print("-"*30)

j1 = Jazz()
j1.info()
print("-"*30)
print('CRV')
crv = CRV('pink',4,'ivtech','Intelligence')
crv.info()

print("-"*30)

# Inheritance
audi = Car('Silver',4,'Super Engine')
crv = CRV()
jazz = Jazz('silver',4,'IVTech')

owner = Owner('001','Tony Stark')

# polymorphism
owner.buyCar(audi)
owner.buyCar(crv)
owner.buyCar(jazz)
# Encapsulation
owner.getInfo()



