class Student:
    id = None
    name = None
    email = None
    grade = None
    courses = []

    def __init__(self, id=None, name=None, email=None, grade=None):
        if (id is not None and name is not None and email is not None and grade is not None):
            self.id = id
            self.name = name
            self.email = email
            self.grade = grade
        else:
            pass

    def setInfo(self):
        self.id = '01'
        self.name = 'aditep'
        self.email = 'test@test.com'
        self.grade = 4
        print('setInfo')
        print(self.id)

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getGrade(self):
        return self.grade

    def addCourse(self,course):
        self.courses.append(course)

    def info(self):
        print('Student Name :',self.name)
        for c in self.courses :
            print(type(c))
            c.info()