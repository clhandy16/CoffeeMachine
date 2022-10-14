# TODO: 1. print report of all coffee machine resources
def runreport():
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print("Money: $" + str(resources["money"]))


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


# TODO: 2. prompt user for drink order
def check_menu(drink):
    drink_on_menu = False
    for item in MENU:
        if drink == item:
            drink_on_menu = True
            collect_coins()
            break
    if not drink_on_menu:
        new_drink = input("Sorry, we only serve espresso, latte or cappuccino. Which would you like?: ")
        check_menu(new_drink)


# TODO: 3. check if resources sufficient to make drink order

# got a start on building the logic for comparing ordered_drink dictionary to resources dictionary
# probably refactor input script to copy relevant drink dictionary from MENU dictionary before expanding
"""
print(MENU[drink]["ingredients"])

ingredients = MENU[drink]["ingredients"]
for item in ingredients:
  print(item + ": " + str(ingredients[item]))
"""

# TODO: 4. process payment

def collect_coins():
    q = float(input("Insert quarters: "))
    d = float(input("Insert dimes: "))
    n = float(input("Insert nickles: "))
    p = float(input("Insert pennies: "))
    count_coins(q, d, n, p)

def count_coins(quarters, dimes, nickles, pennies):
    resources["money"] += quarters * 0.25
    resources["money"] += dimes * 0.10
    resources["money"] += nickles * 0.05
    resources["money"] += pennies * 0.01

# TODO: 5. adjust resources before dispensing coffee

ordered_drink = input("What would you like? (espresso, latte, cappuccino): ")
check_menu(ordered_drink)
