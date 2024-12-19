import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ohlc_grabber import df, close_df
import mplfinance as mpf
from datetime import datetime

# set start as index column
close_df.set_index('time', inplace=True)

# convert datetime to numeric format for calculation 
close_df['time_num'] = close_df.index.map(datetime.timestamp)

# Calculate the regression line
slope, intercept = np.polyfit(close_df['time_num'], close_df['close'], 1)
close_df['regression'] = slope * close_df['time_num'] + intercept

# Calculate the residuals and their standard deviation
residuals = close_df['close'] - close_df['regression']
std_dev = residuals.std()

close_df['regression_upper'] = close_df['regression'] + std_dev
close_df['regression_lower'] = close_df['regression'] - std_dev


# plot
plt.figure(figsize=(10, 6))
plt.plot(close_df.index, close_df['close'], marker='o', linestyle='-', color='b', label='Close Prices')
plt.plot(close_df.index, close_df['regression'], linestyle='--', color='b', label='Regression Line')
plt.plot(close_df.index, close_df['regression_upper'], linestyle='--', color='r', label='Sell Line')
plt.plot(close_df.index, close_df['regression_lower'], linestyle='--', color='g', label='Buy Line')
plt.title('Close Prices Over Time')
plt.xlabel('Time')
plt.ylabel('Close Price')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
