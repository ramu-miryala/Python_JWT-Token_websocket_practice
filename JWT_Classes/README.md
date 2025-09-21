## Flask JWT Auth + User Service

This project is a Flask-based backend that demonstrates:

 User registration with password hashing (PostgreSQL + SQLAlchemy)

 JWT authentication (access tokens)

 Basic Authentication for profile access

 Modular structure with Blueprints, Services, and Models

 Multiple services inside one Flask app (/auth and /users)

# Project Structure
JWT_Classes/
│── app.py                # Entry point, app factory
│── config.py             # Configuration (DB, secret key)
│── extensions.py         # SQLAlchemy instance
│
├── models/
│   └── user_model.py     # User model
│
├── services/
│   ├── auth_service.py   # JWT handling
│   └── user_service.py   # User registration & management
│
└── routes/
    ├── auth_routes.py    # Register, verify, profile routes
    └── user_routes.py    # Users listing route

# Setup
1. Clone the repo & navigate
git clone <your_repo_url>
cd flask_jwt_app

2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install flask flask_sqlalchemy psycopg2-binary werkzeug pyjwt

4. Setup PostgreSQL

Create a database:

CREATE DATABASE testdb;


Update config.py if needed:

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost:5432/testdb"

**Run the App**
python app.py


Server runs at:

http://127.0.0.1:5000

# API Endpoints
 Register a User

POST /auth/register

curl -X POST http://127.0.0.1:5000/auth/register \
     -H "Content-Type: application/json" \
     -d '{"email":"test@example.com", "name":"Ramu", "password":"secret"}'


Response:

{
  "message": "User registered successfully",
  "token": "<JWT_TOKEN>"
}

# Verify JWT Token

POST /auth/verify

curl -X POST http://127.0.0.1:5000/auth/verify \
     -H "Authorization: Bearer <JWT_TOKEN>"

# Profile (Basic Auth)

GET /auth/profile

curl -u test@example.com:secret http://127.0.0.1:5000/auth/profile

# Get All Users

GET /users/

curl http://127.0.0.1:5000/users/

# Notes

JWT tokens expire after 1 hour.

Passwords are stored securely using Werkzeug hashing.

User emails must be unique.

# Example Flow

Register → Get token.

Use token for /auth/verify.

Use Basic Auth for /auth/profile.

Fetch all users via /users/.