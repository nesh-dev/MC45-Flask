import pdb
from app.api.v1.models.user import User
from flask_restful import reqparse, Resource
from flask_jwt_extended import (get_jwt_identity, jwt_required)
from ..middleware.auth_perm import admin_only
from ..models.movie import Post
from app.db_instance import db

class MoviesResource(Resource): 
    parser = reqparse.RequestParser()
  
    parser.add_argument("title", type=str, required=True)
    parser.add_argument("content", type=str, required=True)

    @jwt_required()
    def post(self):
        data = MoviesResource().parser.parse_args()
  
        current_user = get_jwt_identity()
        user_id = current_user[0]
 
        post = Post(user_id=user_id, title=data['title'], content=data['content'])
        db.session.add(post) 
        db.session.commit()
        return { "data": { "id": post.id, "title": post.title, "content": post.content } }, 201
        

class MovieResource(Resource):

    @admin_only
    def delete(self, id): 
        post_to_delete = Post.query.filter_by(id=id).first()
        if post_to_delete: 
            db.session.delete(post_to_delete)
            db.session.commit()
            return { "message": " post has successfully been deleted" }, 202
        return {"message": "post does not exist"}, 404
