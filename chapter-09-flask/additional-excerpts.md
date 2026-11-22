# Additional examples

These examples accompany the chapter. Some are terminal commands or sample output rather than complete programs. Run the `.py` files in this folder for full exercises.

### Example 1

```text
cursor = connection.execute(
    "SELECT id, name, department, salary FROM employees ORDER BY id"
)
```

### Example 2

```text
python3 -m venv venv
```

### Example 3

```text
python -m venv venv
```

### Example 4

```text
venv/bin/python -m pip install flask
```

### Example 5

```text
.\venv\Scripts\python.exe -m pip install flask
```

### Example 6

```text
venv/bin/python app.py
```

### Example 7

```text
.\venv\Scripts\python.exe app.py
```

### Example 8

```text
 * Running on http://127.0.0.1:5000
```

### Example 9

```text
http://127.0.0.1:5000/
```

### Example 10

```text
Employee Directory API
```

### Example 11

```text
venv/bin/python init_db.py
```

### Example 12

```text
.\venv\Scripts\python.exe init_db.py
```

### Example 13

```text
Database initialised
```

### Example 14

```text
venv/bin/python app.py
```

### Example 15

```text
.\venv\Scripts\python.exe app.py
```

### Example 16

```text
http://127.0.0.1:5000/employees
```

### Example 17

```text
[
  {"department": "IT", "id": 1, "name": "Alice", "salary": 42000},
  {"department": "Finance", "id": 2, "name": "Sam", "salary": 38000},
  {"department": "IT", "id": 3, "name": "Priya", "salary": 45000}
]
```

### Example 18

```text
@app.route("/employees/<int:employee_id>")
def get_employee(employee_id):
    connection = get_connection()
    cursor = connection.execute(
        "SELECT id, name, department, salary FROM employees WHERE id = ?",
        (employee_id,)
    )
    row = cursor.fetchone()
    connection.close()

    if row is None:
        return jsonify({"error": "Employee not found"}), 404

    employee = {
        "id": row[0],
        "name": row[1],
        "department": row[2],
        "salary": row[3]
    }
    return jsonify(employee)
```

### Example 19

```text
venv/bin/python app.py
```

### Example 20

```text
.\venv\Scripts\python.exe app.py
```

### Example 21

```text
http://127.0.0.1:5000/employees/1
```

### Example 22

```text
{
  "department": "IT",
  "id": 1,
  "name": "Alice",
  "salary": 42000
}
```

### Example 23

```text
http://127.0.0.1:5000/employees/9999
```

### Example 24

```text
{"error": "Employee not found"}
```

### Example 25

```text
venv/bin/python update_employee.py
```

### Example 26

```text
.\venv\Scripts\python.exe update_employee.py
```

### Example 27

```text
Updated Alice's department
```

### Example 28

```text
venv/bin/python app.py
```

### Example 29

```text
.\venv\Scripts\python.exe app.py
```

### Example 30

```text
http://127.0.0.1:5000/employees/1
```
