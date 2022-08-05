# Simple calculator

print("enter the numbers")
a = int(input("First number:"))
b = int(input("Second number"))

print("\nThe operations are:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = input("\nSelect the operation:")

if operation == '1':
    print("The sum is:", str(a + b))
elif operation=='2':
    print("The sub is:", str(a-b))
elif operation=='3':
    print("The product is:", str(a*b))
elif operation=='4':
    print("The result is:", str(a/b))
else:
    print("Invalid operation")
