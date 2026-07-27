import numpy as np

def annual_return(returns):

    average_daily_return = returns.mean()

    return (1 + average_daily_return) ** 252 - 1


def annual_volatility(returns):

    return returns.std() * np.sqrt(252)


def annual_covariance(returns):

    return returns.cov() * 252


def portfolio_statistics(weights,
                         annual_return,
                         annual_covariance):

    portfolio_return = np.dot(
        weights,
        annual_return
    )


    portfolio_volatility = np.sqrt(
        weights.T @ annual_covariance @ weights
    )
    return portfolio_return, portfolio_volatility