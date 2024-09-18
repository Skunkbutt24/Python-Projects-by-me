logo = '''
________._________
|      | \   -   /
|  ||  |  \  -  /
|  ||  |___\___/
|  ||  |     X
|      |    ___
|      |   / - \
|______|  /  -  \
| ____ | /_______\
||7:30||__________
||____|           |
|_________________|
'''

menus = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.50},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.50},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.00},
    "americano": {"ingredients": {"water": 300, "coffee": 18}, "cost": 2.00},
    "mocha": {"ingredients": {"water": 200, "milk": 100, "coffee": 24, "chocolate": 20}, "cost": 3.50},
    "macchiato": {"ingredients": {"water": 50, "milk": 150, "coffee": 18}, "cost": 2.80},
    "flat white": {"ingredients": {"water": 150, "milk": 150, "coffee": 24}, "cost": 3.20},
    "iced coffee": {"ingredients": {"water": 200, "coffee": 24, "ice": 100}, "cost": 2.50},
    "frappuccino": {"ingredients": {"milk": 150, "coffee": 24, "ice": 150, "whipped_cream": 50}, "cost": 4.00},
    "irish coffee": {"ingredients": {"water": 200, "coffee": 24, "whiskey": 50}, "cost": 5.00}
}

resources = {
    "water": 2900,
    "milk": 600,
    "coffee": 300,
    "chocolate": 100,
    "ice": 500,
    "whipped_cream": 200,
    "whiskey": 100
}
import sys
saved_money=0
total_cost=0
selected_items=[]
selected_items_cost=[]
item_sold=0
star='✪'
bullet='⚪'
print(logo)
print("Welcome to my Coffee Machine. Let's get started.")
while True:
    operation_choice=int(input("Operations:\n=======================\n1. Report\n2. Buy items\n3. Turn off machine\n4. Refill ingredients\n5. Pull out money\nChoose between these: \n"))
    while operation_choice not in range(1,6):
        print("\n"*30)
        operation_choice=int(input("Invalid selection. Try again.\nOperations:\n=======================\n1. Report\n2. Buy items\n3. Turn off machine\n4. Refill ingredients\n5. Withdraw money\nChoose between these: \n"))
    if operation_choice==1:
        print("Here is the report: \n=======================\n")
        print(f"\n{star} Resources available: \n")
        print(f"{bullet} Water: {resources['water']}ml.")
        print(f"{bullet} Milk: {resources['milk']}ml.")
        print(f"{bullet} Coffee: {resources['coffee']}ml.")
        print(f"{bullet} Chocolate: {resources['chocolate']}g.")
        print(f"{bullet} Ice: {resources['ice']}g.")
        print(f"{bullet} Whipped cream: {resources['whipped_cream']}g.")
        print(f"{bullet} Whiskey: {resources['whiskey']}ml.\n")
        print(f"{star} Balance: \n")
        print(f"{bullet} Total Balance: {saved_money}$\n")
        print(f"{star} Item sold: \n")
        print(f"{bullet} Total items sold: {item_sold}.\n")
    elif operation_choice==2:
        while True: 
            print("\n"*30)
            print(f"{star} Here is the Menu: \n=======================\n")
            n=1
            menu_list=list(menus.keys())
            for menu in menu_list:
                print(f"{bullet} {n}. {menu.capitalize()}: {menus[menu]['cost']:.2f}$")
                n+=1
            selected_item_no=int(input("\nWhich item do you want to buy ?\n"))
            while selected_item_no not in range(1,len(menu_list)+1):
                print("\n"*30)
                selected_item_no=int(input("\nInvalid selection. Try again.\nWhich item do you want to buy ?\n"))
            selected_item_name=menu_list[selected_item_no-1]
            resources_available=True
            for ingredient, amount in menus[selected_item_name]['ingredients'].items():
                if resources[ingredient]<amount:
                    print("Sorry, not enough resources available. Try again later.\n")
                    resources_available=False
                    break
            if resources_available:
                for ingredient, amount in menus[selected_item_name]['ingredients'].items():
                    resources[ingredient]-=amount
                selected_items.append(selected_item_name)
                selected_items_cost.append(menus[selected_item_name]['cost'])

                print(f"{selected_item_name.capitalize()} added to your cart for {menus[selected_item_name]['cost']}$\n")
            add_items=input("Do you want to add more items ?\n").lower()
            while add_items not in ["yes","no"]:
                add_items=input("\nInvalid input. Try again.\nDo you want to add more items ?\n").lower()
            if add_items =="yes":
                continue
            elif add_items=="no":
                print("\n"*30)
                print(f"{star} Here is your cart summary:\n")
                n=1
                for item_name,item_price in zip(selected_items,selected_items_cost):
                    print(f"{bullet} {n}. {item_name.capitalize()}: {item_price:.2f}$")
                    n+=1
                    total_cost+=item_price
                    item_sold+=1
                print(f"\n{star} Total amount to pay: {total_cost:.2f}$")
                while True:
                    total_inserted=0
                    print(f"\n{star} Please insert money: \n")
                    bill=int(input(f"{bullet}Bill: "))*1
                    quarters=int(input(f"{bullet}Quarters: "))*0.25
                    dimes=int(input(f"{bullet}Dimes: "))*0.10
                    nickels=int(input(f"{bullet}Nickels: "))*0.05
                    pennies=int(input(f"{bullet}Pennies: "))*0.01
                    total_inserted+=bill+quarters+dimes+nickels+pennies
                    print("\n"*30)
                    if total_inserted<total_cost:
                        remaining_amount=total_cost-total_inserted
                        action=int(input(f"\nNot enough money. Remaining amount {remaining_amount:.2f}$\n{bullet} Press 1 to add money.\n{bullet} Press 2 to get refund.\n"))
                        while action not in [1,2]:
                            action=int(input("\nInvalid input. Try again.\nRemaining amount {remaining_amount:.2f}$\n{bullet} Press 1 to add money.\n{bullet} Press 2 to get refund.\n"))
                        if action==1:
                            continue
                        elif action==2:
                            print(f"\nRefunding {total_inserted:.2f}$\n")
                            selected_items.clear()
                            selected_items_cost.clear()
                            total_cost=0
                            break
                    else:
                        change=total_inserted-total_cost
                        print(f"{star} Transaction successful. Here is your change: {change:.2f}$\nEnjoy your drinks !!!")
                        saved_money+=total_cost
                        selected_items.clear()
                        selected_items_cost.clear()
                        break
            break
        
    elif operation_choice==3:
        turn_off = input("Are you sure you want to turn off machine? (yes/no)\n").lower()
        if turn_off == "yes":
            print("Turning off machine.")
            break
    elif operation_choice == 4:
        print(f"{star} Refill items:\n ")
        resources['water'] += int(input(f"{bullet}Refill water (ml): "))
        resources['milk'] += int(input(f"{bullet}Refill milk (ml): "))
        resources['coffee'] += int(input(f"{bullet}Refill coffee (g): "))
        resources['chocolate'] += int(input(f"{bullet}Refill chocolate (g): "))
        resources['ice'] += int(input(f"{bullet}Refill ice (g): "))
        resources['whipped_cream'] += int(input("Refill whipped cream (g): "))
        resources['whiskey'] += int(input(f"{bullet}Refill whiskey (ml): "))
        print(f"\n{star}Ingredients refilled.\n")
    elif operation_choice == 5:
        print(f"{star} Withdraw Cash: \n")
        password = input(f"{bullet} Enter the password: \n")
        while password != "Limaniphone15_12_24":
            password = input(f"\nWrong password. Try again.\n{bullet}Enter the password: ")
        print(f"{star}All money has been withdrawn. Balance empty now.\n")
        saved_money = 0

    yes_no=input('Type "Yes" to continue or "No" to exit:\n').lower()
    if yes_no=="yes":
        selected_items.clear()
        selected_items_cost.clear()
    else:
        break
    print("\n" * 30)
print("Thanks for using my program. Bye !!!")
                              
            
                
        
                
