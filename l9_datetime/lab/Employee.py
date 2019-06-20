from datetime import datetime
from datetime import timedelta


class Employee:
    id = 'E-00'
    name = 'NameEmp'
    dob = '1-1-1970'
    startWork = '1-1-2019'

    # constructor Overloading
    def __init__(self, id=None, name=None, dob=None, startWork=None):
        if (id is not None and name is not None and dob is not None and startWork is not None):
            self.id = id
            self.name = name
            self.dob = dob
            self.startWork = startWork
        else:
            pass

    # Encapsulations
    def info(self):
        print('ID :', self.id)
        print('NAME :', self.name)
        print('BD:', self.dob)
        print('StarWork :', self.startWork)
        self.ageForEachEmployee()
        self.ageOfEmploy()
        self.totalVacation()

    def ageForEachEmployee(self):
        dt = datetime.today()
        afEmp = dt.strptime(self.dob, '%d-%b-%Y')
        # print((dt-afEmp).days,'day')
        afEmpyear = (dt - afEmp).days / 365

        print('Age :', int(afEmpyear), 'year')


    def dayWork(self):
        dt = datetime.today()
        aoEmp = dt.strptime(self.startWork, '%d-%b-%Y')
        dayWork = (dt - aoEmp).days
        return dayWork

    def ageOfEmploy(self):
        dayWork = self.dayWork()
        aoEmptyear = dayWork / 365
        #print(aoEmptyear)
        if int(aoEmptyear) <= 0:
            monthWork = dayWork / 30
            dayWork2 = dayWork - (int(monthWork) * 30)
            print('Age Of work :', int(monthWork), 'month', dayWork2, 'day')
        elif int(aoEmptyear) > 0:
            aoEmptyear2 = aoEmptyear-int(aoEmptyear)
            print(aoEmptyear2)
            monthWork = aoEmptyear2*365 / 30
            dayWork2 = (monthWork - int(monthWork)) * 30
            print('Age Of work :',int(aoEmptyear), 'year',int(monthWork),'month',int(dayWork2),'day')
        else:
            pass



    def totalVacation(self):
        workyear = self.dayWork() / 365
        #print(workyear)
        if  workyear <= 5:
            print('vacation 10 day')

        elif  workyear <= 9:
            print('vacation 12 day')

        elif  workyear <= 15:
            print('vacation 15 day')

        else:
            print('vacation 15 day')

