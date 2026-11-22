import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

def get_connection():
    return sqlite3.connect("employees.db")

@app.route("/")
def home():
    return "Employee Directory API"

@app.route("/employees")
def list_employees():
    connection = get_connection()
    cursor = connection.execute(
        "SELECT id, name, department, salary FROM employees ORDER BY id"
    )
    rows = cursor.fetchall()
    connection.close()

    employees = []
    for row in rows:
        employee = {
            "id": row[0],
            "name": row[1],
            "department": row[2],
            "salary": row[3]
        }
        employees.append(employee)

    return jsonify(employees)

if __name__ == "__main__":
    app.run()
