#Pickling
'''
Pickling is a way to convert a python object (list, dict, etc.) into a character stream. The idea is that this character stream contains all the information necessary to reconstruct the object in another python script.

The pickle module implements binary protocols for serializing and de-serializing a Python object structure. “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy.
The process of pickling (also known as serialization, flattening, marshalling, or object persistence) involves translating data structures or object state into a format that can be stored (for example, in a file or memory buffer, or transmitted across a network connection link) and reconstructed later in the same or another computer environment.
The byte stream created by pickling is generally specific to the Python implementation used, and may not be compatible between Python releases or between different Python implementations. Pickling is only guaranteed to work between releases of the same Python implementation.
The pickle module is not secure against erroneous or maliciously constructed data. Never unpickle data received from an untrusted or unauthenticated source.
The pickle module is not intended to be secure against erroneous or maliciously constructed data. Never unpickle data received from an untrusted or unauthenticated source.

Pickling a Python Object
Let’s see how to pickle a Python object. We will use the pickle.dump() function to pickle an object. The syntax of pickle.dump() is:

pickle.dump(obj, file, protocol=None, *, fix_imports=True, buffer_callback=None)
obj − This is the object to be pickled.
file − This is the file-like object to which the object is pickled.
protocol − This is the protocol used for pickling. The possible values are 0, 1, 2, 3. The default value is 3.
fix_imports − This is a Boolean value. If true, pickle will try to map the new Python 3 names to the old module names used in Python 2, so that the pickle data stream is readable with Python 2.
buffer_callback − This is a function that will be called to return a writable buffer when pickling large binary values. It should accept an integer and return a bytes object of the specified size.
'''
#Let’s see an example to pickle a Python object −
#Pickling a Python object
import pickle
#The name of the file where we will store the object
shoplistfile = 'shoplist.data'
#The list of things to buy
shoplist = ['apple', 'mango', 'carrot']
#Write to the file
f = open(shoplistfile, 'wb')
#Dump the object to a file
pickle.dump(shoplist, f)
f.close()
#Destroy the shoplist variable
del shoplist
#Read back from the storage
f = open(shoplistfile, 'rb')
#Load the object from the file
storedlist = pickle.load(f)
print(storedlist)

#Unpickling a Python Object
'''
The pickle.load() function is used to unpickle a Python object. The syntax of pickle.load() is:
pickle.load(file, *, fix_imports=True, encoding="ASCII", errors="strict", buffers=None)
file − This is the file-like object to which the object is unpickled.
fix_imports − This is a Boolean value. If true, pickle will try to map the new Python 3 names to the old module names used in Python 2, so that the pickle data stream is readable with Python 2.
encoding − This is the encoding used for data.
errors − This is the error handling scheme used for data.
buffers − This is an object that supports the buffer interface.
'''
#Let’s see an example to unpickle a Python object −
#Unpickling a Python object
import pickle
#The name of the file where we will store the object
shoplistfile = 'shoplist.data'
#Read back from the storage
f = open(shoplistfile, 'rb')
#Load the object from the file
storedlist = pickle.load(f)
print(storedlist)

#Pickling Class Instances
'''
The pickle module can also be used to pickle class instances. The pickle module does not pickle the class itself, but only the instance. The class must be defined in the same module as the one in which the unpickling is to take place. The class must also be defined before the unpickling takes place.
'''
#Let’s see an example to pickle a class instance −
#Pickling class instances
import pickle
class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
#The name of the file where we will store the object
bobfile = 'bob.data'
#The list of things to buy
bob = Person('Bob Smith', 42, 30000, 'software')
#Store the object in a file
f = open(bobfile, 'wb')
pickle.dump(bob, f)
f.close()
#Destroy the bob variable
del bob
# Read back from the storage
f = open(bobfile, 'rb')
# Load the object from the file
bob = pickle.load(f)
f.close()
print(bob.lastName())
print(bob.pay)
print(bob)
print(bob.name)
print(bob.age)
print(bob.job)
print(bob.giveRaise(0.10))
print(bob.pay)

