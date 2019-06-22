grade = [3.5,4.0,3.8,2.9,3.0,1.7,4.0,2.99]
passScore = 3.0
numPass = 0
for sc in grade:
    if sc >= passScore:
        numPass += 1
print('student passed =',numPass)


