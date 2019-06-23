import json as js

# jsonText = "{'a':'b'}"  error
jsonText = '{"a":"b"}'

jData = js.loads(jsonText)
print(jData['a'])
print(jData["a"])
print("*" * 30)

jsonText = """
                {
                "a1":"b1",
                "a2":"b2",
                "a3":"b3",
                "a4":"b4"
                }
                
            """

jData = js.loads(jsonText)
print(jData['a1'])

print("*" * 30)

computers = """{
                "id":"123",
                "brand":"PC",
                "OS":["window","Solaris","Linux"],
                "company":{
                            "id":"com123",
                            "name":"ABC Company Limited",
                            "location":{"postcode":"101000"}
                }

}"""

jComData = js.loads(computers)
print(jComData['id'])
print(jComData['brand'])
print(jComData['OS'][0])
print(jComData['company']['name'])
print(jComData['company']['location']['postcode'])
print("*" * 30)

##########################################################


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

file = open('company.json','w')
# js.dump(jCompdata2, file)
js.dump(jCompdata2, file,indent=4)
print('Yehh')