from l8_oop.lab.Student import *
from l8_oop.lab.Course import *

itcpures = ITCourse('C-01','IT','100')
statcourse = StatCourse('C-02','IT','100')

std1 = Student('01','aditep','test@test.com',4)
std2 = Student('02','top','test@test.com',4)

std1.addCourse(itcpures)
std1.addCourse(statcourse)
std1.info()

std2.info()