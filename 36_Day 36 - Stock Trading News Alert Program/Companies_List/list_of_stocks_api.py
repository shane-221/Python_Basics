#======================================================================================================================#
             # Current list of stocks being actively traded( See Read_notes_before_using_section for output)
#======================================================================================================================#

# Todo: Import statements
import requests
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="../Storage_files/.env")

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
data = price_request.text

# Todo: add as a csv file
with open("Companies_list.csv", mode="w") as csv_file:
    csv_file.write(data)