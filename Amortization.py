def calculate_monthly_payment(principal: float, annual_rate: float, years: int) -> float:
# Calculate the monthly payment for a fixed-rate amortizing loan.
# Convert annual percentage to monthly decimal rate
    r = annual_rate / 100 / 12  
    n = years * 12   # total months

    # Zero-interest special case
    if r == 0:
        return round(principal / n, 2)

    # Amortization formula
    M = (principal * r * (1 + r) ** n) / ((1 + r) ** n - 1)
    return round(M, 2)


def main():
#Input function for user interaction.
#Reads loan details and prints the monthly payment.

    print("Loan_Monthly_Payment Calculator")
    
    principal = float(input("Enter loan amount (principal): "))
    annual_rate = float(input("Enter annual interest rate (%): "))
    years = int(input("Enter loan duration (years): "))

    monthly_payment = calculate_monthly_payment(principal, annual_rate, years)

    print("\nMonthly Payment:₦{:.2f}:".format(monthly_payment))
# Run the program
if __name__ == "__main__":
    main()