logo='''
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
    },
    "americano": {  # New menu item
        "ingredients": {
            "water": 300,
            "coffee": 18,
        },
        "cost": 2.0,
    },
    "mocha": {  # New menu item
        "ingredients": {
            "water": 200,
            "milk": 100,
            "coffee": 24,
            "chocolate": 20,  # Additional ingredient
        },
        "cost": 3.5,
    },
    "macchiato": {  # New menu item
        "ingredients": {
            "water": 50,
            "milk": 150,
            "coffee": 18,
        },
        "cost": 2.8,
    },
    "flat white": {  # New menu item
        "ingredients": {
            "water": 150,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 3.2,
    },
    "iced coffee": {  # New menu item
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "ice": 100,  # Additional ingredient
        },
        "cost": 2.5,
    },
    "frappuccino": {  # New menu item
        "ingredients": {
            "milk": 150,
            "coffee": 24,
            "ice": 150,
            "whipped_cream": 50,  # Additional ingredient
        },
        "cost": 4.0,
    },
    "irish coffee": {  # New menu item
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "whiskey": 50,  # Additional ingredient
        },
        "cost": 5.0,
    }
}

resources = {
    "water": 900,
    "milk": 600,
    "coffee": 300,
    "chocolate": 100,  # Added resource for Mocha
    "ice": 500,  # Added resource for iced coffee and frappuccino
    "whipped_cream": 200,  # Added resource for frappuccino
    "whiskey": 100  # Added resource for Irish coffee
}
saved_money=0
print(logo)
print("Welcome to my coffee machine. Let's get started.")
while True:
    print("Operations: ")
    input_choice = int(input("1. Report\n2. Buy items\n3. Turn off machine\n4. Refill ingredients\n5. Pull out money\n\nChoose between these: "))
    while input_choice not in [1,2,3,4,5]:
        input_choice=int(input("Invalid selection. Try again.\n1. Report\n2. Buy items\n3. Turn off machine\n4. Refill ingredients\n5. Pull out money\n\nChoose between these: "))
    if input_choice==1:
        print("\n"*30)
        print("Here is the report: ")
        print(f"1.Water: {resources['water']}ml.")
        print(f"2.Milk: {resources['milk']}ml.")
        print(f"3.Coffee: {resources['coffee']}ml.")
        print(f"4.Chocolate: {resources['chocolate']}g.")
        print(f"5.Ice: {resources['ice']}g.")
        print(f"6.Whipped cream: {resources['whipped_cream']}g.")
        print(f"7.Whiskey: {resources['whiskey']}ml.")
        print(f"8.Total money: {saved_money}$")
    elif input_choice==2:
        print("\n"*30)
        print("Here is the menu: ")
        n=1
        menu_options=list(menus.keys())
        for menu in menu_options:
            print(f"{n}. {menu.capitalize()}: {menus[menu]['cost']}$")
            n+=1
        input_item=int(input("Which item do you want to buy ?\n"))
        while input_item not in range(1,len(menu_options)+1):
            input_item=int(input("Invalid selection. Try again.\nWhich item do you want to buy ?\n"))
        selected_drink=menu_options[input_item-1]
        for ingredients, amount in menus[selected_drink]['ingredients'].items():
           if resources[ingredients]<amount:
               print("Sorry, Not enough resources available. Try again later.")
               break
           else:
               total_inserted=0
               while True:
                   print(f"Selected Item: {selected_drink.capitalize()}\nCost: {menus[selected_drink]['cost']}$")
                   print("Please insert coins: ")
                   quarters=int(input("Quarters: "))*0.25
                   dimes=int(input("Dimes: "))*0.10
                   nickels=int(input("Nickels: "))*0.05
                   pennies=int(input("Pennies: "))*0.01
                   total_inserted+=quarters+dimes+nickels+pennies
                   if total_inserted<menus[selected_drink]['cost']:
                       remaining_amount=(menus[selected_drink]['cost']-total_inserted)
                       action=int(input(f"Not enough money.\nRemaining amount {remaining_amount:.2f}$\nPress 1 to add money or 2 to get refund: "))
                       if action==1:
                           continue
                       elif action==2:
                           print(f"Refunding {total_inserted:.2f}$\nThanks for using my coffee machine. Bye !!!!")
                       else:
                           print("Invalid selection. Try again.")
                           continue
                   else:
                       change=total_inserted-menus[selected_drink]['cost']
                       print(f"Here is {change:.2f}$")
                       saved_money+=menus[selected_drink]['cost']
                       for ingredient, amount in menus[selected_drink]['ingredients'].items():
                           resources[ingredient]-=amount
                       print(f"Here is your {selected_drink.capitalize()}. Enjoy !!!!")
                   break
           break 
        break
    elif input_choice==3:
        turn_off=input("Are you sure you want to turn off machine ?\n").lower()
        if turn_off=="yes":
            break
    elif input_choice==4:
        resources['water'] += int(input("Refill water (ml): "))
        resources['milk'] += int(input("Refill milk (ml): "))
        resources['coffee'] += int(input("Refill coffee (g): "))
        resources['chocolate'] += int(input("Refill chocolate (g): "))
        resources['ice'] += int(input("Refill ice (g): "))
        resources['whipped_cream'] += int(input("Refill whipped cream (g): "))
        resources['whiskey'] += int(input("Refill whiskey (ml): "))
        print("Ingredients refilled.")
    elif input_choice == 5:
        password = input("Enter the password: ")
        while password != "Liman_123":
            password = input("Wrong password. Try again.\nEnter the password: ")
        if password == "Liman_123":
            print(f"All money has been pulled out. Balance empty now.")
            saved_money = 0
    else:
        print("Invalid choice. Please try again.")
        continue
    input("Enter any button to continue: ")
    print("\n"*30)
          
                       
                       
        