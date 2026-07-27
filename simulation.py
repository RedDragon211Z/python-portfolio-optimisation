import numpy as np

from portfolio import portfolio_statistics

def monte_carlo_simulation(
    annual_return,
    annual_covariance,
    number_of_portfolios,
    number_of_assets
):

    portfolio_returns = []

    portfolio_volatilities = []

    portfolio_weights = []

    for _ in range(number_of_portfolios):

        weights = np.random.random(number_of_assets)

        weights /= weights.sum()

        portfolio_return, portfolio_volatility = (
            portfolio_statistics(
                weights,
                annual_return,
                annual_covariance
            )
        )

        portfolio_returns.append(portfolio_return)

        portfolio_volatilities.append(portfolio_volatility)

        portfolio_weights.append(weights)

    return (
        np.array(portfolio_returns),
        np.array(portfolio_volatilities),
        portfolio_weights
    )