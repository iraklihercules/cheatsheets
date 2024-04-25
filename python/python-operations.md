# Python Operators

### Numeric Operations
[Source](https://docs.python.org/3/library/stdtypes.html)

| Operation         | Result                                                                       | Examples                         |
|-------------------|------------------------------------------------------------------------------|----------------------------------|
| `x + y`           | sum of x and y                                                               |
| `x - y`           | difference of x and y                                                        |
| `x * y`           | product of x and y                                                           |
| `x / y`           | quotient of x and y                                                          | <pre>5 / 2 = 2.5</pre>           |
| `x // y`          | floored quotient of x and y                                                  | <pre>5 // 2 = 2</pre>            |
| `x % y`           | remainder of x / y                                                           | <pre>5 % 2 = 1</pre>             |
| `-x`              | x negated                                                                    |
| `+x`              | x unchanged                                                                  |
| `abs(x)`          | absolute value or magnitude of x                                             | <pre>abs(-5) = 5</pre>           |
| `int(x)`          | x converted to integer                                                       |
| `float(x)`        | x converted to floating point                                                |
| `divmod(x, y)`    | the pair (x // y, x % y)                                                     | <pre>divmod(5, 2) = (2, 1)</pre> |
| `pow(x, y)`       | x to the power y                                                             | <pre>pow(2, 3) = 8</pre>         |
| `x ** y`          | x to the power y                                                             | <pre>2 ** 3 = 8</pre>            |


### Sequence Operations

| Operation              | Result                                                                           | Examples                                                                                                  |
|------------------------|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| `x in s`               | True if an item of s is equal to x, else False                                   | <pre>"b" in "abc" = True<br>"x" in "abc" = False<br>2 in [1, 2, 3] = True<br>5 in [1, 2, 3] = False</pre> |
| `x not in s`           | False if an item of s is equal to x, else True                                   | <pre>1 not in [1, 2, 3] = False<br>5 not in [1, 2, 3] = True</pre>                                        |
| `s + t`                | the concatenation of s and t                                                     | <pre>"ab" + "cd" = "abcd"<br>[1, 2] + [3, 4] = [1, 2, 3, 4]</pre>                                         |
| `s * n` or `n * s`     | equivalent to adding s to itself n times                                         | <pre>"ab" * 3 = "ababab"<br>[1, 2] * 3 = [1, 2, 1, 2, 1, 2]</pre>                                         |
| `s[i]`                 | ith item of s, origin 0                                                          |
| `s[i:j]`               | slice of s from i to j                                                           | <pre>"12345"[1:4] = "234"<br>[1, 2, 3, 4, 5][1:4] = [2, 3, 4]</pre>                                       |
| `s[i:j:k]`             | slice of s from i to j with step k                                               | <pre>"0123456789"[0:6:2] = 024<br>"0123456789"[1:6:2] = 135<br>"0123456789"[4:6:2] = 4</pre>              |
| `len(s)`               | length of s                                                                      |
| `min(s)`               | smallest item of s                                                               |
| `max(s)`               | largest item of s                                                                |
| `s.index(x[, i[, j]])` | index of the first occurrence of x in s (at or after index i and before index j) | <pre>"xabcxdefx".index("x") = 0<br>"xabcxdefx".index("x", 2, 7) = 4</pre>                                 |
| `s.count(x)`           | total number of occurrences of x in s                                            | <pre>"xabcxdefx".count("x") ) 3</pre>                                                                     |


### Mutable Sequence Operations
| Operation                 | Result                                                                                   | Examples                                                                |
|---------------------------|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `s[i] = x`                | item i of s is replaced by x                                                             | <pre>s = [1, 2, 3]<br>s[1] = 5<br># [1, 5, 3]</pre>                     |
| `s[i:j] = t`              | slice of s from i to j is replaced by the contents of the iterable t                     | <pre>s = [1, 2, 3, 4, 5]<br>s[1:4] = [11, 12]<br># [1, 11, 12, 5]</pre> |
| `del s[i:j]`              | same as `s[i:j] = []`                                                                    | <pre>s = [1, 2, 3, 4, 5]<br>del s[1:4]<br># [1, 5]</pre>                |
| `s[i:j:k] = t`            | the elements of s[i:j:k] are replaced by those of t                                      |
| `del s[i:j:k]`            | removes the elements of s[i:j:k] from the list                                           |
| `s.append(x)`             | appends x to the end of the sequence (same as `s[len(s):len(s)] = [x]`)                  |
| `s.clear()`               | removes all items from s (same as `del s[:]`)                                            |
| `s.copy()`                | creates a shallow copy of s (same as `s[:]`)                                             |
| `s.extend(t)` or `s += t` | extends s with the contents of t (for the most part the same as `s[len(s):len(s)] = t``) | <pre>s = [1, 2, 3]<br>s.extend([4, 5])<br># [1, 2, 3, 4, 5]</pre>       |
| `s *= n`                  | updates s with its contents repeated n times                                             |
| `s.insert(i, x)`          | inserts x into s at the index given by i (same as `s[i:i] = [x]`)                        |
| `s.pop()` or `s.pop(i)`   | retrieves the item at i and also removes it from s                                       |
| `s.remove(x)`             | remove the first item from s where s[i] is equal to x                                    |
| `s.reverse()`             | reverses the items of s in place                                                         |

### String Methods
[Source](https://www.w3schools.com/python/python_ref_string.asp)

| Operation      | Result                                                           | Examples                                                                      |
|----------------|------------------------------------------------------------------|-------------------------------------------------------------------------------|
| `capitalize()` | Converts the first character to upper case                       |
| `casefold()`   | Converts string into lower case                                  |
| `center()`     | Returns a centered string                                        | <pre>txt = "banana"<br>x = txt.center(20)<br>print(x)<br>    banana    </pre> |
| `count()`      | Returns the number of times a specified value occurs in a string |
| `encode()`     | Returns an encoded version of the string                         | <pre>"xabcxdefx".count("x") ) 3</pre>                                         |



<pre><br></pre>
<pre><br></pre>
<pre><br></pre>
