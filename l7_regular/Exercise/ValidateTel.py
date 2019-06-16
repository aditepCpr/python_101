import re
# กำหนด แพทเทิล ของ tel
# ขึ้นต้อนด้วย 08 ตัวเลข - ตัวเลช 3 ตัว - ตัวเลช 4 ตัว
telRE = r'^08\d-\d{3}-\d{4}$'

try:
    # เปิดไฟล์
    file = open('/home/aditep/softwares/python/l5_io_FileHandling/io_Exercise/student','r')
    allStds = file.readlines()
    for s in allStds:
        name = s.strip().split(",")[1]
        tel = s.strip().split(",")[3]
        try:
            find = re.match(telRE,tel)
            print(name, " Valid :", find.group())
        except :
            print(name,"Invalid :",tel)
except Exception as e :
    print("Could not found",e)

