from services.shelter import Shelter
from models.adopter import Adopter
from cli.handlers import show_animals_cli,add_animal_cli,search_animal_cli,adopt_animal_cli,return_animal_cli,show_available_animals_cli,show_adopted_animals_cli

cli_options = {
    '1': 'Add animal',
    '2': 'Show all animals',
    '3': "Search animal",
    '4': "Adopt animal",
    '5': "Return animal",
    '6': "Show available animals",
    '7': "Show adopted animals",
    '0': "Exit"
}

shelter = Shelter()

print('===== Pet Shelter =====')
while True:
    print('what do you what to do')
    options=''
    for idx,option in cli_options.items():
        options+=(f'{idx}. {option}\n')
    choice= input(options) 
    match choice:
        case '1':
            add_animal_cli(shelter)
        case '2':
            show_animals_cli(shelter)  
        case '3':
            search_animal_cli(shelter)     
        case '4':
            adopt_animal_cli(shelter)           
        case '5':
            return_animal_cli(shelter)           
        case '6':
            show_available_animals_cli(shelter)  
        case '7':
            show_adopted_animals_cli(shelter)                  
        case '0':
            break
        case _:
            print('Invalid option. Please try again.')    

        
