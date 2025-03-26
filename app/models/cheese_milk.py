from . import db

class CheeseMilk(db.Model):
    __tablename__ = 'cheese_milks'
    
    id = db.Column(db.Integer, primary_key=True)
    cheese_id = db.Column(db.Integer, db.ForeignKey('cheeses.id'), nullable=False)
    milk_id = db.Column(db.Integer, db.ForeignKey('milks.id'), nullable=False)
    percent = db.Column(db.Integer, nullable=True)  # percent 1 to 100
    
    def __repr__(self):
        return f'<CheeseMilk {self.cheese_id}:{self.milk_id}>'
