# DATA STRUCTURE -LIST [] 

# Creating a list 

list_1 = list()
print(f"this is an empty list {list_1}")
print()
print("list are ordered sequencal mutable structure and can contain different data types")
print('-')
list_2 = [1, 2, 3, 4, 5]
print(f"this is an interger type of list {list_2}")
list_3 = ['string', 'yes', 'no']
print(f"this is an string type of list {list_3}")
list_4 = ['string', 'yes', 'no', 3, 5, 6.123, 6.77]
print(f"this is an mixed type of list {list_4}")

print('accessing an object in  a list using index ')
print(list_2[0])
print(list_3[1])
print(list_4[2])

print('Differnt methods and operation on a list')
# append and extend
list_5 = [1, 2, 4, 5, 6, 8]
list_5.append(10) # addes 10 to the end of the list 
# only use to add just an object 
list_5.extend([20, 5]) # extends the list with the new int object 
# extend only works on iteratable object 

# list concatination 

list_6 = [1, 4]
print("id of the first list_6", id(list_6))
list_5 += list_6 # doesnt create a new list 

list_7 = [20, 29]

list_6 = list_6 + list_7

print(list_5)
print(list_6, id(list_6))

l1 = [1, 2, 1, 1, 2, 3, 1, 5, 3, 5, 1]

# item to remove from the list
n = 1
while n in  l1:
    l1.remove(n)

print(l1)

nums = '10,20,30,40,50'

lis = []
number =nums.split(',')
for n in number:
    lis.append(int(n))
print(lis)