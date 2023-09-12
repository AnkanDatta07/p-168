# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:27:53 2023

@author: Ankan Datta
"""

class Books:
    def _init_(self,name,price,author,publish):
        self.book_price = price
        self.book_name = name
        self.book_author = author
        self.book_publish = publish
            
    def add_book(self):
        print("Name: "+self.book_name)
        print("Price: "+str(self.book_price))
        print("Author Of book: "+self.book_author)
        print("Book published in : "+self.book_publish)
        print("Book Added")
            
            
book1 = Books("HarryPotter and Philosopher's stone", 1928,"J.K.Rowling", "1997")
book1.add_book()

book2 = Books("Diary Of Wimpy Kid", 700, "Jeff Kinney", "2017")
book2.add_book()