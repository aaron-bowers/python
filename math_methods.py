# MATH CONCEPTS IN PYTHON

# IMPORT MATH MODULE - Make sure file name is not the same as math
# https://stackoverflow.com/questions/59762996/how-to-fix-attributeerror-partially-initialized-module
import math

# min()  - finds lowest value in iterable
x = min(5, 10, 25)
print(x)

# max()  - finds highest value in iterable
y = max(5, 10, 25)
print(y)

# abs()  - returns the absolute value of a number
x = abs(-7.25)
print(x)

# pow(x,y)  - returns the value of x->(base) to the power of y->(exponent)
x = pow(3,3)
print(x)


# METHODS FROM   MATH   MODULE

# math.sqrt() method - returns square root of a number
# x = math.sqrt(64)
# print(x)

# math.ceil() method - rounds upwards to nearest int and returns num
# math.floor() method - rounds downwards to nearest int and returns num
x = math.ceil(1.4)
y = math.floor(1.4)
print(x, y)

# math.pi
x = math.pi
print(x)