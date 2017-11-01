import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

key = # Add key here
secret = # Add Secret here


def getBookList(name):

    search_url = "https://www.goodreads.com/search/index.xml"
    querystring = {"key": key, "q": name}

    headers = {
        'cache-control': "no-cache",
        'postman-token': "633584f1-6707-fd7f-8480-f83077f162f4"
    }

    response = requests.request("GET", search_url, headers=headers, params=querystring)
    return response.text


def parseXMLForBookSearch(xmlData):

    returnList = {}
    root = ET.fromstring(xmlData)
    for child in root.iter('work'):
        book_data = {}
        tempBook = child.find('best_book')

        book_data["title"] = tempBook.find('title').text
        book_data["author"] = tempBook.find('author').text
        book_data["img"] = tempBook.find('image_url').text
        book_data["rating"] = child.find('average_rating').text

        returnList[tempBook.find('title').text] = book_data

    return returnList


def getSelectedBookDetails(valDict , selectedBook):

    outputDict = valDict[selectedBook]
    return outputDict

#-----------------------------------------------------------------------------------------------------------------------
# This function takes in the path to the cover image of the book as the input parameter.
# This image is sent to the google reverse image search engine.
#  The value returned by the reverse image search is returned by the function.
def imgReverseSearch(filePath):

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


def sanitizeInputText(txt):
    splitText = txt.split(' ')

    removeWordList = ['cover']

    for word in splitText:
        if word in removeWordList:
            print("---")
    return splitText


if __name__ == "__main__":

    rev_img = imgReverseSearch("/home/anirudh/Git/book-shelf-python/image/bookcover_2.jpg")
    print(rev_img)

    xmlResponse = getBookList(rev_img)
    val = parseXMLForBookSearch(xmlResponse)

    for key,value in val.items():
       print(key, value)
