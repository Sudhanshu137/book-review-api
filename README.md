# 📚 Book Review API

This is a simple Book Review REST API built using **Flask** and **MongoDB** as part of the Keploy API Fellowship.

---

## 🚀 Features

- Create, Read, Update, and Delete books
- Add reviews to books
- MongoDB for data storage
- Clean API structure using Flask Blueprints

---

## 🛠️ Tech Stack

- Backend: Flask (Python)
- Database: MongoDB Atlas
- REST API: JSON over HTTP
- Tools: Postman for testing, Python-dotenv for config

---

## 📦 API Endpoints

### 📚 Books

| Method | Endpoint           | Description             |
|--------|--------------------|-------------------------|
| GET    | `/books`           | Get all books           |
| POST   | `/books`           | Add a new book          |
| PUT    | `/books/<id>`      | Update a book           |
| DELETE | `/books/<id>`      | Delete a book           |

### ⭐ Reviews

| Method | Endpoint                    | Description          |
|--------|-----------------------------|----------------------|
| POST   | `/books/<id>/reviews`       | Add a review to book |

---

## ⚙️ How to Run the Server

1. Clone this repository:
```bash
git clone https://github.com/your-username/book-review-api.git
cd book-review-api
