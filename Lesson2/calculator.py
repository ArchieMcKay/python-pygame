operation = input("What operation do you want to perform? ")
val_1 = int(input("Enter the first value: "))
val_2 = int(input("Enter the second value: "))

if operation == '+':
    print(val_1 + val_2)
elif operation == '-':
    print(val_1 - val_2)
elif operation == '*':
    print(val_1 * val_2)
elif operation == '/':
    print(val_1 / val_2);
else:
    print("Operation not permitted")
