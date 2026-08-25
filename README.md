****Portfolio Risk and Optimisation using Monte Carlo Simulation** Overview**

A Python-based portfolio analysis and optimisation project using historical stock market data to investigate the relationship between investment return and risk.

The project analyses a portfolio of major US equities and the S&P 500, calculates key risk and return measures, and uses Monte Carlo simulation to evaluate thousands of possible portfolio allocations.

****Objectives**:**
- Analyse historical performance of selected assets
- Calculate annualised returns and volatility
- Investigate correlations between asset returns
- Calculate portfolio-level risk and return
- Simulate thousands of possible portfolio allocations
- Identify portfolios with the highest Sharpe ratio
- Identify the minimum volatility portfolio
- Analyse the efficient frontier and portfolio risk-return trade-offs
Assets Analysed

The portfolio contains:

- Apple (AAPL)
- Alphabet (GOOGL)
- Amazon (AMZN)
- Microsoft (MSFT)
- Meta (META)
- Tesla (TSLA)
- JPMorgan Chase (JPM)
- NVIDIA (NVDA)
- S&P 500 ETF (SPY)

Historical daily market data is retrieved using the Yahoo Finance API through the yfinance Python library.

**Methodology**

**1. Historical Data**

Daily market data is collected from January 2020 to January 2026. Closing prices are used to calculate daily percentage returns.

**2. Asset Risk and Return**

Daily returns are used to calculate:

- Annualised return
- Daily volatility
- Annualised volatility
- Correlation between assets
- Covariance between asset returns

Annualisation assumes approximately 252 trading days per year.

**3. Portfolio Analysis**

Portfolio return is calculated from the weighted returns of the individual assets.

Portfolio volatility incorporates the covariance between assets, allowing the model to account for the effects of diversification rather than simply averaging individual asset volatility.

**4. Monte Carlo Simulation**

The model generates 10,000 randomly weighted portfolios.

For each portfolio:

- Random asset weights are generated
- Weights are normalised to sum to 100%
- Portfolio return is calculated
- Portfolio volatility is calculated
- Sharpe ratio is calculated
- The portfolio allocation is stored for comparison

The simulated portfolios are then compared to identify the maximum Sharpe ratio portfolio and minimum volatility portfolio.

**5. Efficient Frontier**

The efficient frontier is used to examine the portfolios offering the highest expected return for a given level of risk.

This provides a visual representation of the trade off between portfolio risk and return and allows the simulated portfolios to be evaluated against portfolio optimisation principles.

**Visualisations**

The project produces several visualisations:

- Normalised Stock Prices show the growth of a hypothetical £1 investment in each asset over the selected period.

- Risk vs Return compares the annualised return and volatility of each individual asset.

- Correlation Matrix shows the correlation between the daily returns of each asset, helping demonstrate the potential diversification benefits of combining assets with different return behaviour.

- Monte Carlo Portfolio Optimisation plots the simulated portfolios according to their annualised risk and return. Colour represents the Sharpe ratio, with the maximum Sharpe ratio and minimum volatility portfolios highlighted.

**Technologies**
- Python
- NumPy
- Pandas
- SciPy
- Matplotlib
- Seaborn
- yfinance
- Git / GitHub
- 
**Project Structure**
python-portfolio-optimisation/
│
├── config.py
├── data_loader.py
├── portfolio.py
├── simulation.py
├── optimisation.py
├── visualisations.py
├── main.py
└── README.md

The project is separated into modules to keep data collection, portfolio calculations, simulation, optimisation, visualisation, and configuration logically independent.

**Running the Project**

- Clone the repository: git clone https://github.com/RedDragon211Z/python-portfolio-optimisation.git

- Install the required dependencies: pip install -r requirements.txt

- Run the main program: python main.py
- 
****Key Skills Demonstrated**:**
  
- Financial data analysis
- Portfolio risk modelling
- Statistical analysis
- Monte Carlo simulation
- Portfolio optimisation
- Data visualisation
- Python programming
- Modular software design
- Git and GitHub
