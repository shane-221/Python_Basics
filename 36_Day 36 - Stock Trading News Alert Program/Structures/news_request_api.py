from datetime import timedelta
import requests
import datetime as dt


class NewsApi:
    def __init__(self, stock, api_key, url):
        self.stock_name= stock
        self.api_key = api_key
        self.news_url = url

    def news_request(self):
        days =3
        # Todo: Creating the parameters withe the required arguments for data
        news_parameters={
                    "q":self.stock_name,
                    "apiKey":self.api_key,
                    "to": dt.datetime.now().strftime("%Y-%m-%d"),
                    "from" : (dt.datetime.now()-timedelta(days=days)).strftime("%Y-%m-%d"),            # For the last day
                    "language" :"en",
                    "sort": "popularity",          # By the newest article
                    "pageSize": "5"                 # Get me 5 of them
                        }

        # Todo: Sending the request FOR the data
        try:
            news_request = requests.get(url=self.news_url, params= news_parameters)
            data = news_request.json()
            final_data = []
            if data["totalResults"]!=0:
                for articles in data["articles"]:
                    final_data.append([articles["source"]["name"], articles["title"], articles["author"],articles["url"]])
                return final_data
            elif data["totalResults"]==0:
                print(f"No articles results found for the specified range of {days} days.")
                return final_data
            else:
                "There is an issue with the articles API request"
                return None
        except Exception as e:
            print( f"There was a News error. Code:{e}")
            return exit()
