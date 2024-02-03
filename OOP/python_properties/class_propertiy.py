"""This defines a class with two instance attributes  name and age """

class Person:
    def __init__(self, name, age):
        self.name = name
        self.set_age(age)

    """Getters return thr value of an attribute While setters set a new value for an attribute"""
    def set_age(self, age): # A setter
        if age <= 0:
            raise ValueError("age must be greater than 0")
        self._age = age
    
    def get_age(self, age): # A getter
        return self.age
    # This method has a backward compatibility

john = Person('john', 20)
# since age is an instance attribute and can be assigned a new value by doing 
""""john.age = -1"""
# how ever doing that is wrong age can never be negative

# age = 20
# if age <= 0:
#     raise ValueError("age must be positive")
# else:
#     john.age = age
    
# print(john.age) # this change john.age to 20 wbut when age is less than 

# and you need to do this everytime you want to assign a new value to age 

# to stop repetiveness we use setters and getters 
# to see this go back to the class


"""To define a getter and setter method while achieving backward compatibility, you can use the property() class."""

# property(fget=None, fset=None, fdel=None, doc=None)

# fget is a function to get the value of the attribute, or the getter method.
# fset is a function to set the value of the attribute, or the setter method.
# fdel is a function to delete the attribute.
# doc is a docstring i.e., a comment
from pprint import pprint
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self, age):
        if age <= 0:
            raise ValueError('The age must be positive')
        self._age = age # this is a class atrribute the _age

    def get_age(self):
        return self._age

    age = property(fget=get_age, fset=set_age)
    

print(Person2.age)


person = Person2("moses", 40)

pprint(person.__dict__)
person.age = 30
pprint(Person.__dict__)