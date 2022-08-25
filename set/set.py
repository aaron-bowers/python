# SETS

'''
  - store multiple items in a single variable
  - unordered: uncertain which order they'll appear in
  - unchangeable: CAN'T CHANGE its items but CAN add and remove
  - unindexed
  - duplicates not allowed
  - can contain same/different types
'''

# SET
thisSet = {'apple', 'banana', 'cherry'}
print(thisSet)

# SET WITH DUPLICATES - view console
thisSet = {'apple', 'banana', 'cherry', 'cherry'}
print(thisSet)

# len() of a set
print(len(thisSet))

# type() of a set
print(type(thisSet))

# set() constructor - makes a set
thisSet = set(('apple', 'banana', 'cherry'))
print(thisSet)