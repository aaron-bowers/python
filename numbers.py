# 3 types of numbers
"""
- int: whole number, positive or negative, without decimals, of unlimited length
- float: "floating point number", positive or negative, contains 1 or more decimals, can be scientific numbers with an "e" to indicate the power of 10
- complex: complex numbers, j is the imaginary part
"""

x = 1     # int
y = 2.8   # float
z = 1j    # complex

print(x, y, z)

# float using scientific a scientific number
a = 2e2
print (a)

# complex numbers written using "j" as imaginary part
x = 3 + 5j
y = 5j
z = -5j

# TYPE CONVERSION - convert from one type to another with type declaration
x = 1
y = 2.8
z = 1j
print(x, y, z)

a = float(x)
b = int(y)
c = complex(x)
print(a, b, c)
print(type(a), type(b), type(c))

# RANDOM NUMBER - import built-in module
import random
print(random.randrange(1, 100))