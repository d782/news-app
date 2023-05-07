
class UsersModel():
    name=None
    age=None
    email=None
    password=None
    city=None
    country=None
    telephone=None
    address=None
    
    def __init__(self,newUser) -> None:
        self.name=newUser['name']
        self.age=newUser['age']
        self.email=newUser['email']
        self.password=newUser['password']
        self.city=newUser['city']
        self.country=newUser['country']
        self.telephone=newUser['telephone']
        self.address=newUser['address']
        
    def get_user_as_dict(self):
        return dict({
           "name":self.name,
           "age":self.age,
           "email":self.email,
           "password":self.password,
           "city":self.city,
           "country":self.country,
           "telephone":self.telephone,
           "address":self.address, 
        })