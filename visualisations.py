import matplotlib.pyplot as plt
import seaborn as sea


def plot_normalised_prices(close_prices, tickers):

    normalised_prices = close_prices / close_prices.iloc[0]

    plt.figure(figsize=(10,6))

    plt.title("Normalised Stock Prices")
    plt.xlabel("Date")
    plt.ylabel("Growth of £1 Investment")

    plt.plot(normalised_prices)

    plt.legend(tickers)

    plt.show()



def plot_risk_return(annual_volatility, annual_return, tickers):

    plt.figure(figsize=(10,6))

    plt.scatter(
        annual_volatility,
        annual_return
    )

    for ticker in tickers:
        plt.annotate(
            ticker,
            (
                annual_volatility[ticker],
                annual_return[ticker]
            )
        )

    plt.xlabel("Annual Volatility (Risk)")
    plt.ylabel("Annual Return")
    plt.title("Risk vs Return of Individual Assets")

    plt.show()



def plot_correlation_matrix(returns):

    correlation_matrix = returns.corr()

    plt.figure(figsize=(8,6))

    sea.heatmap(
        correlation_matrix,
        annot=True,
        cmap="coolwarm",
        linewidths=0.5
    )

    plt.title("Correlation Matrix of Daily Stock Returns")

    plt.show()

def plot_monte_carlo(
        portfolio_volatilities,
        portfolio_returns,
        sharpe_ratios,
        best_volatility,
        best_return,
        minimum_volatility,
        minimum_volatility_return):

    plt.figure(figsize=(10,6))

    plt.scatter(
        portfolio_volatilities,
        portfolio_returns,
        c=sharpe_ratios,
        cmap="viridis",
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


def plot_efficient_frontier(
        portfolio_volatilities,
        portfolio_returns,
        sharpe_ratios,
        best_volatility,
        best_return,
        minimum_volatility,
        minimum_volatility_return,
        efficient_volatilities,
        efficient_returns):


    plt.figure(figsize=(10,6))

    plt.scatter(
        portfolio_volatilities,
        portfolio_returns,
        c=sharpe_ratios,
        cmap="viridis",
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


    # Plot the actual efficient frontier
    plt.plot(
        efficient_volatilities,
        efficient_returns,
        linewidth=3,
        label="Efficient Frontier"
    )


    plt.xlabel("Annual Volatility (Risk)")
    plt.ylabel("Annual Return")
    plt.title("Monte Carlo Portfolio Optimisation")

    plt.grid(alpha=0.3)

    plt.legend()

    plt.show()