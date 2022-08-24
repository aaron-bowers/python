# Additional String Methods found @ https://www.w3schools.com/python/python_strings_methods.asp

#  STRINGS are surronded by either single or double quotation marks

print("Hello", " AND ", 'Hello', " ARE THE SAME.")

# MULTILINE STRINGS

a = """1) Hey there, I would just really like to get
to know you better. I bet I would be a great fit
for your organization considering I have such great
communication skills and am diligent and hardworking
in my work."""
print(a)

b = '''2) Hey there, I would just really like to get
to know you better. I bet I would be a great fit
for your organization considering I have such great
communication skills and am diligent and hardworking
in my work.'''
print(b)

# Strings are arrays of bytes representing unicode characters (except for a str of length 1. its just a string)
a = "Hello, World!"
print("H = " + a[0], "W = " + a[7])


# LOOPING through a string
for x in 'banana':
  print(x)

# STRING LENGTH
b = "Aaron"
print(len(b))

# use the IN keyword to find specific words/characters in strings
txt = "the best things in life are free"
c = "free"
d = "life"
print("{} is in txt:".format(c), c in txt)
print("{} is in txt:".format(d), d in txt)
print("{} is in txt:".format(b), b in txt)

# use the IN keyword with IF conditional statements
txt = "The best things in life are free!"
arr = list([c, d, b])
for i in arr:
  if i in txt:
    print("Yes, {} is present in txt".format(i))
  else: print("No, {} is not present in txt".format(i))

# use NOT IN keywords to check if the string is not present in txt
print("{} is not in txt:".format(b), b not in txt)

# SLICING
r = "Hello, World!"
print(r[2:5])
print(r[:5])
print(r[5:])
print(r[:-5])
print(r[-5:])

# UPPER/LOWER methods
s = "hello, world"
print(s.upper())
print(s.lower())

# STRIP method - removes whitespace
t = " Hello, World "
print(t.strip())

# REPLACE method - replaces a string with another string
u = "Hello, World"
print(u.replace("H", "J"))

# SPLIT method
a = "Hello, World"
print(a.split(","))

# CONCATENATE methods
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# FORMAT method - takes the passed arguments, formats them, and places them in the string where the placeholders {} are
age = 36
txt = "My name is Aaron, and I am {}"
print(txt.format(age))

# can use index numbers to be sure the right arguments are placed in the correct placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# ESCAPE character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# \  --> single quote
# \\ --> backslash
# \n --> new line
# \r --> carriage return
# \t --> tab
# \b --> backspace
# \f --> form feed
# \ooo --> octal value
# \xhh --> hex value