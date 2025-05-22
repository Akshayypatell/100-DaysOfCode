# Test Odd Even
"""
test = int(input("Enter number to check whether its Even or Odd?\n"))
if test % 2 == 0:
    print(f"Your entered digit {test} is Even number.")
else:
    print(f"Your Entered digit {test} is Odd number.")
"""
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

stage1 = input("You're at cross road. where do you want to go?\n     Type \"left\" or \"right\" \n").lower()

if stage1 == "left":
    print("You've come to a lake. There's island in the middle of the lake.")

    stage2 = input("  Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
    if stage2 == "wait":
        print("You've arrive at the island unharmed. There is house of 3 doors")

        stage3 = input("One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if stage3 == "yellow":
            print("You won")
        elif stage3 == "red":
            print("Burned by fire. Game Over")
        elif stage3 == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game over.")
    else:
        print("Attacked by trout. Game Over")
else:
    print("Fall into a hole. Game Over.")
