from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Base URL of the Book Management API
BOOK_API_URL = 'http://127.0.0.1:5000/books'

# Route to get all books
@app.route('/consumer/books', methods=['GET'])
def get_books():
    response = requests.get(BOOK_API_URL)
    return jsonify(response.json()), response.status_code

# Route to get a single book by ID
@app.route('/consumer/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    response = requests.get(f"{BOOK_API_URL}/{book_id}")
    return jsonify(response.json()), response.status_code

# Route to add a new book
@app.route('/consumer/books', methods=['POST'])
def add_book():
    new_book = request.json
    response = requests.post(BOOK_API_URL, json=new_book)
    return jsonify(response.json()), response.status_code

# Route to update an existing book
@app.route('/consumer/books/<int:book_id>', methods=['PATCH'])
def update_book(book_id):
    update_data = request.json
    response = requests.patch(f"{BOOK_API_URL}/{book_id}", json=update_data)
    return jsonify(response.json()), response.status_code

# Route to delete a book
@app.route('/consumer/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    response = requests.delete(f"{BOOK_API_URL}/{book_id}")
    return '', response.status_code

if __name__ == '__main__':
    app.run(debug=True, port=5001)
