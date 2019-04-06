n = 10
sum = 0 
i = 1

while i <= n:
    sum += i
    i+=1
    print(sum)
    if sum == 36:
        print('sum = 36 :: Break')
        break
print('The sum is', sum)
        
