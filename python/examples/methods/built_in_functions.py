# Built In Functions
# https://www.w3schools.com/python/python_ref_functions.asp


# abs()          - Returns the absolute value of a number
# all()          - Returns True if all items in an iterable object are true
# any()          - Returns True if any item in an iterable object is true
# ascii()        - Returns a readable version of an object. Replaces none-ascii characters with escape character
# bin()          - Returns the binary version of a number
# bool()         - Returns the boolean value of the specified object
# bytearray()    - Returns an array of bytes
# bytes()        - Returns a bytes object
# callable()     - Returns True if the specified object is callable, otherwise False
# chr()          - Returns a character from the specified Unicode code.
# classmethod()  - Converts a method into a class method
# compile()      - Returns the specified source as an object, ready to be executed
# complex()      - Returns a complex number
# delattr()      - Deletes the specified attribute (property or method) from the specified object
# dict()         - Returns a dictionary (Array)
# dir()          - Returns a list of the specified object's properties and methods
# divmod()       - Returns the quotient and the remainder when argument1 is divided by argument2
# enumerate()    - Takes a collection (e.g. a tuple) and returns it as an enumerate object
# eval()         - Evaluates and executes an expression
# exec()         - Executes the specified code (or object)
# filter()       - Use a filter function to exclude items in an iterable object
# float()        - Returns a floating point number
# format()       - Formats a specified value
# frozenset()    - Returns a frozenset object
# getattr()      - Returns the value of the specified attribute (property or method)
# globals()      - Returns the current global symbol table as a dictionary
# hasattr()      - Returns True if the specified object has the specified attribute (property/method)
# hash()         - Returns the hash value of a specified object
# help()         - Executes the built-in help system
# hex()          - Converts a number into a hexadecimal value
# id()           - Returns the id of an object
# input()        - Allowing user input
# int()          - Returns an integer number
# isinstance()   - Returns True if a specified object is an instance of a specified object
# issubclass()   - Returns True if a specified class is a subclass of a specified object
# iter()         - Returns an iterator object
# len()          - Returns the length of an object
# list()         - Returns a list
# locals()       - Returns an updated dictionary of the current local symbol table
# map()          - Returns the specified iterator with the specified function applied to each item
# max()          - Returns the largest item in an iterable
# memoryview()   - Returns a memory view object
# min()          - Returns the smallest item in an iterable
# next()         - Returns the next item in an iterable
# object()       - Returns a new object
# oct()          - Converts a number into an octal
# open()         - Opens a file and returns a file object
# ord()          - Convert an integer representing the Unicode of the specified character
# pow()          - Returns the value of x to the power of y
# print()        - Prints to the standard output device
# property()     - Gets, sets, deletes a property
# range()        - Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
# repr()         - Returns a readable version of an object
# reversed()     - Returns a reversed iterator
# round()        - Rounds a numbers
# set()          - Returns a new set object
# setattr()      - Sets an attribute (property/method) of an object
# slice()        - Returns a slice object
# sorted()       - Returns a sorted list
# staticmethod() - Converts a method into a static method
# str()          - Returns a string object
# sum()          - Sums the items of an iterator
# super()        - Returns an object that represents the parent class
# tuple()        - Returns a tuple
# type()         - Returns the type of an object
# vars()         - Returns the __dict__ property of an object
# zip()          - Returns an iterator, from two or more iterators


print("\n\nBuilt In Functions\n\n")


# abs() - Returns the absolute value of a number
a = abs(-7.25)  # 7.25
b = abs(3+5j)   # 5.830951894845301 (The absolute value of a complex number)
print("abs():", a, b)


# all() - Returns True if all items in an iterable object are true
a = all([True, True, True])           # True
b = all([0, 1, 1])                    # False
c = all((0, True, False))             # False
d = all({0, 1, 0})                    # False
e = all({0 : "Apple", 1 : "Orange"})  # False
print("all():", a, b, c, d, e)


# any() - Returns True if any item in an iterable object is true
my_list = [False, True, False]
my_tuple = (0, 1, False)
my_set = {0, 1, 0}
my_dict = {0: "Apple", 1: "Orange"}
a = any(my_list)   # True
b = any(my_tuple)  # True
c = any(my_set)    # True
d = any(my_dict)   # True
print("any():", a, b, c, d)


# ascii() - Returns a readable version of an object. Replaces none-ascii characters with escape character
x = ascii("My name is Ståle")  # 'My name is St\xe5le' (Escape non-ascii characters)
print("ascii():", x)


