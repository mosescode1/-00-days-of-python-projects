class Robot:
    
    def __init__(self, name ):
        self._name = name
    
    def talking(self):
        print("i'm a robat that talks")
        return "yes" 
        
    def distance_walked(self, x, y):
        print(x * y)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

x = Robot("moses")
x.distance_walked(2, 4)
x.name = "ayo"
print(x.name)