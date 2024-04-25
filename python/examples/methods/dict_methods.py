# Dictionary Methods
# https://www.w3schools.com/python/python_ref_dictionary.asp


# clear() - Removes all the elements from the dictionary
# copy() - Returns a copy of the dictionary
# fromkeys() - Returns a dictionary with the specified keys and value
# get() - Returns the value of the specified key
# items() - Returns a list containing a tuple for each key value pair
# keys() - Returns a list containing the dictionary's keys
# pop() - Removes the element with the specified key
# popitem() - Removes the last inserted key-value pair
# setdefault() - Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update() - Updates the dictionary with the specified key-value pairs
# values() - Returns a list of all the values in the dictionary


print("\n\nDict Methods\n\n")


# clear() - Removes all the elements from the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.clear()
print("clear():", car, x)  # {} None

# copy() - Returns a copy of the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.copy()
x.clear()
print("copy() A:", car)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
z = car
z.clear()
print("copy() B:", car)  # {}

# fromkeys() - Returns a dictionary with the specified keys and value
x = ('key1', 'key2', 'key3')
value = 5
a = dict.fromkeys(x, value)
print("fromkeys() A:", a)  # {'key1': 5, 'key2': 5, 'key3': 5}
b = dict.fromkeys(x)  # {'key1': None, 'key2': None, 'key3': None}
print("fromkeys() B:", b)


# get() - Returns the value of the specified key
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
y = car.get("imaginary")
z = car.get("imaginary", "default_value")
print("get():", x, y, z)  # Mustang None default_value


# items() - Returns a list containing a tuple for each key value pair
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print("items() A:", x)  # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
# When an item in the dictionary changes value, the view object also gets updated:
car["year"] = 2018
print("items() B:", x)  # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2018)])


# keys() - Returns a list containing the dictionary's keys
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print("keys() A:", x)  # dict_keys(['brand', 'model', 'year'])
# When an item is added in the dictionary, the view object also gets updated:
car["color"] = "white"
print("keys() B:", x)  # dict_keys(['brand', 'model', 'year', 'color'])


# pop() - Removes the element with the specified key
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# The value of the removed item is the return value:
x = car.pop("model")
print("pop():", car, x)  # {'brand': 'Ford', 'year': 1964} Mustang


# popitem() - Removes the last inserted key-value pair
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# The removed item is the return value of the popitem() method
x = car.popitem()
print("popitem():", car, x)  # {'brand': 'Ford', 'model': 'Mustang'} ('year', 1964)


# setdefault() - Returns the value of the specified key.
# If the key does not exist: insert the key, with the specified value
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
z = car.setdefault("color", "Red")
print("setdefault():", car, x, z)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'Red'} Mustang Red


# update() - Updates the dictionary with the specified key-value pairs
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "White", "year": 2022})
print("update():", car)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 2022, 'color': 'White'}


# values() - Returns a list of all the values in the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print("values() A:", x)  # dict_values(['Ford', 'Mustang', 1964])
# When a values is changed in the dictionary, the view object also gets updated
car["year"] = 2018
print("values() B:", x)  # dict_values(['Ford', 'Mustang', 2018])
