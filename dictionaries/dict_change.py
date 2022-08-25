# CHANGE VALUES

# refer to the dict's key and assign a new value
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2021
print(thisdict)

# update() method - update dict with items from given arg
# arg must be a dict or an iterable obj with key:value pairs
thisdict.update({"year":2022})
print(thisdict)