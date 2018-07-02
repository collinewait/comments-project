import datetime
from validate import loginUser
dic=[]
class accounts:
    container=[]
    loggedIn=[{"user_id":0,"active":"0","lastloggedIn":datetime.datetime.now()}]
    def __init__(self,_id,name,password,username,account_type="normal"):
        self._id=_id
        self.name=name
        self.password=password
        self.username=username
        self.account_type=account_type
    def create_account(self):
        created_user={}
        account=accounts(self._id,self.name,self.password,self.username,self.account_type)
        created_user=account.__dict__ 
        account.container.append(created_user)
    def login(self,username,password):
        active={}
        for user_obj in accounts.container:
            if user_obj["username"]==username and user_obj["password"]==password:
                user_id=user_obj["_id"]
                info=accounts.loginUser(loggedIn,user_id)
                return info
                
                
