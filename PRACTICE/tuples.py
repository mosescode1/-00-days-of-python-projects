# they are immutable data structure () and are ordered

tuple_1 = (1, 2, 4, 5)

for i in tuple_1:
    print(i)

sums = sum(tuple_1)
print("the sum of the tuple is :",sums)
min_tup = min(tuple_1)
max_tup = max(tuple_1)
print("the min is {} and max is {}".format(min_tup, max_tup))
length = len(tuple_1)
print("the length of the tuple is :",length)

print('slicinng through funtions')
slices = tuple_1[0:3]
print(slices)
reverse = tuple_1[::-1]
print(reverse)

tuple_2 = (2, 4, 5, 6 ,6)

print(list(tuple_2))
list_1 = [1, 4 , 5, 7]
print(tuple(list_1))
