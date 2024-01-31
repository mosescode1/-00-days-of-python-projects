def safe_print_list(my_list=[], x=0):
    new_list = my_list[:x]
    z = 0
    for i in my_list[:x]:
        print(i, end="")
        z += 1
    print()
    return z
        

my_list = [1, 2, 3, 4, 5]
nb_length = safe_print_list(my_list=my_list, x = 3)
print("nb_print: {:d}".format(nb_length))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 20)
print("nb_print: {:d}".format(nb_print))
        