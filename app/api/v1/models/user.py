from sqlalchemy.orm import backref
from app.db_instance import db
from .role import Role 

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(25), unique=True, nullable=False)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))
    posts = db.relationship('Post', backref='owner', lazy='dynamic')
    
    def __repr__(self):
        return f'User {self.username}'

