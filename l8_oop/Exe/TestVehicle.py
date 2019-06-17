from l8_oop.Exe.Vehicle import Car

honda = Car('red', 4, "IVTech")
crv = Car('silver', 5, 'IVTech')
toyota = Car('black')

print(type(honda))
print(type(crv))

honda.info()
crv.info()
toyota.info()