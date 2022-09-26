#Regex 
'''
Regex is a sequence of characters that forms a search pattern.
When you search for data in a text, you can use this search pattern to describe what you are searching for.
A RegEx can be a single character or a more complicated pattern.
RegEx can be used to check if a string contains the specified search pattern.
'''
import re
# Check if the string starts with 'The' and ends with 'Spain':
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if (x):
    print("YES! We have a match!")
else:
    print("No match")
# Find all lower case characters alphabetically between "a" and "m":
txt = "That will be 59 dollars"
x = re.findall("[a-m]", txt)
print(x)
# Find all digit characters:
txt = "That will be 59 dollars"
x = re.findall("\d", txt)
print(x)
# Find all words that starts with 'ai':
txt = "The rain in Spain"
x = re.findall(r"\b(ai)\w+", txt)
print(x)
# Replace every white-space character with the number 9:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
# Split the string at every white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
# Split the string only at the first occurrence:
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
# Match if the string contains "ai" followed by 0 or more "x" characters:
txt = "The rain in Spain"
x = re.findall("aix*", txt)
print(x)
# Match if the string contains "ai" followed by 1 or more "x" characters:
txt = "The rain in Spain"
x = re.findall("aix+", txt)
print(x)
# Match if the string contains "a" followed by exactly two "l" characters:
txt = "The rain in Spain"
x = re.findall("al{2}", txt)
print(x)
# Match if the string contains either "falls" or "stays":
txt = "The rain in Spain"
x = re.findall("falls|stays", txt)
print(x)
# Match if the string contains any character from (a, r, or n):
txt = "The rain in Spain"
x = re.findall("[arn]", txt)
print(x)
# Match if the string contains any character EXCEPT (a, r, or n):
txt = "The rain in Spain"
x = re.findall("[^arn]", txt)
print(x)
# Match if the string has any a, r, or n characters:
txt = "The rain in Spain"
x = re.findall("[a-n]", txt)
print(x)
# Match if the string has any 2-digit numbers, from 00 to 59:
txt = "8 times before 11:45 AM"
x = re.findall("[0-5][0-9]", txt)
print(x)
# Match if the string has any characters from a to z lower case, and A to Z upper case:
txt = "8 times before 11:45 AM"
x = re.findall("[a-zA-Z]", txt)
print(x)
# Match if the string has any + characters:
txt = "8 times before 11:45 AM"
x = re.findall("[+]", txt)
print(x)
# Match if the string has any + or - characters:
txt = "8 times before 11:45 AM"
x = re.findall("[-+]", txt)
print(x)


