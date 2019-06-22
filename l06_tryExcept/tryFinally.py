#!/python/l6_tryExcrpt
try:
    fh = open("testfile", "w")
    try:
        fh.write("this is my test file for exception handling!!")
    finally:
        print("Going to close the file")
        fh.close()
except IOError:
    print("error: can\'t find file or read data")

try:
    fh = open("testfile","r")
    txt = fh.read()
    print(txt)
except IOError :
    print("error IO")
