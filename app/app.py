from flask import Flask
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager

#blueprints imports
from users.routes import users_router

def application():
    #app
    app=Flask(__name__,instance_relative_config=True)

    #config
    
    app.config.from_object('config.Config')

    #dependencies
    db=MongoEngine(app)
    jwt=JWTManager(app)

    #blueprints
    app.register_blueprint(users_router,url_prefix='/users')

    return app
        
if __name__ =='__main__':
    application().run()

