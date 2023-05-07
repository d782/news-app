from ..schema.users_schema import User
from ..models.users_model import UsersModel

def save(U:UsersModel):
    newUser=U.get_user_as_dict()
    name=newUser["name"]
    age=newUser["age"]
    email=newUser["email"]
    password=newUser["password"]
    city=newUser["city"]
    country=newUser["country"]
    telephone=newUser["telephone"]
    address=newUser["address"]
    
    saveUser=User(name=name,age=age,email=email,password=password,city=city,country=country,telephone=telephone,address=address)
    saveUser.save()


def find(**kwargs):
    results=User.objects(**kwargs).to_json()
    return results

def count(**kwargs):
    results=User.objects(**kwargs).count()
    return results