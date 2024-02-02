class Pet:
    allowed_pet = ['cat', 'dog', 'fish', "rat"]
    def __init__(self, Pet_name, pet_species):
        if pet_species.lower() not in Pet.allowed_pet:
            raise ValueError(f"you can't have a {pet_species} as a pet")
        self.pet_name = Pet_name
        self.pet_age = pet_species
        
    def add_species(self, species):
        Pet.allowed_pet.append(species)

cat = Pet("jerrty", 'cat')
dog = Pet('dwane', 'dog') 

cat.add_species('goat')
print(Pet.allowed_pet)   