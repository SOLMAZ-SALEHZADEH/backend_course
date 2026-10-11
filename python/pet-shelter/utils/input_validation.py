
def get_valid_age():
    while True:
        try:
            age = int(input("Enter animal age: "))

            if age < 0:
                print("Age cannot be negative. Try again.")
                continue

            return age

        except ValueError:
            print("Invalid age. Please enter a whole number.")