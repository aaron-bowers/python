# LIST METHODS

# insert() ADDS an ITEM at a SPECIFIC INDEX of the list
thislist = ['apple', 'banana', 'cherry']
thislist.insert(2, 'watermelon')
print(thislist)

# append() ADDS an ITEM to the END of the list
thislist = ['apple', 'banana', 'cherry']
thislist.append('orange')
print(thislist)

# extend() ADDS items from another list to the list the extend method is used on
# can add any iterable object (tuples, sets, dictionaries, etc)
thislist = ['apple', 'banana', 'cherry']
tropical = ['mango', 'pineapple', 'papaya']
thislist.extend(tropical)
print(thislist)

# remove() REMOVES a specified item from the list
thislist = ['apple', 'banana', 'cherry']
thislist.remove('banana')
print(thislist)

# pop() REMOVES an element at a specific index
thislist = ['apple', 'banana', 'cherry']
thislist.pop(0) # removes item at index 0
print(thislist)

# del keyword does the same and can also delete an entire series
thislist = ['apple', 'banana', 'cherry']
del thislist[1]
print(thislist)
del thislist
# print(thislist)

# clear() method empties a list
thislist = ['apple', 'banana', 'cherry']
thislist.clear()
print(thislist)

# copy() method makes a copy of a list
thislist = ['apple', 'banana', 'cherry']
mylist = thislist.copy()
print(mylist)

'''  OR   '''

mylist = list(thislist)
print(mylist)

# count() - returns the number of elements with the specified value
fruits = ['apple', 'banana', 'cherry', 'cherry']
print(fruits.count('cherry'))
print(fruits.count('apple'))

# index() - returns the index of the first element with the specified value
print('first index where cherry is located =', fruits.index('cherry'))
print('first index where apple is located =', fruits.index('apple'))