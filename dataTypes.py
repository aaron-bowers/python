# BUILT IN DATA TYPES

# Text Type:   str
# Numeric Types:   int, float, complex
# Sequence Types:   list, tuple, range
# Mapping Type:   dict
# Set Types:   set, frozenset
# Boolean Type:   bool
# Binary Types:   bytes, bytearray, memoryview
# None Type:   NoneType

# Get the data type of any object by using type() func
from re import A


x = 5
xType = type(x)
print('data type =', type(x))
print('data type =', xType)

# Setting data type examples

a = str("Hello World")  # str
b = int(20)  # int
c = float(20.5)  # float
d = complex(1j)  # complex
e = list([
    'apple',
    'banana',
    'cherry'
])  # list
f = tuple(('apple', 'banana', 'cherry'))  # tuple
g = range(6)  # range
h = dict({
    'name': 'John',
    'age': 36
})  # dict
i = set({
    'apple',
    'banana',
    'cherry'
})  # set
j = frozenset({
    'apple',
    'banana',
    'cherry'
})  # frozenset
k = True  # bool     TO SET TYPE bool('anything')
l = b"Hello"  # bytes     TO SET TYPE bytes('anything')
m = bytearray(5)  # bytearray
n = memoryview(bytes(5))  # memoryview
o = None  # NoneType

print(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o)
