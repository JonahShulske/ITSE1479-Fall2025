# Jonah Shulske - ITSE-1479 Fall 2025
# Homework 1
# September 14, 2025

# Exercise 1 — Friendly Fortune
name = input("State your name: ")
fortune_Number = int(input("Please enter a number between 1-5: "))
if fortune_Number == 1:
    print("Hello,", name, ", today you will learn something new")
elif fortune_Number == 2:
    print("Hello,", name, ", today you will meet someone interesting")
elif fortune_Number == 3:
    print("Hello,", name, ", today you will discover something fun")
elif fortune_Number == 4:
    print("Hello,", name, ", today you will find luck in life")
elif fortune_Number == 5:
    print("Hello,", name, ", today you will uncover treasure in others")
else:
    print("That is not a valid fortune number")

print("")   # Adding space between Exercises

# Exercise 2 — Even or Odd
input_Number = input("Enter a number: ")
try:
    eoo_Number = int(input_Number)      # "eoo" Stands for Even or Odd
    if eoo_Number % 2 == 0:
        print(eoo_Number, "is even")
    else:
        print(eoo_Number, "is odd")
except ValueError:
    print("Error: Number is not numeric")

print("")

# Exercise 3 — Discount Calculator
input_Price = input("Enter the price of an item: $")
try:
    item_Price = float(input_Price)
except ValueError:
    print("Bad input")
    
input_Discount = input("Enter the item discount: ")
try:
    item_Discount = float(input_Discount)
except ValueError:
    print("Bad input")
    
post_Discount = item_Price - (item_Price * item_Discount / 100)
print(post_Discount)

print("")

# Exercise 4 — The Three Numbers Game
num_1 = float(input("Enter 1st Number: "))
num_2 = float(input("Enter 2nd Number: "))
num_3 = float(input("Enter 3rd Number: "))
if num_1 >= num_2 and num_1 >= num_3:
    largest = float(num_1)
elif num_2 >= num_1 and num_2 >= num_3:
    largest = float(num_2)
elif num_3 >= num_1 and num_3 >= num_2:
    largest = float(num_3)

if num_1 <= num_2 and num_1 <= num_3:
    smallest = float(num_1)
elif num_2 <= num_1 and num_2 <= num_3:
    smallest = float(num_2)
elif num_3 <= num_1 and num_3 <= num_2:
    smallest = num_3
    
num_Average = (num_1 + num_2 + num_3) / 3
print("The largest number is:", largest)
print("The smallest number is:", smallest)
print("The average of the numbers is:", num_Average)

print("")

# Exercise 5 - Temperature Reminder
input_temp = input("Enter the Temperature in Fahrenheit: ")
try:
    temperature = float(input_temp)
    if temperature < 32:
        print("Brr! Wear a coat")
    elif temperature >= 32 and temperature < 70:
        print("Mild weather today")
    elif temperature > 70:
        print("It's warm - Shorts time!")
except ValueError:
    print("Please enter a number")

      



