# Additional examples

These examples accompany the chapter. Some are terminal commands or sample output rather than complete programs. Run the `.py` files in this folder for full exercises.

### Example 1

```text
department = "IT"
print(department == "IT")
print(department == "Finance")
```

### Example 2

```text
True
False
```

### Example 3

```text
department = "IT"

if department == "IT":
    print("This employee works in IT.")
```

### Example 4

```text
This employee works in IT.
```

### Example 5

```text
department = "Finance"

if department == "IT":
    print("This employee works in IT.")
else:
    print("This employee works elsewhere.")
```

### Example 6

```text
This employee works elsewhere.
```

### Example 7

```text
department = "Finance"

if department == "IT":
    print("This employee works in IT.")
elif department == "Finance":
    print("This employee works in Finance.")
else:
    print("This employee works in another department.")
```

### Example 8

```text
This employee works in Finance.
```

### Example 9

```text
department = "IT"
salary = 42000

if department == "IT" and salary > 40000:
    print("IT employee earning more than £40,000")
```

### Example 10

```text
IT employee earning more than £40,000
```

### Example 11

```text
department = "HR"
salary = 42000

if department == "IT" or department == "HR":
    print("Employee is in a supported department")
```

### Example 12

```text
Employee is in a supported department
```

### Example 13

```text
is_active = False

if not is_active:
    print("This employee is inactive")
```

### Example 14

```text
This employee is inactive
```

### Example 15

```text
employee_names = ["Alice", "Sam", "Priya"]

for name in employee_names:
    print(name)
```

### Example 16

```text
Alice
Sam
Priya
```

### Example 17

```text
employees = [
    {"name": "Alice", "department": "IT"},
    {"name": "Sam", "department": "Finance"},
    {"name": "Priya", "department": "IT"}
]

for employee in employees:
    print(employee["name"])
```

### Example 18

```text
Alice
Sam
Priya
```

### Example 19

```text
Employees in IT:
Alice: £42,000.00
Priya: £45,000.00
```

### Example 20

```text
for number in range(3):
    print(number)
```

### Example 21

```text
0
1
2
```

### Example 22

```text
for number in range(1, 4):
    print(number)
```

### Example 23

```text
1
2
3
```

### Example 24

```text

while count < 3:
    print(count)
    count = count + 1
```

### Example 25

```text
0
1
2
```

### Example 26

```text
employee_names = ["Alice", "Sam", "Priya"]

for name in employee_names:
    if name == "Sam":
        print("Found Sam")
        break
    print(name)
```

### Example 27

```text
Alice
Found Sam
```

### Example 28

```text
employee_names = ["Alice", "Sam", "Priya"]

for name in employee_names:
    if name == "Sam":
        continue
    print(name)
```

### Example 29

```text
Alice
Priya
```
