import re, datetime
from flask_restful import reqparse, Resource
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                get_jwt)
from app.db_instance import db
from  ..models.user import User


class RegisterResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True)
    parser.add_argument('password', type=str, required=True)
    parser.add_argument('confirm_password', type=str, required=True)
    parser.add_argument('email', type=str, required=True)
    parser.add_argument('role_id', type=int, required=True)

    def post(self):
        data = RegisterResource().parser.parse_args()
        if not re.match(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                data['email']):
            return {"message": "invalid email"}, 422
        elif len(data['password']) < 6:
            return {"message":
                    "password should atleast six characters long"}
        elif data['username'] == "":
            return {"message": "username should not be empty"}
        elif data['confirm_password'] != data["password"]:
            return {"message": "passwords do not match"}
        # import pdb; pdb.set_trace()
        existing_user = User.query.filter_by(email=data['email']).first()
        
        if existing_user: 
            return {"message": "user already registered"}, 400
        
        hashed_password = generate_password_hash(data['password'], method='sha256')
        user = User(email=data['email'], pass_secure=hashed_password, role_id=data['role_id'])
        db.session.add(user) 
        db.session.commit()
        return {"message": "registration successfully"}, 201

        
class LoginResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True)
    parser.add_argument('password', type=str, required=True)


    def post(self): 
        data = LoginResource().parser.parse_args()
        if not re.match(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                data['email']):
            return {"message": "invalid email"}, 422
        elif len(data['password']) < 6:
            return {"message":
                    "password should atleast six characters long"}
        
        existing_user = User.query.filter_by(email=data['email']).first()
        expires = datetime.timedelta(days=1)
        if check_password_hash(existing_user.pass_secure, data['password']) and existing_user:
            access_token = create_access_token(identity=(existing_user.id, existing_user.role_id), 
                                                    expires_delta=expires)
            return{"access_token": access_token, 
                    "message": "logged in"}, 200

        
        return {"message":"invalid credentials"}, 401
    

    
