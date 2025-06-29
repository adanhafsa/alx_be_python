# simple calculator using match case

#  prompt the user to enter two numbers and select an operation (addition, subtraction, multiplication, or division).
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operation = (input("Choose the operation (+, -, *, /):"))

# perform calculation using match case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*": 
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 == "0":
            print("cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        print("Invalid operation entered.")
        


