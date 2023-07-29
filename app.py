from flask import Flask, jsonify

app = Flask(__name__)

# Sample hardcoded data for three students
students = [
    {"id": 1, "name": "John Doe", "age": 20, "major": "Computer Science"},
    {"id": 2, "name": "Jane Smith", "age": 21, "major": "Electrical Engineering"},
    {"id": 3, "name": "Bob Johnson", "age": 19, "major": "Mechanical Engineering"},
]


@app.route("/api/students", methods=["GET"])
def get_students():
    return jsonify(students)


if __name__ == "__main__":
    app.run(debug=True)
