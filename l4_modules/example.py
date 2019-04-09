def add(a,b):   
    return a + b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def pow(base,power) :
    result = 1
    for t in range(power):
        result*=base
    return result
