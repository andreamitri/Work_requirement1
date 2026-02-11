# Exercise 1: Greeting and Age Check

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"Hello {name}, you can enter!")
else:
    print(f"Sorry {name}, you are too young to enter.")
    

# Exercise 2: Number List Processor

n = int(input("\nEnter a number: "))

numbers = []
for i in range(1, n + 1):
    numbers.append(i)

print(numbers)

if n > 5:
    print("The list is long.")
else:
    print("The list is short.")

    # Exercise 3: Sum of User Inputs

num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

num_list = [num1, num2, num3]
total = num1 + num2 + num3

print("Numbers:", num_list)
print("Total:", total)

if total % 2 == 0:
    print("Your sum is even!")
else:
    print("Your sum is odd!")