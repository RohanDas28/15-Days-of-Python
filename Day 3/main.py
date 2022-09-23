#Indexing
a = "Hello, World!"
print(a[1])

#Slicing
b = "Hello, World!"
print(b[2:5])

#Comprehensions
c = [x for x in range(10)]
print(c)

#File I/O


with open(r"C:\Users\rohan\Desktop\15-Days-of-Python\Day 3\demofile.txt", "a+") as f:
    f.write("Woops! I have deleted the content!")
    print(f.read())

'''
"r"   Opens a file for reading only.
"r+"  Opens a file for both reading and writing.
"rb"  Opens a file for reading only in binary format.
"rb+" Opens a file for both reading and writing in binary format.
"w"   Opens a file for writing only.
"a"   Open for writing. The file is created if it does not exist.
"a+"  Open for reading and writing.  The file is created if it does not exist.
'''


#Working with Binary
with open(r"C:\Users\rohan\Desktop\15-Days-of-Python\Day 3\demofile.txt", "rb+") as f:
    print(f.read())
    f.write(b"Hello, World!")
