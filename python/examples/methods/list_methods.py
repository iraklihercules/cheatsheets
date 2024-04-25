# List Methods
# https://www.w3schools.com/python/python_ref_list.asp


# append()  - Adds an element at the end of the list
# clear()   - Removes all the elements from the list
# copy()    - Returns a copy of the list
# count()   - Returns the number of elements with the specified value
# extend()  - Add the elements of a list (or any iterable), to the end of the current list
# index()   - Returns the index of the first element with the specified value
# insert()  - Adds an element at the specified position
# pop()     - Returns the element at the specified position and then removes it
# remove()  - Removes the first item with the specified value
# reverse() - Reverses the order of the list
# sort()    - Sorts the list


print("\n\nList Methods\n\n")


# append() - Adds an element at the end of the list
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print("append():", fruits)  # ['apple', 'banana', 'cherry', 'orange']


# clear() - Removes all the elements from the list
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print("clear():", fruits)  # []


# copy() - Returns a copy of the list
fruits = ['apple', 'banana', 'cherry', 'orange']
# Case 1
x = fruits
x.clear()
print("copy() A:", fruits)  # []
# Case 2
z = fruits.copy()
z.clear()
print("copy() B:", fruits)  # ['apple', 'banana', 'cherry', 'orange']


# count() - Returns the number of elements with the specified value
fruits = ['apple', 'banana', 'cherry', 'cherry']
x = fruits.count("cherry")
print("count():", x)  # 2


# extend() - Add the elements of a list (or any iterable), to the end of the current list
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
x = fruits.extend(cars)
print("extend():", fruits, x)  # ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo'] None


# index() - Returns the index of the first element with the specified value
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print("index():", x)  # 2


# insert() - Adds an element at the specified position
fruits = ['apple', 'banana', 'cherry']
x = fruits.insert(1, "orange")
print("insert():", fruits, x)  # ['apple', 'orange', 'banana', 'cherry'] None


# pop() - Returns the element at the specified position and then removes it
fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(1)
print("pop():", fruits, x)  # ['apple', 'cherry'] banana


# remove() - Removes the first item with the specified value
fruits = ['apple', 'banana', 'cherry', 'banana']
x = fruits.remove("banana")
print("remove():", fruits, x)  # ['apple', 'cherry', 'banana'] None


# reverse() - Reverses the order of the list
fruits = ['apple', 'banana', 'cherry']
x = fruits.reverse()
print("reverse():", fruits, x)  # ['cherry', 'banana', 'apple'] None


# sort() - Sorts the list
cars = ['Ford', 'BMW', 'Volvo']
x = cars.sort()
print("sort() A:", cars, x)  # ['BMW', 'Ford', 'Volvo'] None
# Sort the list descending
cars.sort(reverse=True)
print("sort() B:", cars)  # ['Volvo', 'Ford', 'BMW']

# Sort the list by the length of the values
# A function that returns the length of the value:
def my_sort(e):
    return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=my_sort)
print("sort() C:", cars)  # ['VW', 'BMW', 'Ford', 'Mitsubishi']
# Sort the list by the length of the values and reversed:
cars.sort(reverse=True, key=my_sort)
print("sort() D:", cars)  # ['Mitsubishi', 'Ford', 'BMW', 'VW']

# Sort a list of dictionaries based on the "year" value of the dictionaries
# A function that returns the 'year' value:
def my_sort_2(e):
    return e['year']
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars.sort(key=my_sort_2)
print("sort() E:", cars)  # [{'car': 'Mitsubishi', 'year': 2000}, {'car': 'Ford', 'year': 2005}, {'car': 'VW', 'year': 2011}, {'car': 'BMW', 'year': 2019}]
