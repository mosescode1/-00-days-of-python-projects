
def mylen(value):
    i = 0
    for _ in value:
        i += 1
    return i
    
listing = {"hello", "moses"}
print(mylen(listing))