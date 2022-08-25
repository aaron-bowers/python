# LIST - stores multiple items in a single variable
"""
  1) defined ordered with indexes starting at 0
  2) changeable meaning add and remove items
  3) allow duplicate values
  4) allow differnt data types
"""

thislist = ['apple', 'banana', 'cherry']
print(thislist)
print(type(thislist)) # <class 'list'>

# LIST METHODS   -   https://www.w3schools.com/python/python_lists_methods.asp

# list() CONSTRUCTOR
thislist = list(('apple', 'banana', 'cherry'))
print(thislist)

# INDEXED - first element starts at 0
print(thislist[0])
# NEGATIVE INDEXES
print(thislist[-1]) # starts from end
# RANGE OF INDEXES
print(thislist[2:5]) # includes index 2 element but not index 5 element
print(thislist[:2]) # includes index 2 element but not index 5 element
print(thislist[1:]) # includes index 2 element but not index 5 element
print(thislist[-4:-1])

# CHECK IF EXISTS
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
else:
  print("No, 'apple' is not in the fruits list")

# CHANGE LIST ITEMS
thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist3[1] = 'blackcurrant'
print(thislist2)
print(thislist3)

# CHANGE RANGE OF ITEMS
thislist3[1:3] = ["honeydoo", "watermelon"]
print(thislist3)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"] # reduces size by 1
print(thislist) # ["apple", "watermelon"]