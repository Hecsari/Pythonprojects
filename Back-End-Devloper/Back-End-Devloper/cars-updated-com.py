# -*- coding: utf-8 -*-
"""
OBJETIVO: 
    - Extraer el precio, titulo, descripción y otros datos de los productos en cars-com.
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

from pymongo import MongoClient #paqueteria de pymongo y llamar mongocliente

client = MongoClient("mongodb://localhost:27017/") #colocar aquí el host adecuado
db = client['cars'] #creación de una base, 'base' es el nombre
col = db['listings_cars'] #creación de la colección con su nombre en ''

opts = Options()   #todo estas dos lineas de código, son de seguridad para evitar que sea evidente el scrapping
opts.add_argument(
	"user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
)

driver = webdriver.Firefox() #llamar el driver en mi caso Firefox, pero puede cambiarlo a CHrome, si lo tiene instalado

# START_URLS= [
# 'https://www.cars.com/for-sale/searchresults.action/?page=1&perPage=100&rd=30&searchSource=SORT&slrTypeId=28879&sort=price-lowest&stkTypId=28881&zc=92121',
# 'https://www.cars.com/for-sale/searchresults.action/?page=2&perPage=100&rd=30&searchSource=PAGINATION&slrTypeId=28879&sort=price-lowest&stkTypId=28881&zc=92121',
# 'https://www.cars.com/for-sale/searchresults.action/?page=3&perPage=100&rd=30&searchSource=PAGINATION&slrTypeId=28879&sort=price-lowest&stkTypId=28881&zc=92121',
# 'https://www.cars.com/for-sale/searchresults.action/?page=4&perPage=100&rd=30&searchSource=PAGINATION&slrTypeId=28879&sort=price-lowest&stkTypId=28881&zc=92121'
# ]

#for url in START_URLS:
#URL SEMILLA = url de desde inicia la búsqueda pero no el scrapping
driver.get('https://www.cars.com/for-sale/searchresults.action/?page=2&perPage=100&rd=30&searchSource=SORT&slrTypeId=28879&sort=price-lowest&stkTypId=28881&zc=92121')

#number_results = driver.find_element_by_xpath('//div/span[@class="filter-count"]').text #sirve para ver el número de resultados

#Ciclo while para que vaya leyendo siempre que encuentre un elemento en ese 'container'
# Mientras la pagina en la que me encuentre, sea menor que la maxima pagina que voy a sacar... sigo ejecutando...

# LOGICA DE MAXIMA PAGINACION CON LAZO WHILE
# VECES VOY A PAGINAR HASTA UN MAXIMO DE 3



PAGINACION_MAX = 4
PAGINACION_ACTUAL = 1

while PAGINACION_MAX < PAGINACION_ACTUAL:
#ESTA PRIMERA PARTE ACCEDE A CADA PAAGINA DEL PRODUCTO DE MANERA VERTICAL Y HORIZONTAL

	links_cars = driver.find_elements(By.XPATH, '//div[@class="shop-srp-listings__listing-container"]/a')  #xpath donde se encuentra cada producto
	links_de_la_pagina = [] #creación de una lista vacía

	D = 0 #contador
	
	for tag_car in links_cars:

		D = D + 1

		links_de_la_pagina.append(tag_car.get_attribute("href"))  #href indica el atributo del link de cada auto para su extracción

	for link in links_de_la_pagina:

		      # Voy a cada uno de los links de los detalles de los productos
		try:

			#Obtencion de los parametros de cada producto 
			driver.get(link)
			#try:
			title = driver.find_element_by_xpath('//*[@id="header-box"]/div/div/div[1]/div/h2[1]').text
			#except:
			#	title = driver.find_element_by_xpath('//*[@id="header-box"]/div/div/div[1]/div/h2[1][text()]').text
	
			year = driver.find_element_by_xpath('//*[@id="header-box"]/div/div/div[1]/div/h4[1]').text
			
			price = driver.find_element(By.XPATH, '//*[@id="header-box"]/div/div/div[2]/div/div/h2').text
			
		#	try:

#			except:
#				mileage = driver.find_element_by_xpath('//*[@id="summary-table"]/tbody/tr[5]/td/span[contains(text(), "mi.")]').text
			try:
				description = driver.find_element(By.XPATH, '//*[@id="summary-table"]/tbody/tr[1]/td/p').text
			except:
				description = driver.find_element_by_xpath('//*[@id="summary-table"]/tbody/tr[1]/td').text
			try:
				testdrive_location = driver.find_element_by_xpath('//*[@id="summary-table"]/tbody/tr[2]/td/em').text
			except:
				testdrive_location = 'No disponible'

			VIN = driver.find_element(By.XPATH, '//*[@id="summary-table"]/tbody/tr[2]/td').text
			Trim = driver.find_element(By.XPATH, '//*[@id="summary-table"]/tbody/tr[3]/td').text
			Full_Style_Name = driver.find_element(By.XPATH, '//*[@id="summary-table"]/tbody/tr[4]/td').text
			mileage = driver.find_element_by_xpath('//*[@id="summary-table"]/tbody/tr[5]/td').text
			Tire_Mileage = driver.find_element(By.XPATH, '//*[@id="summary-table"]/tbody/tr[6]/td').text
			Transmission = driver.find_element(By.XPATH, '//*[@id="summary-table"]/tbody/tr[7]/td').text
			Drive_Type = driver.find_element(By.XPATH, '//*[@id="summary-table"]/tbody/tr[8]/td').text
			Engine = driver.find_element(By.XPATH, '//*[@id="summary-table"]/tbody/tr[9]/td/span[1]').text
			try:
			#| //*[@id="summary-table"]/tbody/tr[9]/td/span[2]
				Fuel_Economy = driver.find_element(By.XPATH, '//*[@id="summary-table"]/tbody/tr[10]/td').text
			# | //*[@id="summary-table"]/tbody/tr[10]/td/span[2]
			except:
				Fuel_Economy = driver.find_element_by_xpath('//*[@id="summary-table"]/tbody/tr[12]/td/span[2]')

			Doors = driver.find_element(By.XPATH, '//*[@id="summary-table"]/tbody/tr[11]/td').text
			Passengers = driver.find_element(By.XPATH, '//*[@id="summary-table"]/tbody/tr[12]/td').text
			try:	
				Exterior_color = driver.find_element(By.XPATH, '//*[@id="summary-table"]/tbody/tr[13]/td').text	 
			except:
				Exterior_color = driver.find_element_by_xpath('//*[@id="summary-table"]/tbody/tr[12]/td/span[2]')

			t = datetime.datetime.now()
			timestamp = t.strftime("%x") 		
			
#CREACIÓN DE COLECCIONES EN LAS BASE DE DATOS MONGO

            #Creación de la colección
			col.insert_one({
				'title': title, #asigna el nombre a los atributos con la colección
				'price': price,
				'year': year,
				'mileage': mileage,
				'description': description,
				'testdrive_location': testdrive_location,
				'VIN': VIN,
				'Trim': Trim,
				'Full_Style_Name' : Full_Style_Name,
				'Tire_Mileage': Tire_Mileage,
				'Transmission': Transmission,
				'Drive_Type': Drive_Type,
				'Engine': Engine,
				'Fuel_Economy': Fuel_Economy,
				'Doors': Doors,
				'Passengers': Passengers,
				'Exterior_color': Exterior_color,
				'timestamp': timestamp

			})
#ACTUALIZACIÓN DE LOS VALORES(manera alternativa)
	        #col.update_one({
            #	'title': title # En este caso es mi ciudad, es decir. Por esta condicion voy a buscar para actualizar
        	#}, {
            #	'$set': { # Si no se encuentra ni un documento con el identificador, se inserta un documento nuevo
            #    	'price': price, # Si si se encuentra un documento con el identificador, se actualiza ese documento con la nueva informacion
            #    	'year': year,
            #    	'mileage': mileage,
            #    	'description': description,
			#	  	'testdrive-location': testdrive-location,
			#		'VIN': VIN,
			#		'Trim': Trim,
            #	}
	        #}, upsert=True) # Flag para utilizar la logica de Upsert
			
			f = open("./datos_cars_sample_selenium.csv", "a") #creación de csv para revisión, se puede comentar

#PARTE II: Si no existe la colección añadirla, si existe, añadir un nuevo precio y que se mantega el anterior, añadir timestamp

			collist = db.list_collection_names()

			new_price = driver.find_element(By.XPATH, '//*[@id="header-box"]/div/div/div[2]/div/div/h2').text


			if "listings_cars" in collist:
				print("listing already exists.")  #Para verificar que la colección existe.
				query = {"title" : title}
				new_values = {"$set" : {"new_price" : new_price, "timestamp": timestamp}}
				update_col = col.update(query, new_values) #añadir nuevos valores de precio junto con marca de tiempo
			else: 
				col.updated()


			#imprime los valores oportunos
			print(title)
			print(year)
			print(price)
			print(mileage)
			print(description)
			print(testdrive_location)
			print(VIN)
			print(Trim)
			print(Full_Style_Name)
			print(Tire_Mileage)
			print(Transmission)
			print(Drive_Type)
			print(Engine)
			print(Fuel_Economy)
			print(Doors)
			print(Passengers)
			print(Exterior_color)


            
            ## Aplasto el boton de retroceso
			driver.back() 

		except Exception as e:
			print(e)
		      # Si sucede algun error dentro del detalle, no me complico. Regreso a la lista y sigo con otro producto.
      	#	driver.back()

	try: 
		nextbutton = driver.find_element(By.XPATH, '//*[@id="ae-main-content"]/div[4]/cars-filters/div[1]/cars-pagination/div[1]/a[2]') #boton siguiente
		nextbutton.click()
	except:
		break

PAGINACION_ACTUAL += 1

print(number_results) #compara el # de resultados de la página con las bajadas de éste
print(D)

count = cars_col.count_documents({})
#CADA CIERTO TIEMPO SE EXTRAE DATOS
# Logica de automatizacion de extraccion
#schedule.every(5).minutes.do(extraer_datos) # Cada 5 minutos ejecuta la extraccion

while True:
     schedule.run_pending()
     time.sleep(1)

driver.close() #cierra el navegador
