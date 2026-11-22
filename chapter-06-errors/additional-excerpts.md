# Additional examples from the book

These are verbatim formatted blocks from the book, preserved in reading order. They include code fragments, terminal commands and example outputs. Some depend on previous steps and are not complete standalone programs. Use the named `.py` files in this directory for running the full practical builds.

### Book example block 1171

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

### Book example block 1182

```text
Total salary: £80,000.00
```

### Book example block 1192

```text
print("Hello, Alex!)
```

### Book example block 1194

```text
SyntaxError
```

### Book example block 1198

```text
salary_text = "hello"
annual_salary = int(salary_text)
```

### Book example block 1201

```text
ValueError
```

### Book example block 1205

```text
annual_salary = 42000
monthly_salary = annual_salary * 12
print(monthly_salary)
```

### Book example block 1209

```text
504000
```

### Book example block 1222

```text
  File "traceback_demo.py", line 5, in <module>
    show_salary("hello")
  File "traceback_demo.py", line 2, in show_salary
    monthly = annual_salary / 12
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

### Book example block 1238

```text
print(employee_name)
```

### Book example block 1240

```text
NameError: name 'employee_name' is not defined
```

### Book example block 1243

```text
result = "42000" / 12
```

### Book example block 1245

```text
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

### Book example block 1248

```text
annual_salary = int("hello")
```

### Book example block 1250

```text
ValueError: invalid literal for int() with base 10: 'hello'
```

### Book example block 1253

```text
employee = {"name": "Alice", "department": "IT"}
print(employee["salary"])
```

### Book example block 1256

```text
KeyError: 'salary'
```

### Book example block 1261

```text
salary_text = input("Enter annual salary: ")

try:
    annual_salary = int(salary_text)
    monthly_salary = annual_salary / 12
    print(f"Monthly salary: £{monthly_salary:,.2f}")
except ValueError:
    print("Please enter a whole number.")
```

### Book example block 1270

```text
Enter annual salary: 42000
Monthly salary: £3,500.00
```

### Book example block 1273

```text
Enter annual salary: hello
Please enter a whole number.
```

### Book example block 1282

```text
for employee in employees:
    total = total + employee["salary"]
```

### Book example block 1285

```text
Total salary: £80,000.00
```

### Book example block 1287

```text
for employee in employees:
    total = employee["salary"]
```

### Book example block 1290

```text
Total salary: £38,000.00
```

### Book example block 1297

```text
def monthly_salary(annual_salary):
    return annual_salary / 12

assert monthly_salary(42000) == 3500
```

### Book example block 1321

```text
Enter annual salary: 42000
Monthly salary: £3,500.00
```

### Book example block 1324

```text
Enter annual salary: hello
Please enter a whole number.
```

### Book example block 1330

```text
def monthly_salary(annual_salary):
    return annual_salary * 12
```

### Book example block 1334

```text
Enter annual salary: 42000
Monthly salary: £504,000.00
```

### Book example block 1337

```text
AssertionError
```

### Book example block 1341

```text
def monthly_salary(annual_salary):
    return annual_salary / 12
```

### Book example block 1354

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

### Book example block 1387

```text
python3 --version
```

### Book example block 1389

```text
python --version
```

### Book example block 1394

```text
mkdir -p ~/python-projects
cd ~/python-projects
```

### Book example block 1397

```text
mkdir "%USERPROFILE%\python-projects"
cd /d "%USERPROFILE%\python-projects"
```

### Book example block 1407

```text
python3 check.py
```

### Book example block 1409

```text
python check.py
```

### Book example block 1411

```text
Local Python ready
```
