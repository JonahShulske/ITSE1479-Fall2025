"""
Jonah Shulske
October 12, 2025
ITSE-1479-Fall2025
"""

def get_unique_words(filename: str):
    """Reads a file and returns a sorted list of unique words."""
    words = []
    with open(filename, "r") as f:
        for line in f:
            line_words = line.strip().split()
            for word in line_words:
                cleaned = word.lower().strip(".,!?\"'()[]{}:;")
                if cleaned:
                    words.append(cleaned)

    unique_words = sorted(set(words))
    return unique_words

if __name__ == "__main__":
    try:
        filename = input("Enter filename: ")
    except OSError as e:
        print(f"Error: {e}")
        exit()
    unique_words = get_unique_words(filename)
    print("Total unique words:", len(unique_words))
    print("Words in alphabetical order:")
    print(unique_words)
