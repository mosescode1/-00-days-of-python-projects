# Defining a class
# we use snake case Or camel case
# we use singularity not plural

class User:
	active_user = 0
	def __init__(self, first, last, age) -> None:
		User.active_user += 1
		self.first = first.title() # all These are instance attributes
		self.last = last.title()   # perculiar to the object being created
		self.age = age
		print(f"{self.first} {self.last} just logged in")

	@classmethod
	def display_user(cls):
		return f"There are {cls.active_user} users"
	
	@classmethod
	def from_string(cls, data_stream):
		first, last, age = data_stream.split(",")  
		age = int(age)
		return cls(first, last, age)
	
	def logout(self):
		User.active_user -= 1
		print(f"{self.first} {self.last} logged out")

	def full_name(self):
		return f"This is {self.first} {self.last}"
	def initials(self):
		return f"{self.first[0]}.{self.last[0]}"

	def likes(self, thing): # instance method Self is always the first parameter
		return f"i'm {self.first} and i like {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, birthday"
	def say_hi(self):
		print(f"{self.first} {self.last} Says HELLLO!!!!!")


# user_1 = User("grace", "aderintoye", 20)
# user_2 = User("moses", "eteng", 20)
# full_name = user_1.full_name()
# full_name2 = user_2.full_name()
# initials = user_1.initials()
# initials2 = user_2.initials()
# likes = user_1.likes("money")
# birthday = user_1.birthday()
# user_1.say_hi()

# print(birthday)

# print(full_name)
# print(initials)
# print(likes)
# print(full_name2)
# print(initials2)

print(User.display_user())
user1 = User("Moses", "effa", 30)
user_2 = User("moses", "eteng", 20)
print(User.display_user())
user1 = User("Moses", "frayman", 30)
user_2 = User("moses", "nigga", 20)
print(User.display_user())


# class method would be use when you want to create an instance 
# working with csv files
tom = User.from_string("tom,jones,89")
print(tom.full_name())