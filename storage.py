import pandas as pd
from logger import logger
class Storage:
    def __init__(self,book_file_path="DATA/Books.csv", user_file_path="DATA/Users.csv",checking_file_path="DATA/Check.csv") -> None:
        self.bfp=book_file_path
        self.ufp=user_file_path
        self.cfp=checking_file_path

    def load_books_data(self):
        try:
            df=pd.read_csv(self.bfp)
            logger.info('Book data loaded')
            return df            
        except Exception as e:
            raise e
        
    def load_users_data(self):
        try:
            df=pd.read_csv(self.ufp)
            logger.info("user data loaded")
            return df
        except Exception as e:
            raise e
        
    def load_checking_data(self):
        try:
            df=pd.read_csv(self.cfp)
            logger.info("Checking data loaded")
            return df
        except Exception as e:
            raise e
        


        
# if __name__=="__main__":
#     obj=Storage()
#     df=obj.load_books_data()
#     for row in df.itertuples():
#         print(row)