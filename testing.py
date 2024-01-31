name = {"name": "moses", "l_name": "effa"}
data = [x for x in range(4) if x % 2 != 0]
def sum(a, b,**kwargs):
    for items in kwargs.values():
        print(items)
        print(a + b)
        

sum(*data, **name)