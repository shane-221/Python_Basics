import requests


class StockApi:
    def __init__(self, stock, api_key, url):
        self.stock_name= stock
        self.api_key = api_key
        self.price_url = url

    def price_request(self):
        # Todo: Creating the parameters withe the required arguments for data
        global price_request
        price_parameters = {
            "apikey": self.api_key,
            "function": "GLOBAL_QUOTE",
            "symbol": self.stock_name
        }

        # Todo: Sending the request FOR the data
        try:
            price_request = requests.get(url=self.price_url, params=price_parameters)
            data = price_request.json()

            if "Global Quote" in data:
                close_price = float((data["Global Quote"]["08. previous close"]).strip())
                current_price = float((data["Global Quote"]["05. price"]).strip())
                percent_change = float(round((((current_price - close_price) / close_price) * 100), 4))

                return percent_change

            else:
                print(f"Full response:{data["Error Message"].capitalize()} ")
                return None
        except Exception as e:
            print(f"There is an error with Price API:{e}.")
            return None