# FUNCTIONS

'''
  - block of code which only runs when called
  - pass data, known as parameters, into the function
  - **by default, must be invoked with the correct number of args
    (if 2 params defined, must called with 2 args)**
  - returns data as a result
'''

#   def   keyword - defines a function
def my_function():
  print("Hello from my_function")

# invoke the function by using the function name with parenthesis after
my_function()

# PARAMETER (PARAM) - the variable listed inside the parens in the function definition
# ARGUMENT (ARG) - the value that is sent to the function when it is called

# 1 PARAM defined, fname
def my_function(fname):
  print(fname + " Refsnes")

# 1 ARG entered as input
my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Invoking with more or less args than the num of params defined, an error is thrown
def my_function(fname, lname):
  print(fname + " " + lname)

# my_function("Emil")
'''   ERROR IN TERMINAL ⬇️
    Traceback (most recent call last):
    File "/Users/aaronbowers/Desktop/Python/functions.py", line 34, in <module>
      my_function("Emil")
    TypeError: my_function() missing 1 required positional argument: 'lname'
'''

# ARBITRARY ARGs  --> *args <-- add a   *   before the param name in the func definition when it's not know how many arguments will be inputed. This is considered a tuple of args, allowing access using indexes
def my_function(*kids):
  print("The youngest child is " + kids[len(kids) - 1])

my_function('Emil', "Tobias", "Linus")

# KEYWORD ARGs  --> kwargs <-- send arguments with  -> key = value <-  syntax so that the order of the args does not matter
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# ARBITRARY KEYWORD ARGs  --> **kwargs <-- add two asterisks before the param name in the func definition if it is not known how many kwargs will be passed into the func
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# DEFAULT PARAM VALUE
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("Chile")
my_function()
my_function("Brazil")
my_function("USA")

# PASS A LIST AS AN ARG

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple","banana","cherry"]
my_function(fruits)

# RETURN a value with the RETURN statement
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# pass  keyword
def myfunction():
  pass