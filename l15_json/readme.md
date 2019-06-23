# JSON

``` การติดต่อ data  ```
```
JsonEncoder

dump()  dumps()  Serializer()

JsonDecoder

load()  loads() DeSerialized
```
### python and Json dateType
```
Python      Json

dict        object
list,tuple  array
str         String
int,float   Number
True        true
False       false
None        null
```
```
CSV = Comma Sparation Value
123,Jacky,jack@gmail.com

เกิดปัญหาที่ไม่รู้ว่าข้อมูลข้างใน type อะไร
ทำให้เกิด

XML  Extensible Markup Language อยู่ในรู้แบบแทค
<id>123</id><name>Jacky</name>

Json = JavaScript Object Notation ->  CSV = JSON =  XML  > Planin-Text
key,valuse
{"id":"123","name":"Jacky"}
.json
```
```json
{
  "firstName": "John",
  "lastName": "Smith",
  "isAlive": true,
  "age":25,
  "height_cm": 167.6,
  "address": {
    "streetAddress": "24 2n Street",
    "city": "New York",
    "state": "NY",
    "postalCode": "10021-300"
  },
  "phoneNumbers": [
    {
    "type":"home",
    "number": "212 55-1234"
    },
    {
    "type": "office",
      "number": "646 555-4567"
    }
  ],
  "children": [],
  "spouse": null
}

```
## loads()

```python

import json

json_data = '{"name":"Beian","city":"Seattle"}'
python_obj = json.loads(json_data)
print(python_obj["name"])
print(python_obj["city"])

```
## array
```python
import json
array = '{"drinks":["coffee","tea","water"]}'
data = json.loads(array)

for element in data['drinks']:
    print(element)
```

## dumps()

```python
# a Python object (dict):
import json
x = {
    "name":"John",
    "age":30,
    "city":"New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

```
``` 
dumps(x)
dumps(x,indent=4)  ทำให้อ่านง่ายขั้น
dumps(x,indent=4,separators=(".","=")) เปลี่ยนจาก . เป็น =
```

## json + python I/O
```python

import json

file = open("Emp.json","r")
data = json.load(file)

print(data)
print(data["firstName"])
print(data["age"])
print(data["phoneNumbers"][0])

```

```python

computers2 = """{
                "list" : [
                {"id":"123",
                "brand":"PC",
                "OS":["window","Solaris","Linux"],
                "company":{
                            "id":"com123",
                            "name":"ABC Company Limited",
                            "location":{"postcode":"101000"}
                }},
                {"id":"124",
                "brand":"PC",
                "OS":["window","Solaris","Linux"],
                "company":{
                            "id":"com124",
                            "name":"ABC Company Limited",
                            "location":{"postcode":"1231000"}
                }}
                ]
}"""

jCompdata2 = js.loads(computers2)

for com in jCompdata2['list']:
    print(com['id'])
    print(com['brand'])
    print(com['OS'][0])
    print(com['company']['name'])
    print(com['company']['location']['postcode'])
    print('#'*30)

## dump

file = open('company.json','w')
# js.dump(jCompdata2, file)
js.dump(jCompdata2, file,indent=4)
print('Yehh')

## read
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

```