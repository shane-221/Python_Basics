import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys

load_dotenv()



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value = True)


driver= webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")


first_name = driver.find_element(By.NAME, value= "fName")
first_name.send_keys("Shane")

second_name= driver.find_element(By.NAME, value= "lName")
second_name.send_keys("Mathew")


email = driver.find_element(By.NAME, value= "email")
email.send_keys(os.getenv("email"))

email.send_keys(Keys.ENTER)