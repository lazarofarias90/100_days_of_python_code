import menu

profit = 0

def is_resource_sufficient(order_ingredients):
    """Returns True when the order can be placed, False if the ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > menu.resources[item]:
            print(f"Sorry there is not enough {item}.") 
            return False
    return True

def process_coins():
    """Returns the total value calculated from the entered currencies."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Returns True if the payment is accepted, or False if the money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Subtract the necessary ingredients from the resources and deliver the drink."""
    for item in order_ingredients:
        menu.resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

turn_on = True

while turn_on:
    user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    if user_order == "off":
        turn_on = False
    elif user_order == "report":
        print(f"Water: {menu.resources['water']}ml")
        print(f"Milk: {menu.resources['milk']}ml")
        print(f"Coffee: {menu.resources['coffee']}g")
        print(f"Money: ${profit}")
    elif user_order in menu.MENU:
        drink = menu.MENU[user_order]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_order, drink["ingredients"])
    else:
        print("Invalid selection. Please choose espresso, latte, or cappuccino.")