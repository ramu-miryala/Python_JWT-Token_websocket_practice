from flask import Blueprint, jsonify
from services.user_service import UserService

user_bp = Blueprint("users", __name__)

@user_bp.route("/", methods=["GET"])
def get_users():
    users = UserService.get_all_users()
    user_list = [{"id": u.id, "email": u.email, "name": u.name} for u in users]
    return jsonify(user_list)
