# Additional examples from the book

These are verbatim formatted blocks from the book, preserved in reading order. They include code fragments, terminal commands and example outputs. Some depend on previous steps and are not complete standalone programs. Use the named `.py` files in this directory for running the full practical builds.

### Book example block 818

```text
for employee in employees:
    if employee["department"] == target_department:
        print(f"{employee['name']}: £{employee['salary']:,.2f}")
```

### Book example block 823

```text
alice_monthly = 42000 / 12
sam_monthly = 38000 / 12
priya_monthly = 45000 / 12
```

### Book example block 830

```text
def greet():
    print("Hello from the Employee Directory")
```

### Book example block 834

```text
greet()
```

### Book example block 836

```text
Hello from the Employee Directory
```

### Book example block 843

```text
def monthly_salary(annual_salary):
    result = annual_salary / 12
    print(f"Monthly salary: £{result:,.2f}")
```

### Book example block 847

```text
monthly_salary(42000)
monthly_salary(38000)
```

### Book example block 850

```text
Monthly salary: £3,500.00
Monthly salary: £3,166.67
```

### Book example block 856

```text
def monthly_salary(annual_salary):
    return annual_salary / 12
```

### Book example block 859

```text
alice_monthly = monthly_salary(42000)
sam_monthly = monthly_salary(38000)

print(f"Alice: £{alice_monthly:,.2f}")
print(f"Sam: £{sam_monthly:,.2f}")
```

### Book example block 865

```text
Alice: £3,500.00
Sam: £3,166.67
```

### Book example block 873

```text
def describe_employee(name, department):
    return f"{name} works in {department}"
```

### Book example block 876

```text
print(describe_employee("Alice", "IT"))
```

### Book example block 878

```text
Alice works in IT
```

### Book example block 914

```text
Alice's monthly salary: £3,500.00
David is not in the directory
```

### Book example block 942

```text
def describe_employee(name, department="Unassigned"):
    return f"{name} works in {department}"

print(describe_employee("Sam"))
print(describe_employee("Priya", "Finance"))
```

### Book example block 948

```text
Sam works in Unassigned
Priya works in Finance
```

### Book example block 952

```text
print(describe_employee(name="David", department="HR"))
```

### Book example block 954

```text
David works in HR
```

### Book example block 958

```text
def monthly_salary(annual_salary):
    result = annual_salary / 12
    return result

print(monthly_salary(42000))
```

### Book example block 964

```text
3500.0
```

### Book example block 966

```text
print(result)
```

### Book example block 972

```text
assert monthly_salary(42000) == 3500
```

### Book example block 975

```text
assert monthly_salary(42000) == 9999
```

### Book example block 977

```text
AssertionError
```

### Book example block 980

```text
assert find_employee(employees, "Alice")["name"] == "Alice"
assert find_employee(employees, "David") is None
```
