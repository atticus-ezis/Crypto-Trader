# pip3 install coinbase-advanced-py in virtual environment

import os 

from coinbase.rest import RESTClient

api_key=os.getenv('CB_PUBLIC_KEY', None)
api_secret=os.getenv('CB_PRIVATE_KEY', None)

client = RESTClient(api_key=api_key, api_secret=api_secret)

