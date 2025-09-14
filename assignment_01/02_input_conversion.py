# Demonstrating type conversion: int(), float(), str()

# Without conversion (input is a string)
num_1 = input("Your first number: ")
num_2 = input("Your second number: ")
print("String concatenation:", num_1 + num_2)

# With int() conversion
num_1 = int(input("Enter an integer: "))
num_2 = int(input("Enter another integer: "))
print("Integer addition:", num_1 + num_2)

# With float() conversion
num_1 = float(input("Enter a decimal number: "))
num_2 = float(input("Enter another decimal number: "))
print("Float division:", num_1 / num_2)

# With str() conversion
age = 20
print("My age is " + str(age))
