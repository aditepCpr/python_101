try:
    file = open("student", "r")

    sum = 0
    allstds = file.readlines()

    print('std =', len(allstds))

    for s in allstds:
        stdcol = s.split(sep=',')
        grade = float(stdcol[4])
        sum += grade

    mean = sum / len(allstds)
    print("mean", mean)

    passStd = []
    for s in allstds:
        stdcol = s.split(sep=',')
        grade = float(stdcol[4])
        if (grade >= mean):
            passStd.append(s)

    print(len(passStd))

    for p in passStd:
        print(p.split(sep=',')[1])
except Exception as e:
    print(e)


