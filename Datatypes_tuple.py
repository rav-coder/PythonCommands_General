
# immutable, ordered data structure: indexing and slicing

# help(tuple)
t = (10, 20, 30, 30, 40, 40, 30)

print(t,type(t))

print(t[:3]) # from index 0 to 2 

print(t.index(30))

print(t.count(30))


l = [10, 20, 30, 40]

for index, value in enumerate(l):
	print(index, value)

for t in enumerate(l):
	print(t, t[0], t[1])
# index value tuple is returned 
# (0, 10)
# (1, 20)
# (2, 30)
# (3, 40)

t = tuple(l) # convert list to tuple
print(t)

l = list(t) # convert tuple to list

