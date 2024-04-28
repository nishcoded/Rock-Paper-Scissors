import random

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
---'    ____)____
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

game_on = True
while game_on:
    game_options = [rock, paper, scissors]
    user_choice = int(input("What would you like to choose? Type 0 for rock, 1 for paper, or 2 for scissors: "))

    if user_choice >= 3 or user_choice <0:
        print("Its an invalid number. Type from 0 to 2.")

    else:
        print("You chose: ")
        print(game_options[user_choice])

        computer_choice = random.randint(0,2)
        print("Computer chose: ")
        print(game_options[computer_choice])

        if user_choice == 0 and computer_choice == 2:
            print("You win")
        elif user_choice == 2 and computer_choice ==0:
            print("You lose")
        elif user_choice > computer_choice:
            print("You win")
        elif user_choice < computer_choice:
            print("You lose")
        elif user_choice == computer_choice:
            print("Its a draw")

    play_again = input("Do you want to play again? Type Y/N? ")
    if play_again.upper() == "N":
        game_on = False
