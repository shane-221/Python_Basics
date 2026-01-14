from dotenv import load_dotenv
from New_token_from_amadeus import BearerToken
load_dotenv()
import requests
import time

# ChatGPT Recommended it to run 3 times using the rage function in case time.sleep does not work.Seems
## like a good idea but did not implement it


def get_iata(amadeus_city_url, city_name):
    get_token = BearerToken()
    get_header_token = {"Authorization": get_token.get_new_token()}

    city = {"keyword": city_name,
            "subType": "CITY",
            }

    try:
        amadeus_request = requests.get(url=amadeus_city_url, params=city, headers=get_header_token)
        data = amadeus_request.json()

    except requests.exceptions.HTTPError as e:
            if e.response.status_code==429:
                time.sleep(2)

                amadeus_request = requests.get(url=amadeus_city_url, params=city, headers=get_header_token)
                data = amadeus_request.json()
            else:
                 return f"There is an  HTTP error: {e}"

    except Exception as e:
         return f"There is an error: {e}"

    finally:
        if ("data" in data) and (len(data['data']))>0:
            iata_code = data["data"][0]["iataCode"]
            return iata_code

        else:
            return " No Code available"

