from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()

money_machine.report()
coffee_maker.report()
is_on=True
menu=Menu()
while is_on:
    # input=input("What would you like? (espresso/latte/cappuccino/):")
    options=menu.get_items()
    choice=input(f"what would you like ?({options}):")
    # coffee_maker.is_resource_sufficient(items)
    if choice=="off":
        is_on=False
    elif choice=="report":
        money_machine.report()
        coffee_maker.report()
    else:
        finddrink=menu.find_drink(choice)
        # print(finddrink.ingredients)
        if coffee_maker.is_resource_sufficient(finddrink) and money_machine.make_payment(finddrink.cost):
                coffee_maker.make_coffee(finddrink)








