# Program to find factorial

num = int(input("Enter a positive number: "))

factorial = 1

if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    for i in range(1, num + 1):
        factorial = factorial * i

    print("Factorial of", num, "is", factorial)

print("Program completed")

# Example: 5! = 5 * 4 * 3 * 2 * 1 = 120
print("Factorial calculation completed successfully")
