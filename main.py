import menu
import coffee_maker
import money_machine

money_machine = money_machine.MoneyMachine()
coffee_maker = coffee_maker.CoffeeMaker()
menu = menu.Menu()

print("Welcome to the Coffee Machine!")
print("What would you like to choose? (espresso/latte/cappuccino/report/off)")

while True:
    choice = input(">").lower()
    if choice == "report":
        coffee_maker.report()
        money_machine.report()

    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = menu.find_drink(choice)
        enough_resources = coffee_maker.is_resource_sufficient(drink)
        if enough_resources:
            money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)

    elif choice == "off":
        break

    else:
        print("Sorry, we currently do not have that item. These are the availeble drinks: ")
        menu.get_items()

print("Thank you for using the Coffee Machine!")
