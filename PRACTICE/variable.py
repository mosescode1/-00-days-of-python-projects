a = int(input("enter an input for a: "))
b = int(input("enter an input for b: "))

print("value of a is {} and value of b is {}".format(a,b))

temp = a
a = b
b = temp
print("Exchanged value")
print("Now the value in a is {}\nthe value of b is {}".format(a,b))