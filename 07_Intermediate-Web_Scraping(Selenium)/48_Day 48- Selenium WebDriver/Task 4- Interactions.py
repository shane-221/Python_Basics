from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#---------------------------------------Opening the page arguments-----------------------------------------------------#
chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option(name= "detach", value= True )
#chrome_options.add_argument("--headless")

#--------------------------------------running the css code------------------------------------------------------------#
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

#---------------------------------------------Pulling the numbers------------------------------------------------------#
banner = driver.find_element(By.ID, value="articlecount")
numbers = banner.find_elements(By.CSS_SELECTOR, value="a[href='/wiki/Special:Statistics']")

data =  [i.text for i in numbers]
print(data[1])



#-------------------------------------------- Click function----------------------------------------------------------#
section = driver.find_element(By.ID, value="articlecount")
section.click()


#--------------------------------------------Find element by link text-------------------------------------------------#
all_portals = driver.find_element(By.LINK_TEXT, value = "Content portals")
all_portals.click()

#-------------------------------------------- searching with text------------------------------------------------------#
search = driver.find_element(By.NAME, value= "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)