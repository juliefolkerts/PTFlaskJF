from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book/<int:book_number>')
def book(book_number):
    book_file = f'k{book_number}.html'
    if os.path.exists(os.path.join('books', book_file)):
        return send_from_directory('books', book_file)
    else:
        return "Book not found", 404

if __name__ == '__main__':
    app.run(debug=True)