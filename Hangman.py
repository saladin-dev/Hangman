import string
import random
import os

correctguess = 0


def man(numguess):
    if numguess == 6:
        print("You lose!")


def hangman_stage_0():
    print("   _____  ")
    print("  |     | ")
    print("        | ")
    print("        | ")
    print("        | ")
    print("        | ")
    print(" _______| ")


def hangman_stage_1():
    print("   _____  ")
    print("  |     | ")
    print("  O     | ")
    print("        | ")
    print("        | ")
    print("        | ")
    print(" _______| ") 


def hangman_stage_2():
    print("   _____  ")
    print("  |     | ")
    print("  O     | ")
    print("  |     | ")
    print("        | ")
    print("        | ")
    print(" _______| ")


def hangman_stage_3():
    print("   _____  ")
    print("  |     | ")
    print("  O     | ")
    print(" /|     | ")
    print("        | ")
    print("        | ")
    print(" _______| ")


def hangman_stage_4():
    print("   _____  ")
    print("  |     | ")
    print("  O     | ")
    print(" /|\    | ")
    print("        | ")
    print("        | ")
    print(" _______| ")


def hangman_stage_5():
    print("   _____  ")
    print("  |     | ")
    print("  O     | ")
    print(" /|\    | ")
    print(" /      | ")
    print("        | ")
    print(" _______| ")


def hangman_stage_6():
    print("   _____  ")
    print("  |     | ")
    print("  O     | ")
    print(" /|\    | ")
    print(" / \    | ")
    print("        | ")
    print(" _______| ")

inputHistory = ""

# List of words for the game
words = ("apple", "orange", "banana", "coconut", "pineapple")
hints = ("red fruit", "organe fruit", "yellow fruit", "hairy fruit", "pizza?")


# Select a random word
word = random.choice(words)
# Get the corresponding hint
hint_index = words.index(word)
current_hint = hints[hint_index]



# Create the hint (# of underscores)
hint = ["_"] * len(word)
lettercount = len(word)



# Number of incorrect guesses
wrong_guesses = 0


# Set to track guessed letters
guessed_letters = set()

#Correct guesses



import os # Make sure os is imported at the top of your script

continueCode = input(
    r"""********************************************************************************
*                                                                                      *
*  ___  ___  ________  ________   ________  _____ ______   ________  ________          *
* |\  \|\  \|\   __  \|\   ___  \|\   ____\|\   _ \  _   \|\   __  \|\   ___  \        *
* \ \  \\\  \ \  \|\  \ \  \\ \  \ \  \___|\ \  \\\__\ \  \ \  \|\  \ \  \\ \  \       *
*  \ \   __  \ \   __  \ \  \\ \  \ \  \  __\ \  \\|__| \  \ \   __  \ \  \\ \  \      *
*   \ \  \ \  \ \  \ \  \ \  \\ \  \ \  \|\  \ \  \    \ \  \ \  \ \  \ \  \\ \  \     *
*    \ \__\ \__\ \__\ \__\ \__\\ \__\ \_______\ \__\    \ \__\ \__\ \__\ \__\\ \__\    *
*     \|__|\|__|\|__|\|__|\|__| \|__|\|_______|\|__|     \|__|\|__|\|__|\|__| \|__|    *
*                                                                                      *
*                                                                                      *
*                        Press [ENTER] to continue...                                  *
*                                                                                      *
****************************************************************************************
"""
)
os.system('cls' if os.name == 'nt' else 'clear')





# Start the game loop

while wrong_guesses < 6:
    
    if bool(correctguess<lettercount) == False:
        print("Congrats you won! 🏆") 
        x = input("Press 1 to play again or 2 to exit: ")
        print("\n")
        break


    print(hint)
    print("🔍Type 'hint' to get a clue or enter a letter to guess")
    userinput = input("Enter a letter: ").lower()
    
    if userinput == "hint":
        print("HINT: ", current_hint)
        continue
        
    inputHistory = inputHistory + " " + userinput
    print (inputHistory)  

    for x in range(0, len(word)):
        if userinput == word[x]:
            hint[x] = userinput
            correctguess += 1
            print("Correct! ✅")


    if userinput not in word:
        wrong_guesses += 1
        if wrong_guesses == 0:
            hangman_stage_0()
        elif wrong_guesses == 1:
            hangman_stage_1()
            print("❌ Incorrect Guess 5 guesses left! You've guessed these so far", "\n", inputHistory)
        elif wrong_guesses == 2:
            hangman_stage_2()
            print("❌ Incorrect Guess 4 guesses left! You've guessed these so far", "\n", inputHistory)
        elif wrong_guesses == 3:
            hangman_stage_3()
            print("❌ Incorrect Guess 3 guesses left! You've guessed these so far", "\n", inputHistory)
        elif wrong_guesses == 4:
            hangman_stage_4()
            print("❌ Incorrect Guess 2 guesses left! You've guessed these so far", "\n", inputHistory)
        elif wrong_guesses == 5:
            hangman_stage_5()
            print("❌ Incorrect Guess 1 guesses left! You've guessed these so far", "\n", inputHistory)
        elif wrong_guesses == 6:
            hangman_stage_6()
            print("❌ 0 guesses left, you lose 😂")
            print("The word was:",words [x])
     