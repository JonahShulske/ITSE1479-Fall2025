"""
Jonah Shulske
October 23, 2025
ITSE-1479 Fall 2025
"""

import string
# Problem 3 - Word Frequency By Length
def get_unique_words(filename: str):
    word_data = {}
    translator = str.maketrans("", "", string.punctuation)
    with open(filename, "r") as file:
        for line in file:
            for word in line.lower().translate(translator).split():
                word = word.strip()
                if not word:
                    continue
                length = len(word)

                if length not in word_data:
                    word_data[length] = {
                        "unique_words": set(),
                        "counts": {}
                    }

                word_data[length]["unique_words"].add(word)
                word_data[length]["counts"][word] = word_data[length]["counts"].get(word, 0) + 1

    for length in sorted(word_data.keys()):
        unique_count = len(word_data[length]["unique_words"])
        most_common_word = ""
        most_common_count = 0

        for word, count in word_data[length]["counts"].items():
            if count > most_common_count:
                most_common_word = word
                most_common_count = count

        print(f"Length {length}: {unique_count} unique words, most common = '{most_common_word}' ({most_common_count})")
    return word_data

if __name__ == "__main__":
    try:
        filename = input("Enter filename: ")
        word_data = get_unique_words(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        exit()