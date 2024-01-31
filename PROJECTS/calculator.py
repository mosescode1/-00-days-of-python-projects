from os import system
from art import logo2
# ADD
def add(num1, num2):
    """Adds the value of num1 and num2"""
    return num1 + num2

# SUBTRACT
def sub(num1, num2):
    """subtract the value of num1 and num2"""
    return num1 - num2

# MULTIPLY
def mul(num1, num2):
    """multiply the value of num1 and num2"""
    return num1 * num2

# DIVIDES
def div(num1, num2):
    """divides the value of num1 and num2"""
    return num1 / num2

# REMAINDER 
def mod(num1, num2):
    """returns the remainder value of num1 and num2"""
    return num1 % num2

operators = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    '%': mod
}


def print_sign(operators):
    for keys in operators:
        print(keys)

def calculator():
    print(logo2, end="")

    num1 = eval(input("Please enter first num: "))


        

    while True: 
        num2 = eval(input("Please enter second num: "))
        print_sign(operators)
        print("Enter the operation you want to perform")
        sign = input("Please enter sign: ")
        function = operators[sign]
        answer = function(num1, num2)
        print(f"{num1} {sign} {num2} = {answer}")

        cont = input("Do you want to continue: y for YES n to restart: ")
        
        if cont == 'y':
            num1 = answer
        else:
            system('clear')
            calculator()
            break

calculator()