from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    rights = db.Column(db.Integer, default=1)  # 1: customer, 5: manager, 9: admin
    description = db.Column(db.Text)        # Jessy Added
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relations
    platters = db.relationship('Platter', backref='client', lazy=True)
    messages = db.relationship('Message', backref='user', lazy=True)
    discussions = db.relationship('Discussion', backref='creator', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username}>'
