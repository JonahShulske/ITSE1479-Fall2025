import string
import random

"""
Jonah Shulske
September 22, 2025
ITSE-1479 Fall 2025
"""

"""
# Problem 1 - Vowel Counter
def count_vowels(word: str) -> int:
    vowel = "aeiouAEIOU"
    vowel_count = 0

    for char in word:
        if char in vowel:
            vowel_count += 1
    return vowel_count

if __name__ == "__main__":

    word = input("Enter a word: ")
    
    print("There are", count_vowels(word), f"vowels in the word \"{word}\"")
"""

"""
# Problem 2 - Password Strength Checker
def any_special_char(password : str):
    return any(char in string.punctuation for char in password)

def check_password(password: str):
    if len(password) <= 6 or str.isalpha(password):
        print("Password is weak")
    elif len(password) > 6 and any(char.isdigit() for char in password) and not any_special_char(password):
        print("Password is medium")
    elif len(password) > 6 and any_special_char(password):
        print("Password is strong")

if __name__ == "__main__":
    password = input("Enter a password: ")
    check_password(password)
"""

# Problem 3 - Word Guesser
def choose_word() -> str:
    secret_word = ["monty", "computer", "python", "glossary", "homework", "clock", "calendar"]
    word = random.choice(secret_word)
    return word

def display_progress(secret_word: str, guessed_letters: list[str]) -> str:
    display = ""

    for char in secret_word:
        if char in guessed_letters:
            display+= char
        else:
            display += "_"

        display += " "

    return display.strip()

def play_game():
    secret_word = choose_word()
    guessed_letters = []

    progress = display_progress(secret_word, guessed_letters)
    print(progress)

if __name__ == "__main__":
    play_game()