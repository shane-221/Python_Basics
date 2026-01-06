#======================================================================================================================#
             # List of stocks being actively traded( See Read_notes_before_using_section for use cases)
#======================================================================================================================#

# Todo: Import statements
import requests
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="../Confidential_data_file/.env")

# Todo: Constants
API_KEY = os.getenv("price_api_key")
CSV_URL = os.getenv("price_url")


# Todo; API Request
price_parameters = {
    "apikey": API_KEY,
    "function": "LISTING_STATUS",
    "state": "active"
}

price_request = requests.get(url=CSV_URL , params=price_parameters)
clean_data = price_request.content      # From Copilot


# Todo: add as a csv file
with open("Companies_list.csv", mode="w") as csv_file:
    csv_file.write(clean_data)