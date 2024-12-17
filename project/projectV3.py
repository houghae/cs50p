# Dependencies.
import matplotlib.pyplot as plt
import csv
import os
import mplfinance as mpf
from alpaca.data import StockHistoricalDataClient
import pandas

# Alpaca trading keys and client.
# Paper trading key only. 
API_key = "PKJUWQ85O4FFNJPN99RC"
API_secret = "dicyifzWYOsz6K76AXUoa8ogI57sjPCAwrhyarDZ"

alpaca_client = StockHistoricalDataClient(API_key, API_secret)

# File paths for CSV storage


# Classes for indicators


# Class for matplotlib visualization
# Plot multiple timeframe charts each with their own indicators.


# Get CSV data function. 
# If CSV data exists already, return it. Else run a function to get it from Alpaca.


# Get Alpaca data function. 
# Get weekly, daily, 4hr, and 1hr data. Max timeframe, candlestick or OHLC data.


# Save CSV data function


# Read CSV data function


def main():
    ...
    # Create a while loop that asks for a ticker or exit command. 

    # Create a dict for all timeframes
    # Create for loop that loops through each timeframe and gets data for the user's ticker and the four timeframes.

    # Plot the data that was requested using the anchor visualization object.

    # Output call to action. Buy, sell, or wait.



if __name__ == "__main__":
    main()
