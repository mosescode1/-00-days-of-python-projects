from more_itertools import first


profile = {'first-name': 'Eteng', 'last_name': 'moses', 'age': 24, 'D.O.B': '02-aug-2023'}

print('#' * 10 + " Looping Through dict " + '#' * 20)

for keys in profile:
    print(keys, ':', profile[keys])
    
print('#' * 10 + "Getting length of a dic " + '#' * 20)
print(len(profile))
print()
print('#' * 10 + "Using the in operator to check avalability of key " + '#' * 20) 
print('date' in profile)
print('first-name' in profile)
print()
print('#' * 20 + "Using the in operator to check avalability of key " + '#' * 20) 
popped = profile.popitem()
print(profile, popped)
# profile.clear() deletes and entire dictionary
# print(profile)
print()
print('getting keys but return them in a tuple')
keys = profile.keys()
print(keys)
print()
print('getting values but return them in a tuple')
values = profile.values()
print(values)
print()
print('g using get(key) from a dic to get the value of the key')
get_method = profile.get('first-name')
print(get_method)
print('g using pop(key) from a dic to remove the item from the dict')
pop_method = profile.pop('age')
print(pop_method)
