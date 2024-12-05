import yfinance as yf


def main():
    ticker, period, interval = user_input()
    fetch_data2(ticker, period, interval)


def fetch_data(ticker, period, interval):
    data1 = yf.download(ticker, period=period, interval=interval)
    return data1


def fetch_data2(ticker, period, interval):
    ticker1 = yf.Ticker(ticker)
    


def user_input():
    ticker = input("Provide ticker symbol:\n")
    period = input("Provide period length as 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max:\n")
    interval = input("Provide candlestick interval as 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo:\n")
    return ticker, period, interval


if __name__ == "__main__":
    main()