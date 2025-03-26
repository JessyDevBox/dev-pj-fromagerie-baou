from datetime import datetime
from . import db

class Milk(db.Model):
    __tablename__ = 'milks'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relations
    platter_cheeses = db.relationship('CheeseMilk', backref='milk', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Milk {self.name}>'
