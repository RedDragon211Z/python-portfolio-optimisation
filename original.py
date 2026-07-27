import numpy as np
import matplotlib.pyplot as plt
import scipy
import yfinance as yf
import pandas as pd
import seaborn as sea

# List of assets we want to analyse, e.g. Apple, Microsoft...
tickers = ["AAPL", "GOOGL", "AMZN", "MSFT", "META", "TSLA", "JPM", "NVDA", "SPY"]

 # Download historical daily market data from Yahoo Finance
stock_data = yf.download(tickers, start = "2020-01-01", end = "2026-01-01")
# The dataset contains Open, High, Low, Close prices and trading volume for each company between these dates

# Extract only closing prices
close_prices = stock_data["Close"]

# Calculate daily percentage returns
returns = close_prices.pct_change()

#Remove rows containing missing values where returns cannot be calculated
returns = returns.dropna()

# Calculate average daily return for each stock
average_daily_return = returns.mean()

# Convert daily returns into annual returns
# There are approximately 252 trading days per year
# This assumes the average daily return continues throughout the year
annual_return = (1+average_daily_return) ** 252 - 1

# Calculate daily volatility (how much the returns fluctuate) using the standard deviation
daily_volatility = returns.std()
annual_volatility = daily_volatility * np.sqrt(252)

normalised_prices = close_prices / close_prices.iloc[0]
plt.figure(figsize=(10,6))

plt.title("Normalised Stock Prices")
plt.xlabel("Date")
plt.ylabel("Growth of £1 Investment")
plt.plot(normalised_prices)
plt.legend(tickers)
plt.show()

plt.figure(figsize=(10,6))

plt.scatter(annual_volatility, annual_return)

for ticker in tickers:
    plt.annotate(ticker,(annual_volatility[ticker],annual_return[ticker]))

plt.xlabel("Annual Volatility (Risk)")
plt.ylabel("Annual Return")
plt.title("Risk vs Return of Individual Assets")
plt.show()

correlation_matrix = returns.corr()

plt.figure(figsize=(8,6))

sea.heatmap(correlation_matrix,annot=True, cmap="coolwarm",linewidths=0.5)
plt.title("Correlation Matrix of Daily Stock Returns")
plt.show()

weights = np.array([
    0.12,  # AAPL
    0.12,  # GOOGL
    0.12,  # AMZN
    0.12,  # MSFT
    0.10,  # META
    0.10,  # TSLA
    0.10,  # JPM
    0.10,  # SPY
    0.12   # NVDA
])

portfolio_return = np.dot(weights, annual_return)
covariance_matrix = returns.cov()

annual_covariance = covariance_matrix * 252
portfolio_volatility = np.sqrt(np.dot(weights.T,np.dot(annual_covariance, weights)))

def portfolio_simulation(weights, annual_return, annual_covariance):
    portfolio_return = np.dot(weights, annual_return)
    portfolio_volatility = np.sqrt(np.dot(weights.T,np.dot(annual_covariance, weights)))
    return portfolio_return, portfolio_volatility

number_of_portfolios = 10000

portfolio_returns = []
portfolio_volatilities = []
portfolio_weights = []

for i in range(number_of_portfolios):

    random_weights = np.random.random(len(tickers))

    # Normalise weights so they add up to 100%
    random_weights = random_weights / np.sum(random_weights)

    portfolio_return, portfolio_volatility = portfolio_simulation(
        random_weights,
        annual_return,
        annual_covariance
    )
    portfolio_returns.append(portfolio_return)
    portfolio_volatilities.append(portfolio_volatility)
    portfolio_weights.append(random_weights)

portfolio_returns = np.array(portfolio_returns)
portfolio_volatilities = np.array(portfolio_volatilities)

sharpe_ratios = portfolio_returns / portfolio_volatilities

for i in range(len(sharpe_ratios)):
    if sharpe_ratios[i] == np.max(sharpe_ratios):
        best_portfolio_number = i
        print(best_portfolio_number)

best_return = portfolio_returns[best_portfolio_number]
best_volatility = portfolio_volatilities[best_portfolio_number]
best_weights = portfolio_weights[best_portfolio_number]

print(f"Best portfolio return: {best_return:.2%}")
print(f"Best portfolio risk: {best_volatility:.2%}")
print(f"Best portfolio weights: ")

for ticker, weight in zip(tickers, best_weights):
    print(f"{ticker}: {weight:.2%}")


for i in range(len(portfolio_volatilities)):
    if portfolio_volatilities[i] == np.min(portfolio_volatilities):
        minimum_volatility_index = i

minimum_volatility_return = portfolio_returns[minimum_volatility_index]

minimum_volatility = portfolio_volatilities[minimum_volatility_index]

minimum_volatility_weights = portfolio_weights[minimum_volatility_index]

print(f"Minimum volatility portfolio return: {minimum_volatility_return:.2%}")
print(f"Minimum volatility portfolio risk: {minimum_volatility:.2%}")

print("\nMinimum volatility allocation:")

for ticker, weight in zip(tickers, minimum_volatility_weights):
    print(f"{ticker}: {weight:.2%}")

plt.figure(figsize=(10,6))

plt.scatter(
    portfolio_volatilities,
    portfolio_returns,
    c = sharpe_ratios,
    cmap = "viridis",
    s=8,
    alpha=0.4,
    label="Simulated Portfolios"
)
plt.colorbar(label="Sharpe Ratio")

plt.scatter(
    best_volatility,
    best_return,
    marker="*",
    s=300,
    c=[max(sharpe_ratios)],
    cmap="viridis",
    vmin=min(sharpe_ratios),
    vmax=max(sharpe_ratios),
    label="Maximum Sharpe Ratio"
)

plt.scatter(
    minimum_volatility,
    minimum_volatility_return,
    marker="o",
    s=150,
    label="Minimum Volatility Portfolio"
)

plt.xlabel("Annual Volatility (Risk)")
plt.ylabel("Annual Return")
plt.title("Monte Carlo Portfolio Optimisation")

plt.grid(alpha=0.3)

plt.legend()

plt.show()
