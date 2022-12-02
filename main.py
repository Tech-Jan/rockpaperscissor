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

# Write your code below this line 👇

import random

yourchoice_error = ""
yourchoice = 0
enemy = random.randint(0, 2)
try:
    yourchoice = int(input("hey chose rock[0] paper[1] scissors[2] plz \n"))
except:
    yourchoice_error = "#error444"
    print(f"plz use the integer 0, 1 or 2 u fool {yourchoice_error}")
if yourchoice >= 0 and yourchoice <= 2 and yourchoice_error != "#error444":
    win_lose_matrix = [[1, 2, 0], [0, 1, 2], [2, 0, 1]]
    win_equal_lose = win_lose_matrix[yourchoice][enemy]
    hand_list = [rock, paper, scissors]
    print("yourhand:" + hand_list[yourchoice] + "\n--------------\n")
    # print(hand_list[yourchoice_hand_index ])
    print("enemiehand:" + hand_list[enemy])

    if win_equal_lose == 0:
        losemessage = "winna"
    elif win_equal_lose == 1:
        losemessage = "equal"
    elif win_equal_lose == 2:
        losemessage = "losa"
    print(losemessage)
else:
    print("wtfff input")
