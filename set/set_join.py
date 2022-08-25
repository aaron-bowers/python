# SET METHODS can be found @ https://www.w3schools.com/python/python_sets_methods.asp

# JOIN SETS

# union() returns a new set with all items from both sets
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# update() inserts items from one set to another
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# intersection_update() will the set where the method is used
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
x.intersection_update(y)  # {'apple'}
print(x)

# intersection() will return a new set that only contains items from both sets
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.intersection(y)
print(z)

# symmetric_difference_update() is the opposite of intersection_update()
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
x.symmetric_difference_update(y)
print(x)

# symmetric_difference() is the oppposite of intersection()
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.symmetric_difference(y)
print(z)