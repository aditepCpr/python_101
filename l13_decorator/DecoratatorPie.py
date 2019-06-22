def decorate_message(fun):
    def addWelcome(site_name): # function ที่เป็น Decorator ต้องถูก design ในรูปแบบประกาศ nested function และ return ข้างใน
        return "welcome to " + fun(site_name)
    return addWelcome

@decorate_message # เรียกใช้ decorate_message เป็น decorator
def site(site_name) : # function หลัก
    return site_name

print(site('Thailand'))


def decor(func):
    def wrap():
        print("$$$$$$$$$$$$$$$")
        func()
        print("$$$$$$$$$$$$$$$")

    return wrap

@decor
def sayhello():
    print("Hello")

sayhello()
# newfunc = decor(sayhello)
# newfunc()