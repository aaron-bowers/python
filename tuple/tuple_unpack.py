# UNPACK A TUPLE
fruits = ['apple', 'banana', 'cherry']

# UNPACK, or extract, VALUES INTO VARIABLES
(green, yellow, red) = fruits
print(green, yellow, red)

# using asterisk * - add an * to the var name and the values will be assigned to the variable as a list
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# if the * is added to another var name then the last, Python assigns values to the var until the number of values left matches the number of variables left
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)