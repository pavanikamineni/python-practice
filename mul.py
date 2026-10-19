# Program to print multiplication table

num = int(input("Enter a number: "))

print("Multiplication table of", num)

for i in range(1, 11):
    result = num * i
    print(num, "x", i, "=", result)

print("Table completed")

# Ask the user for another table
num2 = int(input("Enter another number: "))

for i in range(1, 11):
    print(num2, "x", i, "=", num2 * i)

print("Both multiplication tables are completed")