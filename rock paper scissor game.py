import random
    
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_image  = [rock , paper , scissor]
user_choice = int (input("what do you choose? type 0 for rock , 1 for paper and 2 for scissor\n"))
if user_choice >=0 and user_choice <=2:
    print(game_image[user_choice])
    
computer_choice = random.randint(0,2)
print(f"computer choice {computer_choice} : ")
print(game_image[computer_choice])

if user_choice >= 3 and user_choice < 0:
    print("your input is invalid. you lost!")

elif user_choice  == 0 and computer_choice == 2:
    print("you win!")
    
elif computer_choice == 0 and user_choice == 2:
    print("you lost!")
    
elif computer_choice > user_choice:
    print("you lost!")
    
elif user_choice > computer_choice:
    print("you win!")
    
elif user_choice == computer_choice:
    print("it's draw")
    