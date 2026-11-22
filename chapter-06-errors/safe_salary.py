def monthly_salary(annual_salary):
    return annual_salary / 12

salary_text = input("Enter annual salary: ")

try:
    annual_salary = int(salary_text)
    monthly = monthly_salary(annual_salary)
    print(f"Monthly salary: £{monthly:,.2f}")
except ValueError:
    print("Please enter a whole number.")

assert monthly_salary(42000) == 3500
