#Exercise 1
#Pay-Rate
"""
hours = float(input("Enter Hours Worked: "))
rate = float(input("Enter Pay Rate: "))
if hours > 40:
    pay = (40 * rate) + (hours - 40) * rate * 1.5
else:
    pay = (hours * rate)

print("Pay:", pay)
"""

#Exercise 2
#Pay-Rate Try Except
"""
try:
    hours = float(input("Enter Hours Worked: "))
    rate = float(input("Enter Pay Rate: "))
    if hours > 40:
        pay = (40 * rate) + (hours - 40) * rate * 1.5
    else:
        pay = (hours * rate)
    print("Pay:", pay)
except ValueError:
    print("Error: Please Enter Numeric Input")
"""

#Exercise 3
#Convert Float Between 0 and 1 to Letter Grade
try:
    num_Grade = float(input("Enter a Grade (0.0 - 1.0): "))
    if num_Grade >= 0.9:
        print("A")
    elif num_Grade >= 0.8:
        print("B")
    elif num_Grade >= 0.7:
        print("C")
    elif num_Grade >= 0.6:
        print("D")
    elif num_Grade >= 0.5:
        print("E")
    elif num_Grade >= 0.0:
        print("F")
    else:
        print("Error: Score Out of Range (0.0 - 1.0)")
        
except ValueError:
    print("Error: Input Must Be Float Between 0.0 - 1.0")
    
