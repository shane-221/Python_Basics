#------------------------------------------------Imports---------------------------------------------------------------#

import os
from Structures.stock_request_api import *
from Structures.news_request_api import *
from dotenv import load_dotenv
load_dotenv(dotenv_path="../Storage_files/.env")
from Structures.company_website_section import *
import datetime
from Structures.send_email import *
import mjml


#---------------------------------------------------Constants ---------------------------------------------------------#
STOCK = "IBM"
COMPANY_NAME = "IBM"
PRICE_API_KEY= os.getenv("PRICE_API_KEY")
PRICE_url=os.getenv("PRICE_url")

NEWS_URL= os.getenv("NEWS_URL")
NEWS_API_KEY=os.getenv("NEWS_API_KEY")

#
#-------------------------------------------------Step 1 AND 2---------------------------------------------------------#

    # Todo : Running the API request for price using Classes and Exception handling
stock =StockApi(STOCK, PRICE_API_KEY, PRICE_url)

    # Price data output would be the percentage change or the exit loop.
price_data = stock.price_request()
if price_data is None:
    # Printed the response through the api itself
    exit()


# #--------------------------------------------------Step 4--------------------------------------------------------------#
today =datetime.date.today()

# Todo: Clarifying condition to send the email
if price_data<-1 or price_data>1:
    # Todo: News email request
    news = NewsApi(STOCK, NEWS_API_KEY, NEWS_URL)
    news_data = news.news_request()

    # Need to exit the program if there are no news to present
    if news_data is None:
        exit()
    else:
        #--------------------------------------------------Step 5------------------------------------------------------#
                        # Todo: Email html code being prepared

        # Todo:  If there is news present--- Then need the email needs to be sent to the individual.
        CompanyData = CompanyWebsiteSection(stock=STOCK, price_change=price_data, articles = news_data)
        #Todo: Gets the company data in the correct html format
        company_html = CompanyData.structure()
        # Todo: Places the data into the correct sectiopn of the txt file
            # Changes the code for the email file
        with open("../Structures/email_format.mjml", mode="r") as file:
            email_content  = file.read()
            final_content_mjml = email_content.replace("<!-- Inject your code here -->", company_html)
            html_output =mjml.mjml2html(final_content_mjml)


            # Write this new file back to the original file
        with open(f"../Output_Emails/output_format_{today}.html", mode="w") as file:
            file.write(html_output)


                        # Email code being sent
        email_request =Email(to_email=os.getenv("to_email"),
                             from_email=os.getenv("from_email"),
                             password=os.getenv("password"),
                             host="SMTP.gmail.com"
                             )
        email_request.send_email()