# Flask JWT Authentication API

This is a simple Flask-based REST API that provides user registration, login with Basic Authentication, JWT token generation, token verification, and user management.  
It uses PostgreSQL as the database and stores hashed passwords.

---

##  Features

- ✅ User registration
- ✅ User login using Basic Authentication
- ✅ JWT token generation (with HS256 algorithm)
- ✅ JWT token verification endpoint
- ✅ List all registered users
- ✅ Passwords are securely hashed
- ✅ PostgreSQL database integration

---

##  Prerequisites

- Python 3.9+
- PostgreSQL database
- `pip` (Python package manager)

---

##  Project Setup

### 1️⃣ Install Dependencies

```bash
pip install flask flask_sqlalchemy psycopg2-binary werkzeug pyjwt
