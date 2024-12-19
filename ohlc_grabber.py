from initialize import client
from datetime import datetime, timedelta, timezone
import pandas as pd

# define beginning time period for data

granularity = 3600 
hours = 10
length = granularity * hours

# get start and end time

end_time = datetime.now(timezone.utc)
start_time = end_time - timedelta(seconds=(length))

# convert to int timestamps

start_timestamp = int(start_time.timestamp())
end_timestamp = int(end_time.timestamp())

# convert to str

start = str(start_timestamp)
end = str(end_timestamp)
granularity_str = 'THIRTY_MINUTE'

# specify trading asset

product_id = "BTC-USD"

# plug into get candles 

product = client.get_candles(product_id=product_id, start=start, end=end, granularity=granularity_str)





# clean data

df = pd.DataFrame(product['candles'])

# Rename 'start' to 'time'
df.rename(columns={'start': 'time'}, inplace=True)

# change timestamp to readable date / time
df['time'] = df['time'].apply(lambda x: datetime.fromtimestamp(int(x)))


# remove volume 
df = df.drop(columns=['volume'])

# change prices to floats to be manipulated 
numeric_columns = ['low', 'high', 'open', 'close']
df[numeric_columns] = df[numeric_columns].astype(float)


print(df)

close_df = df[['time','close']]

print(close_df)