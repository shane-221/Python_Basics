from  selenium import webdriver



# Configuring the webdriver
chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Using the webdriver
driver= webdriver.Chrome(options =  chrome_options)
driver.get("http://www.amazon.com")
driver.page_source


# Closing or quitting:
driver.quit()
driver.close()