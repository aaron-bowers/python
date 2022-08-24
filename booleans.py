# When comparing two values, the expression is evaluated and python returns the boolean answer

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

# IF STATEMENTS
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# bool() function
# any string is True, except empty strings
# any number is True, except 0
# any list, tuple, set, and dict are True, except empty ones
# what will result in False = (), [], {}, "", 0, None, False
print(bool("Hello"))
print(bool(15))

x = ""
y = 15

print("empty str", bool(x))
print(bool(y))
print(bool("abc"))
print(bool(123))
print("empty list", bool([]))
print(bool(["apple", "cherry", "banana"]))

# objects made from a class with a __len__ function that returns 0 or False will result in False return from bool()
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# FUNCTIONS THAT RETURN BOOLs
def myFunction():
  return True

print(myFunction())


def myFunction2():
  return True

if myFunction2():
  print("YES!")
else:
  print("NO!")

# isinstance() FUNCTION - determine if an object is a certian type
x = 200
print(isinstance(x, int))
print(isinstance(x, float))
print(isinstance(x, dict))
