# Conditional Processing


# If Statement
'''
if condition: #if condition is true then execute the code block below it.

elif condition: #elif is optional, if the first condition is false then check this condition

else: #else is optional, if all the conditions are false then execute the code block below it.
            
            '''
a = 10
b = 20
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")

# Match Statement
'''
match expression:
    case pattern1:
        statement(s)
    case pattern2:
        statement(s)
    case pattern3:
        statement(s)
    default:
        statement(s)
                    '''

match a:
    case 1:
        print("a is 1")
    case 2:
        print("a is 2")
    case 3:
        print("a is 3")
    case _:
        print("a is not 1, 2 or 3")

# Iterative Processing
'''
for variable in sequence:
    statement(s)
    '''
# For Loop
for x in range(10):
    print(x)

# While Loop
x = 0
while x < 10:
    print(x)
    x += 1

# Recursion
'''
Recursion is a process of defining something in terms of itself. In Python, this has the advantage of very clean and elegant code.
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
