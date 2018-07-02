import datetime 


def loginUser(loggedIn_lst,user_id,):
    for user_obj in loggedIn_lst:
        if user_obj["user_id"]==user_id:
            user_obj["active"]=1
            user_obj["lastloggedIn"]=datetime.datetime.now()
            return"u are logged in"
        else: 
            data={}
            data["user_id"]=user_id
            data["active"]=1
            data["lastloggedIn"]=datetime.datetime.now()
            info=loggedIn_lst.append(data)
            print("you are logged in")

             




        