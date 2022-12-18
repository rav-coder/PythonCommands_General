
# Operators in Python

# 1 Arithmetic Operators + , - , * , / , // , % , **

num1 = 10
num2 = 20

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)


# division is always return a float
# also called crude division
print(10 / 3)

# can go with floor division to get the integer only
print(10 // 3)


print (10 % 3) # remainder

print (10 ** 2) # to the power of



# 2 Comparision operator < , > , <= , >= , == , !=
# result will always be true or false



# 3 Identity operators is , is not
num1 = 100
num2 = 100

print(num1 == num2)
print(num1 is num2)

# identity operator will compare the memory location
l = [10, 20, 30]
l2 = [10, 20, 30]

print (l == l2)
print (l is l2)
print (l is not l2)


# 4 Assignment operators = , += , -= , *= , /=



# 5 Bitwise operators & (AND) , | (OR) , ^ (XOR) , >> (right shift) , << (left shift)

# perform operations on individual bits and convert back to integer format

num1 = 2 # 0b10 or 10
num2 = 1 # 0b1 or 1
print(bin(num1), bin(num2))

print(num1 & num2)  # (1 * 1) * (1 * 0) = 0
print(num1 | num2)  # (1 + 1) + (1 + 0) = 3

print (2 >> 1) # right shift means 10 becomes 01 which has a decimal value of 1
print ( 2 << 1) # left shit means 10 becomes 100 which has a decimal value of 4



# 6 Logical Operators and , or , not
print(10==10 and 20==20) # and returns true if all values are true
print(10==10 or 20==20) # or returns false if all values are false
print(not(10==10)) # not is the complement or opposite



# 7 membership operators in , not in
l5 = [10, 20, 30]
print(50 in l5)
print(30 not in l5)

# case sensitive
s6 = "Python string"
print("Python" in s6)
print("python" not in s6)



