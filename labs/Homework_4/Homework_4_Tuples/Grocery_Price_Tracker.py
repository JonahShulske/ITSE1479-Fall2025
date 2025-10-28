"""
Jonah Shulske
October 23, 2025
ITSE-1479 Fall 2025
"""

# Problem 2 - Grocery Price Tracker
purchases = [
    ("Apple", 0.99, 5),
    ("Banana", 0.59, 8),
    ("Apple", 0.99, 3),
    ("Orange", 1.29, 2),
    ("Banana", 0.59, 4)
    ]
sales_total = {}

for item, price, quantity in purchases:
    total = price * quantity
    sales_total[item] = round(sales_total.get(item, 0) + total)
    sales_total += item

print(sales_total)
