from ..repository.mongo_repository import save,find,count
from ..models.users_model import UsersModel
from flask_jwt_extended import create_access_token
from flask import request,jsonify
from werkzeug.security import generate_password_hash,check_password_hash
import json

def create_user():
    try:
        newUser=UsersModel(request.get_json())
        newUser.password=generate_password_hash(newUser.password)
        findUser=count(email=newUser.email)
        if findUser==0:
            save(newUser)
            return jsonify({'message':'User registered successfully','status':201})
        else:
            return jsonify({'error':'email already registered!'})
    except:
        return jsonify({"error":"an error has ocurred while trying creating user!"})

    

def find_by_filter(**kwargs):
    try:
        return find(**kwargs)
    except:
        jsonify({'error':'An error has ocurred while retrieving data!'})


def login_user():
    try:
        email=request.json.get("email",None)
        password=request.json.get("password",None)
        findUser=find(email=email)
        findUser_obj=json.loads(findUser)
        if len(findUser_obj)>0:
            checkPassword=check_password_hash(findUser_obj[0]["password"],password)
            if not checkPassword:
                return jsonify({'error':'wrong email or password.!'})
            else:
                access_token=create_access_token(identity=email)
                return jsonify({"token":access_token})
        else:
            return jsonify({'error':'wrong email or password.!'})
    except:
        return jsonify({'error':'Internal server error!'})
    
