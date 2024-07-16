def calculate_interest(principal, rate, time):
    # Calculate the interest using the formula
    interest = principal * rate * time / 100
    return interest

def main():
    # Prompt the user for the principal amount
    principal = float(input("Enter the principal amount: "))
    
    # Prompt the user for the interest rate (as a percentage)
    rate = float(input("Enter the annual interest rate (in %): "))
    
    # Prompt the user for the time period in years
    time = float(input("Enter the time period in years: "))
    
    # Calculate the interest
    interest = calculate_interest(principal, rate, time)
    
    # Print the calculated interest
    print(f"The calculated interest is: ${interest:.2f}")

if __name__ == "__main__":
    main()
