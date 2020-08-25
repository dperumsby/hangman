import random

guesses = set()


def get_word():
    with open("words.txt", "r") as file:
        words = file.read().splitlines()
    return random.choice(words)


def make_hidden_word(word):
    hidden_word = ""
    
    for letter in word:
        if letter in guesses:
            hidden_word += letter
        else:
            hidden_word += "_"

    return hidden_word


def play_again():
    while True:
        user_choice = input("\nWould you like to play again? (y/n) ")

        if user_choice == "y":
            guesses.clear()
            return True
        elif user_choice == "n":
            return False
        else:
            print("\nSorry, I didn't quite get that. Please try again.")


def print_ascii_art(number):
    return print(f"{ascii_art[number]}")


def number_incorrect_guesses(word):
    counter = 0
    
    for guess in guesses:
        if guess not in word:
            counter += 1
    
    return counter


def main():
    while True:
        print(introduction)
        cpu_word = get_word()
        print_ascii_art(number_incorrect_guesses(cpu_word))
        print(make_hidden_word(cpu_word))
        guess = input("\nI've picked a word! What is your first guess? ")
        guesses.add(guess)
        print_ascii_art(number_incorrect_guesses(cpu_word))
        print(f"\n{make_hidden_word(cpu_word)}")

        while make_hidden_word(cpu_word) != cpu_word and number_incorrect_guesses(cpu_word) != 6:
            guess = input("\nWhat is your next guess? ")
            guesses.add(guess)
            print_ascii_art(number_incorrect_guesses(cpu_word))
            print(f"\n{make_hidden_word(cpu_word)}")

        if make_hidden_word(cpu_word) == cpu_word:
            print(winner)
    
        else:
            print(loser.format(cpu_word))

        if not play_again():
            break


introduction = """
Welcome to my Hangman game!
I'm going to pick a word and then you have to guess a letter that it might contain.
If you get it right I will add the letter to the board, so you can start to see what the word might be.
Be wary though! You only have 6 incorrect guesses before the hangman's noose pulls tight!
"""

winner = """
Congratulations! You won and will live to see another day!
...Now get out of here before I change my mind!
"""

loser = """
Uh oh! That's 6 incorrect guesses!
The word you were looking for was '{}'. Not that it means much now...
Well this is the end for you. Goodbye!
"""

ascii_art = [
 """
  /===|||
 ||    |
 ||    
 ||   
 ||   
 ||
/==\\
""",

 """
  /===|||
 ||    |
 ||    0
 ||   
 ||   
 ||
/==\\
""",

 """
  /===|||
 ||    |
 ||    0
 ||    |
 ||   
 ||
/==\\
""",

 """
  /===|||
 ||    |
 ||    0
 ||   /|
 ||   
 ||
/==\\
""",

 """
  /===|||
 ||    |
 ||    0
 ||   /|\\
 ||   
 ||
/==\\
""",

 """
  /===|||
 ||    |
 ||    0
 ||   /|\\
 ||   /
 ||
/==\\
""",

 """
  /===|||
 ||    |
 ||    0
 ||   /|\\
 ||   / \\
 ||
/==\\
"""
]

main()
