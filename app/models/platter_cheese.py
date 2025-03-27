from . import db


class PlatterCheese(db.Model):
    __tablename__ = "platter_cheeses"

    id = db.Column(db.Integer, primary_key=True)
    platter_id = db.Column(db.Integer, db.ForeignKey("platters.id"), nullable=False)
    cheese_id = db.Column(db.Integer, db.ForeignKey("cheeses.id"), nullable=False)
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), nullable=True
    )  # Jessy Added
    cheese_weight = db.Column(db.Float, nullable=False)  # weight in grammes

    def __repr__(self):
        return f"<PlatterCheese {self.platter_id}:{self.cheese_id}>"
