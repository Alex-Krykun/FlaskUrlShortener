from src.app import db
from datetime import datetime

class ShortUrls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_id = db.Column(db.String(20), nullable=False, unique=True)
    times_used = db.Column(db.Integer, default=0, nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.now(), nullable=False)
    last_used = db.Column(db.DateTime(), default=datetime.now(), nullable=False)