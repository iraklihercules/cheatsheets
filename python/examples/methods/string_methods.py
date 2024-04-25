# String Methods
# https://www.w3schools.com/python/python_ref_string.asp


# capitalize()   - Converts the first character to upper case
# casefold()     - Converts string into lower case
# center()       - Returns a centered string
# count()        - Returns the number of times a specified value occurs in a string
# encode()       - Returns an encoded version of the string
# endswith()     - Returns true if the string ends with the specified value
# expandtabs()   - Sets the tab size of the string
# find()         - Searches the string for a specified value and returns the position of where it was found
# format()       - Formats specified values in a string
# format_map()   - Formats specified values in a string
# index()        - Searches the string for a specified value and returns the position of where it was found
# isalnum()      - Returns True if all characters in the string are alphanumeric
# isalpha()      - Returns True if all characters in the string are in the alphabet
# isascii()      - Returns True if all characters in the string are ascii characters
# isdecimal()    - Returns True if all characters in the string are decimals
# isdigit()      - Returns True if all characters in the string are digits
# isidentifier() - Returns True if the string is an identifier
# islower()      - Returns True if all characters in the string are lower case
# isnumeric()    - Returns True if all characters in the string are numeric
# isprintable()  - Returns True if all characters in the string are printable
# isspace()      - Returns True if all characters in the string are whitespaces
# istitle()      - Returns True if the string follows the rules of a title
# isupper()      - Returns True if all characters in the string are upper case
# join()         - Converts the elements of an iterable into a string
# ljust()        - Returns a left justified version of the string
# lower()        - Converts a string into lower case
# lstrip()       - Returns a left trim version of the string
# maketrans()    - Returns a translation table to be used in translations
# partition()    - Returns a tuple where the string is parted into three parts
# replace()      - Returns a string where a specified value is replaced with a specified value
# rfind()        - Searches the string for a specified value and returns the last position of where it was found
# rindex()       - Searches the string for a specified value and returns the last position of where it was found
# rjust()        - Returns a right justified version of the string
# rpartition()   - Returns a tuple where the string is parted into three parts
# rsplit()       - Splits the string at the specified separator, and returns a list
# rstrip()       - Returns a right trim version of the string
# split()        - Splits the string at the specified separator, and returns a list
# splitlines()   - Splits the string at line breaks and returns a list
# startswith()   - Returns true if the string starts with the specified value
# strip()        - Returns a trimmed version of the string
# swapcase()     - Swaps cases, lower case becomes upper case and vice versa
# title()        - Converts the first character of each word to upper case
# translate()    - Returns a translated string
# upper()        - Converts a string into upper case
# zfill()        - Fills the string with a specified number of 0 values at the beginning


print("\n\nString Methods\n\n")


# capitalize()  - Converts the first character to upper case
a = "hello, and welcome to my world.".capitalize()  # Hello, and welcome to my world.
b = "python is FUN!".capitalize()                   # Python is fun!
c = "36 is my age.".capitalize()                    # 36 is my age.
print("capitalize():", c)


# casefold() - Converts string into lower case
x = "Hello, And Welcome To My World!".casefold()
print("casefold():", x)  # hello, and welcome to my world!


# center() - Returns a centered string
txt = "banana"
a = txt.center(20, "-")  # "-------banana-------" (Using the symbol "-" as the padding character)
b = txt.center(20)       # "       banana       "
print("center():", a)


# count() - Returns the number of times a specified value occurs in a string
txt = "I love apples, apple are my favorite fruit"
a = txt.count("apple")          # 2 (the number of times the value "apple" appears in the string)
b = txt.count("apple", 10, 24)  # 1 (search from position 10 to 24)
print("count():", a, b)


# encode() - Returns an encoded version of the string
txt = "My name is Ståle"
a = txt.encode()                                              # b'My name is St\xc3\xa5le'
b = txt.encode(encoding="ascii", errors="backslashreplace")   # b'My name is St\\xe5le'
c = txt.encode(encoding="ascii", errors="ignore")             # b'My name is Stle'
d = txt.encode(encoding="ascii", errors="namereplace")        # b'My name is St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
e = txt.encode(encoding="ascii", errors="replace")            # b'My name is St?le'
f = txt.encode(encoding="ascii", errors="xmlcharrefreplace")  # b'My name is St&#229;le'
print("encode():", a)


# endswith() - Returns true if the string ends with the specified value
a = "Hello, welcome to my world.".endswith(".")                 # True
b = "Hello, welcome to my world.".endswith("my world.")         # True
c = "Hello, welcome to my world.".endswith("my world.", 5, 11)  # False
print("endswith():", a, b, c)


