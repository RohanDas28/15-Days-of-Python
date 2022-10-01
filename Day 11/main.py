#Inheritance is a way to form new classes using classes that have already been defined. The newly formed classes are called derived classes, the classes that we derive from are called base classes. Important benefits of inheritance are code reuse and reduction of complexity of a program. The derived classes (descendants) override or extend the functionality of base classes (ancestors).
#The syntax for a derived class definition looks like this:
#class DerivedClassName(BaseClassName):
#    <statement-1>
#    .
#    .
#    .
#    <statement-N>
#The name BaseClassName must be defined in a scope containing the derived class definition. Inheritance is a powerful feature in object-oriented programming. It allows us to define a class that inherits all the methods and properties from another class. Parent class is the class being inherited from, also called base class. Child class is the class that inherits from another class, also called derived class.
#In Python, a class can inherit from multiple parent classes. This is called multiple inheritance. For example:
#class DerivedClassName(Base1, Base2, Base3):
#    <statement-1>
#    .
#    .
#    .
#    <statement-N>
#A derived class can override any methods of its base class or classes. It can also extend the functionality of the base class. When a method is called by its name, the search for the method starts in the class where it was called. If the method is not found, the search continues into the parent class. This rule is recursively applied until the class is found. The method or attribute reference has no meaning outside the class definition. Hence, name conflicts can be easily avoided by using the proper naming convention. For example, an employee class may have a method called displayEmployeeDetails() and a manager class may have a method called displayManagerDetails(). Both of these classes inherit from a base class called employee. To avoid name conflicts, we can prefix the methods with the class name.
#The following example demonstrates the concept of inheritance. We have two classes, Person and Employee, where Employee is the derived class of Person. We use the pass keyword when we do not want to add any other properties or methods to the class.
#class Person:
#    pass
#class Employee(Person):
#    pass
#The pass keyword is used as a placeholder for future code. It is also used in empty control statement, function and class definitions.


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

class Dog(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("I am a dog")

    def bark(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("I am a cat")

    def meow(self):
        print("Meow!")

class Fish(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print("I am a fish")

    def swim(self):
        print("I am swimming")

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print("I am a bird")

    def fly(self):
        print("I am flying")

d = Dog("Tim", 5, "brown")
d.speak()
d.bark()
d.eat()

c = Cat("Bill", 3, "grey")
c.speak()
c.meow()
c.eat()

f = Fish("Bubbles", 1)
f.speak()
f.swim()
f.eat()

b = Bird("Tweety", 2)
b.speak()
b.fly()
b.eat()

