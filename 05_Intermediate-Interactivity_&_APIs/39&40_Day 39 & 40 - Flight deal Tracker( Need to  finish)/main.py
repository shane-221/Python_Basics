# Purpose:  This section looks at the IATA Codes and populates them.


from dotenv import load_dotenv

load_dotenv()
from Get_IATA_request import *
import requests
import os

# ----------------------------------------Sheetly key information------------------------------------------------------#
# Todo: Prep part for the initial request


SHEET_URL = os.getenv("sheet_url")
SHEET_TOKEN = os.getenv("sheetly_token")
sheetly_header = {"Authorization": SHEET_TOKEN}

amadeus_city_url = f"{os.getenv("amadeus_url")}/reference-data/locations"

#------------------------------------------Get request to sheetly to pull all the data----------------------------------#
# Todo: Sending a get request
try:
    data_iata_codes = requests.get(url=SHEET_URL, headers=sheetly_header)
    print(data_iata_codes.text)
except Exception as e:
    print(F" There is an error:{e}")
finally:
    # Use list comprehension to update the data
    sheetly_data = data_iata_codes.json()
#-----------------------------------Getting Countries matched to Codes in Amadeus--------------------------------------#
# Todo: Getting a dictionary of interested countries:( line number: IATA Code) to be used in request etc
countries_iata_code = {x["city"]: (int(x["id"]), x["iataCode"]) for x in sheetly_data["prices"]}
final_country_iata_code = []

# Placed outside the loop to make sure that rate limit is not met.
for i in countries_iata_code:
    # Todo: First check to see if the IATA Codes are populated. If not you neeed to connect ot Amadeus and find the code
    if countries_iata_code[i][1] == "":
        # Todo:sending request with the missing items using the module Get_IATA_Request
        data = get_iata(amadeus_city_url=amadeus_city_url, city_name=i)

        # Todo: Data has come back from he request and the exception have been accounted for. Now need to update my list comprehension.
        country = i
        line_number = countries_iata_code[i][0]
        IATA_code = data
        final_country_iata_code.append({i: (line_number, IATA_code)})
    else:
        final_country_iata_code.append({i: (i[0], i[1])})


#---------------------------------Sending the IATA Codes to Sheetly ---------------------------------------------------#
for entry in final_country_iata_code:
    for city , (row, iata_code) in entry.items():
        payload_data = {
            "price": {
                "IATA Code": iata_code
            }
        }

        # Todo: Sending the final data through sheetly to excel
        send_iata_code_request = requests.put(url=f"{SHEET_URL}/{row}",
                                              headers=sheetly_header,
                                              json=payload_data)
        print(f"Amadeus:{send_iata_code_request.text}")
