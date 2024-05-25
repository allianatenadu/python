# Shopping Cart Program with Quantity Management

# Initialize empty lists to store cart items, prices, and quantities
cart = []
prices = []
quantities = []

# Welcome message
print("Welcome to the Shopping Cart Program!")

# Main loop to display menu and handle user input
while True:
    # Display menu options
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    
    # Prompt user for action choice
    action = int(input("Please enter an action: "))

    # Option 1: Add item to cart
    if action == 1:
        item = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{item}'? "))
        quantity = int(input(f"How many '{item}' would you like to add? "))
        cart.append(item)
        prices.append(price)
        quantities.append(quantity)
        print(f"'{item}' has been added to the cart.")

    # Option 2: View cart
    elif action == 2:
        if not cart:
            print("Your cart is empty.")
        else:
            print("The contents of the shopping cart are:")
            for i in range(len(cart)):
                print(f"{i + 1}. {cart[i]} - ${prices[i]:.2f} x {quantities[i]}")

    # Option 3: Remove item from cart
    elif action == 3:
        if not cart:
            print("Your cart is empty.")
        else:
            print("The contents of the shopping cart are:")
            for i in range(len(cart)):
                print(f"{i + 1}. {cart[i]} - ${prices[i]:.2f} x {quantities[i]}")
            index = int(input("Which item would you like to remove? ")) - 1
            if 0 <= index < len(cart):
                removed_item = cart.pop(index)
                prices.pop(index)
                quantities.pop(index)
                print(f"Item '{removed_item}' removed.")
            else:
                print("Sorry, that is not a valid item number.")

    # Option 4: Compute total price
    elif action == 4:
        total = sum(price * quantity for price, quantity in zip(prices, quantities))
        print(f"The total price of the items in the shopping cart is ${total:.2f}")

    # Option 5: Quit program
    elif action == 5:
        print("Thank you. Goodbye.")
        break

    # Invalid option
    else:
        print("Invalid option. Please try again.")
