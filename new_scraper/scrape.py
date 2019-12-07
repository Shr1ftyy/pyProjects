import requests 
import lxml
import bs4
import os 
from bs4 import BeautifulSoup as soup 

try:
	os.system('cls')
except Exception as e:
	os.system('clear')
else:
	pass

page_html = requests.get('http://books.toscrape.com/').text
page_soup = soup(page_html, "lxml")

book_list = page_soup.findAll("ul")[2]
book_categories = book_list.findAll("li")
category_num = 0
category_links = []
for book in range(category_num, len(book_categories)):
    book_category = book_categories[category_num].a.text.strip()
    print(f"{category_num}. {book_category}")
    category_href = book_categories[category_num].a["href"]
    category_links.append(f"http://books.toscrape.com/{category_href}") 
    category_num += 1

selection_input = input(f"Select Category (0 - {len(book_categories)}): ")
selection = int(selection_input)

open_link = category_links[selection]
link_html = requests.get(open_link).text
link_soup = soup(link_html, 'lxml')

found_results = link_soup.findAll("form")[0].text.strip()
print(f"{found_results}")
#Display Results
books = link_soup.findAll("li", {"class":'col-xs-6 col-sm-4 col-md-3 col-lg-3'})

book_links = []

book_num = 0
for book in range(0, len(books)):
    book = books[book_num]
    bookName = book.h3.a["title"].strip()
    bookPriceInfo = book.findAll("div", {"class":"product_price"})[0]
    bookPrice = bookPriceInfo.p.text.strip()
    bookStockSearch = bookPriceInfo.findAll("p", {"class":"instock availability"})[0]
    bookStock = bookStockSearch.text.strip()
    bookRating = book.findAll("div", {"class":"image_container"})
    bookHref = book.h3.a["href"]
    bookSplit = bookHref.split("..")
    bookLink = (f'http://books.toscrape.com/catalogue{bookSplit[3]}')

    book_links.append(bookLink)
    print(f"Book #{book_num}")
    print(f'Name: {bookName}')
    print(f'Price: {bookPrice}')
    print(f'{bookStock}')
    # print(f"Link: {bookLink}")
    print("\n")
    book_num += 1

book_select = input(f"Select Book (0 - {len(books)}): ")
try:
	os.system('cls')
except Exception as e:
	os.system('clear')
else:
	pass
book_url = book_links[int(book_select)]
bookRequest = requests.get(book_url).text
bookSoup = soup(bookRequest, 'lxml')
bookInfo = bookSoup.findAll("div", {"class":"col-sm-6 product_main"})[0]
bookTitle = bookInfo.h1.text.strip()
book_p_headers = bookInfo.findAll("p")
productPrice = book_p_headers[0].text.strip()
productStock = book_p_headers[1].text.strip()
productDesc = bookSoup.findAll("p")[3].text.split(" ...more")[0]

print(f"Book Title: {bookTitle}")
print(f'Price: {productPrice}')
print(f'{productStock}')
print(f'Description:\n{productDesc}')
