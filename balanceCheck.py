def main():
    # Prompt the user for their account balance
    balance = float(input("Enter your account balance: "))
    
    # Prompt the user for the amount they want to withdraw
    withdrawal_amount = float(input("Enter the amount you want to withdraw: "))
    
    # Check if the account has sufficient funds for the withdrawal
    if balance >= withdrawal_amount:
        # Deduct the amount and print the new balance
        balance -= withdrawal_amount
        print(f"Withdrawal successful. Your new balance is: ${balance:.2f}")
    else:
        # Print an error message
        print("Error: Insufficient funds.")

if __name__ == "__main__":
    main()
