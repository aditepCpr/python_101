class Course():


    def __init__(self, id=None, name=None, length=None):
        if (id is not None and name is not None and length is not None):
            self.id = id
            self.name = name
            self.length = length
        else:
            pass



    def setInfo(self):
       self.id = 'C-01'
       self.name = 'Java'
       self.length = 60

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getLength(self):
        return self.length

    def info(self):
        print('CourseID :',self.id)
        print('CourseName :',self.name)
        print('CourseLength :',self.length)

class ITCourse(Course):


    def __init__(self, id=None, name=None, length=None):
        if (id is not None and name is not None and length is not None):
           super().__init__(id,name,length)
        else:
            pass

class StatCourse(Course):


    def __init__(self, id=None, name=None, length=None):
        if (id is not None and name is not None and length is not None):
           super().__init__(id,name,length)
        else:
            pass