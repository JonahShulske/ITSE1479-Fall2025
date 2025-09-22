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


# Problem 2 - Password Strength Checker
def check_password(password: str) -> str:
    special_char = " !#$%&'()*+,-./:;<=>?@[^_`{|}~"
    if len(password) <= 6 or str.isalpha(password):
        print("Password is weak")
    elif len(password) > 6 and not str.isalpha(password):
        print("Password is medium")
    elif len(password) > 6 and any(password in special_char):
        print("Password is strong")

if __name__ == "__main__":
    password = input("Enter a password: ")
    check_password(password)
