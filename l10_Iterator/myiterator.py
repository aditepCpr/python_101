list = [12, 3, 4, 5, 6, 7, 78]
for index in range(len(list)):
    print(list[index])
print('*' * 30)


class PowerTwo:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


## Examplel
a = PowerTwo(5)
it = iter(a)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

print('*' * 30)

for i in PowerTwo(8):
    print(i)
print('*' * 30)


class PowTwo2:
    n = 0

    def __init__(self, max=0):
        self.max = max

    ## เพื่อเปลี่ยน powtwo object implement Iterator
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

    ## เพื่อให้เรียกใช้งานได้หลายๆรอบ ไม่เข้า raise StopIteration
    def iterator(self):
        return iter(self)

    ## เช็คค่า True or False`
    def hasNext(self):
        if self.n <= self.max:
            return True
        else:
            return False

    ## ดึงค่าจาก __next__
    def next(self):
        return self.__next__()


## Example2
b = PowTwo2(9)

while (b.hasNext()):
    print("1", b.next())
print('*' * 30)

## เรียกใช้แบบไหน ก็ได้  b = iter(b) หรือ b.iterator()

# b = iter(b)
b.iterator()
while (b.hasNext()):
    print("2", b.next())
print('*' * 30)

for x in b.iterator():
    print(x)
print('*' * 30)

for x in iter(b):
    print(x)
print('*' * 30)


class MyProductIterator:
    print('class MyProductIterator')
    products = []
    index = 0

    def __iter__(self):
        print("__iter__")
        self.index = 0
        return self

    def __next__(self):
        print('__next__')
        if self.index <= len(self.products):
            print('__next__ if')
            print("index", self.index)
            result = self.products[self.index]
            self.index += 1
            return result
        else:
            print('__next__ else' )
            StopIteration

    def addProduct(self, prods):
        print('addProduct')
        self.products = prods

    def iterator(self):
        print('iterator')
        self.index = 0
        return iter(self)

    def hasNext(self):
        print('hasNext')
        if self.index < len(self.products):
            return True
        else:
            return False

    def next(self):
        print('next ')
        return self.__next__()


pit = MyProductIterator()
prods = ["mobile", "car", "computer", "furniture", "fashion", "home"]
pit.addProduct(prods)

while (pit.hasNext()):
    print("product name:", pit.next())

for p in pit:
    print("product name:", p)

for p in pit.iterator():
     print("product name:", p)

for p in iter(pit):
    print("product name:", p)
