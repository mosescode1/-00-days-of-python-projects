heights = input("Enter student heights").split()
sumation = 0
i = 0
for std_height in heights:
    i += 1
    sumation += int(std_height)
average_height = sumation / i
print(average_height)
    

