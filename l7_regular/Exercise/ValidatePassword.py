import re
# (?=.*[0-9]) กี่ตัวกอักษรก็ได้ เลข 0 - 9
# (?:.{8,}) ต้องมีตัวอักษร 8 ตัวขึ้นไป
# passRE ต้องมี ทั้งตัวเลข ตัว uppercase และ lowercase  8 ตัวอักษรขึ้นไป
passRE = r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?:.{8,})$'

try:
    # เปิดไฟล์
    file = open('/home/aditep/softwares/python/l5_io_FileHandling/io_Exercise/student','r')
    allStds = file.readlines()
    for s in allStds:
        name = s.strip().split(",")[1]
        password = s.strip().split(",")[5]
        try:
            find = re.match(passRE,password)
            print(name, " Valid :", find.group())
        except :
            print(name,"Invalid :",password)
except Exception as e :
    print("Could not found",e)
