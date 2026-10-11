class AnimalNotFoundError(Exception):
    pass

class AnimalAlreadyAdoptedError(Exception):
    pass

class MaximumAdoptionReachedError(Exception):
    pass

class PetNotAdoptedByThisAdopterError(Exception):
    pass

class DuplicateAnimalError(Exception):
    pass

class AdopterNotFound(Exception):
    pass

class AdopterHasBeenCreatedBefore(Exception):
    pass

class InvalidNationalId(Exception):
    pass

class InvalidPhoneNumber(Exception):
    pass