# I want to calculate the percent std_dv in a week for every usd product 
import os
from coinbase.rest import RESTClient
from datetime import datetime, timedelta, timezone
from initialize import client
import requests
import pandas as pd
import numpy as np
from scipy.stats import linregress

def get_coinbase_products_in_usd():
    url = "https://api.pro.coinbase.com/products"
    response = requests.get(url)

    if response.status_code == 200:
        products = response.json()
        usd_products = [product for product in products if product['quote_currency'] == 'USD']
        # get a list of product symbols, stripping out the '-USD' part
        usd_product_symbols = [product['id'][:-4] for product in usd_products]
        return usd_products, usd_product_symbols
    else:
        print(f"Failed to fetch products: Status code {response.status_code}")
        return []
    
usd_products, usd_product_symbols = get_coinbase_products_in_usd()

#print()
#print(f'Number of products priced in USD: {len(usd_products)}',end='\n\n')

# ONE_MINUTE, FIVE_MINUTE, FIFTEEN_MINUTE, THIRTY, ONE_HOUR, TWO, SIX_HOUR, ONE_DAY





