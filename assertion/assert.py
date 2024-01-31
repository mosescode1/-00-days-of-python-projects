def add(x, y):
    assert x > 0 and y > 0, "both numbers must be possitive" 
    return x + y

print(add(1, 1))
add(-1, -1)