try:
    a = int(input("Please enter: "))
    b = int(input("Please enter: "))
    c = a / b
except ValueError:
    print("exception encountred")
else:
    print("no errors")
    print("c value", c)
finally:
    print("good bye")  
print("some other code")
x = 10
print(x**x)
