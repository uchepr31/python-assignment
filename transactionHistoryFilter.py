def filter_transactions(transactions, threshold):
    # Filter transactions that are above the threshold amount
    filtered_transactions = [transaction for transaction in transactions if transaction > threshold]
    return filtered_transactions

def main():
    # Define a list of transactions
    transactions = [120, 500, 30, 250, 75, 600, 150]
    
    # Prompt the user for the threshold amount
    threshold = float(input("Enter the threshold amount: "))
    
    # Get the filtered transactions
    filtered_transactions = filter_transactions(transactions, threshold)
    
    # Print the filtered transactions
    print("Transactions above the threshold amount:")
    for transaction in filtered_transactions:
        print(f"${transaction:.2f}")

if __name__ == "__main__":
    main()
