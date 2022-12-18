
# mutable, unordered, key should be unique, key shold be immutable
d = {"emp_id": 101, "name": "ABC", "name": "PQR"} 
# name is same key PQR overrides ABC

# hash table is used in the background O(1)

d["contact"] = 123

print(d) # {'emp_id': 101, 'name': 'PQR'}

# unordered so cant find by index, need key
print(d["emp_id"])

# get setdefault
print(d.get("emp_id"))

print(d.get("emp", -1)) # if key exists return value otherwise return -1
print(d.get("emp", "Key does not exist"))

print(d.setdefault("age")) # if key does not exist add key to dict and set its value to none

print(d.setdefault("age"), 50) # add age and set value to 50

d = {}

for key in d:
	print(key, d[key])


# key value relationship
for value in range(1,11):
	d[value] = value * value

print(d)

# key values items
print(d.keys())
print(d.values())
print(d.items())

for t in d.items():
	print(t)


# update and delete
l1 = [1,2,3,4,5]
l2 = [1,4,9,16,25]

d = dict(zip(l1,l2)) # match keys to values
print(d) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

d = dict.fromkeys(l1,0) # put list as key and assign 0 as values
print(d)

d2 = {1:1,2:2,3:3,4:4,6:6}

d.update(d2) # combine two dictionary and assign it to one
print(d)


# pop popitem clear del

d.pop(1) # key as a parameter, will return the deleted item

d.popitem() # randomly picks an element and deletes key and value

# d.clear() delete all elements

# del d remove from memory location