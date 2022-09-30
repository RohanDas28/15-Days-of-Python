class Employee:
    increment=1.5 
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary


    def increase(self):
        self.salary = int(self.salary * Employee.increment)
    
    @classmethod
    def change_increment(cls, amount):
        cls.increment = amount

    @classmethod
    def from_str(cls, emp_str):
        fname, lname, salary = emp_str.split('-')
        return cls(fname, lname, salary)

    @staticmethod
    def isopen(day):
        if day == 'sunday':
            return False
        else:
            return True

Rohan = Employee('Rohan', 'Das', 50000)
Harry = Employee('Harry', 'Bhai', 60000)
Lovish = Employee.from_str('Lovish-Garg-70000')
print(Employee.isopen('sunday'))

print(Lovish.fname, Lovish.lname)
print(Lovish.salary)



