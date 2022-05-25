# Creating a basic calculator
print("Select an option")
print("add")
print("subtract")
print("multiply")
print("divide")
while True:
    option = input("Select an option:")
    if option in ("add", "subtract", "multiply", "divide"):
        Num1 = float(input("Enter Number1:"))
        Num2 = float(input("Enter Number2:"))
        if option == "add":
            print(Num1, "+", Num2, "=", Num1+Num2)
        elif option == "subtract":
            print(Num1, "-", Num2, "=", Num1-Num2)
        elif option == "multiply":
            print(Num1, "*", Num2, "=", Num1*Num2)
        elif option == "divide":
            print(Num1, "/", Num2, "=", Num1/Num2)
    else:
        break
print("Invalid option")