# expandtabs() - Sets the tab size of the string
x = "H\te\tl\tl\to".expandtabs(3)
print("expandtabs():", x)  # H  e  l  l  o


# find() - Searches the string for a specified value and returns the position of where it was found
a = "Hello, welcome welcome to my world.".find("welcome")  # 7 (first occurrence index)
b = "Hello, welcome to my world.".find("e")                # 1
c = "Hello, welcome to my world.".find("e", 5, 10)         # 8 (only search between position 5 and 10)
d = "Hello, welcome to my world.".find("q")                # -1 (Value not found)
print("find():", a)


# format() - Formats specified values in a string
a = "For only {price:.2f} dollars!".format(price=49)              # For only 49.00 dollars!
b = "My name is {fname}, I'm {age}".format(fname="John", age=36)  # My name is John, I'm 36
c = "My name is {0}, I'm {1}".format("John", 36)                  # My name is John, I'm 36
d = "My name is {}, I'm {}".format("John", 36)                    # My name is John, I'm 36
print("format():", a)


# format_map() - Formats specified values in a string
point = {'x': 4, 'y': -5}
x = '{x} {y}'.format_map(point)
print("format_map():", x)  # 4 -5


# index() - Searches the string for a specified value and returns the position of where it was found
a = "Hello, welcome to my world.".index("welcome")   # 7
b = "Hello, welcome to my world.".index("e")         # 1 (first occurrence)
c = "Hello, welcome to my world.".index("e", 5, 10)  # 8 (between 5 and 10 indices)
# d = "Hello, welcome to my world.".index("q")       # Exception (If the value is not found, the index() method will raise an exception)
print("index():", a, b, c)


# isalnum() - Returns True if all characters in the string are alphanumeric
a = "Company12".isalnum()    # True
b = "Company 12".isalnum()   # False
c = "Company\n12".isalnum()  # False
print("isalnum():", a, b, c)


# isalpha() - Returns True if all characters in the string are in the alphabet
a = "Company".isalpha()       # True
b = "Company Name".isalpha()  # False
c = "Company12".isalpha()     # False
d = "Company 12".isalpha()    # False
e = "123".isalpha()           # False
print("isalpha():", a, b, c, d, e)


# isascii() - Returns True if all characters in the string are ascii characters
a = "Company123".isascii()      # True
b = "Company\n123".isascii()    # True
c = "Company<br>123".isascii()  # True
d = "María".isascii()           # False
e = "\u0047".isascii()          # True
print("isascii():", a, b, c, d, e)


# isdecimal() - Returns True if all characters in the string are decimals
a = "1234".isdecimal()      # True
b = "12.34".isdecimal()     # False
c = "12,34".isdecimal()     # False
d = "1234abcd".isdecimal()  # False
e = "abcd".isdecimal()      # False
f = "\u0030".isdecimal()    # True (unicode for 0)
g = "\u0047".isdecimal()    # False (unicode for G)
print("isdecimal():", a, b, c, d, e, f, g)


# isdigit() - Returns True if all characters in the string are digits
a = "50800".isdigit()   # True
b = "abcd".isdigit()    # False
c = "\u0030".isdigit()  # True (unicode for 0)
d = "\u00B2".isdigit()  # True (unicode for ²)
print("isdigit():", a, b, c, d)


# isidentifier() - Returns True if the string is an identifier
# Rules for Naming an Identifier:
#  - Identifiers cannot be a keyword.
#  - Identifiers are case-sensitive.
#  - It can have a sequence of letters and digits. However, it must begin with a letter or _.
#    The first letter of an identifier cannot be a digit.
#  - It's a convention to start an identifier with a letter rather _.
#  - Whitespaces are not allowed.
#  - We cannot use special symbols like !, @, #, $, and so on.
a = 'Python'.isidentifier()    # True
b = 'Py thon'.isidentifier()   # False
c = '22Python'.isidentifier()  # False
d = ''.isidentifier()          # False
print("isidentifier():", a, b, c, d)


# islower() - Returns True if all characters in the string are lower case
a = "hello world!".islower()   # True
b = "Hello world!".islower()   # False
c = "hello 123".islower()      # False
d = "mynameisPeter".islower()  # False
print("islower():", a, b, c, d)


# isnumeric() - Returns True if all characters in the string are numeric
a = "565543".isnumeric()  # True
b = "\u0030".isnumeric()  # True (unicode for 0)
c = "10km2".isnumeric()   # False
d = "-1".isnumeric()      # False
e = "1.5".isnumeric()     # False
print("isnumeric():", a, b, c, d, e)


# isprintable() - Returns True if all characters in the string are printable
a = "Hello! Are you #1?".isprintable()   # True
b = "Hello!\nAre you #1?".isprintable()  # False
print("isprintable():", a, b)


