import bs4 
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=Graphics%20Card'
uClient = uReq(my_url)  
page_html = uClient.read()
uClient.close()
#parse
page_soup = soup(page_html, "html.parser")

#Grab each product
containers = page_soup.findAll("div",{"class":"item-container"})
info_containers = page_soup.findAll("div",{"class":"item-info"})

container = containers[0]
info_container = info_containers[0]



textFile = open("containers.txt", "w+")
textFile.write(str(containers))

item_num = 0 

textFile = open("brands.txt", "w+")
textFile.write("")

filename = "products.csv"
f = open(filename, "w")

headers = "product_name, brand, shipping\n"
f.write(headers)

for container in containers:
	info_container = info_containers[item_num]
	product_name = container.a.img["title"]
	print("Name: " + product_name)
	
	brand = info_container.div.a.img["title"]
	print("Brand: " + brand)

	shipping_container = container.findAll("li",{"class":"price-ship"})
	shipping = str(shipping_container[0].text.strip())

	print("Shipping: " + shipping)
	item_num += 1

	textFile = open("brands.txt", "a")
	textFile.write("Name: " + product_name + "\n")
	textFile.write("Brand: " + brand + "\n")
	textFile.write("Shipping: " + shipping + "\n\n")

	f.write(product_name + "," + brand + "," + shipping + "\n")

f.close()

#print(page_soup.h1)
#print(page_soup.p)
#print(page_soup.body.span) 