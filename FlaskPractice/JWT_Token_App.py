from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import jwt
import datetime

# Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hi_123'  # Change this in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/testdb'
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)

# Create tables
with app.app_context():
    db.create_all()

# Generate JWT token
def generate_token(user):
    payload = {
        'user_id': user.id,
        'email': user.email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token

# Decode and verify JWT
def verify_token(token):
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

# Register API: Store user and return token
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    name = data.get('name')

    if not email or not name:
        return jsonify({'message': 'Email and name are required'}), 400

    # Check if user already exists
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'User already exists'}), 409

    user = User(email=email, name=name)
    db.session.add(user)
    db.session.commit()

    token = generate_token(user)
    return jsonify({'token': token})

# Protected route example
@app.route('/profile', methods=['GET'])
def profile():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({'message': 'Missing token'}), 401

    try:
        token = auth_header.split(" ")[1]  # "Bearer <token>"
    except IndexError:
        return jsonify({'message': 'Token format is invalid'}), 401

    payload = verify_token(token)
    if not payload:
        return jsonify({'message': 'Invalid or expired token'}), 401

    user = User.query.get(payload['user_id'])
    if not user:
        return jsonify({'message': 'User not found'}), 404

    return jsonify({'id': user.id, 'email': user.email, 'name': user.name})

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = []

    for user in users:
        user_data = {
            'id': user.id,
            'email': user.email,
            'name': user.name
        }
        user_list.append(user_data)

    return jsonify(user_list)


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
