import requests 
import bs4
from bs4 import BeautifulSoup as soup 
import os
import sys
import time

print("importing")

from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl	
from PyQt4.QtWebKit import QWebPage 

###################
###	STOCK QUERY ###
###################

class Client(QWebPage):
	def __init__(self, url):
		# self.app = QApplication.instance()
		# if self.app is None:
		self.app = QApplication(sys.argv)
		QWebPage.__init__(self)
		self.loadFinished.connect(self.on_page_load)
		print("Loading")
		self.mainFrame().load(QUrl(url))
		print("Executing")
		self.app.exec_()
		print("Executed")
	def on_page_load(self):
		print("Quitting")
		self.app.quit()


keyword = input("Enter Stock: ")
source = requests.get('https://au.finance.yahoo.com/lookup?s=' + keyword).text
# print(f"Querying: {source}" )

stock_soup = soup(source, 'lxml')

stock_num = 0

try:
	tables = stock_soup.findAll("tbody",{"data-reactid":"54"})
	table = tables[0]
	tableFile = open("table.txt", "w+")
	tableFile.write(str(table.prettify()))
except Exception as e:
	print("----------	No Results Found	----------")
	exit()

columns = table.findAll("tr")
columnsFile = open("columns.txt", "w+")
columnsFile.write(str(columns))

for column in range(stock_num, len(columns)):
	column = columns[stock_num]
	# print(f"{column}" + "\n\n" + f"{stock_num}")

	print(f"	--- Stock Result #: {stock_num}	---		")

	symbol = column.td.a["data-symbol"].strip()
	print(f"Symbol: {symbol}")

	stock_name = column.findAll("td", {"class":"data-col1 Ta(start) Pstart(10px) Miw(80px)"})[0].text.strip()
	print(f"Name: {stock_name}")

	last_price = column.findAll("td", {"class":"data-col1 Ta(start) Pstart(10px) Miw(80px)"})[0].text.strip()
	print(f"Last Price: {last_price}")

	try:
		category = column.findAll("td", {"class":"data-col3 Ta(start) Pstart(20px) Miw(60px)"})[0].a.text.strip()
		print(f'Category: {category}')
	except Exception as e:
		print("Category: N/A")

	stock_type = column.findAll("td", {"class":"data-col4 Ta(start) Pstart(20px) Miw(30px)"})[0].text.strip()
	print(f'Type: {stock_type}')

	exchange = column.findAll("td", {"class":"data-col5 Ta(start) Pstart(20px) Pend(6px) W(30px)"})[0].text.strip()
	print(f'Exchange: {exchange}')
	print('---------------------------------------------------')
	
	stock_num += 1 

stock_selection = input("Enter Stock #: ")
stock_open = columns[int(stock_selection)].td.a["href"]
stock_link = (f"https://au.finance.yahoo.com{stock_open}")
print(f"Stock Link: {stock_link}")

#####################
###	DISPLAY STOCK ###
#####################

run = True
# os.system('cls')
while run:
	# stock_source = requests.get(stock_link).text
	client_response = Client(stock_link)
	print("parsing to html")
	stock_source = client_response.mainFrame().toHtml()
	print("parsed")
	source_soup = soup(stock_source, 'lxml')

	try:
		name_search = source_soup.findAll("div", {"class":"Mt(15px)"})[0]
		name = name_search.div.div.h1.text.strip()
	except Exception as e:
		name = "(Refreshing...)"

	try:
		caption_search = source_soup.findAll("div", {"class":"C($tertiaryColor) Fz(12px)"})[0]
		caption = caption_search.span.text.strip()
	except Exception as e:
		caption = "(Updating...\n)"

		
	try:
		price_search = source_soup.findAll("div", {"id":"quote-header-info"})
		print(f"{price_search}\nend")
		price_result = price_search[0]
		# print("result")
		# print(price_result)					
		price = price_result.findAll("span")[3].text.strip()
	except Exception as e:							  
		price = "(Updating...)"

	try: 				
		gain = price_result.findAll("span")[4].text.strip()
	except Exception as e:
		gain = "(Updating...)"


	try: 
		market_notice = source_soup.findAll("div", {"id":"quote-market-notice"})[0].span.text.strip()
	except Exception as e:
		market_notice = "(Updating)"

	# os.system('cls')

	try:
		print("----------------------------------------------\n")
		print(name)
		print(caption+"\n")
		print(f"Current Price: {price}	{gain}\n")
		print(market_notice)
		print("----------------------------------------------\n")
	except Exception as e:
		("Reconnecting... ")
	
	os.system('clear')
	
	# time.sleep(2)
