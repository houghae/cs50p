import yfinance as yf
import time

def main():
    filters = user_query()
    tickers = stock_screener(filters)
    print(f"Selected tickers: {tickers}")

def user_query():
    # Welcome the user
    # Ask some questions about a preferred strategy and their goals. Leave room for 'I don't know'.
    # Store inputs for use in how the rest of the program will operate.
    print("Hi! Welcome to my CS50 investment tool. Let's go through a few questions to get a feel for how you'd like to invest. Ready?")
    time.sleep(5)
    user_tolerance = int(input("On a scale of 1-5, how risk tolerant are you? (1 being very risk adverse and 5 being very risk tolerant.)\n"))
    user_goal = input("What are your trading/investment goals?\n") # Consider using argparse to create multiple choice question.
    user_strategy = input("Do you have a preferred trading strategy?\n") # momentum, gap trade, std dev fade, breakout, etc.
    user_indicators = input("What indicators would you like to start with?\n") # MACD, bollinger bands, mov avg, std dev channel, etc.
    user_market = input("Do you prefer to trade trending or sideways markets?\n")
    return {"tolerance": user_tolerance, "goal": user_goal, "strategy": user_strategy, "indicators": user_indicators, "market": user_market}

def stock_screener(filters):
    # Start with multiple markets and narrow down potential tickers to explore based on user questions. 
    print("Running stock screener with the following filters:")
    for key, value in filters.items():
        print(f"{key}: {value}")
    return ["AAPL", "MSFT", "TSLA"]  # Example tickers



def get_data():
    tickers = yf.Tickers("AAPL MSFT AMZN QQQ NVDA")
    history = tickers.tickers["AAPL"].history(period="1yr", interval="1d")



def function_n():
    ...


if __name__ == "__main__":
    main()