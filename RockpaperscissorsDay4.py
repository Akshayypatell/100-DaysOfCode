import random
'''
random_integer = random.randint(1,10)
print(random_integer)

# select any one from list
friends = ["Sag", "Tej", "Gau", "Jay"]

# option1
random_integer = random.randint(0,4)
print(friends[random_integer])

# option2
print(random.choice(friends))
'''

# Rock paper scissor
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissor.\n"))
random_val = random.randint(0, 2)
choose=["Rock", "Paper", "Scissor"]
print(f"You have selected {choose[user_input]}.\nComputer has chosen {choose[random_val]}.")
if user_input == random_val:
    print("Draw")
elif user_input == 0 and random_val == 1 or user_input == 1 and random_val == 2 or user_input == 2 and random_val == 0:
    print("Computer Won")
elif user_input == 0 and random_val == 2 or user_input == 1 and random_val == 0 or user_input == 2 and random_val == 1:
    print("You won")
'''
user_input+computer_response
01 #rock and paper # paper-----------------
02 #rock and scissor #rock
10 #paper and rock # paper
12 #paper and scissor # scissor ---------------
20 #scissor and rock # rock-----------------
21 #scissor and paper # scissor
------------- = Computer won
'''
