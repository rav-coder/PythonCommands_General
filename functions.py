
# code reuse, modularity: logically grouping code

s = "Python, HTML, CSS"

print(s.index("HTML"))

# function call and definition

def value_reverse(value): # definition must be first
	if type(value)==list or type(value)==str: # handle the logic of datatypes
		reverse = value[::-1]
	else:
		temp = str(value)
		reverse = temp[::-1]
	return reverse

result = value_reverse(s)
print(result)

# the above function will reserve a list as well
print(value_reverse([1,2,3,4]))

print(value_reverse(1002))
# function might not return something



# 1 Positional argument: need to pass in all the required arguments

def linear_search(l,key):
	for value in l:
		if key==value:
			return True
	else:
		return False

l = [1,2,3,4,5]

key = 2

result = linear_search(l,key)
print(result)


# 2 Default argument
# ord means ASCII value, chr converts ASCII value to a character

print(ord('a'),ord('z'))
print(ord('A'),ord('Z'))

import random

def gen_password(length=8): # if parameter is not passed default is 8
	l=['#','@','$']

	upper = chr(random.randint(65,90))
	lower = chr(random.randint(97,122))

	special = random.choice(l)
	digit = random.randint(10000,99999)
	password = upper + lower + special + str(digit)

	l = random.sample(password,length)

	password=("").join(l)

	return password

result = gen_password(5)
print(result)



# 3 Keyword parameters: order of parameters matter

def validate(username,password):
	if username=="ABC" and password =="Abc@123":
		print("Valid Password")
	else:
		print("Invalid password")

validate("abc123","Abc@123")

validate(password="Abc@123",username="ABC") # can also assign explicitly


# print function: sep is ' ' and end is '\n' by default
print(100,200) # automatically adds a space in between
print("Hi") # in new line
# prints 
# 100 200
# Hi

print(100,200,sep=', ',end=' ')
print("Hi")
# prints
# 100, 200 Hi 



# 4 Variable length positional argument

# l=[1,2,3,4]
# l.append(6,7) : cant add multiple elements
# print(l)

def add_value(*args): # variable length : converts into a tuple
	# print(args)
	l = []
	for value in args:
		l.append(value)

	return l

result = add_value(1,8,9)
print(result)

result = add_value(3,5,6,7,1,3)
print(result)

result = add_value(2)
print(result)


# 5 Variable length keyword argument
# name,email,contact,dob

def get_details(**kwargs): # double star means it will be a dictionary
	print(kwargs)

get_details(name="ABC",email="abc@gmail.com",contact=213232,dob="12-02-1993")

get_details(name="ABC",email="abc@gmail.com",contact=213232)

get_details(name="ABC",contact=213232)




## Recursive Function: Factorial

def factorial(num):
	if num == 1:
		return 1
	else:
		return num * factorial(num - 1)

num1=5

result = factorial(num1)

print(result)


# Binary Search: Sorted List

def binary_search(l,key):
	mid = len(l) // 2 # double divide will return an integer

	if len(l) == 0: # if item not on list and we go to an empty list return false
		return False

	else:

		if l[mid] == key:
			return True

		elif key < l[mid]:
			return binary_search(l[:mid],key)

		else:
			return binary_search(l[mid+1:],key)


l = [1,2,3,4,5,6,7]

key = 4

result = binary_search(l,key)
print(result)

