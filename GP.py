import math

def calculator():
    print("------ Scientific Calculator ------")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Square Root (√)")
    print("6. Power (x^y)")
    print("7. Sine / Cos / Tan")
    print("8. Logarithm (log base 10)")
    print("9. Factorial")
    print("0. Exit")

    while True:
        choice = int(input("\nEnter your choice: "))

        if choice == 0:
            print("Thank you! Exiting...")
            break

        if choice in [1,2,3,4,6]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

        if choice == 1:
            print("Result =", a + b)
        elif choice == 2:
            print("Result =", a - b)
        elif choice == 3:
            print("Result =", a * b)
        elif choice == 4:
            if b != 0:
                print("Result =", a / b)
            else:
                print("Error: Division by zero")
        elif choice == 5:
            n = float(input("Enter number: "))
            print("Square Root =", math.sqrt(n))
        elif choice == 6:
            print("Result =", math.pow(a, b))
        elif choice == 7:
            angle = float(input("Enter angle in degrees: "))
            rad = math.radians(angle)
            print("sin =", round(math.sin(rad), 4))
            print("cos =", round(math.cos(rad), 4))
            print("tan =", round(math.tan(rad), 4))
        elif choice == 8:
            n = float(input("Enter number: "))
            print("log10 =", round(math.log10(n), 4))
        elif choice == 9:
            n = int(input("Enter number: "))
            print("Factorial =", math.factorial(n))
        else:
            print("Invalid choice! Try again.")

# Run the calculator
calculator()
