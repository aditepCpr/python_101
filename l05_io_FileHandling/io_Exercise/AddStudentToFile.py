notExit = True
while notExit:
    cmd = input("add studeny? (Y|N) :")

    if (cmd == "y"):
        file = open("student", 'a')
        id = input("Enter ID :")
        name = input("Enter Name :")
        email = input("Enter Email :")
        tel = input("Enter Tel :")
        grade = input("Enter Grade :")
        std = id + "," + name + "," + email + "," + tel + "," + grade + "\n"
        file.write(std)
        file.close()
        print("Add  Student successful...")
    elif (cmd == "N"):
        notExit = False
    else:
        print("Invalid Command")
