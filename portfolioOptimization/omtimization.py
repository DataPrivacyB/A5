import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

def Optimize(tickers):
    # print("inoptimize",tickers)
    # tickers = pd.read_csv(".\\DataSets\\ind_nifty500list.csv")
    # tickers = tickers['Symbol'][0:4]
    tot = pd.DataFrame()
    for ticker in tickers:
    #stocks = ['AAPL', 'AMZN', 'MSFT', 'YHOO']
        #print(ticker)
        df1 = pd.read_csv("C:\\Users\\sunilchaudhari\\Desktop\\A5Pull\\portfolioOptimization\\DataSets\\Nifty4YearsData\\{}.csv".format(ticker))
        df1.rename(columns={'Close' :ticker},inplace = True)
        df1 = df1[ticker]
        tot = pd.concat([tot,df1],axis=1)
    # print(tot)
    tot.sort_index(inplace=True)
    returns = tot.pct_change()
    # print(returns)
    mean_daily_returns = returns.mean()
    print(mean_daily_returns)
    cov_matrix = returns.cov()

    # # set number of runs of random portfolio weights
    num_portfolios = 25000
    #
    # # set up array to hold results
    print("hello1")
    results = np.zeros((4+len(tickers)-1,num_portfolios))
    print("hello2")
    #
    for i in range(num_portfolios):
        # select random weights for portfolio holdings
        weights = np.array(np.random.random(len(tickers)))
        # rebalance weights to sum to 1
        weights /= np.sum(weights)
        # print("weights",weights)
        # calculate portfolio return and volatility
        portfolio_return = np.sum(mean_daily_returns * weights) * 252
        portfolio_std_dev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252)

        # store results in results array
        results[0, i] = portfolio_return
        results[1, i] = portfolio_std_dev
        # store Sharpe Ratio (return / volatility) - risk free rate element excluded for simplicity
        results[2, i] = results[0, i] / results[1, i]
        # iterate through the weight vector and add data to results array
        for j in range(len(weights)):
            results[j + 3, i] = weights[j]
        # convert results array to Pandas DataFrame
    columns = ['ret', 'stdev', 'sharpe']
    for ticker in tickers:
        columns.append(ticker)

    results_frame = pd.DataFrame(results.T, columns=columns)

    # locate position of portfolio with highest Sharpe Ratio
    returnList = []
    max_sharpe_port = results_frame.iloc[results_frame['sharpe'].idxmax()]
    returnList.append(max_sharpe_port)
    dfDict = {}
    j = 0
    for i in range(3, len(max_sharpe_port)):
        dfDict[tickers[j]] = max_sharpe_port[i]
        j += 1
    returnList.append(dfDict)
    # print(max_sharpe_port)
    # print()
    # locate positon of portfolio with minimum standard deviation
    min_vol_port = results_frame.iloc[results_frame['stdev'].idxmin()]

    # min_vol_port = pd.DataFrame(min_vol_port)
    dfDict = {}
    j=0
    for i in range(3,len(min_vol_port)):
        dfDict[tickers[j]] = min_vol_port[i]
        j += 1

    returnList.append(min_vol_port)
    returnList.append(dfDict)
    # print("max", returnList[0])
    # print("ret1",returnList[0].ret)
    # print("vol1", returnList[0].stdev)
    # print("min", returnList[2])
    # print("ret2", returnList[2].ret)
    # print("vol2", returnList[2].stdev)

    # create scatter plot coloured by Sharpe Ratio
    # plt.scatter(results_frame.stdev, results_frame.ret, c=results_frame.sharpe, cmap='RdYlBu')
    # plt.xlabel('Volatility')
    # plt.ylabel('Returns')
    # plt.colorbar()
    # # plot red star to highlight position of portfolio with highest Sharpe Ratio
    # plt.scatter(max_sharpe_port[1], max_sharpe_port[0], marker=(5, 1, 0), color='r', s=1000)
    # # plot green star to highlight position of minimum variance portfolio
    # plt.scatter(min_vol_port[1], min_vol_port[0], marker=(5, 1, 0), color='g', s=1000)
    # plt.show()

    return returnList

