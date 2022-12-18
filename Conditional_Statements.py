
#Conditional statement

# if [condition]:
# 	statements
# elif [condition]:
# 	statements
# else:
# 	statements

num1 = 100
num2 = 200

if num1 > num2:
	print("num1 is greater than num1")
elif num2 > num1:
	print("num2 is greater than num1")
else:
	print("num1 and num2 is equal")

#every code inside the block must be in the same indentation level


#Loops
#for loop and while loop
# Iteratable datatypes: str list tuple dict set

# for [variable_name] in [iterable datatype]:
# 	statements

l = [10, 20, 30, 40, 50]

sum = 0
for value in l:
	sum += value
	print(value)

print(sum)

# range(5) 0 1 2 3 4
# range(10, 100) 10, 11, 12 ... 99
# range(10, 100, 5) 10, 15, 20 .... 95
sum = 0
for value in range(10, 100, 5):
	sum+= value
	print(value)

print(sum)


#break continue pass enumerate
for value in range(10):
	print(value)

l = [10, 20, 30, 40]
key = 400

for value in l:
	if value == key:
		print("Element found")
		break
	else:
		continue
else:
	print("Element not found") #for loop has an optional else block

print("Statement after loop")

#enumerate
for index, value in enumerate(l):
	if value == key:
		print("Element found at index", index)
		break
	else:
		continue
		print("Statement after continue is not executed")
		print(index, value)
else:
	print("Element not FOUND")

#pass
for index, value in enumerate(l):
	if value == key:
		print("Element found at index", index)
		break
	else:
		pass
		print("Statement after pass is executed")
		print(index, value)
else:
	print("Element not FOUND")


#while loop
# while[condition]:
# 	[statements]
# else:

count = 1
sum = 0

while count <= 20:
	sum += count
	count = count + 1

print(sum)



