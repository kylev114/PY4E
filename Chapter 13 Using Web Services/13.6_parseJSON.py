# Since JSON files are written with same syntax as python(dicts and lists),
# its simpler to directly inject it into python code. In this example,
# we represent a list of users where each user is a dict.

# The json library has two main methods: 
# json.load() converts JSON data into python
# json.dump() converts python into JSON

# Compared to XML, JSON has less detail, so we must know in advance that we are getting a
# list and that the list is of users and each user is a set of key-value pairs. The JSON
# is more succinct (an advantage) but also is less self-describing (a disadvantage)

import json

data = '''[  { "id" : "001", "x" : "2", "name" : "Chuck"} ,
{ "id" : "009", "x" : "7", "name" : "Brent"}  ]'''

info = json.loads(data)
# No need for findall() as the user count is number of dicts

print(info)
print('User count:', len(info))

for item in info: 
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

# For more JSON Documentation
# https://docs.python.org/3/library/json.html
# https://www.w3schools.com/python/python_json.asp