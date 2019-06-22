# Generator
` เป็นการยืมข้อมูล ไม่เปือง RAM `
```
- Solve Iterator Problem (Overhead)
- like an iterator
- Are simple function
- return an iterable set of items 
- can be paused and resumed
- Memory Efficient
- Represent Infinite Stream
```

```python
yield
```

```python
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
     return result

my_nums = square_numbers([1,2,3,4,5])
# my_nums = [x*x for x in [1,2,3,4,5]]

print(my_nums)


```

```python
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

# Generator
def square_numbers(nums):
    for i in nums:
        yield (i*i)

####  lambda  ####
       
# list 
my_nums = [x*x for x in [1,2,3,4,5]]
# Generator
my_nums = (x*x for x in [1,2,3,4,5])

```

เขียน PowTwo ด้วย generator เมื่อเทียบกับ iterator code มีขนาดสั้นลงมาก
```python
def PowTowGen(max = 0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1


ip = PowTowGen(5)

for i in ip :
    print(i)

```

## Pipelining Generators
#### output ของ stream ตัวแรกไปเป็น input ของ stream ตัวถัดไป
```python
with open('sells.log') as file: # เปิดไฟลฺ์จาก sells.log
    pizza_col = (line[3] for line in file ) # แล้วอ่านค่าไฟลืมาที่ละ line ที่ line 4 index[3] 
    per_hour = (int(x) for x in pizza_col if x != 'N/A') #เอาผลลัพท์ของ  pizza_col  มาวนต่อหา per_hour 'มี col ที่ไม่เท่ากับ 'N/A' หรือไม่'
    print("Total pizzas sold =", sum(per_hour)) 
    
# ให้อ่าน sells.log ไฟล์ line 3  ให้อ่านจำนวณชัวโมงมา เพื่อคำนวณ

```