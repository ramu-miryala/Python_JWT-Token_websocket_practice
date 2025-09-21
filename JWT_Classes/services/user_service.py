from werkzeug.security import generate_password_hash, check_password_hash
from models.user_model import User
from extensions import db
from services.auth_service import AuthService

class UserService:
    @staticmethod
    def register_user(email, name, password):
        if User.query.filter_by(email=email).first():
            return None, "User already exists"

        hashed_password = generate_password_hash(password)
        user = User(email=email, name=name, password=hashed_password)

        db.session.add(user)
        db.session.commit()

        token = AuthService.generate_token(user)
        return user, token

    @staticmethod
    def authenticate_user(email, password):
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return None
        return user

    @staticmethod
    def get_all_users():
        return User.query.all()
