# IF ELSE STATEMENTS

# IF STATEMENT
a = 33
b = 200
if b > a:
  print('b is greater than a')

# ELIF STATEMENT
a = 33
b = 33
if b > a:
  print('b is greater than a')
elif b == a:
  print('a and b are equal')

# ELSE STATEMENT
a = 200
b = 33
if b > a:
  print('b is greater than a')
elif a == b:
  print('a and b are equal')
else:
  print('a is greater than b')

# SHORTHAND IF
if a > b: print('a is greater than b')

# SHORTHAND IF ELSE
a = 2
b = 330
print("A") if a > b else print("B") # known as Ternary Operators OR Conditional Expressions

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# AND - keyword, logical operator
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# OR - keyword, logical operator
a = 200
b = 33
c = 500
if a > b or c > a:
  print("At least one of the conditions is True")

# NESTED IF
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# pass statement
a = 33
b = 200

if b > a:
  pass