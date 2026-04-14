# Personal Expense Tracker

def check_expense_category(total_expense):
    if total_expense <= 2000:
        return "Low"
    elif total_expense <= 5000:
        return "Moderate"
    else:
        return "High"

# Taking number of expenses
n = int(input("Enter number of expenses: "))

total = 0

# Taking expense inputs
for i in range(n):
    expense = float(input(f"Enter expense {i+1}: "))
    total += expense

# Checking category
category = check_expense_category(total)

# Display result
print("Total Expense:", total)
print("Expense Category:", category)
