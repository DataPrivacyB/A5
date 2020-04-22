from collections import Counter
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
from sklearn import svm,neighbors
from sklearn.ensemble import VotingClassifier,RandomForestClassifier
from sklearn.preprocessing import StandardScaler

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
    # scaler.fit_transform(X.f3.values.reshape(-1, 1))

    # scaler = MinMaxScaler(feature_range=(-1, 1))
   # X = scaler.fit_transform(X)
    #y = scaler.fit_transform(y)

    #   X_train, X_test,y_train, y_test = train_test_split(X,y,test_size=0.35,random_state=10)
#BaggingClassifier(base_estimator = )
    clf = VotingClassifier([('lsvm',svm.LinearSVC(dual=False)),
                             ('knn', neighbors.KNeighborsClassifier()),
                             ('rfor', RandomForestClassifier(n_estimators=30)),
                             # ('dtree',BaggingClassifier(base_estimator =DecisionTreeClassifier(),
                             #                            n_estimators=30,
                             #                            random_state=8))
                            ])

    kf = KFold(n_splits=11)
    scores = []

    for train_index,test_index in kf.split(X,y):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        # print(y_train)
        # y_train = scaler.fit_transform(y).reshape(-1,1)
        clf.fit(X_train, y_train)
        scores.append(clf.score(X_test, y_test))

    print(sum(scores)/len(scores))
    # print(max(scores))
    return sum(scores)/len(scores)
    #return max(scores)

#do_ml('TCS')
df = pd.read_csv('.\\DataSets\\niftyJoinedCloses.csv')
df = df.dropna(axis=1, how='all')
tickers = df.columns.values.tolist()
confList = [0,0,0,0,0,0]
countList = []
for ticker in tickers[1:]:
    print(ticker)
    x = do_ml(ticker)
    x = x * 100
    print("x :",x)
    x = int(x)

    if x <= 40:
        print("40")
        confList[0] += 1
    elif x >= 40 and x <= 45:
        print("45")
        confList[1] += 1
    elif x >= 45 and x <= 50:
        print("50")
        confList[2] += 1
    elif x >= 50 and x <= 55:
        print("55")
        confList[3] += 1
    elif x >= 55 and x <= 60:
        print("60")
        confList[4] += 1
    else:
        print("0")
        confList[5] += 1
    countList.append(x)
print(confList)
sum = 0
for conf in countList:
    sum += conf
avg = sum/len(countList)
print("Avg Accuracy :",avg)
# #     #x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.25)
#
#
# df = pd.read_csv('.\\DataSets\\niftyJoinedCloses.csv')
# tickers = df.columns.values.tolist()
# print("df before:")
# print(df.iloc[0:3,4:8])
# df = df.dropna(axis=1, how='all')
# print("df after:")
# print(df.iloc[0:3,4:8])
# if 'AUBANK' in tickers:
#     print("present")
# else:
#     print("absent")
