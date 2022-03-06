from app import db 
from werkzeug.security import generate_password_hash

class Profile(db.Model):
    __tablename__ = "profile"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password_hash = generate_password_hash(password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<Profile {self.username}>"
    