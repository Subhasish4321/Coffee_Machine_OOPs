#the main program uses the attributes and methods of other clsses,refer to different classes for better understansing
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()


##Getting the order from the customer
menu=Menu()
is_on=True
while is_on:
    print(f"What would you like to have today? Here's the menu: {menu.get_items()}")
    choice=input()
    if choice=='off':
        is_on=False
    elif choice=='report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
        resource=coffee_maker.is_resource_sufficient(drink)
        if resource:
            print(f'The costs of your drink is {drink.cost}')
            bake_beans=money_machine.make_payment(drink.cost)
            if bake_beans==True:
                coffee_maker.make_coffee(drink)
        else:
            print("Sorry insufficient resources,Please fill the required ingredients.")
            print(coffee_maker.report())
            is_on=False





