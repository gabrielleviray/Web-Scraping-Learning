from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

web_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics+card'

# Opens connection to client and grabs the page
uClient = uReq(web_url)

# Offloads content in variable
web_html = uClient.read()

uClient.close()

# Parse HTML
webpage_soup = soup(web_html, "html.parser")

# Grabs every product on page
containers = webpage_soup.findAll("div", {"class": "item-container"})

filename = "graphics_cards.csv"
f = open(filename, "w")

headers = "Brand, Product, Shipping\n"
f.write(headers)


for container in containers:
	item_brand = container.div.div.a.img["title"]

	item_title = container.findAll("a",{"class":"item-title"})
	item_name = item_title[0].text

	shipping_container = container.findAll("li", {"class":"price-ship"})
	shipping = shipping_container[0].text

	print("brand: " + item_brand)
	print("product_name: " + item_name)
	print("shipping: " + shipping)

	f.write(item_brand + "," + item_name.replace(",", "|") + "," + shipping + "\n")

f.close()