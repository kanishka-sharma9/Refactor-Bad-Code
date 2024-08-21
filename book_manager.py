from storage import Storage
import pandas as pd
class BookManager:
    def __init__(self,storage:Storage) -> None:
        self.storage=storage
        self.books=self.storage.load_books_data()

    def add_book(self, title, author, isbn):
        new_row=pd.DataFrame(data=[[title,author,isbn,True]],columns=["Title","Author","ISBN","Availability"])
        self.books=pd.concat([self.books,new_row],axis=0,ignore_index=True)
        self.books.to_csv("DATA/Books.csv",index=False)
    
    def update_books(self,isbn,title,author):
        if title:
            self.books.loc[self.books["ISBN"]==isbn,"Title"] = title
        if author:
            self.books.loc[self.books["ISBN"]==isbn,"Author"] = author

        self.books.to_csv("DATA/Books.csv",index=False)

    def delete_books(self,isbn):
        self.books = self.books.drop(self.books[self.books['ISBN'] == isbn].index)
        self.books.to_csv("DATA/Books.csv",index=False)

    def list_books(self):
        return self.books
    
    def find_books_by_isbn(self, isbn):
        df=self.books
        return df[df["ISBN"]==isbn]
    
    def find_books_by_title(self, title):
        df=self.books
        return df[df["Title"]==title]

    def find_books_by_author(self, author):
        df=self.books
        return df[df["Author"]==author]

if __name__=="__main__":
    obj=BookManager(Storage())
    # print(obj.find_book_by_isbn(1))
    obj.update_books(1,"BOoK1","")

    # obj.update_books()