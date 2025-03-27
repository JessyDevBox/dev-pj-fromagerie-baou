from datetime import datetime
from . import db


class Cheese(db.Model):
    __tablename__ = "cheeses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.Text)
    quality_label = db.Column(db.String(100), default=False)
    is_bio = db.Column(db.Bool, default=False)
    age_days_min = db.Column(db.Integer)  # age in days minimum
    age_days_max = db.Column(db.Integer)  # age in days maximum
    country_code = db.Column(
        db.String(3), default="FR"
    )  # country code with 2, 3 letters
    price_per_kg = db.Column(db.Integer, nullable=False)  # in centimes
    paste_type_id = db.Column(db.Integer, db.ForeignKey("paste_tyep.id"), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relations
    platter_cheeses = db.relationship("PlatterCheese", backref="cheese", lazy=True)
    platter_cheeses = db.relationship("CheeseMilk", backref="cheese", lazy=True)

    def __repr__(self):
        return f"<Cheese {self.name}>"
