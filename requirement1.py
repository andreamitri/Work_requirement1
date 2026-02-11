# Exercise 1: Greeting and Age Check

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"Hello {name}, you can enter!")
else:
    print(f"Sorry {name}, you are too young to enter.")
    