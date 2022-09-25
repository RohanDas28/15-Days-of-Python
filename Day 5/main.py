#Functions
'''
Functions: A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

'''
# def function_name(parameters):
#     statement(s)
#     return value

def my_function():
    print("Hello from a function")

my_function()

# Function Arguments
'''
There are four types of arguments in Python: Required, Keyword, Default and Variable-length.
'''
# Required Arguments
'''
Required arguments are the arguments passed to a function in correct positional order. Here, the number of arguments in the function call should match exactly with the function definition.
'''
# def function_name(arg1, arg2, ...):
#     statement(s)
#     return value

def printme(str):
    print(str)
    return

printme("I'm first call to user defined function!")
printme("Again second call to the same function")

# Keyword Arguments
'''
Keyword arguments are related to the function calls. When you use keyword arguments in a function call, the caller identifies the arguments by the parameter name.
'''
# def function_name(arg1, arg2, ...):
#     statement(s)
#     return value

def printinfo(name, age):
    print("Name: ", name)
    print("Age ", age)
    return
    
printinfo(age=18, name="Rohan")


# Default Arguments
'''
A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument.
'''
# def function_name(arg1, arg2, ...):
#     statement(s)
#     return value

def printinfo(name, age=18):
    print("Name: ", name)
    print("Age ", age)
    return

printinfo(name="Rohan")

# Variable-length Arguments
'''
You may need to process a function for more arguments than you specified while defining the function. These arguments are called variable-length arguments and are not named in the function definition, unlike required and default arguments.
'''
# def function_name(arg1, arg2, ...):
#     statement(s)
#     return value

def printinfo(arg1, *vartuple):
    print("Output is: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return

printinfo(10)
printinfo(70, 60, 50)

# Anonymous Functions
'''
Anonymous functions are also called lambda functions because they are not declared with the standard def keyword. You can use the lambda keyword to create small anonymous functions.
'''
# lambda arguments: expression

sum = lambda arg1, arg2: arg1 + arg2

print("Value of total : ", sum(10, 20))
print("Value of total : ", sum(20, 20))

# Return Statement
'''
The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.
'''
# def function_name(arg1, arg2, ...):
#     statement(s)
#     return value

def sum(arg1, arg2):
    total = arg1 + arg2
    print("Inside the function : ", total)
    return total

total = sum(10, 20)
print("Outside the function : ", total)

# Scope of Variables
'''
All variables in a program may not be accessible at all locations in that program. This depends on where you have declared a variable.
'''
# Global vs. Local variables
'''
Variables that are defined inside a function body have a local scope, and those defined outside have a global scope.
'''
# Global variables
total = 0 # This is global variable.

def sum(arg1, arg2):
    total = arg1 + arg2 # Here total is local variable.
    print("Inside the function local total : ", total)
    return total

sum(10, 20)
print("Outside the function global total : ", total)

# The global Statement
'''
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function. To create a global variable inside a function, you can use the global keyword.
'''
# Global variables
total = 0 # This is global variable.

def sum(arg1, arg2):
    global total
    total = arg1 + arg2 # Here total is global variable.
    print("Inside the function global total : ", total)
    return total

sum(10, 20)
print("Outside the function global total : ", total)

#Exception Handling
'''
Exception handling is a process of handling the run-time errors so that the normal flow of the program can be maintained.
'''
# try:
#     You do your operations here;
#     ......................
# except ExceptionI:
#     If there is ExceptionI, then execute this block.
# except ExceptionII:
#     If there is ExceptionII, then execute this block.
#     ......................
# else:
#     If there is no exception then execute this block.

try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()

# try...finally
'''
The finally block is a place to put any code that must execute, whether the try-block raised an exception or not.
'''
# try:
#     You do your operations here;
#     ......................
#     Due to any exception, this may be skipped.
# finally:
#     This would always be executed.

try:
    fh = open("testfile", "w")
    try:
        fh.write("This is my test file for exception handling!!")
    finally:
        print("Going to close the file")
        fh.close()
except IOError:
    print("Error: can\'t find file or read data")


