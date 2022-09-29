#Oops Basics in Python


class Employee:
    increment=1.5 
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary


    def increase(self):
        self.salary = int(self.salary * Employee.increment)


Rohan = Employee('Rohan', 'Das', 50000)
Harry = Employee('Harry', 'Bhai', 60000)


print(Rohan.fname, Harry.fname)
print(Rohan.salary, Harry.salary)
Rohan.increase()
Harry.increase()
print(Rohan.fname, Harry.fname)
print(Rohan.salary, Harry.salary)


