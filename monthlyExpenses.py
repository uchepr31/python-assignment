def main():
    # Define the expense categories
    categories = ["rent", "groceries", "utilities", "entertainment"]
    
    # Initialize a dictionary to store the expenses
    expenses = {}
    
    # Prompt the user to enter the amount for each category
    for category in categories:
        amount = float(input(f"Enter the amount for {category}: "))
        expenses[category] = amount
    
    # Calculate the total monthly expense
    total_expense = sum(expenses.values())
    
    # Print the expenses for each category
    print("\nMonthly Expenses:")
    for category, amount in expenses.items():
        print(f"{category.capitalize()}: ${amount:.2f}")
    
    # Print the total monthly expense
    print(f"\nTotal Monthly Expense: ${total_expense:.2f}")

if __name__ == "__main__":
    main()
