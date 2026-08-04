
from extensions import db
from datetime import datetime


class Inquiry(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), nullable=False)

    subject = db.Column(db.String(200), nullable=False)

    summary = db.Column(db.Text)

    category = db.Column(db.String(100))

    priority = db.Column(db.String(30))

    department = db.Column(db.String(100))

    message = db.Column(db.Text, nullable=False)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    status = db.Column(
        db.String(30),
        default="Pending"
    )