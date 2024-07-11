from app import db

class Cookies(db.Model):
    __tablename__ = 'cookies'

    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(100))
    http_only = db.Column(db.Boolean)
    name = db.Column(db.String(100))
    path = db.Column(db.String(100))
    same_site = db.Column(db.String(100))
    secure = db.Column(db.Boolean)
    value = db.Column(db.String(100))
    updated_at = db.Column(db.DateTime)

    def __repr__(self) -> str:
        return f"Token INIT: {self.updatedAt}"
    