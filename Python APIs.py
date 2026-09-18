from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set up database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)


# Book Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publisher = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'{self.book_name} - {self.author} - {self.publisher}'


# READ - Get all books
@app.route('/books')
def get_books():
    books = Book.query.all()
    output = []

    for book in books:
        book_data = {
            'id': book.id,
            'book_name': book.book_name,
            'author': book.author,
            'publisher': book.publisher
        }

        output.append(book_data)

    return {'books': output}


# READ - Get one book
@app.route('/books/<int:id>')
def get_book(id):
    book = Book.query.get_or_404(id)

    return {
        'id': book.id,
        'book_name': book.book_name,
        'author': book.author,
        'publisher': book.publisher
    }


# CREATE - Add a book
@app.route('/books', methods=['POST'])
def add_book():
    book = Book(
        book_name=request.json['book_name'],
        author=request.json['author'],
        publisher=request.json['publisher']
    )

    db.session.add(book)
    db.session.commit()

    return {
        'message': 'Book added successfully',
        'id': book.id
    }


# UPDATE - Update a book
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)

    book.book_name = request.json['book_name']
    book.author = request.json['author']
    book.publisher = request.json['publisher']

    db.session.commit()

    return {'message': 'Book updated successfully'}


# DELETE - Delete a book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)

    db.session.delete(book)
    db.session.commit()

    return {'message': 'Book deleted successfully'}


# Create database and Book table
with app.app_context():
    db.create_all()


# Run Flask application
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
