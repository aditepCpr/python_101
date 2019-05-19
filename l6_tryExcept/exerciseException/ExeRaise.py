from l6_tryExcept.exerciseException.Myexception.myexception import MyMathException, MyMathError


def div(a1, a2):
    return a1 / a2


a1 = 3
a2 = 0

try:
    if (a2 == 0):
        raise MyMathException("divide by zero ..... MyMathException")
    res = div(a1, a2)
    print(res)
except MyMathException as e:
    print(e.getMsg())

try:
    if (a2 == 0):
        raise MyMathError("divide by zero ..... MyMathError")
    res = div(a1, a2)
    print(res)
except MyMathError as e:
    print(e)
