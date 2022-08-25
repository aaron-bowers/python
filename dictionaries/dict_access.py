# ACCESS DICTIONARIES

# bracket notation
thisDict = {
  "brand":"Ford",
  "model":"Mustang",
  "year":1964,
}
x = thisDict["model"]
print(x)

# get() method
y = thisDict.get("model")
print(y)

# keys() method - returns a list of all the keys
z = thisDict.keys()
print(z)

thisDict["color"] = 'white'
print(z)

# values() method - returns a list of all the values from a dict
a = thisDict.values()
print(a)

thisDict["year"] = 2020
print(a)

# items() method - return each item in a dict as a tuple
b = thisDict.items()
print(b)

# check if KEY exists using the   in   keyword
thisDict = {
  "brand":"Ford",
  "model":"Mustang",
  "year":1964,
}
if "model" in thisDict:
  print("Yes, 'model' is one of the keys in thisDict")