# bin() - Returns the binary version of a number
x = bin(36)  # 0b100100
print("bin():", x)


# bool() - Returns the boolean value of the specified object
x = bool(1)  # True
print("bool():", x)


# bytearray() - Returns an array of bytes
x = bytearray(4)  # bytearray(b'\x00\x00\x00\x00')
print("bytearray():", x)


# bytes() - Returns a bytes object
x = bytes(4)  # bytes(): b'\x00\x00\x00\x00'
print("bytes():", x)


# callable() - Returns True if the specified object is callable, otherwise False
# Check if a function is callable:
def x_func():
    return 5
a = callable(x_func)  # True
b = callable(15)      # False
print("callable():", a, b)


# chr() - Returns a character from the specified Unicode code.
x = chr(97)  # a
print("chr():", x)


# compile() - Returns the specified source as an object, ready to be executed
a = compile('print(55)', 'test', 'eval')
b = compile('print(15)\nprint(88)', 'test', 'exec')
print("compile():")
exec(a)  # 55
exec(b)  # 15, 88


# complex() - Returns a complex number
a = complex(3, 5)    # (3+5j)
b = complex('3+5j')  # (3+5j)
print("complex():", a, b)


# delattr() - Deletes the specified attribute (property or method) from the specified object
# Delete the "age" property from the "person" object
class Person1:
    name = "John"
    age = 36
    country = "Norway"
delattr(Person1, 'age')
print("delattr():", dir(Person1))  # [..., 'country', 'name']


# dict() - Creates a dictionary (Array)
x = dict(name="John", age=36, country="Norway")
print("dict():", x)  # {'name': 'John', 'age': 36, 'country': 'Norway'}


# dir() - Returns a list of the specified object's properties and methods
class Person2:
    name = "John"
    age = 36
    country = "Norway"
# Display the content of an object
print("dir():", dir(Person2))  # [..., 'age', 'country', 'name']


# divmod() - Returns the quotient and the remainder when argument1 is divided by argument2
x = divmod(5, 2)  # (2, 1) = [(5 // 2), (5 % 2)]
print(x)


# enumerate() - Takes a collection (e.g. a tuple) and returns it as an enumerate object
x = ('apple', 'banana', 'cherry')
print("enumerate():")
for i, item in enumerate(x):
    print(i, item)


# eval() - Evaluates and executes an expression
print("eval():")
x = 'print(55)'
eval(x)  # 55


# exec() - Executes the specified code (or object)
print("exec():")
# Execute a block of code
x = 'name = "John"\nprint(name)'
exec(x)  # John


# filter() - Use a filter function to exclude items in an iterable object
def my_filter(x):
    return not x < 18
ages = [5, 12, 17, 18, 24, 32]
adults = filter(my_filter, ages)
print("filter():")
for x in adults:
    print(x)


# float() - Returns a floating point number
a = float(3)        # 3.0
b = float("3.500")  # 3.5
print("float():", a, b)


# format() - Formats a specified value
# Legal values:
# '<' - Left aligns the result (within the available space)
# '>' - Right aligns the result (within the available space)
# '^' - Center aligns the result (within the available space)
# '=' - Places the sign to the left most position
# '+' - Use a plus sign to indicate if the result is positive or negative
# '-' - Use a minus sign for negative values only
# ' ' - Use a leading space for positive numbers
# ',' - Use a comma as a thousand separator
# '_' - Use a underscore as a thousand separator
# 'b' - Binary format
# 'c' - Converts the value into the corresponding unicode character
# 'd' - Decimal format
# 'e' - Scientific format, with a lower case e
# 'E' - Scientific format, with an upper case E
# 'f' - Fix point number format
# 'F' - Fix point number format, upper case
# 'g' - General format
# 'G' - General format (using a upper case E for scientific notations)
# 'o' - Octal format
# 'x' - Hex format, lower case
# 'X' - Hex format, upper case
# 'n' - Number format
# '%' - Percentage format
a = format(0.5, '%')  # 50.000000% (Format the number 0.5 into a percentage value)
b = format(255, 'b')  # 11111111 (Format 255 into a binary value)
c = format(255, 'x')  # ff (Format 255 into a hexadecimal value)
print("format():", a, b, c)


# frozenset() - Returns a frozenset object
# Freeze the list, and make it unchangeable:
mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
# x[1] = "strawberry"  # TypeError: 'frozenset' object does not support item assignment


