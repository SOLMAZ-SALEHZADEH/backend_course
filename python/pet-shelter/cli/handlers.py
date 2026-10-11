from exceptions import DuplicateAnimalError,AnimalNotFoundError,AnimalAlreadyAdoptedError,MaximumAdoptionReachedError,PetNotAdoptedByThisAdopterError,AdopterNotFound,InvalidNationalId,InvalidPhoneNumber
from models.adopter import Adopter
from utils.decorators import animal_action
from utils.input_validation import get_valid_age

def show_animals_cli(shelter):
    animals = shelter.show_animals()  
    print(animals)   

def get_adopter():
    national_id = input('Enter adopter national ID: ')

    try:
        return Adopter.search(national_id)
    except AdopterNotFound as error:
        print(error)

    name = input('Enter adopter name: ')
    phone = input('Enter adopter phone: ')

    try:
        return Adopter(name, phone, national_id, [])
    except InvalidNationalId as error:
        print(error)
        return None
    except InvalidPhoneNumber as error:
        print(error) 
        return None   

@animal_action
def add_animal_cli(shelter):
    name = input("Enter animal name: ").lower()
    age:int = get_valid_age()
    gender = input("Enter animal gender: ").lower()
    breed = input("Enter animal breed: ").lower()
    species = input("Enter animal species (Dog/Cat/Bird/Rabbit): ").capitalize()
    try:
        shelter.add_animal(name,age,gender,breed,species)
        print('The animal added successfully')
    except DuplicateAnimalError as error:
        print(error)      
def search_animal_cli(shelter):
    name:str = input('enter animal name: ').lower()
    age:int = get_valid_age()
    gender:str = input('enter animal gender: ').lower() 
    breed:str = input('enter animal breed: ').lower() 
    try:
        animal = shelter.search_animal(name,age,gender,breed)
        print(animal.show_info())
    except AnimalNotFoundError as error:
        print(error)


def adopt_animal_cli(shelter):
    name = input("Enter animal name: ").lower()
    age:int = get_valid_age()
    gender = input("Enter animal gender: ").lower()
    breed = input("Enter animal breed: ").lower()
    adopter = get_adopter()
    if adopter is None:
        return
    try:
        shelter.adopt_animal(name,age,gender,breed,adopter)
        print('animal is adopted successfully')
    except AnimalAlreadyAdoptedError as error:
        print(error)
    except MaximumAdoptionReachedError as error:
        print(error)    
    except AnimalNotFoundError as error:       
        print(error)   

def return_animal_cli(shelter):
    name:str = input('enter animal name: ')
    age:int = get_valid_age()
    gender:str = input('enter animal gender: ') 
    breed:str = input('enter animal breed: ') 
    national_id = input('enter adopter national id: ')
    try:
        adopter= Adopter.search(national_id)
        shelter.return_animal(name,age,gender,breed,adopter)
        print('animal is returned successfully')
    except PetNotAdoptedByThisAdopterError as error:
        print(error)    
    except AnimalNotFoundError as error:   
        print(error)  
    except AdopterNotFound as error:
        print(error)     

def show_available_animals(shelter):
    animals = shelter.show_available_animals()  
    print(animals) 

def show_available_animals_cli(shelter):
    animals = shelter.show_available_animals()  
    print(animals)  

def show_adopted_animals_cli(shelter):
    animals = shelter.show_adopted_animals()  
    print(animals)     
