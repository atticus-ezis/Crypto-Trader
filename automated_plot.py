from datetime import datetime, timedelta, timezone
import os 
from coinbase.rest import RESTClient
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
from time import sleep 

def startup():

    granularity = 3600 * 24
    periods = 7

    length = granularity * periods

    end_time = datetime.now(timezone.utc)
    start_time = end_time - timedelta(seconds=length)

    start = str(int(start_time.timestamp()))
    end = str(int(end_time.timestamp()))

    product_id = "COTI-USD"
    granularity_str = "SIX_HOUR" # ONE_MINUTE, FIVE_MINUTE, FIFTEEN_MINUTE, THIRTY, ONE_HOUR, TWO, SIX_HOUR, ONE_DAY

    return start, end, product_id, granularity_str

def ohlc_grabber():

    api_key=os.getenv('CB_PUBLIC_KEY', None)
    api_secret=os.getenv('CB_PRIVATE_KEY', None)
    client = RESTClient(api_key=api_key, api_secret=api_secret)

    start, end, product_id, granularity_str = startup()

    product = client.get_candles(product_id=product_id, start=start, end=end, granularity=granularity_str)

    return product

def data_cleaner():

    product = ohlc_grabber()
    df = pd.DataFrame(product['candles'])

    df.rename(columns={'start':'time'}, inplace=True)

    df['time'] = df['time'].apply(lambda x: datetime.fromtimestamp(int(x)))

    df_close = df[['time','close']]

    df_close['close'] = df_close['close'].astype(float)

    return df_close

def data_plotter():

    df_close = data_cleaner()

    df_close.set_index('time', inplace=True)

    df_close['time_num'] = df_close.index.map(datetime.timestamp)

    slope, intercept = np.polyfit(df_close['time_num'], df_close['close'], 1)

    df_close['regression'] = slope * df_close['time_num'] + intercept

    difference =  df_close['regression'] - df_close['close']
    st_dv = difference.std()

    df_close['regression-upper'] = df_close['regression'] + st_dv
    df_close['regression-lower'] = df_close['regression'] - st_dv

    plt.figure(figsize=(10, 6))
    plt.plot(df_close.index, df_close['close'], marker='o', linestyle='-', color='b', label='Close Prices')
    plt.plot(df_close.index, df_close['regression'], linestyle='--', color='b', label='Regression Line')
    plt.plot(df_close.index, df_close['regression-upper'], linestyle='--', color='r', label='Sell Line')
    plt.plot(df_close.index, df_close['regression-lower'], linestyle='--', color='g', label='Buy Line')
    plt.title(f'Close Prices Over Time')
    plt.xlabel('Time')
    plt.ylabel('Close Price')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    while True:
        data_plotter()
        sleep(60)

main()








