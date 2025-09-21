class Config:
    SECRET_KEY = "user-secret-key"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost:5432/testdb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
