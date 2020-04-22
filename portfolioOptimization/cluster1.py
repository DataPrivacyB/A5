import pandas_datareader.data as web
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import Normalizer
from sklearn.pipeline import make_pipeline
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs

def getClusters():
    #tickers = pd.read_csv(".\\DataSets\\ind_nifty500list.csv")
    tickers = pd.read_csv("C:\\Users\\Akshay Bali\\Desktop\\A5Pull\\portfolioOptimization\\DataSets\\ind_nifty500list.csv")
    # tickers = pd.read_csv(".\\DataSets\\niftyShareNames.csv")
    tickers = tickers['Symbol'][0:350]
    # tickers = tickers['TICKER'][0:49]
    stock_open = pd.DataFrame()
    stock_close = pd.DataFrame()
    for ticker in tickers:
        df = pd.read_csv("C:\\Users\\Akshay Bali\\Desktop\\A5Pull\\portfolioOptimization\\DataSets\\Nifty4YearsData\\{}.csv".format(ticker))
        # df = pd.read_csv(".\\DataSets\\Nifty2YearsData\\{}.csv".format(ticker))

        df.rename(columns={'Close': ticker}, inplace=True)
        close = df[ticker]
        df.drop([ticker], 1, inplace=True)
        df.rename(columns={'Open': ticker}, inplace=True)
        open = df[ticker]

        # open.rename(columns={'Open' :ticker},inplace = True)
        # close.rename(columns={'Close': ticker}, inplace=True)
        stock_open = pd.concat([stock_open,open],axis=1)
        stock_open.fillna(0, inplace=True)

        stock_close = pd.concat([stock_close, close], axis=1)
        stock_close.fillna(0,inplace=True)

    # # Calculate daily stock movement
    stock_close = np.array(stock_close).T
    stock_open = np.array(stock_open).T

    row, col = stock_close.shape

    # create movements dataset filled with 0's
    movements = np.zeros([row, col])

    for i in range(0, row):
     movements[i,:] = np.subtract(stock_close[i,:], stock_open[i,:])

    #for i in range(0, len(tickers)):
     #print('Company: {}, Change: {}'.format(tickers[i], sum(movements[i][:])))


    # create the Normalizer
    normalizer = Normalizer()
    new = normalizer.fit_transform(movements)
    #print(new.max())
    #print(new.min())
    #print(new.mean())
    print("1")
    #
    normalizer = Normalizer()
    #
    # # create a K-means model with 10 clusters
    kmeans = KMeans(n_clusters=4 ,max_iter=10000)


    # # make a pipeline chaining normalizer and kmeans
    pipeline = make_pipeline(normalizer,kmeans)

    # # fit pipeline to daily stock movements
    pipeline.fit(movements)

    # # predict cluster labels
    labels = pipeline.predict(movements)

    # create a DataFrame aligning labels & companies
    df = pd.DataFrame({'labels': labels, 'companies': tickers})
    df = df.sort_values('labels')
    df.to_csv('C:\\Users\\Akshay Bali\\Desktop\\A5Pull\\portfolioOptimization\\DataSets\\temp.csv')


     # visualize the results
    reduced_data = PCA(n_components = 2).fit_transform(new)

    # # run kmeans on reduced data
    kmeans = KMeans(n_clusters=4, max_iter=100)
    kmeans.fit(reduced_data)
    labels = kmeans.predict(reduced_data)

    # create DataFrame aligning labels & companies
    dfDict = {}
    for i in range(0,len(labels)):
        dfDict[tickers[i]] = labels[i]
    # print(dfDict)
    df = pd.DataFrame({'labels': labels, 'companies': tickers})
    df = df.sort_values('labels')
    df.to_csv('C:\\Users\\Akshay Bali\\Desktop\\A5Pull\\portfolioOptimization\\DataSets\\temp.csv')
    return dfDict

    # # Define step size of mesh
    # h = 0.1
    # #
    # # plot the decision boundary
    # x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:,0].max() + 1
    # y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:,1].max() + 1
    # xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    #
    # # Obtain abels for each point in the mesh using our trained model
    # Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])
    #
    # # Put the result into a color plot
    # Z = Z.reshape(xx.shape)
    #
    # # define colorplot
    # cmap = plt.cm.Paired
    #
    # # plot figure
    # plt.clf()
    # plt.figure(figsize=(5,5))
    #
    # plt.imshow(Z, interpolation='nearest',
    #  # extent = (xx.min(), xx.max(), yy.min(), yy.max()),
    # extent = (-.6,.6,-.6,.6),
    #  cmap = cmap,
    #  aspect = 'auto', origin='lower')
    # # plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=5)
    #
    #
    # # plot the centroid of each cluster as a white X
    # centroids = kmeans.cluster_centers_
    # print('centroids',centroids)
    # # plt.scatter(centroids[:, 0], centroids[:, 1],
    # #  marker='x', s=169, linewidth=3,
    # #  color='w', zorder=10)
    #
    # # plt.title('K-Means Clustering on Stock Market Movements (PCA-Reduced Data)')
    # # plt.xlim(-.6, .6)
    # # plt.ylim(-.6, .6)
    # # plt.show()
    #
    #
    # style.use("fivethirtyeight")
    #
    # # make_blobs() is used to generate sample points
    # # around c centers (randomly chosen)
    #
    # # label the axes
    # #
    # # cost = []
    # # for i in range(1, 11):
    # #     KM = KMeans(n_clusters=i, max_iter=500)
    # #     KM.fit(new)
    # #
    # #     # calculates squared error
    # #     # for the clustered points
    # #     cost.append(KM.inertia_)
    # #
    # # # plot the cost against K values
    # # plt.plot(range(1, 11), cost, color='g', linewidth='3')
    # # plt.xlabel("Value of K")
    # # plt.ylabel("Sqaured Error (Cost)")
    # # plt.show()  # clear the plot
    # #
