# students_service.py

from flask import Flask, jsonify, request

app = Flask(__name__)

students = {
    '1': {'name': 'Alice', 'grade': 'A'},
    '2': {'name': 'Bob', 'grade': 'B'}
}


@app.route('/')
def home():
    return "students Service is Live!"

@app.route('/students/<id>')
def students(id):
    students_info = students.get(id, {})
    return jsonify(students_info)

# Create (Post) a new students
@app.route('/students', methods=['POST'])
def create_students():
    data = request.json
    new_id = str(len(students) + 1)
    students[new_id] = data
    return jsonify({'message': 'students created successfully', 'students_id': new_id}), 201

# Update (Put) an existing students by its ID
@app.route('/students/<id>', methods=['PUT'])
def update_students(id):
    if id in students:
        data = request.json
        students[id].update(data)
        return jsonify({'message': 'students updated successfully'})
    else:
        return jsonify({'error': 'students not found'}), 404

# Delete (Delete) a students by its ID
@app.route('/students/<id>', methods=['DELETE'])
def delete_students(id):
    if id in students:
        del students[id]
        return jsonify({'message': 'students deleted successfully'})
    else:
        return jsonify({'error': 'students not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    