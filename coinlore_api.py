# coinlore_api.py

import requests


def get_global_crypto_data():
    url = "https://api.coinlore.net/api/global/"
    response = requests.get(url)
    return response.json()


def get_all_coins(start=0, limit=100):
    url = f"https://api.coinlore.net/api/tickers/?start={start}&limit={limit}"
    response = requests.get(url)
    return response.json()


# Define other API functions here...
def main():
    # Call the API functions and perform data analysis
    # Example:
    global_data = get_global_crypto_data()
    all_coins = get_all_coins()
    print(global_data)
    print(all_coins)
