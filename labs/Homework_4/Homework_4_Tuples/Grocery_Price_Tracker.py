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
    sales_total[item] = sales_total.get(item, 0) + total

for item, total in sales_total.items():
    print(f"{item}: ${total}")

sorted_sales = sorted(sales_total.items(), key=lambda x: x[1], reverse=True)

for item, total in sorted_sales:
        print(f"{item}: ${total}")
