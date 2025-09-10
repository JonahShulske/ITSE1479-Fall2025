# Functions Assignment
# Jonah Shulske
# September 10, 2025

# Rewrite The Pay Program Using a Function

def Calculate_Pay(hours, rate):
    total = 0
    
    if hours > 40:
        total = 40 * rate + (hours - 40) * rate * 1.5
    else:
        total = hours * rate
        
    return total

hours = float(input("Enter Hours Worked: "))
rate = float(input("Enter Pay Rate: "))
print()
total_Pay = Calculate_Pay(hours, rate)
print("Total Pay:", total_Pay)
