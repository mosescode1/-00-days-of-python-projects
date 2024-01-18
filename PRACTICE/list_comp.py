# LIST COMPREHENSION
print("[expression for item in iteratable]")
list_1 = [x for x in range(10)]
print(list_1)

list_2 = [1, 2, 3, 4, 5]
list_3 = [x**2 for x in list_2]
print("list {} comp list {}".format(list_2, list_3))

list_4 = ['mary', 'jane', 'john', 'doe']
list_5 = [(x).upper() for x in list_4]
print("list {} comp list {}".format(list_4, list_5))

list_6 = ['mary', 'grace', 'john', 'man']
list_7 = [names for names in list_4 if names in list_6]
print(list_7)

list_8 = [names.upper() for names in list_6 ]
print(list_8)
list_9 = [names for names in list_8 if names in list_7]
print(list_9)

list_10 = "I love cat and dogs"

print(list_10[-1::-1])