from app import db 

class Coin(db.Model):
    __tablename_ = "coin"
    id = db.Column(db.Integer, primary_key=True)
    coin_id = db.Column(db.String(64), nullable=False)
    current_value = db.Column(db.Float())
    timestamp = db.Column(db.DateTime())

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def __repr__(self):
        return f"<Coin {self.coin_id} ${self.current_value}"