from storage import Storage
import pandas as pd
from logger import logger
class CheckManager:
    def __init__(self,storage:Storage) -> None:
        self.storage=storage
        self.check=self.storage.load_checking_data()

    def add_check_in(self,user_id,isbn):
        new_row=pd.DataFrame([[user_id,isbn]], columns=["User_id","ISBN"])
        self.check=pd.concat([self.check,new_row],ignore_index=True)
        self.check.to_csv("DATA/Check.csv",index=False)
        

    def remove_check_in(self,isbn):
        self.check = self.check.drop(self.check[self.check['ISBN'] == isbn].index)
        self.check.to_csv("DATA/Check.csv",index=False)

