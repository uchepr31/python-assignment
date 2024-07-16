def is_eligible_for_loan(age, income, credit_score):
    # Define the eligibility criteria
    age_criteria = 21 <= age <= 65
    income_criteria = income >= 30000
    credit_score_criteria = credit_score >= 700
    
    # Check if all criteria are met
    if age_criteria and income_criteria and credit_score_criteria:
        return True
    else:
        return False

def main():
    # Prompt the user for their age
    age = int(input("Enter your age: "))
    
    # Prompt the user for their annual income
    income = float(input("Enter your annual income: "))
    
    # Prompt the user for their credit score
    credit_score = int(input("Enter your credit score: "))
    
    # Determine if the user is eligible for a loan
    if is_eligible_for_loan(age, income, credit_score):
        print("You are eligible for a loan, be happy lol !!.")
    else:
        print("You are not eligible for a loan.")

if __name__ == "__main__":
    main()
