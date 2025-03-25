from datetime import datetime
from . import db

class Platter(db.Model):
    __tablename__ = 'platters'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relations
    platter_cheeses = db.relationship('PlatterCheese', backref='platter', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Platter {self.name}>'
    
    @property
    def total_weight(self):
        return sum(pc.cheese_weight for pc in self.platter_cheeses)
    
    @property
    def total_price(self):
        # cheese.price_per_kg (in centimes)
        # cheese_weight (in grammes)
        return sum(pc.cheese_weight * (pc.cheese.price_per_kg / 100) / 1000 for pc in self.platter_cheeses)
