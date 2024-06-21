"""
This program is a simple pizza ordering system. 

It allows the user to select a pizza size, quantity, and toppings. 
The prices for the pizza sizes and toppings are predefined. 

The user is prompted to select a pizza size and quantity, and then to select toppings. 
The user's input is validated, and they are prompted again if their input is invalid. 

The program calculates the price for each item (pizza size + toppings) and the total price (quantity * item price). 
The order confirmation includes the price for each item and the overall total.
"""

# Initialize pizza sizes and prices
pizza_prices = {"Small": 6.00, "Medium": 8.00, "Large": 10.00}

# Initialize toppings and prices
toppings_prices = {"Pepperoni": 1.00, "Sausage": 1.00, "Olives": 1.00}

# Display the pizza menu
print("Welcome to our Pizza Shop")
print("1. Small cheese pizza: $6.00")
print("2. Medium cheese pizza: $8.00")
print("3. Large cheese pizza: $10.00")

# INPUT SECTION
# Prompt the user to select a pizza size and validate the user's input
while True:
    pizza_choice = input("Please enter the number associated with your pizza size: ")
    if pizza_choice == "1":
        pizza = "Small"
        break
    elif pizza_choice == "2":
        pizza = "Medium"
        break
    elif pizza_choice == "3":
        pizza = "Large"
        break
    else:
        print("Invalid choice. Please try again.")

# Prompt the user to select quantity
while True:
    quantity = input("Please enter the quantity: ")
    if not quantity.isdigit() or int(quantity) < 1:
        print("Invalid quantity. Please enter a positive number.")
    else:
        quantity = int(quantity)
        break

# Prompt the user to select toppings
print("Please enter 1 if you want the topping and 0 if you do not.")

# Prompt and validate the user's input for each topping
toppings = ["Pepperoni", "Sausage", "Olives"]
selected_toppings = []
for topping in toppings:
    while True:
        choice = input(f"{topping}: ")
        if choice not in ["0", "1"]:
            print(
                "Invalid choice for topping. Please enter 1 if you want the topping and 0 if you do not."
            )
        else:
            if choice == "1":
                selected_toppings.append(topping)
            break
2
# PROCESSING SECTION
# Calculate the total price
item_price = pizza_prices[pizza] + sum(
    toppings_prices[topping] for topping in selected_toppings
)
total_price = quantity * item_price

# OUTPUT SECTION
# Display the order confirmation
print("Thank you for your order!")
print(
    f"Quantity: {quantity}  Item: {pizza} cheese pizza with {', '.join(selected_toppings) if selected_toppings else 'no toppings'} = ${item_price:.2f}"
)
print(f"Total: ${total_price:.2f}")
