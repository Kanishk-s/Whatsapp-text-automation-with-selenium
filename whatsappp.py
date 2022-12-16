import time
from selenium.webdriver.common.keys import Keys

from selenium import  webdriver
import os
from selenium.webdriver.common.by import By
os.environ['PATH'] += r"C:\selenium drivers"
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
print("scan QR press enter")
input()

search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]')
search_box.send_keys('decode')
time.sleep(2)
receiver = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]/div/div')
receiver.click()
time.sleep(2)
message = "selenium test"
mesage_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
mesage_box.send_keys(message, Keys.ENTER)
time.sleep(5)
