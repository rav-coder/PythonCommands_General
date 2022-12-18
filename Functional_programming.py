
# List comprehension

l = [1,2,3,4,5]

l2 = []

for value in l:
	l2.append(value*value)

print(l2)

# or
l3 = [value*value for value in l] # specify output at the start, then iteration follows
print(l3)

# using comprehension: when we have a iterable element and want to perform the same set of operation on all the elements
l = [1,2,3,4,5,6,7]

# return a list of even elements only
l4 = [value for value in l if value%2 ==0]
print(l4)

# make a list which stores the length of each element
l=['abc','abdsf','xxssdd']

l5=[len(value) for value in l] # comprehension is faster than a normal for loop, its implicit call rather than explicit
print(l5)

l6 = [(value1,value2) for value1 in range(1,5) for value2 in range(100,103)]
print(l6) # we can write if else statements and nested for loops also

l = [[1,2,3],[4,5,6],[7,8,9]]
l2 = []

for value in l:
	for val2 in value:
		l2.append(val2)

print(l2)

l3=[val2 for value in l for val2 in value]
print(l3)

# even or odd
l=[1,2,3,4,5,6]

l2=['Even' if value%2==0 else 'Odd' for value in l]
print(l2)



# Dictionary comprehension
d = {x:x**2 for x in range(1,11)}
print(d)

# ASCII value
d = {chr(x):x for x in range(97,123)}
print(d)

d2 = {value:key for key,value in d.items()} # swap
print(d2)



# map, filter and lambda function: much faster than comprehension

# Map: output will always be the same length as the input
# finding only odd or even elements can not be done with map since output length varies from input list length
def sqr(num1):
	return num1**2

l = [1,2,3,4,5]

# map returns a map object, can typecast map to list: for value in list(map(sqr,l)): print(value)
print(list(map(sqr,l))) # map takes a function and a iterable element as arguments

l2 = [10,20,30,40,50]

def add(num1,num2):
	return num1+num2

result = list(map(add,l,l2)) # can have any number of iterable elements
print(result)


# Filter: to filter out some elements from the list

def check_num(num1): # one element passed from filter
	if num1%2 == 0: # return true should be the values we want
		return True
	else:
		return False # filters and rejects elements that return false

result = list(filter(check_num,l)) # returns a filter object with elements that are true
print(result)



# Lambda: works well with the map function, small function that doesn't need to have a seperat definition

l3=[1,2,3,6,7]

result=list(map(lambda num1:num1**2,l3)) # cannot do item assignment
print(result)

result = list(filter(lambda num:num%2==0,l3)) # check if the elements mod 2 is 0 or not, comparision operator means lamda will return T or F
print(result)


# sort dictionary on the basis of values
d = {1:10,2:2,3:30}
print(sorted(d)) # sorted works on the basis of keys only

print(dict(sorted(d.items(),key=lambda x:x[1]))) # basis of values




# Generator functions: returns one or any numbers of values specified at a time
l = [1,2,3,4,5]

def printVal(l): # in normal function, transfers control and come back to caller
	for value in l:
		print(value)

printVal(l)


# lets say we are generating infinite fib series numbers
def fibo():
	first_num = 0
	second_num = 1
	yield second_num # this line is only executed once since its outside the while loop
	while(True):
		next_val = first_num + second_num
		yield next_val # instead of return we have a yield
		first_num,second_num = second_num,next_val

print(fibo()) # prints a generator class object

g = fibo()

# print(next(g)) # next starts executing the function until it encounters the yield statement and comes back to caller
# print(next(g)) # maintains the state and starts executing right below the yield statement and reruns
# print(next(g))
# print(next(g))

for value in range(10): # print first 10 fib numbers
	print(next(g))

for value in range(20): # now we print the next 20 fib numbers as state is being saved
	print(next(g))


# need to handle exception of going beyond the length of the list when using next

l = [1,2,3,4]

l2 = (value*value for value in l) # having () in comprehension means we get a generator object
print(l2) # reducing memory consumption as we are generating values one at a time rather than all once
print(next(l2))





# Iterators: much better than list for performance reasons with large data
l = [10,20,30,40]
i = iter(l)

print(next(i))

import itertools

l2 = [20,30,40,60]
l3 = [200,300,400,600]


i = itertools.chain(l,l2,l3)

print(next(i))

for value in i:
	print(value) # iterates over all 3 lists and prints the elements


# cycle: can iterate continuosly ( need a stop condition )
count = 0

for value in itertools.cycle(l):
	if count<16: # 16 means it prints 10,20,30,40 (4 elements) four times
		print(value)
	else:
		break
	count += 1


# repeat
count = 0
for value in itertools.repeat(l):
	if count<4: # print the list [10, 20, 30, 40] four times
		print(value)
	else:
		break
	count += 1


# Tee
i = iter(l)
t = itertools.tee(i) # by defualt two iterators as tuples

for value in t[0]:
	print(value)

for value in t[1]: # iterate over the same list again
	print(value)

t = itertools.tee(i,5) # we will have 5 iterable tee objects

# slice for iterators
i = iter(l)
for value in itertools.islice(i,0,2): # will only print the fist two elements in the list 10 and 20
	print(value)



# series of infinite numbers: count to stop the infinite loop
count = 0
for value in itertools.count(100,5): # specify the start and increment, but no end unlike range(100,200)
	if count > 20: # count() means it will start with 0 and increment by 1
		break
	else:
		print(value)
	count += 1


# permutation and combination
l=[1,2,3]

print(list(itertools.permutations(l,2))) # all possibilities listed

print(list(itertools.combinations(l,2))) # order does not matter: [(1, 2), (1, 3), (2, 3)]
