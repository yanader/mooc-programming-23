# Write your solution here:
class Pet:

    def __init__(self, name:str, species:str, year_of_birth:int) -> None:
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth

def new_pet(name: str, species:str, year_of_birth: int):
    return Pet(name, species, year_of_birth)