#  create file
file  = open("testCreateFile.txt","w")

# write file and close
file.writelines("testCreateFile!")
file.close()


# read file
f = open("testCreateFile.txt","r")
print(f.read())