import os

from dotenv import load_dotenv

load_dotenv()
class DevConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///data.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "yekterces"

class DevPsqlConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:PA55word@localhost/late_nite_api"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "yekterces"

class ProdConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get("POSTGRES_CON_STR")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "yekterces"