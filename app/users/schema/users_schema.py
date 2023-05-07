import mongoengine as me

class User(me.Document):
    name=me.StringField(required=True)
    age=me.IntField()
    email=me.StringField(required=True)
    password=me.StringField(required=True)
    city=me.StringField(required=True)
    country=me.StringField(required=True)
    telephone=me.StringField(required=True)
    address=me.StringField(required=True)
