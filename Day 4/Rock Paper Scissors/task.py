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
choices =[rock, paper, scissors]
computerchoice = (random.randint(0,2))
player_choice = (int(input("Choose 0 for rock, 1 for paper, 2 for scissors: ")))

if player_choice == 0 and computerchoice == 0:
    print(choices[player_choice])
    print(rock + "You Draw")
elif player_choice == 0 and computerchoice == 1:
    print(choices[player_choice])
    print(paper + "You lose")
elif player_choice == 0 and computerchoice == 2:
    print(choices[player_choice])
    print(scissors + "You win")
elif player_choice == 1 and computerchoice == 0:
    print(choices[player_choice])
    print(rock + "You win")
elif player_choice == 1 and computerchoice == 1:
    print(choices[player_choice])
    print(paper + "You Draw")
elif player_choice == 1 and computerchoice == 2:
    print(choices[player_choice])
    print(scissors + "You lose")
elif player_choice == 2 and computerchoice == 0:
    print(choices[player_choice])
    print(rock + "You lose")
elif player_choice == 2 and computerchoice == 1:
    print(choices[player_choice])
    print(paper + "You Win")
elif player_choice == 2 and computerchoice == 2:
    print(choices[player_choice])
    print(scissors + "You Draw")

