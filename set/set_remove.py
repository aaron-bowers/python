# REMOVE ITEMS FROM A SET

thisSet = {'apple', 'banana', 'cherry'}
thisSet.remove('banana') # if the item does not exist, remove() will raise an error
print(thisSet)


thisSet = {'apple', 'banana', 'cherry'}
thisSet.discard('banana') # if the item does not exist, discard() will NOT raise an error
print(thisSet)

# pop() - removes last item of set, but their unordered, so it's unknown what will be removed
''' return value will be the removed item '''
thisSet = {'apple', 'banana', 'cherry'}
x = thisSet.pop()
print(x)
print(thisSet)

# clear() empties the set
thisSet = {'apple', 'banana', 'cherry'}
thisSet.clear()
print(thisSet)

# del keyword deletes the set completely
thisSet = {'apple', 'banana', 'cherry'}
del thisSet
print(thisSet)