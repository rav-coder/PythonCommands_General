import re

## for a single character
# . means it maches any character
# [a-z] match lowecase character
# [a-zA-Z] matches upper and lowecase
# [0-9] digit class

## some shortcuts
# [0-9] digit class can also be written as \d
# compliment of digit i.e. [^0-9] can be written as \D
# alphanumeric [a-zA-Z0-9] can be written as \w
# compliment of alphanumric is \W
# match with space can be \s
# compliment of space can be \S


## multiple characters
# + atleast one
# * zero or more
# ^ start of the string
# $ end of the string
# ? optional

# [a-z]{4} means there has to be four occurences of lower case character

# [a-z]{2,4} range means at least 2 or at max 4 lower case characters


s = "ABCDE1234A" # the pattern is 5 alphabets followed by 4 digits followed by a character

s2 = "AAAAAAAABCDE1234A"

r = re.compile("[A-Z]{5}[0-9]{4}[A-Z]") # s = "AAAAAABCDE1234A" this would be valid under this expression so we need to specify start and end

l = re.findall(r,s)

print(l)

s2 = "AAAAAAAABCDE1234A"

r2 = re.compile("^[A-Z]{5}[0-9]{4}[A-Z]") # specify start matching with ^

l2 = re.findall(r2,s2)

print(l2)


# specify the end as well with $ 
s3 = "ABCDE1234AAA"

r3 = re.compile("^[A-Z]{5}[0-9]{4}[A-Z]$") 

l3 = re.findall(r3,s)

print(l3)


# findall and search
s4 = "12-02-2021"
r4 = re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")

l4 = re.findall(r4,s4) # find all matching patterns in a list and return

print(l4)


m = re.search(r4,s4) # if pattern exists if returns a match object else None
# print(m)

if m:
	print(m.group())
else:
	print("pattern not found")



# if we put paranthesis around the regular expression we get a group and name them as well
r5 = re.compile("^(?P<day>[0-9]{2})-(?P<month>[0-9]{2})-(?P<year>[0-9]{4})$")

m = re.search(r5,s4) # if pattern exists if returns a match object else None
# print(m)

if m:
	print(m.group(0),m.group(1),m.group(2),m.group(3)) # group 0 returns the full string, 
	# group 1 returns the first group 12 in this case, group 2: 02, group 3:2021

	print(m.group("day"), m.group("month"), m.group("year"))
else:
	print("pattern not found")


# lets say we want to match with +91 being optional
s = "+91 23423423"
s2 = "12323213" # both need to pass, make regex

r = re.compile("(\+91\s)?[0-9]{8}") # ? specifies the whole group +91 is optional and \s means a space
# add \ before + symbol to let regex know to escape it (its not the defualt + which means at least one)

a = re.search(r,s)
b = re.search(r,s2)

print(a,b)

# non capturing group add ?: to specify ("(?:\+91\s)?([0-9]{8})") +91 will not be listed in group


