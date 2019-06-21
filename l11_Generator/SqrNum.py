def sqr_num(nums):
    res = []
    for n in nums :
        res.append(n*n)
    return res

msqr = sqr_num([1,2,3,4,5,6])
print(msqr)



# Generator

def sqr_num2(nums):
    for n in nums:
        yield n*n

msqr = sqr_num2([1,2,3,4,5,6])
print(msqr)
print(next(msqr))
print(next(msqr))
print(next(msqr))
print(next(msqr))
print(next(msqr))
print(next(msqr))
print('*'*30)

for x in msqr:
    print(x)

msqr = sqr_num2([1,2,3,4,5,6])
for x in iter(msqr):
    print(x)
print('*'*30)

# list
msqr = [x*x for x in [1,2,3,4,5,6]]
print(msqr)
# generator
msqr = (x*x for x in [1,2,3,4,5,6])
print(msqr)
print('*'*30)


def sqr_4(num):
    yield num * num

msqr = sqr_num2([1,2,3,4,5,6])
for x in msqr:
    for y in sqr_4(x) :
        print(y)

## Test Mem   iterator vs Generator

import  os
import psutil
process = psutil.Process(os.getpid())
def sqr_num3(nums):
    # res = []
    for n in range(nums):
    #     res.append(n*n)
    # return  res
       yield n*n

print('Mem Before',process.memory_info().rss,"Byte") # in bytes
msqr = sqr_num3(10000)
print("Mem After",process.memory_info().rss,"Byte") # in bytes
# for x in msqr:
#     print(x)