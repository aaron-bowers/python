# ADD NEW ITEMS

# add() method
thisSet = {'apple', 'banana', 'cherry'}
thisSet.add('orange')
print(thisSet)

# add items from one set to another set using update()
thisSet = {'apple', 'banana', 'cherry'}
tropical = {'pineapple', 'mango', 'papaya'}
thisSet.update(tropical)
print(thisSet)

# add items from any iterable to a set
thisSet = {'apple', 'banana', 'cherry'}
myList = ['kiwi', 'orange']
thisSet.update(myList)
print(thisSet)