import jwt
import datetime
from flask import current_app

class AuthService:
    @staticmethod
    def generate_token(user):
        payload = {
            "user_id": user.id,
            "email": user.email,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        token = jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")
        return token

    @staticmethod
    def verify_token(token):
        try:
            payload = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            return {"valid": True, "payload": payload}
        except jwt.ExpiredSignatureError:
            return {"valid": False, "message": "Token has expired"}
        except jwt.InvalidTokenError as e:
            return {"valid": False, "message": str(e)}
