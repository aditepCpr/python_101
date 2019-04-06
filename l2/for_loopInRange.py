numbers = [1,2,3,4,5,6,7,8,9,10]
print('numbers =',type(numbers),numbers)
sum = 0
for val in range(1,11):  # 11-1 = 10 ,  1 -> 10
        print('val = ',val,type(val))
        sum += val
        print('sum =',sum)
print('end loop sum =',sum)

# range(10)
# range(1,10)
# range(1,10,2)
# range(begin,end,step)