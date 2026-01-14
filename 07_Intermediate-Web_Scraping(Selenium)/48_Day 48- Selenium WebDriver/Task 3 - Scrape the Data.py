from selenium import webdriver
from selenium.webdriver.common.by import By


# Getting the page to stay open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Getting the driver to work
driver=webdriver.Chrome(options =chrome_options)
driver.get("https://www.python.org/")


# Broken down by sections until Im at the list functions
header = driver.find_element(By.CSS_SELECTOR, value=".event-widget")
ul= header.find_element(By.CSS_SELECTOR, value = ".menu")
items = ul.find_elements(By. TAG_NAME, value ="li")

# Using the sections to create the list of items
events={}
n=0
for event in items:
    date =event.find_element(By.TAG_NAME, value= "time")
    title = event.find_element(By. TAG_NAME, value = "a")
    events[n] = {f"time:2025-{date.text}, name :{title.text}"}
    n = n + 1
print(events)

#driver.quit()