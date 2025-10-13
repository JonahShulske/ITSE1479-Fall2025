"""
Jonah Shulske
October 8, 2025
ITSE-1479 Fall 2025
"""

if name == "main":
    # Problem 1 - Word Length Filter
    sentence = input("Input a sentence: ")

    split_sen  = sentence.split()
    print(split_sen)

    for word in split_sen:
        if len(word) < 4:
            print(f"{word} is less than 4 chars")
        elif len(word) < 6:
            print(f"{word} is less than 6 chars but bigger than 4")
        else:
            print(f"{word} is bigger than 6")