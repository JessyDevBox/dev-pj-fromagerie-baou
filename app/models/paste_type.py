from datetime import datetime
from . import db


class PasteType(db.Model):
    __tablename__ = "paste_types"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relations
    platter_cheeses = db.relationship(
        "CheeseMilk", backref="cheese", lazy=True, cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<PasteType {self.name}>"
