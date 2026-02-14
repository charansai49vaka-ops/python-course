num1=int(input("Enter num1:"))
a=input("Select a operator (+, -, *, /):")
num2=int(input("Enter the second number: "))
match a:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)
    case _:
        print("Not found")
        