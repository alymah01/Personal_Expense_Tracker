
# Personal Expense Tracker

print("Welcome to my Personal Expense Tracker!")
print("This program will help me track my spending.")

# My expenses

food = float(input("How much did you spend on food? $"))


gas = float(input("How much did you spend on gas? $"))
shopping = float(input("How much did you spend on shopping? $"))
entertainment = float(input("How much did you spend on entertainment? $"))


# Display expenses
print("Food: $", food)
print("Gas: $", gas)
print("Shopping: $", shopping)
print("Entertainment: $", entertainment)


# Calculate total expenses
total = food + gas + shopping + entertainment

# Display total spending
print("Total Expenses: $", round(total, 2))


# Calculate spending percentages
food_percent = (food / total) * 100
gas_percent = (gas / total) * 100
shopping_percent = (shopping / total) * 100
entertainment_percent = (entertainment / total) * 100

# Display percentages
print("Food:", round(food_percent, 1), "%")
print("Gas:", round(gas_percent, 1), "%")
print("Shopping:", round(shopping_percent, 1), "%")
print("Entertainment:", round(entertainment_percent, 1), "%")


# Create a spending chart
import matplotlib.pyplot as plt

categories = ["Food", "Gas", "Shopping", "Entertainment"]
amounts = [food, gas, shopping, entertainment]

plt.bar(categories, amounts)
plt.title("My Personal Expenses")
plt.xlabel("Expense Category")
plt.ylabel("Amount Spent ($)")

plt.savefig("expense_chart.png")
plt.show()

# Save expenses to a CSV file
import csv

with open("expenses.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Amount"])
    writer.writerow(["Food", food])
    writer.writerow(["Gas", gas])
    writer.writerow(["Shopping", shopping])
    writer.writerow(["Entertainment", entertainment])
    writer.writerow(["Total", total])

print("Expenses saved successfully!")
highest = max(amounts)

print("Highest expense:", categories[amounts.index(highest)], "- $", f"{highest:.2f}")