#Unpickling Class Instances
'''
The pickle module can also be used to unpickle class instances. The pickle module does not unpickle the class itself, but only the instance. The class must be defined in the same module as the one in which the unpickling is to take place. The class must also be defined before the unpickling takes place.
'''
#Let’s see an example to unpickle a class instance −
#Unpickling class instances
import pickle
class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
#The name of the file where we will store the object
bobfile = 'bob.data'
# Read back from the storage
f = open(bobfile, 'rb')
# Load the object from the file
bob = pickle.load(f)
f.close()
print(bob.lastName())
print(bob.pay)
print(bob)
print(bob.name)
print(bob.age)
print(bob.job)
print(bob.giveRaise(0.10))
print(bob.pay)

#Pickling Class Instances with Inheritance
'''
The pickle module can also be used to pickle class instances with inheritance. The pickle module does not pickle the class itself, but only the instance. The class must be defined in the same module as the one in which the unpickling is to take place. The class must also be defined before the unpickling takes place.
'''
#Let’s see an example to pickle a class instance with inheritance −
#Pickling class instances with inheritance
import pickle
class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')
    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent + bonus)
#The name of the file where we will store the object
suefile = 'sue.data'
#The list of things to buy
sue = Manager('Sue Jones', 45, 40000)
#Store the object in a file
f = open(suefile, 'wb')
pickle.dump(sue, f)
f.close()
#Destroy the sue variable
del sue
# Read back from the storage
f = open(suefile, 'rb')
# Load the object from the file
sue = pickle.load(f)
f.close()
print(sue.lastName())
print(sue.pay)
print(sue)
print(sue.name)
print(sue.age)
print(sue.job)
print(sue.giveRaise(0.10))
print(sue.pay)

#Unpickling Class Instances with Inheritance
'''
The pickle module can also be used to unpickle class instances with inheritance. The pickle module does not unpickle the class itself, but only the instance. The class must be defined in the same module as the one in which the unpickling is to take place. The class must also be defined before the unpickling takes place.
'''
#Let’s see an example to unpickle a class instance with inheritance −
#Unpickling class instances with inheritance
import pickle
class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')
    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent + bonus)
#The name of the file where we will store the object
suefile = 'sue.data'
# Read back from the storage
f = open(suefile, 'rb')
# Load the object from the file
sue = pickle.load(f)
f.close()
print(sue.lastName())
print(sue.pay)
print(sue)
print(sue.name)
print(sue.age)
print(sue.job)
print(sue.giveRaise(0.10))
print(sue.pay)

#Pickling Class Instances with Inheritance and Overriding
'''
The pickle module can also be used to pickle class instances with inheritance and overriding. The pickle module does not pickle the class itself, but only the instance. The class must be defined in the same module as the one in which the unpickling is to take place. The class must also be defined before the unpickling takes place.
'''
#Let’s see an example to pickle a class instance with inheritance and overriding −
#Pickling class instances with inheritance and overriding
import pickle
class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')
    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent + bonus)
class Department:
    def __init__(self, *args):
        self.members = list(args)
    def addMember(self, person):
        self.members.append(person)
    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)
#The name of the file where we will store the object
deptfile = 'dept.data'
#The list of things to buy
bob = Person('Bob Smith', 42, 30000, 'software')
sue = Person('Sue Jones', 45, 40000, 'hardware')
tom = Manager('Tom Doe', 50, 50000)
development = Department(bob, sue)
development.addMember(tom)
#Store the object in a file
f = open(deptfile, 'wb')
pickle.dump(development, f)
f.close()
#Destroy the development variable
del development
# Read back from the storage
f = open(deptfile, 'rb')
# Load the object from the file
development = pickle.load(f)
f.close()
development.giveRaises(0.10)
development.showAll()

#Unpickling Class Instances with Inheritance and Overriding
'''
The pickle module can also be used to unpickle class instances with inheritance and overriding. The pickle module does not unpickle the class itself, but only the instance. The class must be defined in the same module as the one in which the unpickling is to take place. The class must also be defined before the unpickling takes place.
'''
#Let’s see an example to unpickle a class instance with inheritance and overriding −
#Unpickling class instances with inheritance and overriding
import pickle
class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')
    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent + bonus)
class Department:
    def __init__(self, *args):
        self.members = list(args)
    def addMember(self, person):
        self.members.append(person)
    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)
#The name of the file where we will store the object
deptfile = 'dept.data'
# Read back from the storage
f = open(deptfile, 'rb')
# Load the object from the file
development = pickle.load(f)
f.close()
development.giveRaises(0.10)
development.showAll()

