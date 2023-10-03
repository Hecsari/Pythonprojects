# -*- coding: utf-8 -*-
"""
OBJETIVO: 
    - Extraer el precio, titulo, descripción y otros datos de uno de los productos en cars-com.
    - Extracciones horizontal

CREADO POR: Hecsari Bello
ULTIMA VEZ EDITADO: 12 mayo 2021
"""

#paqueterias de Selenium y webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import datetime

from pymongo import MongoClient 

client = MongoClient("mongodb://localhost:27017/") #colocar aquí el host adecuado

db = client['vehicle'] #creación de una base, 'base' es el nombre
cars_col = db['listing_vehicle'] #creación de la colección con su nombre en ''


opts = Options()   #todo estas dos lineas de código, son de seguridad para evitar que sea evidente el scrapping
opts.add_argument(
	"user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
)

driver = webdriver.Firefox() #llamar el driver en mi caso Firefox, pero puede cambiarlo a CHrome, si lo tiene instalado


#URL SEMILLA = url de desde inicia la búsqueda pero no el scrapping
#driver.get('https://www.tred.com/buy/mercedes-benz/clk-class/2004/WDBTJ65J14F081638?utm_source=cars.com&utm_campaign=search_result')
driver.get('https://www.tred.com/buy/kia/optima/2015/5XXGR4A63FG420504?utm_source=cars.com&utm_campaign=search_result') #ústed puede ingresar cualquier url de un producto que quiero de cars.com



try:
		
	try:
		title = driver.find_element_by_xpath('//*[@id="header-box"]/div/div/div[1]/div/h2[1]').text
	except:
		title = driver.find_element_by_xpath('//*[@id="header-box"]/div/div/div[1]/div/h2[1][text()]').text
	
	year = driver.find_element_by_xpath('//*[@id="header-box"]/div/div/div[1]/div/h4[1]').text

	
	price = driver.find_element(By.XPATH, '//*[@id="header-box"]/div/div/div[2]/div/div/h2').text
	try:
		mileage = driver.find_element_by_xpath('//*[@id="summary-table"]/tbody/tr[5]/td/span/span').text
	except:
		mileage = driver.find_element_by_xpath('//*[@id="summary-table"]/tbody/tr[5]/td/span[contains(text(), "mi.")]').text
	try:
		escription = driver.find_element(By.XPATH, '//*[@id="summary-table"]/tbody/tr[1]/td/p').text
	except:
		description = driver.find_element_by_xpath('//*[@id="summary-table"]/tbody/tr[1]/td').text

	testdrive_location = driver.find_element_by_xpath('//*[@id="summary-table"]/tbody/tr[2]/td').text
	VIN = driver.find_element(By.XPATH, '//*[@id="summary-table"]/tbody/tr[2]/td').text
	Trim = driver.find_element(By.XPATH, '//*[@id="summary-table"]/tbody/tr[3]/td').text
	Full_Style_Name = driver.find_element(By.XPATH, '//*[@id="summary-table"]/tbody/tr[4]/td').text
	Tire_Mileage = driver.find_element(By.XPATH, '//*[@id="summary-table"]/tbody/tr[5]/td').text
	Transmission = driver.find_element(By.XPATH, '//*[@id="summary-table"]/tbody/tr[6]/td').text
	Drive_Type = driver.find_element(By.XPATH, '//*[@id="summary-table"]/tbody/tr[7]/td').text
	Engine = driver.find_element(By.XPATH, '//*[@id="summary-table"]/tbody/tr[8]/td').text
	Fuel_Economy = driver.find_element(By.XPATH, '//*[@id="summary-table"]/tbody/tr[9]/td').text
	Doors = driver.find_element(By.XPATH, '//*[@id="summary-table"]/tbody/tr[10]/td').text
	Passengers = driver.find_element(By.XPATH, '//*[@id="summary-table"]/tbody/tr[11]/td').text
	Exterior_color = driver.find_element(By.XPATH, '//*[@id="summary-table"]/tbody/tr[12]/td').text	 
			
			


	f = open("./datos_one_vehicle_sample_selenium.csv", "a") #para escribir y almacenar los datos
			
	print(title)
	print(year)
	print(price)

#	print(mileage)
#	print(description)
#	print(testdrive_location)
#	print(VIN)
#	print(Trim)
#	print(Full_Style_Name)
#	print(Tire_Mileage)
#	print(Transmission)
#	print(Drive_Type)
#	print(Engine)
#	print(Fuel_Economy)
#	print(Doors)
#	print(Passengers)
#	print(Exterior_color)
#	print()
    
	
	#timestamp = datetime.datetime.today().strftime('%d-%m-%Y') #call the date at the momment
######################################################################Segunda parte del código##########################################################################################################################################
	
#creación de colecciones en la base de datos, con los elementos obtenidos de los productos
	car_dict = {
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
	}

	cars = cars_col.insert_one(car_dict)


#	print(cars)


#Verificar en MongoDB si la lista ya existe en la base de datos
	collist = db.list_collection_names()
  #Para verificar que la colección existe.
	if "listings_cars" in collist:
		print("listing already exists.")
		new_prices_today = []
		new_prices_today.append(price)		
		
		cars2_dict = {"timestamp" : timestamp, "new_prices_today": new_prices_today }

		cars_dict.updated(cars2_dict)

		print(cars_dict)
	else: 
		cars_col.updated()

except:
	print('error')


driver.close()
	