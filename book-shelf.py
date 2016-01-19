__author__ = 'ANI'

try   :
    import requests
    from bs4 import BeautifulSoup
    import sqlite3
    import time

# This import statement is to disable urllib3 'insecure platform warning' exception.
    import requests.packages.urllib3
    requests.packages.urllib3.disable_warnings()

except :
     print "Error in importing the modules \n"

print("------BOOKSHELF------")

#-----------------------------------------------------------------------------------------------------------------------
# Makes use of pygame image module to capture the image of the book cover using the webcam and saved.
# The captured image path can be used as the input parameter to the cover_find() function.
def img_capture():

    try:
        import pygame.camera

    except:
        print " Error in importing pygame.camera"

    try:
        pygame.camera.init()
        cam = pygame.camera.Camera(0,(640,480))
        print "Hold the book cover toward the webcam"
        time.sleep(3)
        print "Capturing image"
        cam.start()
        img = pygame.Surface((640,480))
        cam.get_image(img)
        cover_img = pygame.image.save(img, "img.jpg")
        cam.stop()
        time.sleep(2)
        print "Image captured successfully"
        print "\n"

    except:
        print "There was some problem in capturing the image"


#-----------------------------------------------------------------------------------------------------------------------
# This function takes in the path to the cover image of the book as the input parameter.
# This image is sent to the google reverse image search engine.
#  The value returned by the reverse image search is returned by the function.
def cover_find(filePath):

    searchUrl = 'http://www.google.hr/searchbyimage/upload'
    multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}

    response = requests.post(searchUrl,files = multipart,allow_redirects=False)
    url2 = response.headers['Location']

    # If proper headers are not given google reverse search returns an empty list. So to get the reverse search name
    # always use the proper headers.
    headers = {'user-agent':"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"}

    r1 = requests.get(url2, headers = headers)
    data1 = r1.text
    soup1 = BeautifulSoup(data1,"html.parser")

    img_reverse = soup1.find_all("a",{"class":"_gUb"})
    imgsch_name= img_reverse[0].text
    #The data that is extracted is of type 'unicode' .This must be converted to 'string 'before passing it to search() fn.
    return str(imgsch_name)

#-----------------------------------------------------------------------------------------------------------------------

def search(book_name):

    # The input is taken in by the user either by text input  or by the 'text input field' or
    # the 'imgsch_name' returned by reverse search image of the book cover.

    headers = {'user-agent':"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"}
    para = {"q":book_name,"search_type":"books"}
    r =requests.get("https://www.goodreads.com/search?utf8=?",params=para,headers=headers)

    data = r.text
    soup = BeautifulSoup(data,"html.parser")

    search_result=soup.find_all("a",{"class":"bookTitle"})
    search_list = []
    search_url = []

    for i in search_result:
        temp_title = i.span.text
        search_list.append(temp_title)
        search_url.append(i.get("href"))

        print str(search_result.index(i)+1)+ " " + temp_title
    return search_list,search_url

#-----------------------------------------------------------------------------------------------------------------------
# Extracts the required data about the book from 'goodreads.com '.
# The data is returned by the function in a list.
def book_data():

    book_desc = []

    author_name = soup.find_all("span",{"itemprop":"name"})
    book_desc.append(author_name[0].text)

    cover_name = soup.find_all("h1",{"id":"bookTitle"})
    book_desc.append(cover_name[0].text)

    description = soup.find_all("div" , {"id" : "description"})
    book_desc.append(description[0].text)

    rating = soup.find_all("span" , {"class" : "average"})
    book_desc.append(rating[0].text)

    img_url = soup.find_all("img",{"id":"coverImage"})
    book_desc.append(img_url)

    return book_desc

#-----------------------------------------------------------------------------------------------------------------------
def main():

    print "How may i help you ? \n" \
          "1. Book name \n" \
          "2. Cover Image \n" \
          "3. My books \n"

    selection = raw_input("Type the option number : ")

    try :
        if int(selection) == 1 :
            input_name = raw_input(" What is the name of the book : ")
            print("\n")

            ret_list,ret_url = search(input_name)

            print ("\n")
            option_sel = raw_input("Select the appropriate book : ")
            return option_sel

            book_sel =  ret_list[int(option_sel)-1]
            sel_bookurl = "https://www.goodreads.com" + ret_url[int(option_sel)-1]

            print book_sel,sel_bookurl








        if int(selection) == 2 :
            #img = img_capture()
            #img_path= os.path.abspath(img)

            ret_name = cover_find(filePath="img.jpg")
            search(book_name=ret_name)

            print "\n"
            book_name = raw_input("Select the appropriate book number : ")




        if int(selection) == 3:
            pass

    except:
        print "Not a valid input"


#-----------------------------------------------------------------------------------------------------------------------
# This function creates a new database named 'book.db'
# In case the database already exists the connection to the db is made.
def book_db():

    conn = sqlite3.connect(r"D:\PYTHON\book.db")

    cur = conn.cursor()

    try:
        cur.execute(""" CREATE TABLE BOOK
         (
           NAME           TEXT    NOT NULL,
           AUTHOR         TEXT    NOT NULL,
           DESCRIPTION    CHAR(50),
           RATING         DECIMAL  );
            """)

    except:

        return conn,cur

#-----------------------------------------------------------------------------------------------------------------------

if __name__=="__main__":

    main()