# isspace() - Returns True if all characters in the string are whitespaces
a = "   ".isspace()      # True
b = "   s   ".isspace()  # False
print("isspace():", a, b)


# istitle() - Returns True if the string follows the rules of a title
a = "Hello, And Welcome To My World!".istitle()  # True
b = "HELLO, AND WELCOME TO MY WORLD".istitle()   # False
c = "hello, and Welcome To My World!".istitle()  # False
d = "Hello".istitle()                            # True
e = "22 Names".istitle()                         # True
f = "This Is %'!?".istitle()                     # True
print("istitle():", a, b, c, d, e, f)


# isupper() - Returns True if all characters in the string are upper case
a = "THIS IS NOW!".isupper()      # True
b = "Hello World!".isupper()      # False
c = "hello 123".isupper()         # False
d = "MY NAME IS PETER".isupper()  # True
print("isupper():", a, b, c, d)


# join() - Converts the elements of an iterable into a string
my_tuple = ("John", "Peter", "Vicky")
a = "#".join(my_tuple)    # John#Peter#Vicky
my_dict = {"name": "John", "country": "Norway"}
b = "TEST".join(my_dict)  # nameTESTcountry
print("join():", a, b)


# ljust() - Returns a left justified version of the string
a = "banana".ljust(20)       # banana               is my favorite fruit.
b = "banana".ljust(20, "_")  # banana______________ is my favorite fruit.
print("ljust():", a, "is my favorite fruit.")


# lower() - Converts a string into lower case
x = "Hello my FRIENDS".lower()  # hello my friends
print("lower():", x)


# lstrip() - Returns a left trim version of the string
a = "     banana     ".lstrip()
print("lstrip() A:", "of all fruits", a, "is my favorite")  # of all fruits banana      is my favorite
b = ",,,,,ssaaww.....banana".lstrip(",.asw")
print("lstrip() B:", b)   # banana


# maketrans() - Returns a translation mapping table to be used with the translate() method to replace specified characters.
# Create a mapping table, and use it in the translate() method to replace any "S" characters with a "P" character

my_table = str.maketrans("S", "P")
a = "Hello Sam!".translate(my_table)  # Hello Pam!
print("maketrans() A:", a)

# Use a mapping table to replace many characters:
my_table = str.maketrans("mSa", "eJo")
b = "Hi Sam!".translate(my_table)  # Hi Joe!
print("maketrans() B:", b)

# The third parameter in the mapping table describes characters that you want to remove from the string:
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
c = "Good night Sam!".translate(mytable)  # G i Joe!
print("maketrans() C:", c)

# The maketrans() method itself returns a dictionary describing each replacement, in unicode:
x = "mSa"
y = "eJo"
z = "odnght"
my_table = str.maketrans(x, y, z)  # {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print("maketrans() D:", my_table)


# partition() - Returns a tuple where the string is parted into three parts
txt = "I could eat bananas all day"
a = txt.partition("bananas")  # ('I could eat ', 'bananas', ' all day')
b = txt.partition("apples")   # ('I could eat bananas all day', '', '')
print("partition():", a)


# replace() - Returns a string where a specified value is replaced with a specified value
a = "I like bananas".replace("bananas", "apples")  # I like apples
b = "1 1 1 1".replace("1", "2")     # 2 2 2 2 (Replace all occurrence of the word "one")
c = "1 1 1 1".replace("1", "2", 2)  # 2 2 1 1 (Replace the two first occurrence of the word "one")
print("replace():", a)


# rfind() - Searches the string for a specified value and returns the last position of where it was found
a = "Mi casa, su casa.".rfind("casa")  # 12 (The last occurrence of the string "casa")
txt = "Hello, welcome to my world."
b = txt.rfind("e")                     # 13 (The last occurrence of the letter "e")
c = txt.rfind("e", 5, 10)              # 8 (The last occurrence of the letter "e" when you only search between position 5 and 10)
d = txt.rfind("q")                     # -1 (Value not found)
print("rfind():", a)


# rindex() - Searches the string for a specified value and returns the last position of where it was found
a = "Mi casa, su casa.".rindex("casa")  # 12 (The last occurrence of the string "casa")
txt = "Hello, welcome to my world."
b = txt.rindex("e")                     # 13 (The last occurrence of the letter "e")
c = txt.rindex("e", 5, 10)              # 8 (The last occurrence of the letter "e" when you only search between position 5 and 10)
# d = txt.rindex("q")                   # Exception (If the value is not found, the rindex() method will raise an exception)
print("rindex():", a)


# rjust() - Returns a right justified version of the string
txt = "banana"
a = txt.rjust(20)       # "              banana" (A 20 characters long, right justified version of the word "banana")
b = txt.rjust(20, "-")  # "--------------banana" (Using the symbol "-" as the padding character:)
print("rjust():", b)


