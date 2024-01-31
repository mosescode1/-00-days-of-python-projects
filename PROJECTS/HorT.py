import random
choice = int(input("Enter your choice: between 0 and 1: "))

list_table = ["hEAD", "TAIL"]

comp_choice = random.randint(0, 1)
print(comp_choice)
print(list_table[choice])

print(f"your choice is: {list_table[choice]}")
print(f"computer choice is: {list_table[comp_choice]}")