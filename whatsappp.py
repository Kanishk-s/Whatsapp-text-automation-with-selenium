import time
from selenium.webdriver.common.keys import Keys
from selenium import  webdriver
import os
from selenium.webdriver.common.by import By

def process():
    print("Do you want to send message type yes else type no")
    ans = input()
    if ans == "yes":
        take_contact()
    else:
        return
    process()

def take_contact():
    print("Enter contact name")
    cn_name = input()
    search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]')
    search_box.send_keys(cn_name, Keys.ENTER)
    send_message()


def send_message():
    time.sleep(2)
    print("Type the message you want to send")
    mess = input()
    message_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    message_box.send_keys(mess, Keys.ENTER)
    time.sleep(5)

os.environ['PATH'] += r"C:\selenium drivers"
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
print("scan QR press enter")
input()
process()
driver.quit()
