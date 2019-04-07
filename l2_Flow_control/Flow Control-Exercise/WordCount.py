text = """Hello python,how are you today.
today is Monday and There are 2 pens on The table"""
find = 'on'
counter = 0
flen = len(find)

for i in range(len(text)):
    if text[i] == find[0]:       
        sub = text[i:i+flen]
        if sub == find:
            counter += 1
print(counter)


