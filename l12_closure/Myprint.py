def myprint(msg):
# This is the outer enclosing function
    def inner_print():
    # this is the nested function
        print(msg)
    return inner_print

p1 = myprint("TEST HELLO PYTHON CLOSURE 1")
p1()
p2 = myprint("TEST HELLO PYTHON CLOSURE 2")
p2()

# Closure
myprint('testHello 3')()