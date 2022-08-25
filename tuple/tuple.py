# TUPLES

'''
  - stores a collection of data
  - ordered
  - unchangeable - CANNOT change/add/remove after tuple is created
  - allow duplicate values
  - indexed starting at 0
  - written with round brackets
'''

thistuple = ('apple', 'banana', 'cherry')
print(thistuple)
print(len(thistuple))

# CREATE a tuple with only one item
thistuple = ('apple',)  # must have a comma after first item or won't recognize as a tuple
print(type(thistuple))

# tuple() constructor
thistuple = tuple(('apple', 'banana', 'cherry'))  # must have double round-brackets
print(thistuple)

''' Accessing tuples is just like lists '''