# getattr() - Returns the value of the specified attribute (property or method)
class Person3:
    name = "John"
    age = 36
    country = "Norway"
a = getattr(Person3, 'age')  # 36
# b = getattr(Person3, 'nothing')  # AttributeError: type object 'Person3' has no attribute 'undefined'
c = getattr(Person3, 'nothing', 'default_value')  # default_value
print("getattr():", a, c)


# globals() - Returns the current global symbol table as a dictionary
x = globals()
# print("globals() A:", x)  # globals variables dict (functions, classes, variables and etc).
print("globals() B:", x["__file__"])  # /app/methods/built_in.py (specific value)


# hasattr() - Returns True if the specified object has the specified attribute (property/method)
class Person4:
    name = "John"
    age = 36
    country = "Norway"
a = hasattr(Person4, 'age')      # True
b = hasattr(Person4, 'nothing')  # False
print("hasattr():", a, b)


# hash() - Returns the hash value of a specified object
a = hash(True)     # 1
b = hash(15)       # 15
c = hash(24.5)     # 1152921504606847000
d = hash("Hello")  # 8306397851098016629
print("hash():", a, b, c, d)


# help() - Executes the built-in help system
# help()
# help(print)


# hex() - Converts a number into a hexadecimal value
x = hex(255)  # 0xff
print("hex():", x)


# id() - Returns the id of an object
x = ('apple', 'banana', 'cherry')
y = id(x)  # 138928066325440
print("id()", y)


# input() - Allowing user input
# x = input('Enter your name:')
# print('Hello, ' + x)


# int() - Returns an integer number
a = int(3.5)   # 3
b = int("12")  # 12
print("int():", a, b)


# isinstance() - Returns True if a specified object is an instance of a specified object
a = isinstance(5, int)  # True
# Check if "Hello" is one of the types described in the type parameter:
b = isinstance("Hello", (float, int, str, list, dict, tuple))  # True
class Person5:
    name = "John"
p = Person5()
c = isinstance(p, Person5)  # True
print("isinstance():", a, b, c)


# issubclass() - Returns True if a specified class is a subclass of a specified object
class PersonBase:
    age = 36
class Person6(PersonBase):
    name = "John"
    age = PersonBase
x = issubclass(Person6, PersonBase)  # True
print("issubclass():", x)


# iter() - Returns an iterator object
x = iter(["apple", "banana", "cherry"])
print("iter():", next(x))
print("iter():", next(x))
print("iter():", next(x))


# len() - Returns the length of an object
a = len(["apple", "banana", "cherry"])  # 3
b = len("Hello")  # 5
print("len():", a, b)


# list() - Returns a list
x = list(('apple', 'banana', 'cherry'))  # ['apple', 'banana', 'cherry']
print("list():", x)


# locals() - Returns an updated dictionary of the current local symbol table
# x = locals()
# print(x)


# map() - Returns the specified iterator with the specified function applied to each item
# Calculate the length of each word in the tuple
def my_map(n):
    return len(n)
lengths = map(my_map, ('apple', 'banana', 'cherry'))  # 5 6 6
for x in lengths:
    print(x)


# max() - Returns the largest item in an iterable
a = max(5, 10)                    # 10
b = max("Mike", "John", "Vicky")  # Vicky
c = max(1, 5, 3, 9)               # 9
print("max():", a, b, c)


# memoryview() - Returns a memory view object
x = memoryview(b"Hello")
print("memoryview():", x)
# return the Unicode of the first character
print(x[0])
# return the Unicode of the second character
print(x[1])


# min() - Returns the smallest item in an iterable
a = min(5, 10)                    # 5
b = min("Mike", "John", "Vicky")  # John
c = min(1, 5, 3, 9)               # 1
print("min():", a, b, c)


# next() - Returns the next item in an iterable
my_list = iter(["apple", "banana", "cherry"])
print("next():", next(my_list))  # apple
print("next():", next(my_list))  # banana
print("next():", next(my_list))  # cherry
# Return a default value when the iterator has reached to its end
my_list_2 = iter(["apple", "banana", "cherry"])
print("next() 2:", next(my_list_2, "end"))  # cherry
print("next() 2:", next(my_list_2, "end"))  # cherry
print("next() 2:", next(my_list_2, "end"))  # cherry
print("next() 2:", next(my_list_2, "end"))  # cherry


