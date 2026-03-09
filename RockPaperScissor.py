import random


rock =   '''
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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
while True:
    game_images = [rock, paper, scissor]
    print("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors")
    user_choice = int(input())
    computer_choice = random.randint(0, 2)
                        
    if user_choice < 0 and user_choice > 2:
        print("Error: You need have to a number between 0 and 2!")
        ####
    if user_choice == 0 and computer_choice == 2:
        print(f"you won: {game_images[user_choice]}\nComputer lost: {game_images[computer_choice]}")
    elif user_choice == 2 and computer_choice == 0:
        print(f"you lose: {game_images[user_choice]}\nComputer won: {game_images[computer_choice]}")
    elif user_choice > computer_choice:
        print(f"you won: {game_images[user_choice]}\nComputer lost: {game_images[computer_choice]}")
    elif user_choice < computer_choice:
        print(f"you lose: {game_images[user_choice]}\nComputer won: {game_images[computer_choice]}")
    else:
        print(f"Its a tie, you both chose: {game_images[computer_choice]} ")
    

    play_again = input("Play again? (y/n): ")

    if play_again.lower() == "q":
        print("Thanks for playing!")
        break

    

#basic logic of problem
