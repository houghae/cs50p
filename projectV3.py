# Dependencies.
# Use matplotlib for charts, mplfinance is a specific module for charting stocks.
# Use Alpaca for stock data. Arguably more robust than yfinance.
# Use pandas for data handling and I/O. pandas is used heavily for data analysis.
# Use os to create dir
import matplotlib.pyplot as plt
import mplfinance as mpf
from alpaca.data import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
import pandas as pd
import os
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


# Alpaca trading keys and client.
# Paper trading key only.
# Capitalize vars that are constants, like API keys and dir paths. 
# Blur or replace keys before filming.
API_KEY = "placeholder"
API_SECRET = "placeholder"

alpaca_client = StockHistoricalDataClient(API_KEY, API_SECRET)

# Create file path for CSV storage in case there isn't yet a dir. 
# This enables portability and makes the code more robust if I share it.
HIST_DATA_DIR = "historical_data"
os.makedirs(HIST_DATA_DIR, exist_ok=True)

# Classes for indicators



# Class for matplotlib visualization
# Plot multiple timeframe charts each with their own indicators.



# If CSV data exists already, return it. Else run a function to get it from Alpaca.
def get_data(ticker, timeframe):
    # create csv var named ticker_timetrame.csv
    csv_file = os.path.join(HIST_DATA_DIR, f"{ticker}_{timeframe}.csv")
    # search hist data dir for that file. If it exists, return it. Else run the get alpaca data function.
    if os.path.exists(csv_file):
        return pd.read_csv(csv_file) # Prob need to do this later, pd.read_csv(filepath, index_col="timestamp", parse_dates=True)
    else:
        alpaca_data = get_alpaca_data(ticker, timeframe)
        alpaca_data.to_csv(csv_file)
        return alpaca_data


# Get Alpaca data function. 
def get_alpaca_data(ticker, timeframe):
    # Get weekly, daily, 4hr, and 1hr data. Max timeframe, candlestick or OHLC data.
    now = datetime.now(ZoneInfo("America/New_York"))
    tf_dict = {
        "1-Hour": [TimeFrameUnit.Hour, 1],
        "4-Hour": [TimeFrameUnit.Hour, 4],
        "Daily": [TimeFrameUnit.Day, 1],
        "Weekly": [TimeFrameUnit.Week, 1],
    }

    request = StockBarsRequest(
        symbol_or_symbols = [ticker],
        # TFU can be Hour, Day, Week, Month. Use amount = 4 for 4hr timeframe, 1 for day and week.
        timeframe=TimeFrame(amount=tf_dict[timeframe][1], unit=tf_dict[timeframe][0]), # specify timeframe
        start=now - timedelta(days = 1827), # specify start datetime, default=the beginning of the current day.
        # end_date=None, # specify end datetime, default=now
        limit=10, # specify number of data points
    )
    return alpaca_client.get_stock_bars(request).df



def main():
    ...
    # Create a while loop that asks for a ticker or exit command. 

    # Create a dict for all timeframes
    # Create for loop that loops through each timeframe and gets data for the user's ticker and the four timeframes.

    # Plot the data that was requested using the anchor visualization object.

    # Output call to action. Buy, sell, or wait.



if __name__ == "__main__":
    main()
