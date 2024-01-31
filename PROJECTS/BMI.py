# A body mass index calculator
weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
bmi = weight / (height ** 2)
print(int(bmi))