#------------------------------------------------Imports---------------------------------------------------------------#

import os
from Structures.stock_request_api import *
from Structures.news_request_api import *
from dotenv import load_dotenv
load_dotenv(dotenv_path="../Storage_files/.env")
from Structures.website_code_conversion import *
import datetime
from Structures.send_email import *




#---------------------------------------------------Constants ---------------------------------------------------------#
STOCK = "IBM"
COMPANY_NAME = "IBM"
PRICE_API_KEY= os.getenv("PRICE_API_KEY")
PRICE_url=os.getenv("PRICE_url")

NEWS_URL= os.getenv("NEWS_URL")
NEWS_API_KEY=os.getenv("NEWS_API_K"
                       "EY")
today =datetime.date.today()

#
#-------------------------------------------------Step 1 AND 2---------------------------------------------------------#

    # Todo : Running the API request for price using Classes and Exception handling
stock =StockApi(STOCK, PRICE_API_KEY, PRICE_url)

    # Price data output would be the percentage change or the exit loop.
price_data = stock.price_request()
print(price_data)                                                                                                       # Check 1: works
if price_data is None:
    # Printed the response through the module itself-see_request_api.py
    exit()


#--------------------------------------------------Step 4--------------------------------------------------------------#


# Todo: Clarifying condition to send the email
if price_data<-1 or price_data>1:
    # Todo: News email request
    news = NewsApi(STOCK, NEWS_API_KEY, NEWS_URL)
    news_data = news.news_request()
    print(news_data)                                                                                                    # Check 2: works

    # Todo : Outcome 1 of the request - Need to exit the program if there are no news to present
    if news_data is None:
        exit()
    # Todo : Outcome 2 of the news email request - When there are news results to be presented.
    else:
        #--------------------------------------------------Step 5------------------------------------------------------#
                        # Todo: Email html code being prepared

        # Todo:  If there is news present---the email format needs to be changed to meet the new format
        CompanyData = CompanyWebsiteSection(stock=STOCK, price_change=price_data, articles = news_data)
        html_code = CompanyData.structure()
        # Todo: Places the data into the correct sectiopn of the txt file

        with open("../Structures/email_format.html", mode="r") as file:
            email_content  = file.read()
            final_content_html = email_content.replace("<!-- Inject your code here -->", html_code)



            # Write this new file back to the original file
        with open(f"../Output_Emails/output_format_{today}.html", mode="w") as file:
            file.write(final_content_html)

        # using the email function to create a subject

                        # Email code being sent
        email_request =Email(to_email=os.getenv("to_email"),
                             from_email=os.getenv("from_email"),
                             password=os.getenv("password"),
                             host="SMTP.gmail.com"
                             )
        email_request.send_email()