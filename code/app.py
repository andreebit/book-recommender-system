from utils import recommender
from models import book
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(data={'university': 'UPC - Exígete, innova!', 'course': 'Inteligencia Artificial'})


@app.route('/books')
def books():
    return jsonify(data=book.get_all())


@app.route('/books/<book_id>')
def books_item(book_id):
    return jsonify(data=book.get_by_id(book_id))


@app.route('/books/<book_id>/recommendations')
def recommendations(book_id):
    book_item = book.get_by_id(book_id)
    return jsonify(data=recommender.recommendations(book_item['title']))