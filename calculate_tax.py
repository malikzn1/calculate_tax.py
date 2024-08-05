def calculate_weekly_tax(weekly_income):
    if weekly_income < 500:
        tax_rate = 0.10
    elif weekly_income >= 500 and weekly_income < 1500:
        tax_rate = 0.15
    elif weekly_income >= 1500 and weekly_income < 2500:
        tax_rate = 0.20
    else:
        tax_rate = 0.30
    
    tax_withholding = weekly_income * tax_rate
    return tax_withholding

# Example usage
weekly_income = float(input("Enter weekly income: "))
tax_withholding = calculate_weekly_tax(weekly_income)
print(f"Weekly Tax Withholding: ${tax_withholding:.2f}")
