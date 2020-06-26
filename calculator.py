#calculator.py

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2


choice = input("Enter your operator:-\n")


num1 = int(input("Enter first number:-\n"))
num2 = int(input("Enter second number:-\n"))

if choice == '+':
    print("sum of: ",add(num1,num2))

elif choice == '-':
    print("sub is: ",sub(num1,num2))

elif choice == '*':
    print("mul is: ",mul(num1,num2))

elif choice == '/':
    print("Div is: ",div(num1,num2))

else:
    print("invalid operator")    
