import requests
from prettytable import PrettyTable
import os

"""api_key = 'pk_34f14243a7624a73a7ff7000f47f7e17' #TODO hide api key - add env variable
"""
class CryptoCurrency:
    base_url = "https://cloud.iexapis.com/stable/crypto"
    prices = []
    def __init__(self, symbol):
        self.symbol = symbol
        self.add_prices_to_list()

    @property
    def complete_url(self):
        return f"{CryptoCurrency.base_url}/{self.symbol}/price?token={os.environ['API_KEY']}"

    @property
    def price(self):
        req = requests.get(self.complete_url).json() #This method will convert the JSON data into a Python dictionary
        return float(req.get('price'))

    def add_prices_to_list(self):
        CryptoCurrency.prices.append([self.price, self.symbol])

    @staticmethod
    def prices_table():
        pt = PrettyTable(["Prices", "Crypto Name"])
        pt.add_rows(CryptoCurrency.prices)
        return pt

    @staticmethod
    def clean_prices():
        CryptoCurrency.prices.clear()

    @staticmethod
    def show_prices():
        print(CryptoCurrency.prices_table())