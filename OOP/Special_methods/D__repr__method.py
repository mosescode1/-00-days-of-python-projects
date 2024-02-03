"""The __repr__ dunder method defines behavior when you pass an instance of a class to repr()"""

# basically and __repr__ returns a string that can be executed and yeild thesame value as the object

# it means if you pass he returned string object_name.__repr__() to the eval you would get the same value as the object_name


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self) -> str:
        return f"person({self.name}, {self.age})"
    
    def __str__(self) -> str:
        return f"{self.name}, {self.age}"
        

person = Person("Moses Effa", 40)
print(repr(person)) # ===>>> We get <__main__.Person object at 0x7f1c7de8c310> if we don't implement the __repr__
# by default it contains the memory address of the person object

"""When we create the __repr__ python will automatically call it"""

print(repr(person)) # ====> person(Moses Effa, 40)
print(person) # ===> still prints Moses Effa, 40 it calls the __str__ not the __repr__
print(str(person)) # ===> still prints Moses Effa, 40 it calls the __str__ not the __repr__


"""Main diffrence 

    The __str__ method returns a string representation of an object that is human-readable while the __repr__ method returns a string representation of an object that is machine-readable.

"""