# the __str__ method is a special method also known as a dunder method that makes a representation of a class 

class Person:
    def __init__(self, first_name:str, last_name:str, age:int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def __str__(self) -> str:
        return f"Person({self.first_name}, {self.last_name}, {self.age})"

# the person class has three instance attributes which are
        # first_name
        # last_name
        # age
# this create a new instance object to the class 
person = Person('Moses', 'Eteng', 25)
# when we try to print an instance of the object we get the address of where it is stored 
print(person) # ==> <__main__.Person object at 0x7fc0abc8c310>


# We use the __str__ to represent the instance of a class so we need to implement the __str__ in our class so python will internally call the __str__ when the instance call it


# now when we execute the print(person) it returns the strings representation and not the memory address 
print(person) # Person(Moses, Eteng, 25)