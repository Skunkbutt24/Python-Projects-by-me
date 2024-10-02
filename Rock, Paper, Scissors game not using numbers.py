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
move_names = ["rock", "paper", "scissors"]
move_images = {"rock":rock, "paper":paper, "scissors":scissors}
score=0
total=0
print("Welcome to my Rock, Paper, Scissors game. Let's get started.")
while True:
    user_choice = input("What's your move? Type Rock, Paper, or Scissors:\n").lower()
    computer_choice = random.choice(move_names)
    while user_choice not in move_names:
        print("Invalid move. Try again.")
        user_choice = input("What's your move ?\nType Rock, Paper, or Scissors:\n").lower()
    print(f"Your move is {user_choice.capitalize()}:\n{move_images[user_choice]}")
    print(f"Computer's move is {computer_choice.capitalize()}:\n{move_images[computer_choice]}")
    if user_choice == computer_choice:
        print("It's a draw.")
        total+=1
        print(f"Your Score: {score}")
        print(f"Total Game: {total}")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        score+=1
        total+=1
        print(f"Your Score: {score}")
        print(f"Total Game: {total}")
    else:
        print("You lose!")
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
