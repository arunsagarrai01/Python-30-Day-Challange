# Output

print("Hello, World!")

# Printing Variables
name = "Arun"
print(name)

# Printing multiple items
age = 21
print("Age:", age)


# Input in Python

myName = input("Enter your name: ")
print("Hello,", myName)

# Input with type conversion
# Integer input
age = int(input("Enter your age: "))
print("Your age is:", age)

# Float input
price = float(input("Enter price: "))
print("Price is:", price)

# Taking multiple inputs
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
print("Sum", a + b)

# Method 2: in a single line
c, d = map(int, input("Enter two numbers: ").split())
print("sum:", c + d)


# Formatting Output
name = "Arun"
age = 21
print("Name:", name, "Age:", age)

# Using f-strings
print(f"Name: {name}, Age: {age}")

# Simple Example Program
name = input("Enter your name: ")
marks = int(input("Enter your marks: "))

print(f"Hello {name}, you scored {marks} marks.")












