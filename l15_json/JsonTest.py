import json

json_data = '{"name":"Beian","city":"Seattle"}'
python_obj = json.loads(json_data)
print(python_obj["name"])
print(python_obj["city"])


########################  Array ###############################

array = '{"drinks":["coffee","tea","water"]}'
data = json.loads(array)

for element in data['drinks']:
    print(element)


###################### dumps() ###############################

# a Python object (dict):

x = {
    "name":"John",
    "age":30,
    "city":"New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

#############################################################

