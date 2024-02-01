class Square:
    def __init__(self, length) -> None:
        self.lenght = length
    def area(self):
        return self.lenght * 2

def addFunction(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Enter a valid integer')
    return a + b
