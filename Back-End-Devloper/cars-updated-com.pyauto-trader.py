# -*- coding: utf-8 -*-
"""
OBJETIVO: 
    - Extraer el precio, titulo, descripción y otros datos de los productos en autotrader.
    - Extracciones verticales y horizontales con Selenium.
    - Guardar los datos en la base de datos de Mongo
    - Creación de la base de datos y sus colecciones
CREADO POR: Hecsari Bello
ULTIMA VEZ EDITADO: 13 mayo 2021
"""

#paqueterias de Selenium y webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import schedule
import datetime
import random
from time import sleep

from pymongo import MongoClient #paqueteria de pymongo y llamar mongocliente

client = MongoClient("mongodb://localhost:27017/") #colocar aquí el host adecuado
db = client['autotrader'] #creación de una base, 'base' es el nombre
col = db['listings_auto'] #creación de la colección con su nombre en ''

opts = Options()   #todo estas dos lineas de código, son de seguridad para evitar que NO sea evidente el scrapping
opts.add_argument(
 	"user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
)

#here you can add the urls of interest
start_urls = [
'https://www.autotrader.com/cars-for-sale/san-diego-ca-92121?channel=ATC&relevanceConfig=default&dma=&sellerTypes=p&searchRadius=50&location=&marketExtension=include&isNewSearch=false&showAccelerateBanner=false&sortBy=relevance&numRecords=100&firstRecord=100',
#'https://www.autotrader.com/cars-for-sale/san-diego-ca-92121?channel=ATC&relevanceConfig=default&dma=&sellerTypes=p&searchRadius=50&location=&marketExtension=include&isNewSearch=false&showAccelerateBanner=false&sortBy=relevance&numRecords=100&firstRecord=200',
]

#url = 'https://www.autotrader.com/cars-for-sale/san-diego-ca-92121?channel=ATC&relevanceConfig=default&dma=&sellerTypes=p&searchRadius=50&location=&marketExtension=include&isNewSearch=false&showAccelerateBanner=false&sortBy=relevance&numRecords=100&firstRecord=100'



driver = webdriver.Firefox() #llamar el driver en mi caso Firefox, pero puede cambiarlo a CHrome, si lo tiene instalado

for url in start_urls:
	driver.get(url)


	autos_section = driver.find_elements_by_xpath('//div[@data-cmp="itemCard"]')

#number_of_results = driver.find_element_by_xpath('//span[@class="padding-horizontal-2 text-size-md-200 text-size-lg-300 text-right"]')



for auto in autos_section:
	title = auto.find_element_by_xpath('.//h2[@class="text-bold text-size-400 text-size-sm-500 link-unstyled"]').text
	print(title)
	price = auto.find_element_by_xpath('.//span[@class="first-price"]').text
	print(price)
	try:
		c_price = auto.find_elements_by_XPATH('//div[@class="ribbon-content-right"]')
	except:
		c_price = 'No disponible'
	mileage = auto.find_element_by_xpath('.//div[@class="text-bold"]').text
	print(mileage)
	color =  auto.find_element_by_xpath('//ul[@data-cmp="list"]/li[1]/span').text
	print(color)
	Fuel_Economy = auto.find_element_by_xpath('//ul[@data-cmp="list"]/li[2]/span').text
	print(Fuel_Economy)
	Drive_Type = auto.find_element_by_xpath('//ul[@data-cmp="list"]/li[3]/span').text
	print(Drive_Type)
	Engine = auto.find_element_by_xpath('//ul[@data-cmp="list"]/li[4]/span').text
	print(Engine)
	print()


#TODO ESTO SIRVE PARA GUARDAR TODOS LOS DATOS COMO CSV
	# f = open("./datos_auto_trader_selenium.csv", "a")
	# f.write(title + " " + price + " " + mileage + " " + color + " " + Fuel_Economy + " " + Drive_Type + " " + Engine + "\n")
	# f.close()





	t = datetime.datetime.now()
	timestamp = t.strftime("%x") 			
	# # #CREACIÓN DE COLECCIONES EN LAS BASE DE DATOS MONGO

	#Creación de la colección
	col.insert_one({
		'title': title, #asigna el nombre a los atributos con la colección
		'price': price,
		'c_price': c_price,
		'mileage': mileage,
		'color' : color,
		'Fuel_Economy': Fuel_Economy,
		'Drive_Type': Drive_Type,
		'Engine': Engine,	
		'timestamp': timestamp
	})


#PARTE II: Si no existe la colección añadirla, si existe, añadir un nuevo precio y que se mantega el anterior, añadir timestamp
	collist = db.list_collection_names()
	new_price = driver.find_element(By.XPATH, './/span[@class="first-price"]').text

	if "listings_auto" in collist:
	 	print("listing already exists.")  #Para verificar que la colección existe.
	 	query = {"title" : title}
	 	new_values = {"$set" : {"new_price" : new_price, "timestamp": timestamp}}
	 	update_col = col.update(query, new_values) #añadir nuevos valores de precio junto con marca de tiempo
	else: 
	 	col.updated()

count = col.count_documents({}) #cuenta el número de colecciones
print(count)

driver.close()
