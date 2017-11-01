# Book Shelf

This project was made to understand the basics of webscraping and using the data for something useful. I have a lot of books and novels
at home . Having to keep track of all the books is very difficult . Many of the old books have no proper cover page or last pages and have no description . So i 
am making a software that would extract all the relevant information about the book (name, author ,description and rating) from "goodreads.com".
The data extracted is stored in a db . I am also adding the functionalitiy of searching the db when offline .

The basic steps in the working of the software is as following :

1.Input from user

    > Text Input : The input can be in the form of keywords given by the user . The input is then sent to the goodreads website which then
                    returns alist of book relevent to the given keywords.
      
    > Cover search : The main idea behind input is using the coverpage of the book to find the name of the book without having to type a 
                      big name( Yes i am very lazy ) . The image taken from a webcam or any image file is sent to Goole reverse image 
                      search.The text given in " Best guess for this image " is taken as a keyword for searching in the 'goodreads' website.
                      
2.Selection of the book from the list.
    
    The user can select the required book from the list returned by the website. On selection of the book , the data about the book is
    extracted  and shown to the user. The user can add the book to the database . 
    
Important feature that can be added :

1. Exception handling .
2. Saving the book cover thumbnail in the db.
3. Input sanitization.
4. Whether the books have been lent to someone or not.
5. UI for the software.

    
    
