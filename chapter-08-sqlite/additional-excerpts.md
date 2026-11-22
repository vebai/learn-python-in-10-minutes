# Additional examples

These examples accompany the chapter. Some are terminal commands or sample output rather than complete programs. Run the `.py` files in this folder for full exercises.

### Example 1

```text
employees = [
    {"name": "Alice", "department": "IT", "salary": 42000},
    {"name": "Sam", "department": "Finance", "salary": 38000},
    {"name": "Priya", "department": "IT", "salary": 45000}
]
```

### Example 2

```text
for employee in employees:
    if employee["name"] == "Alice":
        print(employee)
```

### Example 3

```text
import sqlite3
```

### Example 4

```text
connection = sqlite3.connect("employees.db")
```

### Example 5

```text
connection.close()
```

### Example 6

```text
import sqlite3

connection = sqlite3.connect("employees.db")

connection.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        salary INTEGER NOT NULL
    )
""")

connection.commit()
connection.close()
```

### Example 7

```text
connection.execute(
    "INSERT OR IGNORE INTO employees (id, name, department, salary) VALUES (?, ?, ?, ?)",
    (1, "Alice", "IT", 42000)
)
connection.execute(
    "INSERT OR IGNORE INTO employees (id, name, department, salary) VALUES (?, ?, ?, ?)",
    (2, "Sam", "Finance", 38000)
)
connection.execute(
    "INSERT OR IGNORE INTO employees (id, name, department, salary) VALUES (?, ?, ?, ?)",
    (3, "Priya", "IT", 45000)
)

connection.commit()
connection.close()
```

### Example 8

```text
import sqlite3

connection = sqlite3.connect("employees.db")

cursor = connection.execute(
    "SELECT id, name, department, salary FROM employees ORDER BY id"
)

for row in cursor:
    print(row)

connection.close()
```

### Example 9

```text
(1, 'Alice', 'IT', 42000)
(2, 'Sam', 'Finance', 38000)
(3, 'Priya', 'IT', 45000)
```

### Example 10

```text
import sqlite3

connection = sqlite3.connect("employees.db")

cursor = connection.execute(
    "SELECT name, department FROM employees WHERE id = ?",
    (1,)
)

row = cursor.fetchone()
print(row)

connection.close()
```

### Example 11

```text
('Alice', 'IT')
```

### Example 12

```text
import sqlite3

connection = sqlite3.connect("employees.db")

cursor = connection.execute(
    "SELECT name, department FROM employees WHERE id = ?",
    (99,)
)

row = cursor.fetchone()

if row is None:
    print("Employee not found.")
else:
    print(row)

connection.close()
```

### Example 13

```text
Employee not found.
```

### Example 14

```text
import sqlite3

connection = sqlite3.connect("employees.db")

connection.execute(
    "UPDATE employees SET department = ? WHERE id = ?",
    ("Engineering", 1)
)

connection.commit()
connection.close()
```

### Example 15

```text
import sqlite3

connection = sqlite3.connect("employees.db")

cursor = connection.execute(
    "SELECT name, department FROM employees WHERE id = ?",
    (1,)
)
print(cursor.fetchone())

connection.close()
```

### Example 16

```text
('Alice', 'Engineering')
```

### Example 17

```text
connection = sqlite3.connect("employees.db")

# Execute your SQL statements here.

connection.commit()
connection.close()
```

### Example 18

```text
All employees:
(1, 'Alice', 'IT', 42000)
(2, 'Sam', 'Finance', 38000)
(3, 'Priya', 'IT', 45000)

Employee with id 1:
('Alice', 'IT')

Employee with id 1 after update:
('Alice', 'Engineering')
```

### Example 19

```text
Records after reopening:
(1, 'Alice', 'Engineering', 42000)
(2, 'Sam', 'Finance', 38000)
(3, 'Priya', 'IT', 45000)
```
