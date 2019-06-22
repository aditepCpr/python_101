from l04_modules.example import  add
from l04_modules.example import *
import sys
import l04_modules.example as ex


print(add(1, 2))
print(div(1,2))

for p in sys.path:
    print(p)
print(dir(ex))

print(ex.add.__doc__)



