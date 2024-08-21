from storage import Storage
import pandas as pd

class UserManager:
    def __init__(self, storage:Storage):
        self.storage = storage
        self.users = self.storage.load_users_data()

    def add_user(self,user_id,name):
        new_row=pd.DataFrame([[user_id,name]], columns=["User_id","Name"])
        self.users=pd.concat([self.users,new_row],axis=0,ignore_index=True)
        self.users.to_csv("DATA/Users.csv",index=False)


    def update_user(self,user_id,name):
        if name:
            self.users.loc[self.users["User_id"]==user_id,"Name"] = name

        self.users.to_csv("DATA/Users.csv",index=False)

    def delete_user(self,user_id):
        self.users = self.users.drop(self.users[self.users['User_id'] == user_id].index)
        self.users.to_csv("DATA/Users.csv",index=False)

    def list_users(self):
        return self.users
    
    def find_user_by_id(self,user_id):
        return self.users[self.users['User_id']==user_id]
    


# if __name__=="__main__":
#     obj=UserManager(Storage())

#     obj.add_user('id1',"person1")
    
    # obj.delete_user(user_id="id1")

#     print(obj.list_users())