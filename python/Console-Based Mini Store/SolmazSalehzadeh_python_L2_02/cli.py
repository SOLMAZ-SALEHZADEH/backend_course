from store import Store
from models.cart import Cart

is_loggedIn = False

store = Store()
cart = Cart(store)

def logIn(Username: str, Password: str) -> None:
    """Implement the login flow for managers."""
    usres = [{"Username": 'admin', "Password": "1234"}]

    global is_loggedIn

    is_loggedIn = any(
        user['Username'] == Username and user['Password'] == Password
        for user in usres
    )

    if is_loggedIn:
        print("\n✅ Login successful! Welcome, Manager.")
    else:
        print("\n❌ Login failed! Please try again or return to main menu.\n")

def add_product() -> None:
    """Handle adding products to the store."""
    print(
        '\n--------------------------------\n'
        '📦 Add Products\n'
        '--------------------------------'
    )

    while True:
        name = input(
            'Enter product name (or "done" to finish): '
        ).strip().lower()

        if name == 'done':
            print('Returning to main menu...\n')
            break
        else:
            try:
                price = float(input('Enter product price: '))

                if price < 0:
                    raise ValueError

            except ValueError:
                print("Invalid price")
                continue

            try:
                stock = int(input('Enter product stock quantity: '))

                if stock < 0:
                    raise ValueError

            except ValueError:
                print("Invalid stock")
                continue

            store.add_product(name, price, stock)
            print(f'✅ Product added: {name} - ${price} (Stock: {stock})\n')


def select_shopping_flow() -> None:
    """Handle the customer shopping flow."""
    while True:
        selected_flow = input(
            '\nWhat would you like to do?\n'
            ' 1.Add item to cart\n'
            ' 2. Remove item from cart\n'
            ' 3. View cart\n'
            ' 4. Checkout\n'
            ' 5. Return to main menu \n'
            'Enter choice:'
        )

        match selected_flow:
            case '1' | 'add':
                product_name = input(
                    '\nEnter product name:'
                ).strip().lower()

                try:
                    product_quantity = int(input('Enter quantity:'))

                    if product_quantity <= 0:
                        raise ValueError("Invalid quantity")

                    cart.add_to_cart(
                        product_name,
                        product_quantity
                    )

                    print(f'✅ Added {product_quantity} x {product_name} to cart')
                    print('\n--------------------\n🛍️ CUSTOMER PORTAL\n--------------------')
                    print("\n Available products:")

                    for product in store.list_products():
                        print(product)
                except ValueError as error:
                    print(error)
                    continue

            case '2' | 'remove':
                product_name = input(
                    'Enter product name to remove:'
                ).strip().lower()

                try:
                    cart.remove_from_cart(product_name)
                    print(f'🗑️ Removed {product_name} from cart.\n')
                except ValueError as error:
                    print(error)

            case '3' | 'view cart':
                items = cart.view_cart()

                if not items:
                    print('There is nothing in your basket')
                else:
                    print('\n🛒 Your cart:')

                    for item in items:
                        print(
                            f'{item.product_obj.name} x{item.quantity} '
                            f'- ${item.product_obj.price * item.quantity}\n'
                        )

                    print(f'💰 Total: ${cart.total_price()}')

            case '4' | 'Checkout':
                try:
                    print('\n🧾 Final Checkout:')
                    items, total_price = cart.checkout()
                    for item in items:
                        print(
                            f'{item.product_obj.name} x{item.quantity} '
                            f'- ${item.product_obj.price * item.quantity}\n'
                        )

                    print(f'💳 Total amount due: ${total_price}')
                    print('🎉 Thank you for shopping with us!')

                except ValueError as error:
                    print(error)

            case '5' | 'return':
                print('Returning to main menu...\n')
                break

            case _:
                print("Invalid choice")


