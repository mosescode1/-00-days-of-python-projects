# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age
        
#     @property  
#     def get_age(self):
#         return self._age
    
#     age = property(fget=get_age)
    

# moses = Person('mosees', 30)
# print(moses.age)
# print(moses.get_age())


# setter Decorator
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age
    
    @age.setter
    def set_age(self, value):
        if value <= 0:
            raise ValueError('The age must be positive')
        self._age = value
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('The name cannot be empty')
        self._name = value
