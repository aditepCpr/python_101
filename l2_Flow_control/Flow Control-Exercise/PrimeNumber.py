num = 10;
if num > 0:
    for j in range(2,num):
        if (num % j) == 0:
            print(num,"is not a prime number")
            print(j,"times",num//j,"is",num)
            break
    else:
        print(num,'prime number')
else:
       print(num,"is not a prime number")



