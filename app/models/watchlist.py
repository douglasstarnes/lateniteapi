from app import db 

class Watchlist(db.Model):
    __tablename__ = "watchlist"
    id = db.Column(db.Integer, primary_key=True)
    coin_id = db.Column(db.String(64), nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey("profile.id"))
    profile = db.relationship("Profile", backref=("coins"))

    def __init__(self, coin_id, profile):
        self.coin_id = coin_id
        self.profile = profile

    def save(self):
        db.session.add(self)
        db.session.commit()    