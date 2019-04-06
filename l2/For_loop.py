numbers = [7,4,1,2,5,8,9,4,11]
print('numbers =',type(numbers),numbers)
sum = 0
for val in numbers:
        print('val = ',val,type(val))
        sum += val
        print('sum =',sum)
print('end loop sum =',sum)

## Output

# numbers = <class 'list'> [7, 4, 1, 2, 5, 8, 9, 4, 11]
# val =  7 <class 'int'>
# sum = 7
# val =  4 <class 'int'>
# sum = 11
# val =  1 <class 'int'>
# sum = 12
# val =  2 <class 'int'>
# sum = 14
# val =  5 <class 'int'>
# sum = 19
# val =  8 <class 'int'>
# sum = 27
# val =  9 <class 'int'>
# sum = 36
# val =  4 <class 'int'>
# sum = 40
# val =  11 <class 'int'>
# sum = 51

# end loop sum = 51