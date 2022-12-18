first_num = 10
second_num = 20
addition = first_num + second_num
print(addition)

# python automatically declared the type in the background
print(type(first_num), type(second_num))

# id is the memory location
print(id(first_num), id(second_num))

# object intering : if we define two variables having same values, python will
# not create a new memory location
a = 10
b = 10

print(id(a), id(b))

# id
# type

# 1 variable name should start with lower case characters
# 2 digits are allowed but not at the start
# 3 _ allowed