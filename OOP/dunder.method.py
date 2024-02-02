"""__repr__ is used to provide nicer string representation a representation"""


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # helps in returning the string representation
    def __repr__(self):
        return f"{self.name} and {self.age}" 
    

person = Human("moses", 20)
person = str(person)
print(person)