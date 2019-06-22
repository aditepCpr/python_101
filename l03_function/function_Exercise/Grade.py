def nummin(*num):
    nummin = num[0]
    for n in num:
        if  nummin > n:
            nummin = n
    return nummin

def nummax(*num):
    nummax = num[0]
    for n in num:
        if  nummax < n:
            nummax = n
    return nummax
    
def average(*num):
    sum  = 0
    for n in num:
        sum += n       
    return sum / len(num)
    
print(nummin(5,1,2,3,4,21,4,5,76,123))
print(nummax(5,1,2,3,4,21,4,5,76,123))
print(average(5,2,3,6,4,11))