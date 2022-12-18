
# JSON and XML only have data, no functions

# Json objects : python dictionaries{"key":"value"}
# numbers : int float
# array : list
# " " : " " or ' ' or """ """

import json

handle = open("EmployeeData.json","r")
content = handle.read()

print(content)

l = json.loads(content)
# print(l)

d = l[-1]
print(d['id'])

d['id'] = 1000


## open in write mode

# j = json.dumps(d) : automatically does all the conversions
# json.dumps(d,indent=4,sort_keys=True): adds indentation with 4 spaces and sorts in alphabetic order
# handle = open("out.json","w")
# handle.write(j)




## Parse XML files
# pip install xmltodict

# import xmltodict
# handle = open("xml","r")
# content = handle.read()

# d = xml.dict.parse(content) : gives the dictionary
# print(d['Result']['Code'])
# d['Result']['Code'] = 3

# x = xmltodict.unparse(d)
