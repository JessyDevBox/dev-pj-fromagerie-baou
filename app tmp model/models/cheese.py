# app/models/cheese.py
from datetime import datetime
from app import db


class Cheese(db.Model):
    __tablename__ = "cheeses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    cheese_type_id = db.Column(
        db.Integer, db.ForeignKey("cheese_type.id"), nullable=False
    )

    # Relation avec le modèle User
    user = db.relationship("CheeseType", backref=db.backref("cheeses", lazy=True))

    def __repr__(self):
        return f"<Cheese {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "cheese_type_id": self.cheese_type_id,
        }
