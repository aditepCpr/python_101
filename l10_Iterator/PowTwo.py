class PowTwo:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            # logic code
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


a = PowTwo(5)
it = iter(a)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

for i in PowTwo(8):
    print(i)