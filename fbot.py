import selenium
from selenium import webdriver
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
message = "//*[@id='js_11']"
send = "/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[2]/div[2]/a"

semail = driver.find_element_by_id(email)
#you need to enter your email or phone-number here to login
semail.send_keys("email@example.com")

spassword = driver.find_element_by_id(password)
#password goes here
spassword.send_keys("password")

slogin = driver.find_element_by_id(login)
slogin.click()

time.sleep(2)

counter = 0

while counter < 10: #set this value to the number of messages you wanna send. If you want to send 100 messages, write counter < 100
    smessage = driver.find_element_by_xpath(message)
    smessage.send_keys("Hi! I am a Bot") #change this text to whatever you wanna send
    ssend = driver.find_element_by_xpath(send)
    ssend.click()
    counter += 1

