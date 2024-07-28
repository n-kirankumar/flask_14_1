from flask import Flask, request, jsonify, abort
import json

app = Flask(__name__)


# Load books from a JSON file
def load_books():
    with open('books.json', 'r') as f:
        return json.load(f)


# Save books to a JSON file
def save_books(books):
    with open('books.json', 'w') as f:
        json.dump(books, f, indent=4)


# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    books = load_books()
    return jsonify(books)


# Get a single book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    books = load_books()
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        abort(404)
    return jsonify(book)


# Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.json
    books = load_books()
    new_book['id'] = books[-1]['id'] + 1 if books else 1
    books.append(new_book)
    save_books(books)
    return jsonify(new_book), 201


# Update an existing book
@app.route('/books/<int:book_id>', methods=['PATCH'])
def update_book(book_id):
    books = load_books()
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        abort(404)

    data = request.json
    book.update(data)
    save_books(books)
    return jsonify(book)


# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    books = load_books()
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        abort(404)

    books.remove(book)
    save_books(books)
    return '', 204


if __name__ == '__main__':
    app.run(debug=True, port=5000)
