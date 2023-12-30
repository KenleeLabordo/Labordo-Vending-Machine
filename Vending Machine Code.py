class VendingMachine:
    def __init__(self):
        # Initialize the snacks with their names, prices, and quantities
        self.snacks = {
            'A1': {'name': 'Salt and Vinegar Chips', 'price': 3, 'quantity': 5},
            'A2': {'name': "Miss sweety's white chocolate", 'price': 5, 'quantity': 5},
            'A3': {'name': 'Nuka Cola', 'price': 2, 'quantity': 5},
            'A4': {'name': 'C&C Cookies', 'price': 4, 'quantity': 5},
            'A5': {'name': 'Cuboid Gum', 'price': 1, 'quantity': 5},
            'B1': {'name': "Dee'z Nuts", 'price': 3, 'quantity': 5},
            'B2': {'name': "T-Pain's Granola Bars", 'price': 4, 'quantity': 5},
            'B3': {'name': 'Echo Echo Candy', 'price': 2, 'quantity': 5},
            'B4': {'name': "Garret's Popcorn", 'price': 5, 'quantity': 5},
            'B5': {'name': 'Not so fun Pretzels', 'price': 3, 'quantity': 5}
        }

        # Initialize the combo deals with their names and prices
        self.combo_deals = {
            'C1': {'name': 'Salt and Vinegar with Nuka Cola', 'price': 6},
            'C2': {'name': "Miss sweety's white chocolate with C&C Cookies", 'price': 9},
            'C3': {'name': "Dee'z Nuts with T-Pain's Granola Bars and Soda", 'price': 9},
            'C4': {'name': 'Cuboid Gum with Echo Echo Candy', 'price': 3},
            'C5': {'name': 'Salt and Vinegar Chips with Echo Echo Candy', 'price': 5},
            'C6': {'name': "Garret's Popcorn with Soda and Chips", 'price': 10},
            'C7': {'name': "Miss sweety's white chocolate with Echo Echo Gum", 'price': 6},
            'C8': {'name': 'C&C Cookies with Nuka Cola and Echo Echo Candy', 'price': 8},
            'C9': {'name': 'Not so fun Pretzels with Nuka Cola', 'price': 5},
            'D1': {'name': "Dee'z Nuts with Echo Echo Candy and Nuka Cola", 'price': 8},
            'D2': {'name': "Cuboid Gum with Garret's Popcorn and Miss sweety's white chocolate", 'price': 11},
            'D3': {'name': "Echo Echo Candy with Garret's Popcorn and Nuka Cola", 'price': 9},
            'D4': {'name': 'Salt and Vinegar Chips with Not so fun Pretzels and Echo Echo Candy', 'price': 8},
            'D5': {'name': "T-Pain's Granola Bar with Gum and Soda", 'price': 7},
            'D6': {'name': 'C&C Cookies with Not So Fun Pretzels and Salt and Vinegar Chips', 'price': 9}
        }

        # Initialize the balance amount for demonstration
        self.balance = 30

        # Set the administrator password
        self.admin_password = 'admin_pass'

    def display_user_menu(self):
        # Display options for the user menu
        print("\n==== USER MENU ====")
        print("1. Buy a snack")
        print("2. Buy a combo deal")
        print("3. Check balance")
        print("4. Exit")

    def display_admin_menu(self):
        # Display options for the administrator menu
        print("\n==== ADMINISTRATOR MENU ====")
        print("1. Modify product price")
        print("2. Modify product quantity")
        print("3. Modify product name")
        print("4. Set administrator password")
        print("5. Exit")

    def display_snacks(self):
        # Display available snacks with their names, prices, and quantities
        print("\nAvailable Snacks:")
        for key, snack in self.snacks.items():
            print(f"{key}. {snack['name']} - Dhs{snack['price']} - Quantity: {snack['quantity']}")

    def display_combo_deals(self):
        # Display available combo deals with their names and prices
        print("\nAvailable Combo Deals:")
        for combo, details in self.combo_deals.items():
            print(f"{combo}. {details['name']} - Dhs{details['price']}")

    def buy_snack(self, choice):
        # Allow the user to buy a snack and update the balance
        try:
            snack = self.snacks[choice]
            if snack['quantity'] > 0:
                print(f"\nYou bought {snack['name']} for Dhs{snack['price']}!")
                snack['quantity'] -= 1
                self.balance -= snack['price']
                print(f"Remaining quantity: {snack['quantity']}")
                print(f"Remaining balance: Dhs{self.balance}")
            else:
                print(f"\nSorry, {snack['name']} is out of stock.")
        except KeyError:
            print("\nInvalid choice. Please enter a valid product key.")

    def buy_combo_deal(self, choice):
        # Allow the user to buy a combo deal and update the balance
        try:
            combo = self.combo_deals[choice]
            print(f"\nYou bought the combo deal: {combo['name']} for Dhs{combo['price']}!")
            self.balance -= combo['price']
            print(f"Remaining balance: Dhs{self.balance}")
        except KeyError:
            print("\nInvalid choice. Please enter a valid product key.")

    def check_balance(self):
        # Display the user's current balance
        print(f"\nYour current balance is: Dhs{self.balance}")

    def run_user(self):
        # Run the user interface
        while True:
            self.display_user_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.display_snacks()
                snack_choice = input("Enter the product key of the snack you want to buy: ")
                self.buy_snack(snack_choice)
            elif choice == '2':
                self.display_combo_deals()
                combo_choice = input("Enter the product key of the combo deal you want to buy: ")
                self.buy_combo_deal(combo_choice)
            elif choice == '3':
                self.check_balance()
            elif choice == '4':
                print("\nThank you for using the vending machine. Have a great day!")
                break
            else:
                print("\nInvalid choice. Please enter a number between 1 and 4.")

    def modify_product_price(self, product_key):
        # Allow the administrator to modify the price of a product
        try:
            new_price = float(input("Enter the new price for the product: "))
            if new_price > 0:
                self.snacks[product_key]['price'] = new_price
                print(f"\nPrice for {self.snacks[product_key]['name']} updated to Dhs{new_price}.")
            else:
                print("\nInvalid price. Please enter a positive value.")
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")

    def modify_product_quantity(self, product_key):
        # Allow the administrator to modify the quantity of a product
        try:
            new_quantity = int(input("Enter the new quantity for the product: "))
            if new_quantity >= 0:
                self.snacks[product_key]['quantity'] = new_quantity
                print(f"\nQuantity for {self.snacks[product_key]['name']} updated to {new_quantity}.")
            else:
                print("\nInvalid quantity. Please enter a non-negative value.")
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")

    def modify_product_name(self, product_key):
        # Allow the administrator to modify the name of a product
        new_name = input("Enter the new name for the product: ")
        self.snacks[product_key]['name'] = new_name
        print(f"\nName for {product_key} updated to {new_name}.")

    def set_admin_password(self):
        # Set a new administrator password
        new_password = input("Enter a new administrator password: ")
        self.admin_password = new_password
        print("\nAdministrator password set successfully.")

    def run_administrator(self):
        # Run the administrator interface
        admin_password = input("Enter the administrator password: ")
    
        if admin_password == self.admin_password:
            while True:
                self.display_admin_menu()
                admin_choice = input("Enter your choice (1-5): ")

                if admin_choice == '1':
                    self.display_snacks()
                    product_key = input("Enter the product key to modify the price: ")
                    self.modify_product_price(product_key)
                elif admin_choice == '2':
                    self.display_snacks()
                    product_key = input("Enter the product key to modify the quantity: ")
                    self.modify_product_quantity(product_key)
                elif admin_choice == '3':
                    self.display_snacks()
                    product_key = input("Enter the product key to modify the name: ")
                    self.modify_product_name(product_key)
                elif admin_choice == '4':
                    self.set_admin_password()
                elif admin_choice == '5':
                    print("\nExiting administrator mode.")
                    break
                else:
                    print("\nInvalid choice. Please enter '1', '2', '3', '4', or '5'.")
        else:
            print("\nIncorrect password. Access denied.")

    def run(self):
        # Determine whether the user or administrator is accessing the vending machine
        user_or_admin = input("Enter 'user' or 'admin' to access the vending machine: ")

        if user_or_admin == 'user':
            self.run_user()
        elif user_or_admin == 'admin':
            self.run_administrator()
        else:
            print("\nInvalid choice. Please enter 'user' or 'admin'.")

if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run()
