def PowTowGen(max = 0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1


ip = PowTowGen(5)

for i in ip :
    print(i)
