MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

def runreport():
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print("Money: $" + str(resources["money"]))

def check_menu(drink):
    for item in MENU:
        if drink == item:
            return MENU[item]
            break
        else:
            new_drink = input("Sorry, we only serve espresso, latte or cappuccino. Which would you like?: ")
            check_menu(new_drink)


# TODO: 3. check if resources sufficient to make drink order

# got a start on building the logic for comparing ordered_drink dictionary to resources dictionary
# probably refactor input script to copy relevant drink dictionary from MENU dictionary before expanding

def check_resources(ingredients):
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

# TODO: 4. process payment

def process_coins():
    print("Please insert coins.")
    total = float(input("Insert quarters: ")) * 0.25
    total += float(input("Insert dimes: ")) * 0.10
    total += float(input("Insert nickles: ")) * 0.05
    total += float(input("Insert pennies: ")) * 0.01
    return total


def is_payment_sufficient(pmt, drink_cost):
    if pmt >= drink_cost:
        change = round(pmt - drink_cost, 2)
        resources["money"] += round(drink_cost, 2)
        print(f"Thank you! Your change is ${change}.")
        return True
    else:
        print("Sorry, insufficient funds. Refunding payment.")
        return False


def make_coffee(drink_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}! Enjoy!")

is_on = True

while is_on:
    ordered_drink = input("What would you like? (espresso, latte, cappuccino): ")
    if ordered_drink == "off":
        print("The coffee machine has been turned off.")
        is_on = False
    elif ordered_drink == "report":
        runreport()
    else:
        drink_info = MENU[ordered_drink]
        if check_resources(drink_info["ingredients"]):
            payment = process_coins()
            if is_payment_sufficient(payment, drink_info["cost"]):
                make_coffee(ordered_drink, drink_info["ingredients"])
