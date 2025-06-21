from flask import Flask
from flask_cors import CORS
from routes.book_routes import book_api  # ✅ Import your routes

app = Flask(__name__)
CORS(app)

app.register_blueprint(book_api)  # ✅ Register routes

@app.route("/")
def home():
    return "Book Review API is running!"

@app.route("/test-mongo")
def test_mongo():
    from utils.db import books_collection
    book = books_collection.find_one()
    if book:
        return {"message": "MongoDB connected!", "sample_book": book["title"]}
    return {"message": "MongoDB connected, but no books yet!"}

if __name__ == "__main__":
    app.run(debug=True)
