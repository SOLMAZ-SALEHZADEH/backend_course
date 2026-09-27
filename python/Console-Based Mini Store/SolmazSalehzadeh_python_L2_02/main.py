import cli

# main script MINI STORE MANAGEMENT SYSTEM
print(
    '=================================\n'
    '🛍️ MINI STORE MANAGEMENT SYSTEM\n'
    '=================================\n'
)

user_role = ''

# cli
while True:
    user_role = input(
        '👋 Welcome! Please select your role:\n'
        ' 1. Store Manager\n'
        ' 2. Customer\n'
        ' 3. Exit Program\n'
        ' Enter choice:\n'
    )

    match user_role:
        case '1':
            print(
                '\n--------------------------------\n'
                '🔐 Store Manager Login\n'
                '--------------------------------'
            )

            username = input("Username: ")
            password = input("Password: ")

            cli.logIn(username, password)

            if cli.is_loggedIn:
                cli.add_product()

        case '2':
            print(
                '\n--------------------\n'
                '🛍️ CUSTOMER PORTAL\n'
                '--------------------'
            )

            print('Hello, dear customer! ')
            print("\n Available products:")

            for product in cli.store.list_products():
                print(product)

            cli.select_shopping_flow()

        case '3':
            print("👋 Goodbye! See you next time.")
            break

        case _:
            print("Invalid choice")