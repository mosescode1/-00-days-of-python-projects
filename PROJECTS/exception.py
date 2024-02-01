# try:
#     x = int(input("Please enter: "))
# except (RuntimeError, TypeError, NameError, ValueError):
#     pass

class B(Exception):
    pass

class C(B):
    pass
class D(C):
    pass

for cls in [D, B, C, D]:
    print(cls)
    try:
        raise cls()
    except B:
        print('B')
    except D:
        print("D")
    except C:
        print("C")