class Robot:
    """this is implementing a robot
    """
    population = 0 # class attribute
    def __init__(self, name , price) -> None:
        self.name = name
        self.price = price
        Robot.population += 1
    
    # def __del__(self):
    #     print("robot destroyed")
        
    def SetEnergy(self, energy):
        self.energy = energy
        
    def __str__(self) -> str:
        my_str = f"my name is {self.name} and my price is {self.price}"
        return my_str
    
    def __add__(self, other):
        price = self.price + other.price
        return price
    def __gt__(self, other):
        cmp = self.price > other.price
        return cmp
    def __lt__(self, other):
        oop = self.price < other.price
        return oop
        
# creating and object for the class robot

r1 = Robot("moses", 1000)
r2 = Robot("effa", 150)

print(r2 < r1)
