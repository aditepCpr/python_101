num_1 = 1
num_2 = 1
def fibo(num):
    global num_1,num_2
    for n in range(num):
        num_3 = num_1 + num_2
        num_2 = num_1
        num_1 = num_3
        if num_3 > num:
            break
        else:
            print(num_3)

print(fibo(1597))

