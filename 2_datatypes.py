# Datatypes

# 1 Int :
num1 = 100
print(type(num1))


# 2 Float
num2 = 15.23
print(type(num2))

# immutable : can not modify the variable in the same memory location
# integer and floats and strings are immutable
test1 = 100
print(id(test1))

test1 = 105
print(id(test1))


# 3 String ''  ""  """ """
s = "Python"
print(s, id(s) , type(s))

# New will be enclosed in single quote inside the string
s = "'New' Python"
print(s, id(s))

# for double quotes inside
s = """ "NEW" Python """
print(s)


# 4 list : []
# list is mutable i.e. can change in the same memory location
# can save multiple data types
l = [10, 20, 30, 40, 50, "Python", "Django"]
print(l, id(l))

l.append(60)
print(l, id(l))


# 5 tuple
# tuple is immutable, can not add update or delete any element unlike list
# can have different data types
t = (10, 20, 30, "new")
print(t)


# 6 Dictionary: (mutable)
# key value pair or hashmap

d = {"name":"ABC", "email":"abc.gmail.com"}
print(d)


# Set {} (mutable)
s = {10, 20, 30}


# 8 bool : True False
t = True;
print(t)


# 9 complex (work with complex numbers) complex : 5 + 3

help(str) # get a manual for the different datatypes