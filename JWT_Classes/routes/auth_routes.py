from flask import Blueprint, request, jsonify
from services.user_service import UserService
from services.auth_service import AuthService
import base64

auth_bp = Blueprint("auth", __name__)

# Register
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    email, name, password = data.get("email"), data.get("name"), data.get("password")

    if not email or not name or not password:
        return jsonify({"message": "Email, name, and password are required"}), 400

    user, token = UserService.register_user(email, name, password)
    if not user:
        return jsonify({"message": "User already exists"}), 409

    return jsonify({"message": "User registered successfully", "token": token}), 201


# Verify Token
@auth_bp.route("/verify", methods=["POST"])
def verify_token():
    token = None
    auth_header = request.headers.get("Authorization")

    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]
    elif request.is_json:
        token = request.json.get("token")
    elif not token:
        token = request.args.get("token")

    if not token:
        return jsonify({"message": "Token is missing"}), 400

    result = AuthService.verify_token(token)
    if not result["valid"]:
        return jsonify({"message": result["message"]}), 401

    return jsonify({"message": "Token is valid", "payload": result["payload"]}), 200


# Profile (Basic Auth)
@auth_bp.route("/login", methods=["GET"])
def profile():
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Basic "):
        return jsonify({"message": "Missing or invalid Authorization header"}), 401

    try:
        encoded_credentials = auth_header.split(" ")[1]
        decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8")
        email, password = decoded_credentials.split(":")
    except Exception:
        return jsonify({"message": "Invalid Basic Auth format"}), 401

    user = UserService.authenticate_user(email, password)
    if not user:
        return jsonify({"message": "Invalid email or password"}), 401

    return jsonify({"id": user.id, "email": user.email, "name": user.name})
