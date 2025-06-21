from flask import Blueprint, request, jsonify
from bson import ObjectId
from utils.db import books_collection

book_api = Blueprint("book_api", __name__)

# Serializer
def serialize_book(book):
    return {
        "id": str(book["_id"]),
        "title": book["title"],
        "author": book["author"],
        "published_year": book["published_year"],
        "reviews": book.get("reviews", [])
    }

# GET /books - Get all books
@book_api.route("/books", methods=["GET"])
def get_books():
    books = books_collection.find()
    return jsonify([serialize_book(book) for book in books])

# POST /books - Add a new book
@book_api.route("/books", methods=["POST"])
def add_book():
    data = request.json
    new_book = {
        "title": data["title"],
        "author": data["author"],
        "published_year": data["published_year"],
        "reviews": []
    }
    result = books_collection.insert_one(new_book)
    return jsonify({"message": "Book added", "id": str(result.inserted_id)}), 201

# PUT /books/<id> - Update a book
@book_api.route("/books/<id>", methods=["PUT"])
def update_book(id):
    data = request.json
    books_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    return jsonify({"message": "Book updated"})

# DELETE /books/<id> - Delete a book
@book_api.route("/books/<id>", methods=["DELETE"])
def delete_book(id):
    books_collection.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Book deleted"})

# POST /books/<id>/reviews - Add a review
@book_api.route("/books/<id>/reviews", methods=["POST"])
def add_review(id):
    data = request.json
    review = {
        "reviewer": data["reviewer"],
        "comment": data["comment"],
        "rating": data["rating"]
    }
    books_collection.update_one(
        {"_id": ObjectId(id)},
        {"$push": {"reviews": review}}
    )
    return jsonify({"message": "Review added"})
