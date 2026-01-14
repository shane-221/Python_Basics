import os
import requests
from dotenv import load_dotenv
load_dotenv()

class BearerToken:
    def  __init__(self):
        self.body = None
        self.header = None
        self.API_KEY= os.getenv("amadeus_api_key")
        self.API_SECRET =os.getenv("amadeus_api_secret")


        self.amadeus_url= os.getenv("amadeus_bearer_token")

    

    def get_new_token(self):
        self.header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.body = {
            'grant_type': 'client_credentials',
            'client_id': self.API_KEY,
            'client_secret': self.API_SECRET
                    }
        try:
            connection =requests.post(url=self.amadeus_url, headers = self.header, data =self.body)
            data= connection.json()
            bearer_token = f"Bearer {data["access_token"]}"
            return bearer_token
        except Exception as e:
            print (f"There is an exception:{e}")


