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

#Write your code below this line 👇
choice = input('What do you chose? Type 0 for rock, 1 for paper or 2 for scissors.\n')
if int(choice) > 2 or int(choice) <0:
    print("Invalid input, you lose.")
else:
    choice = int(choice)
    comp_choice = random.randint(0,2)
    art = [rock, paper,scissors]
    print(art[choice])
    print(f"Computer chose:\n{art[comp_choice]}")
    if choice == 0 and comp_choice == 2:
        print('You win.')
    elif choice == 1 and comp_choice == 0:
        print('You win.')
    elif choice == 2 and comp_choice == 1:
        print('You win.')
    elif choice == comp_choice:
        print("Tie. Try again.")


    else:
        print("You lose.")

