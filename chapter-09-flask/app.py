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

if __name__ == "__main__":
    app.run()
