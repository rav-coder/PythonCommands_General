#string:
# s = ' ' " " """ """

# 1 strings are immutable
s1 = "Python"
print(id(s1))

s1 = "Java"
print(id(s1)) #takes the variable name and puts it in a new memory location


# 2 ordered data structure, indexing and slicing available
s = "Python sample string"
print(s[0])
print(s[-1]) #go from right to left

#slicing
print(s[0:6]) #not inclusive at the end
print(s[7:]) #goes to the end of the statement
print(s[:6]) #from 0 to specified

#stride
print(s[::2]) # not specifying the start or end, print every 2nd character
print(s[::3]) # print every 3rd character
print(s[::-1]) # print every character from right to left

print(s[0:6:2]) # slice with stride has 3 parameters


for value in s:
	print(value)

for value in s[::2]:
	print(value)

# help(str)
# print(dir(str))

#format
num1 = 100
num2 = 200
print("value of num1 is", num1, "value of num2", num2)
print("value of num1 is {} and value of num2 is {}".format(num1, num2)) #default is {0}
print("value of num1 is {1} and value of num2 is {0}".format(num1, num2)) #can specify index
print("value of num1: {val1} and value of num2: {val2}".format(val1=num1, val2=num2)) #can specify name

#capitalize upper lower title
s= "python sample string"
s1 = s.capitalize() #first letter is capitalized for the string
print(s1)

print(s.upper()) # doesnt change original s
print(s.lower())
print(s.title()) # first letter of every word capitalized
print(s.isupper())
print(s.islower())
print(s.istitle())


#split
s = "HTML,CSS,PYTHON"
l = s.split(",") # a list of comma seperated values
print(l)

s1 = (" ").join(l) # a string with space seperated
print(s1)


# transform string with mapping
s1 = "abcd"
s2 = "1234"

s3 = "Python abcd sample abcd"

table = str.maketrans(s1,s2)
result = s3.translate(table) # replaced abcd with 1234
print(result) #Python 1234 s1mple 1234


# find substring and index
s = "HTML,CSS,PYTHON,PYTHON"
print("PYTHON" in s) 
print(s.index("PYTHON")) # gets the index of the first PYTHON found

print(s.find("python")) # returns -1 if the substring is not found rather than thrwoing an error
print(s.rfind("PYTHON")) # find first index starting from the right


#strip unwanted characters 
s = "    sample string    "
print(s.strip(" "))

s = "****sample string****"
print(s.lstrip("*")) # remove from left hand side
print(s.rstrip("*")) # remove from right hand side


# convert string to a fixed length
s = "Python"
print(s.center(20,"*")) # centers the string *******Python*******
print(s.ljust(20,"*")) # left adjusts and adds ***
print(s.rjust(20,"*")) # left adjusts and adds ***


# replace
s = "HTML,CSS,PYTHON,PYTHON"
print(s.replace('HTML', 'HTML5'))