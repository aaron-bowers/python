# UPDATE TUPLES

''' Tuples are immutable, but there is a workaround '''
''' Convert to a list, change the list, convert back to a tuple '''

x = ('apple', 'banana', 'cherry')
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# ADD TO A TUPLE
''' Convert to a list and perform list methods to add item(s). Then convert back to tuple with tuple() constructor '''
# REMOVE FROM TUPLE
''' Convert to a list and perform list methods to remove item(s). Then convert back to tuple with tuple() constructor '''