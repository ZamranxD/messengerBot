import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome("./chromedriver") #try "./chromedriver.exe" if "./chromedriver" doesn't work for you

#just put the link of anyone's inbox whom you wanna text. I've put mine in there as an example
driver.get("https://web.facebook.com/messages/t/ZamranxD")

#setting xpath values to access these elements
email = "email"
password = "pass"
login = "loginbutton"
message = '//*[@id="mount_0_0_Hi"]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[4]/div[2]/div/div/div'
send = '//*[@id="mount_0_0_x7"]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/span[2]/div'

semail = driver.find_element(By.ID, email)
#you need to enter your email or phone-number here to login
semail.send_keys("example@example.com")

spassword = driver.find_element(By.ID, password)
#password goes here
spassword.send_keys("dummypass")

slogin = driver.find_element(By.ID, login)
slogin.click()

time.sleep(2)

counter = 0

while counter < 10: #set this value to the number of messages you wanna send. If you want to send 100 messages, write counter < 100
    smessage = driver.find_element(By.XPATH, message)   #this is not working as of now for some reason - might be the wrong Xpath or im prolly selecting the wrong element's Xpath
    smessage.send_keys("Hi! I am a Bot") #change this text to whatever you wanna send
    ssend = driver.find_element(By.XPATH, send)
    ssend.click()
    counter += 1

