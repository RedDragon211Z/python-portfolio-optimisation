import yfinance as yf

def download_stock_data(tickers, start_date, end_date):

    stock_data = yf.download(
        tickers,
        start=start_date,
        end=end_date
    )

    return stock_data


def calculate_returns(stock_data):

    close_prices = stock_data["Close"]

    returns = close_prices.pct_change().dropna()

    return close_prices, returns