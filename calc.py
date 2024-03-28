num_of_years = 5
annual_interest_rate = 5
principal_amount = 350000
total_amount = principal_amount * (1 + (annual_interest_rate / 100) * num_of_years)
monthly_payment = 50000
for i in range(12 * num_of_years):
    total_amount = monthly_payment + total_amount + (total_amount * (annual_interest_rate / 100) / 12)
print(total_amount)
