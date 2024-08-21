from book_manager import BookManager
from user_manager import UserManager
from checking import CheckManager
from storage import Storage
from logger import logger
class Library:
    def __init__(self,book_manager:BookManager,user_manager:UserManager,check_manager:CheckManager) -> None:
        self.book_manager = book_manager
        self.user_manager = user_manager
        self.check_manager = check_manager

    def check_out_book(self,isbn,user_id):
        self.check_manager.add_check_in(user_id,isbn)
        self.book_manager.books.loc[self.book_manager.books["ISBN"]==isbn,"Availability"] = False
        self.book_manager.books.to_csv("DATA/Books.csv",index=False)
        logger.info("Book Checked out")
        return True
        # self.user_manager.users[self.user_manager.users["User_id"]==user_id]["Books_issued"].append(isbn)


    def check_in_book(self,isbn):
        user_id=self.check_manager.check[self.check_manager.check["ISBN"] == isbn]["User_id"]
        self.check_manager.remove_check_in(isbn)
        self.book_manager.books.loc[self.book_manager.books["ISBN"]==isbn,"Availability"] = True
        self.book_manager.books.to_csv("DATA/Books.csv",index=False)
        logger.info("Book Checked in")
        return True
        # self.user_manager.users[self.user_manager.users["User_id"]==user_id]["Books_issued"].remove(isbn)

    def check_availability(self,name):
        return self.book_manager.books[self.book_manager.books['Title']==name]['Availability']


# if __name__=="__main__":
#     storage=Storage()
#     obj=Library(BookManager(storage),UserManager(storage),CheckManager(storage))
#     obj.check_out_book(1,"id2")
#     obj.check_in_book(2)
#     print(obj.book_manager.books)
    # print(obj.check_availability("book1"))