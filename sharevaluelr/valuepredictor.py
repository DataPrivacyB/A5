from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import pandas as pd


import numpy as np






def calculate_value(value1,value2,value3):
    shr=pd.read_csv('C:\\Users\\Akshay Bali\\Desktop\\A5Pull\\sharevaluelr\\nifty50.csv')
    feature_column=['open', 'high', 'low']
    target_column=['close']


    feature_value=shr[feature_column]
    target_value=shr[target_column]



    x_train,x_test,y_train,y_test=train_test_split(feature_value,target_value,test_size=0.3,random_state=1)

    lr=LinearRegression()

    lr.fit(x_train,y_train)
    value_input=[[value1,value2,value3]]

    calculated_value=lr.predict(value_input)

    #print(calculated_value)
    #print(y_test)

    #print(lr_incorrect)

    return calculated_value
