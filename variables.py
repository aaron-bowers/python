# variable are created when assigned a value
x = 5
y = "Hello, World!"

"""
CREATING VARIABLES
"""

# do not need to be declared with any particular type, and can change after being set
x = 4
print(x)
x = "Sally"
print(x)

# CASTING - specifying the data type of a variable
x = str(3)
y = int(3)
z = float(3)
print(x, type(x), y, type(y), z, type(z))

# single or double quotes is acceptable
x = "John"
y = 'John'

# variable names are case sensitive
a = 4
A = "Sally"

# GLOBAL VARIABLES - created outside a function and can be used within functions
x = 'awesome'


def myFunc():
    print("Python is " + x)


myFunc()

# LOCAL VARIALBES

x = 'awesome'


def myFunc():
    x = 'fantastic'
    print('Python local is ' + x)


myFunc()

print("Python global is " + x)

# Create a GLOBAL varabile INSIDE A FUNCTION using the GLOBAL keyword


def myFunc():
    global x
    x = 'fantastic'


myFunc()

print("Python is " + x)
