class User:
    def __init__(self, name) -> None:
        self.__name = name
    def name(self):
        username = self.__name 
        print(f"This is your {username}")
    @property
    def UserName(self):
        return self.__name
    
    @UserName.setter
    def getUsername(self):
        print(f"your userName is {self.__name}")
        

x = User("username")
x.UserName()
x.name()