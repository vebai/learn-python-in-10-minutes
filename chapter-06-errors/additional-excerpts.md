# Additional examples

These examples accompany the chapter. Some are terminal commands or sample output rather than complete programs. Run the `.py` files in this folder for full exercises.

### Example 1

```text
employees = [
    {"name": "Alice", "salary": 42000},
    {"name": "Sam", "salary": 38000}
]

total = 0
for employee in employees:
    total = total + employee["salary"]

print(f"Total salary: £{total:,.2f}")
```

### Example 2

```text
Total salary: £80,000.00
```

### Example 3

```text
print("Hello, Alex!)
```

### Example 4

```text
SyntaxError
```

### Example 5

```text
salary_text = "hello"
annual_salary = int(salary_text)
```

### Example 6

```text
ValueError
```

### Example 7

```text
annual_salary = 42000
monthly_salary = annual_salary * 12
print(monthly_salary)
```

### Example 8

```text
504000
```

### Example 9

```text
  File "traceback_demo.py", line 5, in <module>
    show_salary("hello")
  File "traceback_demo.py", line 2, in show_salary
    monthly = annual_salary / 12
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

### Example 10

```text
print(employee_name)
```

### Example 11

```text
NameError: name 'employee_name' is not defined
```

### Example 12

```text
result = "42000" / 12
```

### Example 13

```text
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

### Example 14

```text
annual_salary = int("hello")
```

### Example 15

```text
ValueError: invalid literal for int() with base 10: 'hello'
```

### Example 16

```text
employee = {"name": "Alice", "department": "IT"}
print(employee["salary"])
```

### Example 17

```text
KeyError: 'salary'
```

### Example 18

```text
salary_text = input("Enter annual salary: ")

try:
    annual_salary = int(salary_text)
    monthly_salary = annual_salary / 12
    print(f"Monthly salary: £{monthly_salary:,.2f}")
except ValueError:
    print("Please enter a whole number.")
```

### Example 19

```text
Enter annual salary: 42000
Monthly salary: £3,500.00
```

### Example 20

```text
Enter annual salary: hello
Please enter a whole number.
```

### Example 21

```text
for employee in employees:
    total = total + employee["salary"]
```

### Example 22

```text
Total salary: £80,000.00
```

### Example 23

```text
for employee in employees:
    total = employee["salary"]
```

### Example 24

```text
Total salary: £38,000.00
```

### Example 25

```text
def monthly_salary(annual_salary):
    return annual_salary / 12

assert monthly_salary(42000) == 3500
```

### Example 26

```text
Enter annual salary: 42000
Monthly salary: £3,500.00
```

### Example 27

```text
Enter annual salary: hello
Please enter a whole number.
```

### Example 28

```text
def monthly_salary(annual_salary):
    return annual_salary * 12
```

### Example 29

```text
Enter annual salary: 42000
Monthly salary: £504,000.00
```

### Example 30

```text
AssertionError
```

### Example 31

```text
def monthly_salary(annual_salary):
    return annual_salary / 12
```

### Example 32

```text
salary_text = input("Enter annual salary: ")

if salary_text.strip() == "":
    print("No salary entered.")
else:
    try:
        annual_salary = int(salary_text)
        monthly = monthly_salary(annual_salary)
        print(f"Monthly salary: £{monthly:,.2f}")
    except ValueError:
        print("Please enter a whole number.")

assert monthly_salary(42000) == 3500
```

### Example 33

```text
python3 --version
```

### Example 34

```text
python --version
```

### Example 35

```text
mkdir -p ~/python-projects
cd ~/python-projects
```

### Example 36

```text
mkdir "%USERPROFILE%\python-projects"
cd /d "%USERPROFILE%\python-projects"
```

### Example 37

```text
python3 check.py
```

### Example 38

```text
python check.py
```

### Example 39

```text
Local Python ready
```
