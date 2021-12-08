#JSON FILE
#JSON 1

import json
data = '''
{
    "name":"Jenny",
    "phone":{
        "type":"intl",
        "number":"+1 587 707 9197"
    },
    "email":{
        "hide":"yes"
    }
'''
info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])

#Json is similar with python and use a lot of dictionary format

#JSON 2
import json
data = '''
[
    { "id": "001",
      "x":"2"
      "name":"chuck
    },
    { "id": "009",
      "x":"7"
      "name":"chuck
    }
]'''
info = json.loads(input)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
