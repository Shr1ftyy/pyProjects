import requests 
import bs4
from bs4 import BeautifulSoup as soup 
import os

###################
###	STOCK QUERY ###
###################

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
os.system('cls')
while run:
	stock_source = requests.get(stock_link).text
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
		price_result = price_search[0]					
		price = price_result.findAll("span")[1].text.strip()
	except Exception as e:							  
		price = "(Updating...)"

	try: 				
		gain = price_result.findAll("span")[2].text.strip()
	except Exception as e:
		gain = "(Updating...)"


	try: 
		market_notice = source_soup.findAll("div", {"id":"quote-market-notice"})[0].span.text.strip()
	except Exception as e:
		market_notice = "(Updating)"

	os.system('cls')

	try:
		print("----------------------------------------------\n")
		print(name)
		print(caption+"\n")
		print(f"Current Price: {price}	{gain}\n")
		print(market_notice)
		print("----------------------------------------------\n")
	except Exception as e:
		("Reconnecting... ")
