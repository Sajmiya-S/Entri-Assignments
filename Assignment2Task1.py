# Create a basic calculator program to perform various arithmetic operations

print("\nWelcome to Calculator\n*********************")
print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulo\n6. Exponentiation\n7. Floor Division\n8. Exit")

a = int(input("\nEnter first number: "))
b = int(input("\nEnter second number: "))
c = int(input("\nEnter your choice: "))

if c == 1:
    print("\nYou have selected 'Addition'")
    print(a," + ",b,"= ",a + b)
elif c == 2:
    print("\nYou have selected 'Subtraction'")
    print(a," - ",b,"= ",a - b)
elif c == 3:
    print("\nYou have selected 'Multiplication'")
    print(a," * ",b,"= ",a * b)
elif c == 4:
    print("\nYou have selected 'Division'")
    if b == 0:
        print("\nCannot divide by 0")
    else:
        print(a," / ",b,"= ",a / b)
elif c == 5:
    print("\nYou have selected 'Modulo'")
    if b == 0:
        print("\nCannot divide by 0")
    else:
        print(a," % ",b,"= ",a % b)
elif c == 6:
    print("\nYou have selected 'Exponentiation'")
    print(a," to the power of ",b,"= ",a ** b)
elif c == 7:
    print("\nYou have selected 'Floor Division'")
    if b == 0:
        print("\nCannot divide by 0")
    else:
        print(a," // ",b,"= ",a // b)
elif c == 8:
    print("\nExit")
else:
    print("\nIncorrect choice")
    
