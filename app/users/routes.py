from flask import Blueprint
from flask import request,jsonify

from .use_cases.use_cases import create_user,login_user

users_router=Blueprint('users',__name__)

@users_router.route('/login',methods=["POST"])
def login():
    return login_user()

@users_router.route('/sign-up',methods=["POST"])
def sign_up():
    return create_user()