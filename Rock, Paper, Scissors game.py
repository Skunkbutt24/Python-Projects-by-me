logo = '''
██████████████████████████
█▄─▄▄▀█─▄▄─█─▄▄▄─█▄─█─▄███
██─▄─▄█─██─█─███▀██─▄▀████
▀▄▄▀▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀
█████████████████████████████████
█▄─▄▄─██▀▄─██▄─▄▄─█▄─▄▄─█▄─▄▄▀███
██─▄▄▄██─▀─███─▄▄▄██─▄█▀██─▄─▄███
▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀
██████████████████████████████████████████████
█─▄▄▄▄█─▄▄▄─█▄─▄█─▄▄▄▄█─▄▄▄▄█─▄▄─█▄─▄▄▀█─▄▄▄▄█
█▄▄▄▄─█─███▀██─██▄▄▄▄─█▄▄▄▄─█─██─██─▄─▄█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
'''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
print(logo)
move_images = [rock, paper, scissors]
move_names = ["Rock", "Paper", "Scissors"]
score=0
total=0
print("Welcome to my Rock, Paper, Scissors game. Let's get started.")
while True:
    user_choice = int(input("Type 1 for Rock, Type 2 for Paper, Type 3 for Scissors:\n"))
    while user_choice < 1 or user_choice > 3:
        print("Invalid Number. Try again.")
        user_choice = int(input("Type 1 for Rock, Type 2 for Paper, Type 3 for Scissors:\n"))
    computer_choice = random.randint(1, 3)
    print(f"Your move is {move_names[user_choice - 1]}:\n{move_images[user_choice - 1]}")
    print(f"Computer's move is {move_names[computer_choice - 1]}:\n{move_images[computer_choice - 1]}")
    if user_choice == computer_choice:
        print("It's a Draw.")
        total+=1
        print(f"Your Score: {score}")
        print(f"Total Game: {total}")
    elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
        print("You Win!")
        score+=1
        total+=1
        print(f"Your Score: {score}")
        print(f"Total Game: {total}")       
    else:
        print("You Lose!")
        total+=1
        print(f"Your Score: {score}")
        print(f"Total Game: {total}")
    continue_game=input("Press Enter to continue: \n")
    if continue_game=="":
        continue
    else:
        break
print(f"Your Score: {score}\nTotal game: {total}")
print("Thanks for using my program. Bye !!!!!!")

