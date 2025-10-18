"""
Jonah Shulske
October 12, 2025
ITSE-1479 Fall 2025
"""

def read_grades(filename: str):
    """Reads student names and grades from a file.
    Returns two lists: names and grades."""
    names = []
    grades = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                name = parts[0]
                try:
                    grade = int(parts[1])
                    names.append(name)
                    grades.append(grade)
                except ValueError:
                    print(f"Error: Skipping invalid grade for {name}: {parts[1]}")
    return names, grades

def analyze_grades(names, grades):
    """Analyze and print class statistics."""
    if not grades:
        print("Error: No Grades Found")
        return

    average = sum(grades) / len(grades)
    max_grade = max(grades)
    min_grade = min(grades)
    max_index = grades.index(max_grade)
    min_index = grades.index(min_grade)

    print(f"Average grade: {average:.2f}")
    print(f"Highest grade: {max_grade} (earned by {names[max_index]})")
    print(f"Lowest grade: {min_grade} (earned by {names[min_index]})")

def lookup_grade(names, grades, search_name):
    """Look up a student’s grade by name."""
    search_name = search_name.strip().lower()
    for i, name in enumerate(names):
        if name.lower() == search_name:
            print(f"{name}'s grade: {grades[i]}")
            return
    print("Error: Student not found")

if __name__ == "__main__":
    try:
        filename = input("Enter filename: ")
    except OSError as e:
        print(f"Error: {e}")
        exit()
    names, grades = read_grades(filename)
    analyze_grades(names, grades)
    search_name = input("Enter a name to look up: ")
    lookup_grade(names, grades, search_name)
