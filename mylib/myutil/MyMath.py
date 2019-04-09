def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

def pow(base,power) :
    result = 1
    for t in range(power):
        result*=base
    return result

# def pow(base,power):
#     return base**power
#
# print(add(10,20))
# print(mul(5,10))
# print(sub(5,10))
# print(div(5,10))
# print(pow(5,3))

