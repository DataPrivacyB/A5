from collections import Counter
import numpy as np
import pandas as pd
from sklearn.model_selection import cross_validate
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn import svm,neighbors,preprocessing,metrics,linear_model
from sklearn.model_selection import cross_val_score, cross_val_predict,StratifiedKFold
from sklearn import metrics
from sklearn.ensemble import VotingClassifier,RandomForestClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
import keras
from keras.models import Sequential
from keras.layers import Dense,LSTM

def process_data_for_labels(ticker):
    days = 14
    df = pd.read_csv('.\\DataSets\\niftyJoinedCloses.csv')
    df = df.dropna(axis=1, how='all')
    tickers = df.columns.values.tolist()

    if ticker in tickers:
        for i in range(1, days + 1):
            df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]

        return tickers[1:], df
    else:
        print("absent")
        return [], []



def buy_sell_hold(*args):
    cols = [c for c in args]
    requirement = 0.02
    for col in cols:
        if col > 0.025:
            return 1
        if col < -0.045:
            return -1
    return 0

def extract_featureSets(ticker):
    tickers, df = process_data_for_labels(ticker)
    df['{}_target'.format(ticker)] = list(map(buy_sell_hold,
                                              df['{}_1d'.format(ticker)],
                                              df['{}_2d'.format(ticker)],
                                              df['{}_3d'.format(ticker)],
                                              df['{}_4d'.format(ticker)],
                                              df['{}_5d'.format(ticker)],
                                              df['{}_6d'.format(ticker)],
                                              df['{}_7d'.format(ticker)],
                                              df['{}_8d'.format(ticker)],
                                              df['{}_9d'.format(ticker)],
                                              df['{}_10d'.format(ticker)],
                                              df['{}_11d'.format(ticker)],
                                              df['{}_12d'.format(ticker)],
                                              df['{}_13d'.format(ticker)],
                                              df['{}_14d'.format(ticker)]
                                              ))
    vals = df['{}_target'.format(ticker)].values.tolist()
    # str_vals = [str(i) for i in vals]
    # print('Data spread ',Counter(str_vals))

    df.fillna(0, inplace=True)
    df = df.replace([np.inf,-np.inf],np.nan)
    df.dropna(inplace=True)
    df_vals = df[[t for t in tickers]].pct_change()
    df_vals = df_vals.replace([np.inf,-np.inf],0)
    df_vals.fillna(0, inplace=True)
    X = df_vals.values
    y = df['{}_target'.format(ticker)].values

    return X,y,df

def do_ml(ticker):
    X,y,df = extract_featureSets(ticker)
    scaler = StandardScaler()

    model = Sequential()
    model.add(LSTM(50,))

    kf = KFold(n_splits=11)
    scores = []

    for train_index,test_index in kf.split(X,y):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        X_train = np.reshape(X_train,(X_train.shape[0],X_train.shape[1],1))
        print(X_train.shape)
        # print(y_train)
        # y_train = scaler.fit_transform(y).reshape(-1,1)
        # clf.fit(X_train, y_train)
        # scores.append(clf.score(X_test, y_test))

    # print(sum(scores)/len(scores))
    # print(max(scores))
    # return sum(scores)/len(scores)
    return 0

#do_ml('TCS')
df = pd.read_csv('.\\DataSets\\niftyJoinedCloses.csv')
df = df.dropna(axis=1, how='all')
tickers = df.columns.values.tolist()
confList = []
for ticker in tickers[1:20]:
    print(ticker)
    confList.append(do_ml(ticker))

sum = 0
for conf in confList:
    sum += conf
avg = sum/20
print("Avg Accuracy :",avg)
