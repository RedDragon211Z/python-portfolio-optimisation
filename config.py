import numpy as np

tickers = ["AAPL", "GOOGL", "AMZN", "MSFT", "META", "TSLA", "JPM", "NVDA", "SPY"]
start_date = "2020-01-01"
end_date = "2026-01-01"

TRADING_DAYS = 252

NUMBER_OF_PORTFOLIOS = 10000

INITIAL_WEIGHTS = np.array([
    0.12,  # AAPL
    0.12,  # GOOGL
    0.12,  # AMZN
    0.12,  # MSFT
    0.10,  # META
    0.10,  # TSLA
    0.10,  # JPM
    0.12,  # NVDA
    0.10  # SPY
])

