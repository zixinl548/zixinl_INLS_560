# input() is always captured as string so you have to "cast" it
'''
num_1 = (input("Your first number: "))
num_2 = (input("Your second number: "))

print(num_1 + num_2)


num_1 = int(input("Your first number: "))
num_2 = int(input("Your second number: "))

print(num_1 / num_2)
'''

num_1 = float(input("Your first number: "))
num_2 = float(input("Your second number: "))

print(num_1 / num_2)