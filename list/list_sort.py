# SORT LIST
thislist = ['orange', 'mango', 'kiwi', 'pineapple', 'banana']
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# DESCENDING
thislist = ['orange', 'mango', 'kiwi', 'pineapple', 'banana']
thislist2 = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
thislist2.sort(reverse = True)
print(thislist)
print(thislist2)

# CUSTOM SORT FUNCTION - use keyword argument   key = function
# EXAMPLE - sort the list with numbers closest to 50
def myFunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myFunc) # [50, 65, 23, 82, 100]
print(thislist)

# perform case-insensitive sorts
thislist = ['orange', 'Mango', 'kiwi', 'Pineapple', 'banana']
thislist.sort() # without making case-insensitive 👇
print(thislist) # ['Mango', 'Pineapple', 'banana', 'kiwi', 'orange']

thislist.sort(key = str.lower) # make case-insensitive 👇
print(thislist) # ['banana', 'kiwi', 'Mango', 'orange', 'Pineapple']

# REVERSE ORDER
thislist = ['orange', 'mango', 'kiwi', 'pineapple', 'banana']
thislist.reverse()
print(thislist)