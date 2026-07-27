from config import *

from data_loader import *

from portfolio import *

from simulation import *

from visualisations import *

from optimisation import *

# Download historical stock data
stock_data = download_stock_data(
    tickers,
    start_date,
    end_date
)


# Extract closing prices and calculate daily returns
close_prices, returns = calculate_returns(stock_data)


# Calculate annual statistics for each asset
annual_returns = annual_return(returns)

annual_volatilities = annual_volatility(returns)

annual_covariances = annual_covariance(returns)


# Plot individual stock analysis
plot_normalised_prices(
    close_prices,
    tickers
)

plot_risk_return(
    annual_returns,
    annual_volatilities,
    tickers
)

plot_correlation_matrix(
    returns
)


# Calculate your manually chosen portfolio
portfolio_return, portfolio_volatility = portfolio_statistics(
    INITIAL_WEIGHTS,
    annual_returns,
    annual_covariances
)

print(f"Chosen portfolio return: {portfolio_return:.2%}")
print(f"Chosen portfolio risk: {portfolio_volatility:.2%}")


# Run Monte Carlo simulation
portfolio_returns, portfolio_volatilities, portfolio_weights = monte_carlo_simulation(
    annual_returns,
    annual_covariances,
    NUMBER_OF_PORTFOLIOS,
    len(tickers)
)


# Calculate Sharpe ratios
sharpe_ratios = portfolio_returns / portfolio_volatilities


# Find maximum Sharpe portfolio
best_portfolio_number = np.argmax(sharpe_ratios)

best_return = portfolio_returns[best_portfolio_number]

best_volatility = portfolio_volatilities[best_portfolio_number]

best_weights = portfolio_weights[best_portfolio_number]


print("\nMaximum Sharpe Portfolio")
print(f"Return: {best_return:.2%}")
print(f"Risk: {best_volatility:.2%}")

for ticker, weight in zip(tickers, best_weights):
    print(f"{ticker}: {weight:.2%}")


# Find minimum volatility portfolio
minimum_volatility_index = np.argmin(portfolio_volatilities)

minimum_volatility_return = portfolio_returns[minimum_volatility_index]

minimum_volatility = portfolio_volatilities[minimum_volatility_index]

minimum_volatility_weights = portfolio_weights[minimum_volatility_index]


print("\nMinimum Volatility Portfolio")
print(f"Return: {minimum_volatility_return:.2%}")
print(f"Risk: {minimum_volatility:.2%}")

for ticker, weight in zip(tickers, minimum_volatility_weights):
    print(f"{ticker}: {weight:.2%}")


plot_monte_carlo(
    portfolio_volatilities,
    portfolio_returns,
    sharpe_ratios,
    best_volatility,
    best_return,
    minimum_volatility,
    minimum_volatility_return
)

target_returns = np.linspace(
    min(annual_returns),
    max(annual_returns),
    50
)

efficient_returns = []
efficient_volatilities = []
for target in target_returns:

    result = optimise_portfolio(
        target,
        annual_returns,
        annual_covariances,
        len(tickers)
    )

    efficient_returns.append(target)

    efficient_volatilities.append(result.fun)

plot_efficient_frontier(
    portfolio_volatilities,
    portfolio_returns,
    sharpe_ratios,
    best_volatility,
    best_return,
    minimum_volatility,
    minimum_volatility_return,
    efficient_volatilities,
    efficient_returns
)