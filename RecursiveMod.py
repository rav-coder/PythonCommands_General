"""
Docstring: This module contains binary search implementation.

"""

# Binary Search: Sorted List

def binary_search(l,key):
	"""
	Binary Search : input a list and key
	return True if key exists else return false

	"""
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

# print(__name__) # saves the name of the module: prints main

if(__name__) == '__main__': # move the executing statements so that RecursiveMod import does not execute these lines
	l = [1,2,3,4,5,6,7]

	key = 4

	result = binary_search(l,key)
	print(result)