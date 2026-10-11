from  models.animals import Dog, Cat, Bird, Rabbit, Animal
from models.adopter import Adopter
from exceptions import AnimalNotFoundError,AnimalAlreadyAdoptedError,MaximumAdoptionReachedError,PetNotAdoptedByThisAdopterError,DuplicateAnimalError

species_classes = {
    "Dog": Dog,
    "Cat": Cat,
    "Bird": Bird,
    "Rabbit": Rabbit
}
class Shelter():
    def add_animal(self,name:str,age:int,gender:str,breed:str,species:str):

        if species not in species_classes:
            print("Invalid animal species.")
            return

        animal_class = species_classes[species]

        for animal in Animal.animals:
            if (
                type(animal) is animal_class
                and animal.name == name
                and animal.age == age
                and animal.gender == gender
                and animal.breed == breed
            ):
                raise DuplicateAnimalError(
                    "An animal with these features already exists in the shelter."
                )

        animal_class(name, age, gender, breed, False)
    def delete_animal(self,name:str,age:int,gender:str,breed:str):
        animal = self.search_animal(name,age,gender,breed) 
        Animal.animals.remove(animal)  
    def search_animal(self,name:str,age:int,gender:str,breed:str):
        for animal in Animal.animals:
            if(animal.name == name and animal.age == age and animal.gender == gender and animal.breed == breed):
                return animal
        else:
            raise AnimalNotFoundError('This animal does not exist in the shelter') 
    def show_animals(self):
        if not Animal.animals:
            return "There are no animals in the shelter."

        animals_list = []

        for index, animal in enumerate(Animal.animals, start=1):
            animal_info = f"Animal #{index}\n{animal.show_info()}"
            animals_list.append(animal_info)

        return "\n\n".join(animals_list)
    def adopt_animal(self,
    name: str,
    age: int,
    gender: str,
    breed: str,
    adopter: Adopter):
        if len(adopter.adopted_animals) >= 9:
            raise MaximumAdoptionReachedError('The adopTer already has adopted 9 pets')
        animal = self.search_animal(name,age,gender,breed) 
        if animal.is_adopted :
            raise AnimalAlreadyAdoptedError('The animal has been adopted already')
        animal.is_adopted = True
        animal.adopter = adopter
        adopter.adopted_animals.append(animal)

    def return_animal(self,name:str,age:int,gender:str,breed:str,adopter: Adopter):
        animal = self.search_animal(name,age,gender,breed,) 
        if animal not in adopter.adopted_animals:
            raise PetNotAdoptedByThisAdopterError('Pet not adopted by this adopter')

        animal.is_adopted = False
        animal.adopter = None
        adopter.adopted_animals.remove(animal)
    def search_by_name(self,animal_name):
        result = filter(lambda animal:animal.name == animal_name,Animal.animals)
        return list(result)
    def search_by_species(self,species:str):
        species_class= species_classes[species]
        result = filter(lambda animal:isinstance(animal, species_class), Animal.animals)
        return list(result)
    def show_available_animals(self):
        animals = list(filter(lambda animal: not animal.is_adopted , Animal.animals))
        
        if not animals:
            return "There are no animals in the shelter."

        animals_list = []

        for index, animal in enumerate(animals, start=1):
            animal_info = f"Animal #{index}\n{animal.show_info()}"
            animals_list.append(animal_info)

        return "\n\n".join(animals_list)
    def show_adopted_animals(self):
        animals = list(filter(lambda animal: animal.is_adopted ,Animal.animals))
        
        if not animals:
            return "There are no animals in the shelter."

        animals_list = []

        for index, animal in enumerate(animals, start=1):
            animal_info = f"Animal #{index}\n{animal.show_info()}"
            animals_list.append(animal_info)

        return "\n\n".join(animals_list)

