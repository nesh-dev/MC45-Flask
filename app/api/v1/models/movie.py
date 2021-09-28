from app.db_instance import db
from .user import User

class Movie: 

    def __init__(self, id, title, overview, poster, vote_average, vote_count):
        self.id = id 
        self.title = title
        self.overview = overview
        self.poster = poster 
        self.vote_average = vote_average
        self.vote_count = vote_count


class Post(db.Model): 

    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
