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

final_html_code_companies=""

#======================================================================================================================#
                #   Step 1 : Convert ENV File companies into a list
#======================================================================================================================#
companies = os.getenv("COMPANIES")
companies_list =companies.split(",")
print(companies_list)


for company in companies_list:
    #==================================================================================================================#
                    #   Step 2 ,3 , and 4: Work out the price change for each of the companies
    #==================================================================================================================#
        # Todo : Work out the price change for the Companies
    stock =StockApi(company, PRICE_API_KEY, PRICE_url)
    price_data = stock.price_request()
    print(price_data)

        # Todo: Capture the error statements: Print statement from stock_request_api.py and then exit()
    if price_data is None:
        exit()

    #==================================================================================================================#
            # Step 5: Checking if the news api needs to be sent depending on the price change condition
    #==================================================================================================================#

        # Todo: Clarifying condition to send the email b
    if price_data< -1*int(PRICE_CHANGE_CONDITION) or price_data>int(PRICE_CHANGE_CONDITION):
        # Todo: News email request
        news = NewsApi(company, NEWS_API_KEY, NEWS_URL)
        news_data = news.news_request()
        print(news_data)
        # Todo: Outcomes from the api request.
        if news_data is None:
            # Todo: Capture the error statements in the news_request_api.py and then exit()
            exit()

        else:
            # =========================================================================================================#
                        # Step 6: Take the price change data and the news data and send it to email
            # =========================================================================================================#
                            # Todo( Overall): Email html code being prepared

            # Todo:  When there is news to be presented-create a custom section for each of the companies.
            CompanyData = CompanyWebsiteSection(stock=company, price_change=price_data, articles = news_data)
            html_code = CompanyData.structure()
            final_html_code_companies += html_code


# =============================================================================================================#
                        # Step 7: Final embedding into an HTML output file and sending.
# =============================================================================================================#


# Todo: Places the data into the correct section of the template html file.
with open("../Structures/email_format.html", mode="r") as file:
    email_content  = file.read()
    final_content_html = email_content.replace("<!-- Inject your code here -->", final_html_code_companies)



# Todo: Once replaced- take this new file and place it into output file with date.
with open(f"../Output_Emails/output_format_{TODAY}.html", mode="w") as file:
    file.write(final_content_html)

# Todo: send the email using the correct subject and parameters.

                # Email code being sent
email_request =Email(to_email=TO_EMAIL,
                     from_email=FROM_EMAIL,
                     password=PASSWORD,
                     host=HOST
                     )
email_request.send_email()