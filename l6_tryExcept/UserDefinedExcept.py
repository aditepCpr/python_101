class Networkkerror(RuntimeError):
    def __init__(self,arg):
        self.args = arg

try:
    raise Networkkerror("Bad hostname")
except Networkkerror as e:
    print(e.args)