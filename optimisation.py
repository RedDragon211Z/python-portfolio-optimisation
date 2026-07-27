import numpy as np
from scipy.optimize import minimize

from portfolio import portfolio_statistics


def minimise_volatility(
        weights,
        annual_covariance
):
    """
    Objective function:
    minimise portfolio volatility
    """

    portfolio_volatility = np.sqrt(
        weights.T @ annual_covariance @ weights
    )

    return portfolio_volatility



def optimise_portfolio(
        target_return,
        annual_returns,
        annual_covariance,
        number_of_assets
):

    # Starting guess: equal allocation to every asset
    initial_weights = np.ones(number_of_assets) / number_of_assets


    # Constraint 1:
    # All portfolio weights must add up to 100%
    constraints = [
        {
            "type": "eq",
            "fun": lambda weights: np.sum(weights) - 1
        },

        # Constraint 2:
        # Portfolio must achieve target return
        {
            "type": "eq",
            "fun": lambda weights:
                np.dot(weights, annual_returns) - target_return
        }
    ]


    # Each asset weight must be between 0% and 100%
    bounds = tuple(
        (0, 1)
        for _ in range(number_of_assets)
    )


    result = minimize(
        minimise_volatility,
        initial_weights,
        args=(annual_covariance,),
        method="SLSQP",
        bounds=bounds,
        constraints=constraints
    )


    return result