def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Prompt for and add an item
            item = input("Enter the item to add: ")
            item = item.strip()
            shopping_list.append(item)
            pass
        elif choice == 2:
            # Prompt for and remove an item
            item_remove = input("Enter the item to be removed: ")
            item_remove = item_remove.stip()
            shopping_list.remove(item_remove)
            pass
        elif choice == 3:
            # Display the shopping list
            print(shopping_list)
            pass
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()