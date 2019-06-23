import json

file = open("Emp.json","r")
data = json.load(file)

print(data)
print(data["firstName"])
print(data["age"])
print(data["phoneNumbers"][0])

