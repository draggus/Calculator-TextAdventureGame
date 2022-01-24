def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y==0:
        return "Cant divide by zero!"
    else:
        return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Factorial")
print("6.Exponential")

while True:
    choice = input("Enter choice(1/2/3/4/5/6): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter the First Number: "))
        num2 = float(input("Enter the Second Number: "))
        if choice == '1':
            print(num1, "+", num2,"=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2,"=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
    elif choice in('1', '2', '3', '4', '5', '6'):
        if choice == '5':
            num1 = float(input("Enter the Number: "))
            num1 = int(num1)
            factorial = 1
            if num1 < 0:
                print("Sorry, factorial does not exist for negative numbers")
            elif num1 == 0:
                print("The factorial of 0 is 1")
            else:
                for i in range(1, num1 + 1):
                    factorial = factorial * i
                    print("The factorial of", num1, "is", factorial)
        elif choice == '6':
            num1 = float(input("Enter the base number: "))
            num1 = int(num1)
            num2 = float(input("Enter the exponential number: "))
            num2 = int(num2)
            exponent = num1 ** num2
            print("Exponential value of the equation is:",exponent)
        next_calculation = input("Lets do the next calculation? (yes/no): ")
        if next_calculation == "no":
            print("Thanks for calculating with us :)")
            break
    else:
        print("Invalid Input")