class Myiterator:
    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            # logic code
            print()
        else:
            raise StopIteration


itr = Myiterator(15)
itb = iter(itr)
iter(itr)
