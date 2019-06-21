def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers([1,2,3,4,5])
# my_nums = [x*x for x in [1,2,3,4,5]]

print(my_nums) # [1, 4, 9, 16, 25]

for x in my_nums:
    print(x)

print('#### Generator ####')
# Generrator
def square_numbers(nums):
    for i in nums:
        yield (i*i)

my_nums = square_numbers([1,2,3,4,5])
# my_nums = [x*x for x in [1,2,3,4,5]]

print(my_nums) # [1, 4, 9, 16, 25]

# iterator
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))

for x in my_nums:
    print(x)
# lambda
# list
my_nums = [x*x for x in [1,2,3,4,5]]
# Generator
my_nums = (x*x for x in [1,2,3,4,5])

print(my_nums)