"""
Jonah Shulske
October 8, 2025
ITSE-1479 Fall 2025
"""

def categorize_words(sentence: str):
    words = []
    short_words = []
    medium_words = []
    long_words = []

    for word in sentence.split():
        words.append(word)
        word_length = len(word)
        if word_length < 4:
            short_words.append(word)
        elif word_length >= 4 and word_length <= 6:
            medium_words.append(word)
        else:
            long_words.append(word)

    print(f"Short Words: (<4): {short_words}")
    print(f"Medium Words: (4-6): {medium_words}")
    print(f"Long Words: (>6): {long_words}")

if __name__ == "__main__":
    # Problem 1 - Word Length Filter
    sentence = input("Input a sentence: ")
    categorize_words(sentence)