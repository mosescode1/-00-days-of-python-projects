class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"my name is {self.name}, and age: {self.age}")
    
    @classmethod
    def call(cls):
        return Person('John Doe', 30)
    
    @staticmethod
    def girlfriend(name):
        print(f"my girlfriend name is {name}")
    @staticmethod
    def addNum(a, b):
        return a + b

class Employee(Person):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_tittle = job_title
        
    # def greet(self):
    #     print(f"my name is {self.name} and i am {self.age} a working {self.job_tittle}")


mom = Person.call()
mom.greet()
employ = Employee("moses", 20, 'programmer')

employ.greet()
employ.girlfriend('grace')
resuilt = employ.addNum(2, 4)
print(resuilt)