def logOperation(op,func): # closure
    def log():
        print("Log:","Operator=",op,',Result is',func)
    return log

def add(n1,n2):
    return  n1+n2
def sub(n1,n2):
    return  n1-n2
def mul(n1,n2):
    return  n1*n2
def div(n1,n2):
    return  n1/n2

# print("Log : result is",add(2,3))
# print("Log : result is",div(2,3))
# print("Log : result is",mul(2,3))
# print("Log : result is",sub(2,3))

a = logOperation("Add",add(2,3))
a()

logOperation("div",div(2,3))()
logOperation("mul",mul(2,3))()
logOperation("sub",sub(2,3))()