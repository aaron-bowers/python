# LIST COMPREHENSION
'''
  - shorthand for loop that will print all items in a list
  - shorter syntax to create a new list based on the values of an existing list
'''
### OLD WAY
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

### LIST COMPREHENSION WAY
### newlist = [expression  for  item  in  iterable  if  condition  ==  True]
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = [x for x in fruits if "a" in x]
print(newlist)

''' condition (which is optional) is like a filter that only accepts the items that valuate to True '''
# EXAMPLE - only accept items that are not apple
newlist = [x for x in fruits if x != "apple"]
print(newlist)

''' iterable can be any iterable object '''
# EXAMPLE - use range() to create an iterable
newlist = [x for x in range(10)]
print(newlist)

''' expression is the current item in the iteration, but also the outcome, and can be manipulated before it ends up in the new list '''
# EXAMPLE - set the values in the new list to upper case
newlist = [x.capitalize() for x in fruits]
newlist2 = [x.upper() for x in fruits]
print(newlist)
print(newlist2)

''' expression can also contain conditions as a way to manipulate the outcome '''
# EXAMPLE - return "orange" instead of "banana"
newlist = [x if x != 'banana' else 'orange' for x in fruits]
print(newlist)