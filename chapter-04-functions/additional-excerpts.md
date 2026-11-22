# Additional examples

These examples accompany the chapter. Some are terminal commands or sample output rather than complete programs. Run the `.py` files in this folder for full exercises.

### Example 1

```text
for employee in employees:
    if employee["department"] == target_department:
        print(f"{employee['name']}: £{employee['salary']:,.2f}")
```

### Example 2

```text
alice_monthly = 42000 / 12
sam_monthly = 38000 / 12
priya_monthly = 45000 / 12
```

### Example 3

```text
def greet():
    print("Hello from the Employee Directory")
```

### Example 4

```text
greet()
```

### Example 5

```text
Hello from the Employee Directory
```

### Example 6

```text
def monthly_salary(annual_salary):
    result = annual_salary / 12
    print(f"Monthly salary: £{result:,.2f}")
```

### Example 7

```text
monthly_salary(42000)
monthly_salary(38000)
```

### Example 8

```text
Monthly salary: £3,500.00
Monthly salary: £3,166.67
```

### Example 9

```text
def monthly_salary(annual_salary):
    return annual_salary / 12
```

### Example 10

```text
alice_monthly = monthly_salary(42000)
sam_monthly = monthly_salary(38000)

print(f"Alice: £{alice_monthly:,.2f}")
print(f"Sam: £{sam_monthly:,.2f}")
```

### Example 11

```text
Alice: £3,500.00
Sam: £3,166.67
```

### Example 12

```text
def describe_employee(name, department):
    return f"{name} works in {department}"
```

### Example 13

```text
print(describe_employee("Alice", "IT"))
```

### Example 14

```text
Alice works in IT
```

### Example 15

```text
Alice's monthly salary: £3,500.00
David is not in the directory
```

### Example 16

```text
def describe_employee(name, department="Unassigned"):
    return f"{name} works in {department}"

print(describe_employee("Sam"))
print(describe_employee("Priya", "Finance"))
```

### Example 17

```text
Sam works in Unassigned
Priya works in Finance
```

### Example 18

```text
print(describe_employee(name="David", department="HR"))
```

### Example 19

```text
David works in HR
```

### Example 20

```text
def monthly_salary(annual_salary):
    result = annual_salary / 12
    return result

print(monthly_salary(42000))
```

### Example 21

```text
3500.0
```

### Example 22

```text
print(result)
```

### Example 23

```text
assert monthly_salary(42000) == 3500
```

### Example 24

```text
assert monthly_salary(42000) == 9999
```

### Example 25

```text
AssertionError
```

### Example 26

```text
assert find_employee(employees, "Alice")["name"] == "Alice"
assert find_employee(employees, "David") is None
```
