import string
import random

"""
Jonah Shulske
September 22 - September 25, 2025
ITSE-1479 Fall 2025
"""

# Problem 1 - Vowel Counter
def count_vowels(word: str) -> int:
    vowel = "aeiouAEIOU"    #
    vowel_count = 0

    for char in word:
        if char in vowel:
            vowel_count += 1
    return vowel_count

if __name__ == "__main__":

    word = input("Enter a word: ")
    if not word.isalpha():
        print("Error: Words don't have numbers and/or special characters")
        word = ""
    elif len(word) < 1:
        print("Error: Words must be at least 1 character long")
        word = ""

    if len(word) > 0:
        print("There are", count_vowels(word), f"vowels in the word \"{word}\"")


print("")

# Problem 2 - Password Strength Checker
#:param password is the string that the user will enter
#:return the characters entered by the users that will be sent to check_password
def any_special_char(password : str):
    return any(char in string.punctuation for char in password)

def check_password(password: str):
    if len(password) < 6 or str.isalpha(password):
        print("Password is weak")
    elif (len(password) > 6 and any(char.isalpha() for char in password)
          and any(char.isdigit() for char in password) and not any_special_char(password)):
        print("Password is medium")
    elif (len(password) > 6 and any(char.isalpha() for char in password)
          and any(char.isdigit() for char in password) and any_special_char(password)):
        print("Password is strong")

if __name__ == "__main__":
    password = input("Enter a password: ")
    check_password(password)

# Problem 3 - Word Guesser
#return: The random word that's chosen from choose_word
def choose_word() -> str:
    secret_word = ["monty", "computer", "python", "glossary", "homework", "clock", "calendar", "kronos", "recursion"]
    word = random.choice(secret_word)
    return word

#return: Just making sure there isn't extra garbage visible to the user
def display_progress(secret_word: str, guessed_letters: list[str]) -> str:
    display = ""

    for char in secret_word:
        if char in guessed_letters:
            display += char
        else:
            display += "_"

        display += " "

    return display.strip()


def play_game():
    secret_word = choose_word()
    guessed_letters = []
    max_attempts = 6
    wrong_attempts = 0

    # Actual game running here as long as the player has less than 6 wrong attempts
    while wrong_attempts < max_attempts:
        print("\nWord:", display_progress(secret_word, guessed_letters))
        print(f"Attempts remaining: {max_attempts - wrong_attempts}")
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

        guess = input("Guess a letter: ").lower()

        # Check for errors: No entry, more than 1 entry, non-letters, and already guessed letters
        if len(guess) < 1:
            print("Error: Enter a letter")
            continue
        elif len(guess) > 1:
            print("Error: Enter only one letter")
            continue
        elif not guess.isalpha():
            print("Error: Guess must be a letter")
            continue
        elif guess in guessed_letters:
            print("Error: Letter already guessed")
            continue

        # Add to wrong attempts if user entered wrong char
        if guess not in secret_word:
            wrong_attempts += 1

        guessed_letters.append(guess)

        # Winning and losing screens
        if all(char in guessed_letters for char in secret_word):
            print("\nYou Won!")
            print(f"The secret word was: {secret_word}")
            exit()
        elif wrong_attempts >= max_attempts:
            print("\nGame Over")
            print(f"The secret word was: {secret_word}")
            exit()

    progress = display_progress(secret_word, guessed_letters)
    print(progress)


if __name__ == "__main__":
    play_game()