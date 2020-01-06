import sys, os, time, getpass, threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from signal import signal, SIGINT

try:
	options = webdriver.ChromeOptions()
	options.add_argument('--headless')
	prefs={ 'disk-cache-size': 4096 }
	options.add_experimental_option('prefs', prefs)
	options.add_argument("user-data-dir=/home/astitva/.config/google-chrome/Default")
	driver = webdriver.Chrome("/home/astitva/Documents/chromedriver78",chrome_options=options)
	driver.get("https://moodle.iiit.ac.in/my")
	Handle = input("Enter email : \t")
	Pass = getpass.getpass(prompt="Enter password : \t")
	driver.find_element(By.ID, "username").send_keys(Handle)
	driver.find_element(By.ID, "password").send_keys(Pass)
	driver.find_element(By.NAME, "submit").click()
	i=1
	list_courses= [];
	print("\r",end="")
	while True:
		try:
			name = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/section/div/aside/div/div[2]/div/div["+str(i)+"]/div[1]/h2/a").text
			list_courses.append(name)
			i+=1
		except:
			break
	driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/section/div/aside/div/div[2]/div/div[6]/div[1]/h2/a").click()
	driver.find_element(By.XPATH, "//span[contains(.,'Attendance')]").click()
	driver.find_element(By.LINK_TEXT, "All courses").click()
	i=1
	while True:
		try:
			cname = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/section/div/table/tbody/tr/td[2]/h3['+str(i)+']').text
			if cname in list_courses:
				print(cname+":")
				x = len(cname)+1
				for p in range(x):
					print("~",end="")
				print()
				tot=driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/section/div/table/tbody/tr/td[2]/table['+str(i)+']/tbody/tr[1]/td[2]').text
				att=driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/section/div/table/tbody/tr/td[2]/table['+str(i)+']/tbody/tr[2]/td[2]').text
				print("Total Classes :\t",tot)
				print("Attended :\t",att)
				print("__________________________________________________________")
				print()
			i+=1
		except :
			break
except:
	driver.quit()
	exit(0)
driver.quit()