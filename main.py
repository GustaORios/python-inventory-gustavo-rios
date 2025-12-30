
#menu
mainMenu = ("1.Add Item","2.View inventory","3.Update item","4.Remove item", "5.Exit")
selectedOption = 0

def printMenu(menuItems):
    print("-" * 20)
    for menu in menuItems:
        print(menu)

class Product:
    def __init__(self, name, price, quantity, brand):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.brand = brand 

    def display_details(self, product_id):
        print(f"ID: {product_id} | Name: {self.name} | Brand: {self.brand[0]} | Category: {getattr(self, 'category', 'N/A')}")
        print(f"Price: ${self.price:.2f} | Quantity: {self.quantity}")
        pass

class PerishableProduct(Product):
    def __init__(self, name, price, quantity, brand, expiry_date):
        super().__init__(name, price, quantity, brand)
        self.expiry_date = expiry_date

    def display_details(self, product_id):
        super().display_details(product_id)
        print(f"Expiry Date: {self.expiry_date}")

inventory = {}
categories = ["Electronics", "Home", "Office"]
product_ids = set()


def add_item():
    try:
        print("\nAdd Item")
        print("-" * 10)
        p_id = input("Enter product ID: ")
        if p_id in product_ids:
            print("Error: ID already exists.")
            return

        name = input("Enter product name: ")
        print(f"Categories: {categories}")
        cat = input("Select category: ")
        brand_name = input("Enter brand name: ")
        brand = (brand_name,)
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        new_product = Product(name, price, qty, brand)
        new_product.category = cat
        
        inventory[p_id] = new_product
        product_ids.add(p_id)
        print("Item added successfully!")
    except ValueError:
        print("Invalid input. Please enter numbers for price and quantity.")

def view_inventory():
    print("\nCurrent Inventory")
    print("-" * 10)
    if not inventory:
        print("Inventory is empty.")
    else:
        for p_id, obj in inventory.items():
            obj.display_details(p_id)
            print("-" * 20)

    
while(selectedOption != 5):
    printMenu(mainMenu)
    selectedOption = int(input("Enter option number (1-5): "))
    if(selectedOption not in range(1,6)): # 1 to 5
        print("Please don't make this mistake AGAIN or else...")
        continue
    if selectedOption == 1:
        add_item()
    elif selectedOption == 2:
        view_inventory()
    elif selectedOption == 3:
        print("3")
       # update_item()
    elif selectedOption == 4:
        print("4")
       # remove_item()
    elif selectedOption == 5:
        print("5")
       # save_to_file()
        print("Saving and exiting...")
        break
    else:
        print("Invalid choice.")
