import json as js
file = open("company.json","r")

jCompData = js.load(file)
for com in jCompData['list']:
    print(com['id'])
    print(com['brand'])
    print(com['OS'][0])
    print(com['company']['name'])
    print(com['company']['location']['postcode'])
    print('#' * 30)