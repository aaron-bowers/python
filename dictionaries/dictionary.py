# DICTIONARIES

'''
  - key:value  pairs  (much like objects from JS)
  - ordered: defined order, will not change (prior to Python 3.6, they were not ordered)
  - changeable: change/add/remove
  - NO DUPLICATES   (much like objects from JS)
'''

thisDict = {
  "brand":"Ford",
  "model":"Mustang",
  "year":1964,
}
print(thisDict)
print(thisDict["brand"])

# NO DUPLICATES
thisDict = {
  "brand":"Ford",
  "model":"Mustang",
  "year":1964,
  "year":1964,
}
print(thisDict)

# Get it's LENGTH; len()
print(len(thisDict))

# Return data type
print(type(thisDict))