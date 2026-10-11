from models.animals import Animal
from utils.phonenumber_Validation import phonenumber_validation
from utils.nationalid_validation import nationalid_validation
from exceptions import AdopterNotFound,AdopterHasBeenCreatedBefore,InvalidNationalId,InvalidPhoneNumber


class Adopter:
    adopters=[]
    def __init__(self, name:str, phone:str, national_id:str, adopted_animals:list[Animal]):
        self.name = name
        self.phone = phone
        self.national_id = national_id
        self.adopted_animals = adopted_animals
        try:
            Adopter.search(national_id)
        except AdopterNotFound:
            Adopter.adopters.append(self)
        else:
            raise AdopterHasBeenCreatedBefore('An adopter with this national ID already exists')

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        if phonenumber_validation(phone):
            self._phone = phone
        else:
            raise InvalidPhoneNumber("Invalid phone number")

    @property
    def national_id(self):
        return self._national_id

    @national_id.setter
    def national_id(self, national_id):
        if nationalid_validation(national_id):
            self._national_id = national_id
        else:
            raise InvalidNationalId('Invalid national ID')
    @classmethod
    def search(cls, national_id: str):
        for adopter in cls.adopters:
            if adopter.national_id == national_id:
                return adopter

        raise AdopterNotFound('Adopter has not been found')      