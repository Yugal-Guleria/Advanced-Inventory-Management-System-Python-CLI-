#Created an disc named inventory to store data 
inventory = {
    "vegetables": ["Tomato", "Potato"],
    "fruits": ["Mango", "Pineapple"]
}

#Creating an function to get the category type 
def get_category():
    return input("Enter category (vegetables/fruits): ").lower()

#Creating an function to get the item type 
def get_item():
    return input("Enter item name: ")

#Creating an fucntion to check category is valid or not 
def is_valid_category(category):
    return category in inventory

#Creating an function to view item 
def view_items():
    for category in inventory:
        print(f"\n{category}:")
        for item in inventory[category]:
            print("-", item)

#Creating an function to add item 
def add_item():
    category = get_category()
    item = get_item()

    if is_valid_category(category):
        inventory[category].append(item)
        print("Item added successfully")
    else:
        print("Invalid category")

#Creating an function to check item 
def check_item():
    category = get_category()
    item = get_item()

    if is_valid_category(category):
        if item in inventory[category]:
            print(/n "Item is available")
        else:
            print(/n "Out of stock")
    else:
        print(/n "Invalid category")

#Creating the main loop 

while True:
    print("::: INVENTORY SYSTEM :::")
    print("1. View Items")
    print("2. Add Item")
    print("3. Check Item")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        view_items()

    elif choice == "2":
        add_item()

    elif choice == "3":
        check_item()

    elif choice == "4":
        print("Exiting system...")
        break

    else:
        print("Invalid choice")