from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

import jwt
import datetime
import base64


# ------------------------------
# Flask App Configuration
# ------------------------------
app = Flask(__name__)
app.config['SECRET_KEY'] = 'user-secret-key'  # secret-key
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/testdb' #database url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ------------------------------
# User Model
# ------------------------------
class User(db.Model):

    __tablename__ = 'users'  #table name
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(200), nullable=False)  # Hashed password

# Create tables if they don't exist
with app.app_context():
    db.create_all()


# ------------------------------
# JWT Token Generator
# ------------------------------
def generate_token(user):
    payload = {
        'user_id': user.id,
        'email': user.email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token


# ------------------------------
# JWT Token Verifier (Optional)
# ------------------------------
@app.route('/verify', methods=['POST'])
def verify_token_route():
    token = None

    # Check Authorization header first (Bearer token)
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith('Bearer '):
        token = auth_header.split(' ')[1]

    # Or, allow token in JSON body
    if not token and request.is_json:
        token = request.json.get('token')

    # Or, allow token as a query parameter
    if not token:
        token = request.args.get('token')

    if not token:
        return jsonify({'message': 'Token is missing'}), 400

    # Now try to verify the token
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return jsonify({'message': 'Token is valid', 'payload': payload}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired'}), 401
    except jwt.InvalidTokenError as e:
        return jsonify({'message': 'Invalid token', 'error': str(e)}), 401



# ------------------------------
# Register Route (POST)
# ------------------------------
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    name = data.get('name')
    password = data.get('password')

    if not email or not name or not password:
        return jsonify({'message': 'Email, name, and password are required'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'User already exists'}), 409

    hashed_password = generate_password_hash(password)

    user = User(email=email, name=name, password=hashed_password)
    db.session.add(user)
    db.session.commit()

    token = generate_token(user)
    return jsonify({'message': 'User registered successfully', 'token': token})


# ------------------------------
# Basic Auth Protected Profile (GET)
# ------------------------------
@app.route('/profile', methods=['GET'])
def profile_basic():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Basic '):
        return jsonify({'message': 'Missing or invalid Authorization header'}), 401

    try:
        # Decode Basic Auth credentials
        encoded_credentials = auth_header.split(' ')[1]
        decoded_credentials = base64.b64decode(encoded_credentials).decode('utf-8')
        email, password = decoded_credentials.split(':')
    except Exception:
        return jsonify({'message': 'Invalid Basic Auth format'}), 401

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid email or password'}), 401

    return jsonify({'id': user.id, 'email': user.email, 'name': user.name,'password':user.password})

# ------------------------------
# Get All Users 
# ------------------------------
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [{
        'id': user.id,
        'email': user.email,
        'name': user.name
    } for user in users]

    return jsonify(user_list)

# ------------------------------
# Run App
# ------------------------------
if __name__ == '__main__':
    app.run(debug=True)
