# Additional examples from the book

These are verbatim formatted blocks from the book, preserved in reading order. They include code fragments, terminal commands and example outputs. Some depend on previous steps and are not complete standalone programs. Use the named `.py` files in this directory for running the full practical builds.

### Book example block 605

```text
department = "IT"
print(department == "IT")
print(department == "Finance")
```

### Book example block 609

```text
True
False
```

### Book example block 615

```text
department = "IT"

if department == "IT":
    print("This employee works in IT.")
```

### Book example block 620

```text
This employee works in IT.
```

### Book example block 624

```text
department = "Finance"

if department == "IT":
    print("This employee works in IT.")
else:
    print("This employee works elsewhere.")
```

### Book example block 631

```text
This employee works elsewhere.
```

### Book example block 633

```text
department = "Finance"

if department == "IT":
    print("This employee works in IT.")
elif department == "Finance":
    print("This employee works in Finance.")
else:
    print("This employee works in another department.")
```

### Book example block 642

```text
This employee works in Finance.
```

### Book example block 650

```text
department = "IT"
salary = 42000

if department == "IT" and salary > 40000:
    print("IT employee earning more than £40,000")
```

### Book example block 656

```text
IT employee earning more than £40,000
```

### Book example block 658

```text
department = "HR"
salary = 42000

if department == "IT" or department == "HR":
    print("Employee is in a supported department")
```

### Book example block 664

```text
Employee is in a supported department
```

### Book example block 666

```text
is_active = False

if not is_active:
    print("This employee is inactive")
```

### Book example block 671

```text
This employee is inactive
```

### Book example block 675

```text
employee_names = ["Alice", "Sam", "Priya"]

for name in employee_names:
    print(name)
```

### Book example block 680

```text
Alice
Sam
Priya
```

### Book example block 685

```text
employees = [
    {"name": "Alice", "department": "IT"},
    {"name": "Sam", "department": "Finance"},
    {"name": "Priya", "department": "IT"}
]

for employee in employees:
    print(employee["name"])
```

### Book example block 694

```text
Alice
Sam
Priya
```

### Book example block 718

```text
Employees in IT:
Alice: £42,000.00
Priya: £45,000.00
```

### Book example block 741

```text
for number in range(3):
    print(number)
```

### Book example block 744

```text
0
1
2
```

### Book example block 748

```text
for number in range(1, 4):
    print(number)
```

### Book example block 751

```text
1
2
3
```

### Book example block 758

```text

while count < 3:
    print(count)
    count = count + 1
```

### Book example block 763

```text
0
1
2
```

### Book example block 773

```text
employee_names = ["Alice", "Sam", "Priya"]

for name in employee_names:
    if name == "Sam":
        print("Found Sam")
        break
    print(name)
```

### Book example block 781

```text
Alice
Found Sam
```

### Book example block 785

```text
employee_names = ["Alice", "Sam", "Priya"]

for name in employee_names:
    if name == "Sam":
        continue
    print(name)
```

### Book example block 792

```text
Alice
Priya
```
