import random

word_list = ["akshay", "sagar", "tejas", "gaurav"]
choosen_word = random.choice(word_list)
placeholder = ""
print(choosen_word)

for position in range(len(choosen_word)):
    placeholder += "_"
print(placeholder)
game_over = False
correct_letters = []
lives = 6
while not game_over:
    display = ""
    print(f"********************* {lives}/6 lives left ***********************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"you have already guessed {guess}")

    for var in choosen_word:
        if var == guess:
            display += var
            correct_letters.append(guess)
        elif var in correct_letters:
            display += var
        else:
            display += "_"
    print(display)

    if guess not in choosen_word:
        lives -= 1
        print(f"You guessed {guess}, thats not in the word. you loose a life.")
        if lives == 0:
            game_over = True
            print(f"You loose. {choosen_word} is the correct word.")

    if "_" not in display:
        game_over = True
        print("You win")