# rpartition() - Returns a tuple where the string is parted into three parts
# Search for the last occurrence of the word "bananas", and return a tuple with three elements:
# 1 - everything before the "match",
# 2 - the "match",
# 3 - everything after the "match".
a = "one two two three".rpartition("two")  # ('one two ', 'two', ' three')
# If the specified value is not found, the rpartition() method returns a tuple containing:
# 1 - an empty string,
# 2 - an empty string,
# 3 - the whole string:
b = "Sample text".rpartition("apples")  # ('', '', 'Sample text')
print("rpartition():", a)


# rsplit() - Splits the string at the specified separator, and returns a list
txt = "apple, banana, cherry"
a = txt.rsplit(", ")     # ['apple', 'banana', 'cherry']
# Split the string into a list with maximum 2 items
# (setting the maxsplit parameter to 1, will return a list with 2 elements!)
b = txt.rsplit(", ", 1)  # ['apple, banana', 'cherry']
print("rsplit():", b)


# rstrip() - Returns a right trim version of the string
a = "     banana     ".rstrip()  # "      banana" (Remove any white spaces at the end of the string)
b = "banana,,,,,ssqqqww.....".rstrip(",.qsw")  # banana (Remove the trailing characters if they are commas, periods, s, q, or w)
print("rstrip():", a)


# split() - Splits the string at the specified separator, and returns a list
a = "welcome to the jungle".split()  # ['welcome', 'to', 'the', 'jungle'] (Split a string into a list where each word is a list item)
txt = "apple#banana#cherry#orange"
b = txt.split("#")  # ['apple', 'banana', 'cherry', 'orange'] (Use a hash character as a separator)
# setting the maxsplit parameter to 1, will return a list with 2 elements!
c = txt.split("#", 1)  # ['apple', 'banana#cherry#orange'] (Split the string into a list with max 2 items)
print("split():", a)


# splitlines() - Splits the string at line breaks and returns a list
txt = "Line one\nLine two"
a = txt.splitlines()      # ['Line one', 'Line two']
b = txt.splitlines(True)  # ['Line one\n', 'Line two'] (Split the string, but keep the line breaks)
print("splitlines():", a)


# startswith() - Returns true if the string starts with the specified value
txt = "Hello, welcome to my world."
a = txt.startswith("Hello")       # True
b = txt.startswith("wel", 7, 20)  # True (Check if position 7 to 20 starts with the characters "wel")
print("startswith():", a, b)


# strip() - Returns a trimmed version of the string
a = "     banana     ".strip()                       # banana (Remove spaces at the beginning and at the end of the string)
b = ",,,,,rrttgg.....banana....rrr".strip(",.grt")   # banana (Remove the leading and trailing characters)
c = ",,,,,rrttgg.....banana....rrr".strip(",.grta")  # banan
print("strip():", a)


# swapcase() - Swaps cases, lower case becomes upper case and vice versa
x = "Hello My Name Is PETER".swapcase()  # hELLO mY nAME iS peter
print("swapcase():", x)


# title() - Converts the first character of each word to upper case
a = "Welcome to my world".title()  # Welcome To My World
b = "Welcome to my 2nd world".title()  # Welcome To My 2Nd World
c = "hello b2b2b2 and 3g3g3g".title()  # Hello B2B2B2 And 3G3G3G
print("title():", a)


# translate() - Returns a translated string
# use a dictionary with ascii codes to replace 83 (S) with 80 (P):
txt = "Hello Sam!"
my_dict = {83:  80}
a = txt.translate(my_dict)   # Hello Pam!
my_table = str.maketrans("S", "P")
b = txt.translate(my_table)  # Hello Pam!
my_table = str.maketrans("mSa", "eJo")
c = txt.translate(my_table)  # Hello Joe! (Use a mapping table to replace many characters)
txt = "Good night Sam!"
my_table = str.maketrans("mSa", "eJo", "odnght")
d = txt.translate(my_table)  # G i Joe! (The third parameter in the mapping table describes characters that you want to remove from the string)
my_dict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
e = txt.translate(my_dict)   # G i Joe! (The same example as above, but using a dictionary instead of a mapping table)
print("translate():", a)


# upper() - Converts a string into upper case
x = "Hello my friends".upper()  # HELLO MY FRIENDS
print("upper():", x)


# zfill() - Fills the string with a specified number of 0 values at the beginning
a = "50".zfill(10)                     # 0000000050
b = "10.000".zfill(10)                 # 000010.000
c = "hello".zfill(10)                  # 00000hello
d = "welcome to the jungle".zfill(10)  # zfill(): welcome to the jungle
print("zfill():", a, b, c)
