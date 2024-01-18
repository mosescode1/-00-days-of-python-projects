alpha = dict()
with open('/home/ossigma/Desktop/LEARNING/100-days-of-python-projects/PROJECTS/file.csv') as f:
    content = f.read().splitlines()
    # print(content)
    for item in content[1:]:
        letter, word = item.split('\t')
        alpha[letter] = word

check = input("enter name: ").upper()
print(check, end=' ==> ')
for char in check:
    if char == check[-1]:
        print(alpha[char])
        print()
    else:
        print(alpha[char], end=' ,')