# object() - Returns a new object
x = object()  # <object object at 0x74b6e5d18470>
print("object():", x)


# oct() - Converts a number into an octal
x = oct(12)  # 0o14
print("oct():", x)


# open() - Opens a file and returns a file object
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exist
# In addition you can specify if the file should be handled as binary or text mode
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# f = open("demofile.txt", "r")
# print(f.read())


# ord() - Convert an integer representing the Unicode of the specified character
x = ord("h")  # 104
print("ord():", x)


# pow() - Returns the value of x to the power of y
a = pow(2, 3)     # 8
# Return the value of 2 to the power of 3, modulus 5. Same as (2 * 2 * 2) % 5:
b = pow(2, 3, 5)  # 3
print("pow():", a, b)


# print() - Prints to the standard output device
# print("Hello World")


# range() - Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
# a = range(5)         # 0 1 2 3 4
# b = range(5, 10)     # 5 6 7 8 9 (Create a sequence of numbers from 5 to 10)
# c = range(4, 10, 2)  # 4 6 8 (Create a sequence of numbers from 4 to 10, but increment by 2 instead of 1)
for i in range(4, 10, 2):
    print(i)


# repr() - Returns a readable version of an object
print(repr("Hello"))  # 'Hello'
print(repr(pow))      # <built-in function pow>
print(pow)            # <built-in function pow>


# reversed() - Returns a reversed iterator
alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
for x in ralph:
    print("reversed():", x)


# round() - Rounds a numbers
a = round(5.76543, 2)  # 5.77
b = round(5.76543)     # 6
print("round():", a, b)


# set() - Returns a new set object
x = set(('apple', 'banana', 'cherry'))  # {'apple', 'cherry', 'banana'}
print("set():", x)


# setattr() - Sets an attribute (property/method) of an object
class Person7:
    name = "John"
    age = 36
    country = "Norway"
setattr(Person7, 'age', 40)
setattr(Person7, 'new', 15)
print("setattr():", dir(Person7))


# slice() - Returns a slice object
my_list = ("a", "b", "c", "d", "e", "f", "g", "h")
a = slice(3)
print("slice():", a)             # slice(None, 3, None) | slice(start, end, step)
print("slice() 1:", my_list[a])  # ('a', 'b', 'c')
b = slice(3, 5)
print("slice() 2:", my_list[b])  # ('d', 'e')
c = slice(0, 8, 3)
print("slice() 3:", my_list[c])  # ('a', 'd', 'g')


# sorted() - Returns a sorted list
my_tuple = ("b", "g", "a", "d", "f", "c", "h", "e")
a = sorted(my_tuple)  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print("sorted():", a)
b = sorted(my_tuple, reverse=True)  # ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
print("sorted():", b)
my_tuple = ("Jenifer", "Sally", "Jane")
c = sorted(my_tuple, key=len)  # ['Jane', 'Sally', 'Jenifer']
print("sorted():", c)
def my_sort_2(n):
  return abs(10-n)
my_tuple = (5, 3, 1, 11, 2, 12, 17)
d = sorted(my_tuple, key=my_sort_2) # [11, 12, 5, 3, 17, 2, 1]
print(d)


# str() - Returns a string object
x = str(3.5)  # 3.5
print("str():", x)


# sum() - Sums the items of an iterator
a = (1, 2, 3, 4, 5)
x = sum(a)  # 15
print("sum():", x)
# Start with the number 7, and add all the items in a tuple to this number
a = (1, 2, 3, 4, 5)
x = sum(a, 7)  # 22
print("sum():", x)


# tuple() - Returns a tuple
x = tuple(['apple', 'banana', 'cherry'])  # ('apple', 'banana', 'cherry')
print("tuple():", x)


# type() - Returns the type of an object
a = type(('apple', 'banana', 'cherry'))  # <class 'tuple'>
b = type("Hello World")                  # <class 'str'>
c = type(33)                             # <class 'int'>
print("type():", a, b, c)


# vars() - Returns the __dict__ property of an object
class Person8:
    name = "John"
    age = 36
    country = "norway"
x = vars(Person8)  # returns the __dict__ attribute of an object.
print("vars():", x)


# zip() - Returns an iterator, from two or more iterators
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
# If one tuple contains more items, these items are ignored
x = zip(a, b)
for i in x:
    print(i)
# ('John', 'Jenny')
# ('Charles', 'Christy')
# ('Mike', 'Monica')
