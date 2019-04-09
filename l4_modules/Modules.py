#from l4_modules.example import  add
from l4_modules.example import *
import sys
import l4_modules.example as ex


print(add(1, 2))
for p in sys.path:
    print(p)

print(div(ex))
print(ex.add.__doc__)



