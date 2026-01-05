#======================================================================================================================#
                                                # Imports
#======================================================================================================================#


from Structures.stock_request_api import *
from Structures.news_request_api import *
from dotenv import load_dotenv
load_dotenv(dotenv_path="../Storage_files/.env")
from Structures.website_code_conversion import *
import datetime
from Structures.send_email import *



#======================================================================================================================#
                                                # Constants
#======================================================================================================================#

    # Todo: Company
STOCK = "IBM"
COMPANY_NAME = "IBM"

    # Todo: Price Constants
PRICE_API_KEY= os.getenv("PRICE_API_KEY")
PRICE_url=os.getenv("PRICE_url")
PRICE_CHANGE_CONDITION  = os.getenv("PRICE_CHANGE_CONDITION")

    # Todo: News constants
NEWS_URL= os.getenv("NEWS_URL")
NEWS_API_KEY=os.getenv("NEWS_API_K"
                       "EY")
    #Todo: Data constants
TODAY =datetime.date.today()

    # Todo: Email Constants
TO_EMAIL =os.getenv("to_email")
FROM_EMAIL =os.getenv("from_email")
HOST = os.getenv("HOST")
PASSWORD = os.getenv("PASSWORD")

#======================================================================================================================#
                #   Step 1 ,2 , and 3: Work out the price change of the companies
#======================================================================================================================#
    # Todo : Work out the price change for the Companies
stock =StockApi(STOCK, PRICE_API_KEY, PRICE_url)
price_data = stock.price_request()

    # Todo: Capture the error statements: Print statement from stock_request_api.py and then exit()
if price_data is None:
    exit()

#======================================================================================================================#
        # Step 4: Checking if the news api needs to be sent depending on the price change condition
#======================================================================================================================#


    # Todo: Clarifying condition to send the email b
if price_data< -1*PRICE_CHANGE_CONDITION or price_data>PRICE_CHANGE_CONDITION:
    # Todo: News email request
    news = NewsApi(STOCK, NEWS_API_KEY, NEWS_URL)
    news_data = news.news_request()

    # Todo: Outcomes from the api request.
    if news_data is None:
        # Todo: Capture the error statements in the news_request_api.py and then exit()
        exit()

    else:
        # =============================================================================================================#
                    # Step 5: Take the price change data and the news data and send it to email
        # =============================================================================================================#
                        # Todo( Overall): Email html code being prepared

        # Todo:  When there is news to be presented-create a custom section for each of the companies.
        CompanyData = CompanyWebsiteSection(stock=STOCK, price_change=price_data, articles = news_data)
        html_code = CompanyData.structure()


        # # Todo: Places the data into the correct section of the template html file.
        # with open("../Structures/email_format.html", mode="r") as file:
        #     email_content  = file.read()
        #     final_content_html = email_content.replace("<!-- Inject your code here -->", html_code)
        #
        #
        #
        #     # Todo: Once replaced- take this new file and place it into output file with date.
        # with open(f"../Output_Emails/output_format_{TODAY}.html", mode="w") as file:
        #     file.write(final_content_html)
        #
        # # Todo: send the email using the correct subject and parameters.
        #
        #                 # Email code being sent
        # email_request =Email(to_email=TO_EMAIL,
        #                      from_email=FROM_EMAIL,
        #                      password=PASSWORD,
        #                      host=HOST
        #                      )
        # email_request.send_email()