from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

CoffeeMaker.report()
MoneyMachine.report()

is_on=True

while is_on:
    options=menu.get_items()
    choice=input(f"what would you like ?")

