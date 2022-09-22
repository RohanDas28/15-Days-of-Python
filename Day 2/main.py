#Strings
print("Hello")
print("123")
#Integer
print(123 + 345)
#Float
print(3.14159)
#Boolean
True
False
#Type
print(type(123))
print(type(3.14159))
print(type(123 + 345))
print(type("Hello"))
print(type(True))
#Type Conversion
print(str(100))
print(int("100"))
print(float("100"))
print(str(100) + str(100))
print(int("100") + int("100"))
print(float("100") + float("100"))
#Maths
print(3 + 5)
print(7 - 4)
print(3 * 2)
print(6 / 3)
print(2 ** 3)
print(5 % 2)
print(5 // 2)
print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)
#BMI Calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)
#F-Strings
score = 0
height = 1.8
isWinning = True
#f-String
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

#String Manipulation
print("Hello"[4])
print("123" + "345")
print("Hello" + " " + "World")
print("Hello" * 5)
