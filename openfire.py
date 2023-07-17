import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
#driver.get ("http://192.168.3.41:9090/login.jsp?url=%2Findex.jsp")
driver.get("http://192.168.3.41:9090/user-create.jsp")
#login
input_element = driver.find_element(By.CLASS_NAME, "form-control")
input_element.clear()
input_element.send_keys("cdelgado")
input_element = driver.find_element(By.NAME,"password")
input_element.clear()
input_element.send_keys("gatito")
button = driver.find_element(By.ID,"submit").click()


#creating Users
with open('users.csv','r') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print("Creating user :"+str(row[1]))
		text_box = driver.find_element(By.NAME,"username").send_keys(str(row[0]))
		text_box = driver.find_element(By.NAME,"name").send_keys(str(row[1]))
		text_box = driver.find_element(By.NAME,"password").send_keys(str(row[0]))
		text_box = driver.find_element(By.NAME,"passwordConfirm").send_keys(str(row[0]))
		sleep(5)
		button = driver.find_element(By.NAME, "another").click()

#text_box1 = driver.find_element_by_name('name').send_keys("testing")
#text_box2 = driver.find_element_by_name('password').send_keys("testing")
#text_box3 = driver.find_element_by_name('passwordConfirm').send_keys("testing")
#button = driver.find_element_by_name('another').click()

