class Animal:
    animals:list["Animal"] =[]
    def __init__(self, name, age, gender, breed, is_adopted):
        self.name = name 
        self.age = age
        self.gender = gender
        self.breed = breed
        self.is_adopted = is_adopted
        self.adopter = None
        Animal.animals.append(self)
    def show_info(self):
        return (
        f"Name: {self.name}\n"
        f"Age: {self.age}\n"
        f"Gender: {self.gender}\n"
        f"Breed: {self.breed}\n"
        f"Adopted: {self.is_adopted}\n"
        f"Sound: {self.make_sound()}"
    )    
    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, age, gender, breed, is_adopted):
        super().__init__(name, age, gender, breed, is_adopted)
    def make_sound(self):
        return 'woof woof'        
    
class Cat(Animal):
    def __init__(self, name, age, gender, breed, is_adopted):
        super().__init__(name, age, gender, breed, is_adopted)
    def make_sound(self):
        return 'mio mio' 

class Bird(Animal):
    def __init__(self, name, age, gender, breed, is_adopted):
        super().__init__(name, age, gender, breed, is_adopted)
    def make_sound(self):
        return 'ooo oooo'       

class Rabbit(Animal):
    def __init__(self, name, age, gender, breed, is_adopted):
        super().__init__(name, age, gender, breed, is_adopted)
    def make_sound(self):
        return 'uuuhh uuuhh'            
