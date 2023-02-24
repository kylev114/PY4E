import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
stuffParse = stuff.findall('users/user')

print(stuffParse)
print('User Count:', len(stuffParse))

# The findall method retrieves a Python list of subtrees that represent the user
# structures in the XML tree. Then we can write a for loop that looks at each of
# the user nodes, and prints the name and id text elements as well as the x attribute
# from the user node.

for item in stuffParse:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))

# Note that findall() method requires the element to find and its parent element.
# In line 5, <user> elements are nested within the <users> parent. 
# If we use findall() with just the user element# the method returns <user> elments 
# that are not nested in a parent which are 0 in the xml text.

stuffParse = stuff.findall('user')
print('User count:', len(stuffParse))
