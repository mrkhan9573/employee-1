from flask import Flask, jsonify

app = Flask(__name__)

employees = [
    {
        "id": 1,
        "name": "John",
        "department": "IT"
    },
    {
        "id": 2,
        "name": "David",
        "department": "HR"
    },
    {
        "id": 3,
        "name": "Sara",
        "department": "Finance"
    }
]

@app.route("/")
def home():
    return jsonify({
        "message": "Employee Management API",
        "status": "Running"
    })

@app.route("/employees")
def get_employees():
    return jsonify(employees)

@app.route("/employees/<int:id>")
def get_employee(id):
    employee = next((e for e in employees if e["id"] == id), None)

    if employee:
        return jsonify(employee)

    return jsonify({"message": "Employee not found"}), 404


@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
