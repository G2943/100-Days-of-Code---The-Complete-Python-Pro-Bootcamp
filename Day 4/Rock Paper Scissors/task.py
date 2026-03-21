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

user_choice = input("Enter your choice: 1 for Rock, 2 for Paper, 3 for Scissors \n")

comp_choice = random.randint(1, 3)

if(user_choice == 1 and comp_choice == 1):
    print("Match Tie!")
elif(user_choice == 1 and comp_choice == 2):
    print("Computer Wins!")
elif(user_choice == 1 and comp_choice == 3):
    print("You win!")
elif(user_choice == 2 and comp_choice == 1):
    print("You Win!")
elif(user_choice == 2 and comp_choice == 2):
    print("will write afterward!")