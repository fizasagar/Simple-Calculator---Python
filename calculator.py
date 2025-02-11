# SIMPLE CALCULATOR USING PYTHON PROGRAMMING 

def calculator(num1, num2, operation):
    if operation == "addition":
        return num1 + num2
    elif operation == "subtraction":
        return num1 - num2
    elif operation == "multiplication":
        return num1 * num2
    elif operation == "division":
        if num2 == 0:
            return "Division by zero is not allowed"
        return num1 / num2
    else:
        return "Invalid Operation"

# MAIN PROGRAM
def main():
    print("Welcome To Fiza's Python Calculator")
    # user's name here
    name = input("Enter your name: ")
    # numbers and operation
    num1= float(input("Enter your first number: "))
    num2= float(input("Enter your second number: "))
    print("Choose the operation to perform : Addition, Subtraction, Multiplication, Division")
    operation = input("Enter operation: ").strip().lower()
    result = calculator(num1,num2,operation)
    print(f"Dear {name}, the result of {operation} your numbers is: {result}")

main()    