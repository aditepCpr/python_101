class MyMathException(Exception):
    def __init__(self, arg):
        self.args = arg

    def getMsg(self):
        return ''.join(self.args)


class MyMathError(ArithmeticError):
    """Invalid Number"""
    pass

