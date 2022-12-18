
# 1 set
# mutable: add update delete
# unique elements
# can only add immutable elements in set: int float tuple str
# unordered: no indexing or slicing

s = {10,20,30,30, 90}
print(s) # {10, 20, 30}

s.add(50)
print(s)

s2 = {10,30,30, 20, 40, 50, 60, 60}

s3 = s.union(s2) # all unique elements 
print(s3)

s4 = s.intersection(s2)
print(s4)

s5 = s.difference(s2) # all elements in s that is not in s2
print(s5)

s6 = s.symmetric_difference(s2) # not common elements of both sets
print(s6)


# Update
s.update(s2) # performs union of s and s2 and saves it to s

s.intersection_update(s2) # perfroms intersection, common elements of s and s2 saved to s

s.difference_update(s2)

s.symmetric_difference_update(s2)

print(s2.issubset(s)) # if all elements of s2 is present in s we get true

s.issuperset(s2)


# list to set
l = [1,2,3,3,4,5]

l2 = [1, 3, 5, 7,]

s= set(l)
print(s)

s2 = set(l2)

s3 = s.union(s2) 

l3 = list(s3)
l3.sort() # get unique elements and sort them from two lists
print(l3)

l3 = sorted(s3)
print(l3) # sorted set and add it to list


# pop remove discard clear del
r = s.pop() # pick one element from set and remove it, return the element

s.remove(5) # removes 5 from the set, no return

s.discard(3) # no error thrown in element does not exist unlike remove

#s.clear() empty set





# MATH and RANDOM

l = [1,2,3,4,5]

print(sum(l)) # sum of all elements in the list

print(max(l)) # find the max element
min(l)

num = 23.2323

print(round(num,2)) # round to two decimals

# print(dir(__builtins__)) help(__builtins__)


# math
import math

# sum function might have rounding issues

l = [0.1] * 10
print(sum(l)) # returns 0.9999999999999999 instead of 1

print(math.fsum(l)) # return 1.0


num1 = 15.5559
print(math.floor(num1), math.ceil(num1))

print(math.sqrt(12))
print(math.factorial(3))

print(math.modf(num1)) # seperates the decimal and the integer part

d, i = math.modf(num1) # assign to two different values

print(math.pow(10,2))

print(math.log(100,10)) # log 10 base of 100

print(math.log10(100)) # any other log base available

print(math.sin(0)) # takes input in radians

print(math.sin(math.radians(30))) # sin of 30 degree

# cos tan

# help(math)
# print(dir(math))





# random numbers
import random


print(random.random()) # random number form 0 to 1

l = [1,2,3,4,5,6]

print(random.choice(l)) # from the list pick a random number

print(random.randint(10,100)) # random int from 10 to 100
print(random.randrange(10,100)) # exclusive at the end, 100 not included

print(random.uniform(10,20)) # floating point random number



