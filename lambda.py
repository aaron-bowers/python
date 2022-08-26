# LAMBDA - small anonymous function
'''
  - takes any num of args, but can only have one expression
  - SYNTAX  -->  lambda arguments : expression
'''

# Add 10 to arg a, and return the result
x = lambda a : a + 10
print(x(5))

# take any num of arguments
x = lambda a, b : a * b
print(x(5,6))

# return a lambda function from within another function
def myfunc(n):
  return lambda a : a * n  # function returns a lambda

mydoubler = myfunc(2)
print(mydoubler(5))
mytrippler = myfunc(3)
print(mytrippler(5))
