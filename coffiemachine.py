from cofeedata import MENU, resources
from copy import deepcopy

turn_on = True



def get_report(resources):
    """Get the report of the resources available"""
    for keys, values in resources.items():
        print(f"{keys}: {values}")

def check_resources(user_choice):
    """Check if resources to make the drinks are available"""
    check = deepcopy(MENU)
    for num in check[user_choice]['ingredient'].values():
        pass
    







while turn_on:
    user_choice = input("What Would You like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'off':
        turn_on = False
    elif user_choice == 'report':
        get_report(resources)
    elif user_choice not in ["espresso","latte", "cappuccino"]:
        print("Enter a Valid Drink")

    check_resources(user_choice)
