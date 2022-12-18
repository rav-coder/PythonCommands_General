
# list:
# lists are mutable - add update and delete
# ordered - indexing and slicing
# can store any type of data - heterogenous datatype

l = [10, 20, 30, 40, "Python", [100, 200, 300]]

print(l,type(l))

print(l[0])
print(l[-1]) # prints last element on the list
print(l[-1] [1]) # go to end of list, and the second element on the list 200

# print(l[20]) list index out of range

print(l[1:3])

print(l[::-1]) # reverse the list

l = [100, 200, 300, 400]

for value in l[::2]:
	print(value)

# append : takes one argument only
print(id(l))
l.append(600) # modify in the same memory location
print(l, id(l))

# extend : add multiple elements
l.extend([500,600, 700])
print(l)

# will add character by character like this 'P', 'y', 't', 'h', 'o', 'n'
l.extend("Python")
print(l)


# insert at index : only one element
l.insert(1, 1000)

l2 = l
print(id(l), id(l2)) # memory location is the same 


# copy with different memory location
l3 = l.copy()
print(id(l), id(l3))


# update and delete from list - pop remove clear del
l = [10, 20, 30, 20, 20, 40, 20, 20]
l[2] = 300

r = l.pop() # remove the last element
r = l.pop(1) # remove on index
r = l.remove(20) # remove by element value - first occurence

# l.clear() removes all elements on the list
# del l remove the list from the memory location

print(l)

l.sort() # sorts the original list

print(l[::-1]) # reverse the list
# or l.reverse()

l3 = sorted(l) # returns a list sorted and assings it : any data type

print(l.index(20)) # search from left to right, first found index
print(l.count(20)) # total occurence in the list of the given element

print(l + l2) # add two lists together


l = [0.1]

print(l * 10) # add the same element 0.1 ten times in the list
# [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
