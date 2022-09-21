'''
DAY 01 Python Structures & Data Types
'''
#Data Types
#1. Numbers
#2. Strings
#3. Lists
#4. Tuples
#5. Dictionaries
#6. Sets
#7. Booleans
#8. None

#Numbers
#1. Integers
#2. Floats
#3. Complex Numbers

#Strings
#1. Single Quotes
#2. Double Quotes
#3. Triple Quotes



# Python Structures
#List
'''
List is a collection of items in a particulatr order. You can make a list that includes the letters of the alphabet, the digits from 0-9, or the names of all the people in your family. You can put anything you want into a list, and the items in your list don't have to be related in any particular way. Because a list usually contains more than one element, it is a good idea to make the name of your list plural, such as letters, digits, or names. In Python, square brackets ([]) indicate a list, and individual elements in the list are separated by commas.'''

a = ["Rohan", "1", "Haris", "2"]
print(a)

#Multi-Dimensional List
'''
A list within a list is called a multidimensional list. To access an element in a multidimensional list, use the names of the lists one at a time.'''

b = [["Rohan", "1"], ["Haris", "2"]]
print(b[0][1])

#List Slicing
'''
You can make any subset of a list that you want with a simple syntax. To make a slice, you specify the index of the first and last elements you want to work with. As with the range() function, Python stops one item before the second index you specify. To output the first three elements in a list, you would request indices 0 through 3, which would return elements 0, 1, and 2.'''
c = ["Rohan", "1", "Haris", "2"]
print(c[0:3])

#List Methods
'''
Python provides a number of useful methods that you can use with lists. For example, you can use the append() method to add an item to a list, regardless of where the item needs to go in the list. The append() method doesn't return a new list; it just modifies the original list.'''
d = ["Rohan", "1", "Haris", "2"]
d.append("3")
print(d)

#List Comprehension
'''
List comprehension is an elegant way to define and create lists based on existing lists. List comprehension is generally more compact and faster than normal functions and loops for creating list.'''
e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = [i for i in e if i % 2 == 0]
print(f)

#Tuples
'''
A tuple is a collection of items in a particular order. You can make a tuple that contains the letters of the alphabet, the digits from 0-9, or the names of all the people in your family. You can put anything you want into a tuple, and the items in your tuple don't have to be related in any particular way. Because a tuple usually contains more than one element, it is a good idea to make the name of your tuple plural, such as letters, digits, or names. In Python, parentheses () indicate tuples, and individual elements in the tuple are separated by commas.'''
g = ("Rohan", "1", "Haris", "2")
print(g)

#Tuple Slicing
'''
You can make any subset of a tuple that you want with a simple syntax. To make a slice, you specify the index of the first and last elements you want to work with. As with the range() function, Python stops one item before the second index you specify. To output the first three elements in a tuple, you would request indices 0 through 3, which would return elements 0, 1, and 2.'''
h = ("Rohan", "1", "Haris", "2")
print(h[0:3])

#Tuple Methods
'''
Python provides a number of useful methods that you can use with tuples. For example, you can use the count() method to find out how many times a value appears in a tuple.'''
i = ("Rohan", "1", "Haris", "2")
print(i.count("0"))

#Tuple Comprehension
'''
Tuple comprehension is an elegant way to define and create tuples based on existing tuples. Tuple comprehension is generally more compact and faster than normal functions and loops for creating tuple.'''
j = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
k = tuple(i for i in j if i % 2 == 0)
print(k)

#sets
'''
A set is a collection in which each item must be unique. Python provides a data type for sets. A set in Python is similar to the mathematical concept of a set. This is based on a collection of objects. However, the main difference between a set and a list is that a set cannot have multiple occurrences of the same object. A set is created by placing all the items (elements) inside curly braces {}, separated by comma, or by using the built-in function set(). It can have any number of items and they may be of different types (integer, float, tuple, string etc.). But a set cannot have a mutable element, like a list, set or dictionary, as its element.'''
l = {"Rohan", "1", "Haris", "2"}
print(l)

#Set Methods
'''
Python provides a number of useful methods that you can use with sets. For example, you can use the add() method to add an item to a set, regardless of where the item needs to go in the set. The add() method doesn't return a new set; it just modifies the original set.'''
m = {"Rohan", "1", "Haris", "2"}
m.add("3")
print(m)

#Set Comprehension
'''
Set comprehension is an elegant way to define and create sets based on existing sets. Set comprehension is generally more compact and faster than normal functions and loops for creating set.'''
n = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
o = {i for i in n if i % 2 == 0}
print(o)

#Dictionary
'''
A dictionary in Python is a collection of key-value pairs. Each key-value pair maps the key to its associated value. You can use a key to access the value associated with that key. A dictionary is a mutable data type that can store arbitrary objects. Dictionaries are sometimes found in other languages as "associative memories" or "associative arrays". Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys. Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. You can't use lists as keys, since lists can be modified in place using index assignments, slice assignments, or methods like append() and extend().'''
p = {"Rohan": "1", "Haris": "2"}
print(p)

#Dictionary Methods
'''
Python provides a number of useful methods that you can use with dictionaries. For example, you can use the get() method to get the value of a key in a dictionary, regardless of where the key needs to go in the dictionary. The get() method doesn't return a new dictionary; it just modifies the original dictionary.'''
q = {"Rohan": "1", "Haris": "2"}
print(q.get("Rohan"))

#Dictionary Comprehension
'''
Dictionary comprehension is an elegant way to define and create dictionaries based on existing dictionaries. Dictionary comprehension is generally more compact and faster than normal functions and loops for creating dictionary.'''
r = {"Rohan": "1", "Haris": "2"}
s = {k:v for k,v in r.items() if v == "1"}
print(s)

