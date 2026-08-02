from flask import Flask, jsonify
import os

app = Flask(__name__)

employees = [
    {"id": 1, "name": "John", "department": "IT"},
    {"id": 2, "name": "Sara", "department": "HR"},
    {"id": 3, "name": "David", "department": "Finance"}
]

@app.route("/")
def home():
    return jsonify({
        "application": "Employee API",
        "version": "1.0",
        "status": "Running"
    })

@app.route("/employees")
def employees_list():
    return jsonify(employees)

@app.route("/employees/<int:id>")
def employee(id):
    emp = next((e for e in employees if e["id"] == id), None)

    if emp:
        return jsonify(emp)

    return jsonify({"message": "Employee Not Found"}), 404


@app.route("/health")
def health():
    return jsonify({"status": "UP"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
