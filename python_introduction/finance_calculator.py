# prompt the user for their monthly income
Monthly_income = int(input("Enter your monthly income:"))
# prompt the user for their monthly expenses
Monthly_expenses = int(input("Enter your total monthly expenses:"))

# calculate the monthly savings by subtracting monthly expenses from the monthly income.
Monthly_savings = Monthly_income - Monthly_expenses
print(f"Your monthly savings are: {Monthly_savings}")

# define variable rate
rate = 0.05
annual_savings = Monthly_savings * 12
# Calculate the projected savings after one year, incorporating the interest. Use the simplified formula for annual savings projection: (Projected Savings = Projected_savings = annual_savings + (annual_savings * 0.05))
Projected_savings = annual_savings + (annual_savings * 0.05)
print(f"Projected savings after one year, with interest, is: {Projected_savings}")
