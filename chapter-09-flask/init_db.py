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

print("Database initialised")
