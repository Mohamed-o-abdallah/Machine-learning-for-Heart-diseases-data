# -*- coding: utf-8 -*-
"""heart_disease.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1euPAQSz3cSPQ0qQIxSpQQpwSaIl44k_y
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn import preprocessing 
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('/content/heart_disease_data.csv')
print(data.head())
print(data.shape)
print(data.info)
print(data.isnull().sum())
print(data.describe())

x = data.iloc[:,:-1]
y = data.iloc[:,-1]
scale=preprocessing.MinMaxScaler()
scaled_data=scale.fit_transform(data)
scaled_data=pd.DataFrame(scaled_data,columns=data.columns)
print(scaled_data)
data_correlation=scaled_data.corr()
print(data_correlation)
sns.heatmap(data_correlation,annot=True)
plt.show()
sns.pairplot(scaled_data)
plt.show()
print(x)
print(y)

########################################## ==> model 1 (LogisticRegression)<==###########################################################

#by using Holdout Method

x_train, x_test, y_train,y_test = train_test_split(x,y, test_size=0.2, stratify=y, random_state=2)
print(x.shape, x_train.shape, x_test.shape)
model = LogisticRegression()
model.fit(x_train,y_train)
x_train_predict = model.predict(x_train)
accuracy = accuracy_score(x_train_predict,y_train)
print('the accuracy of the train data is',accuracy)
# accuracy on test data
X_test_prediction = model.predict(x_test)
test_data_accuracy = accuracy_score(X_test_prediction, y_test)
print('Accuracy on Test data : ', test_data_accuracy)

#if the accuracy of the train data is far superior to the test data the model become  overfiting


input_data = (62,0,0,140,268,0,0,160,0,3.6,0,2,2)

# change the input data to a numpy array
input_data_as_numpy_array= np.asarray(input_data)

# reshape the numpy array as we are predicting for only on instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
prediction = model.predict(input_data_reshaped)

if (prediction[0]== 0):
  print('The Person does not have a Heart Disease')
else:
  print('The Person has Heart Disease')

########################################## ==> model 2 (K-Nearest Neighbors) <==###########################################################

#by using Validation SetApproach

from sklearn import neighbors
X=data.iloc[:,:-1]
Y=data.iloc[:,-1]
X_train, X_test, Y_train, Y_test=train_test_split(X, Y,test_size=0.5)

model_2 =neighbors.KNeighborsClassifier(n_neighbors=5)
model_2.fit(X_train,Y_train)
x_train_predict = model_2.predict(X_train)
accuracy = accuracy_score(x_train_predict,Y_train)
print('the accuracy of the train data is',accuracy)
X_test_prediction = model_2.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy on Test data : ', test_data_accuracy)

########################################## ==> model 3 ( Naïve Bayes) <==###########################################################

#by using Holdout Method

from sklearn.naive_bayes import GaussianNB
X=data.iloc[:,:-1]
Y=data.iloc[:,-1]
X_train, X_test, Y_train, Y_test=train_test_split(X, Y,test_size=0.3)
model_3 =GaussianNB()
model_3.fit(X_train,Y_train)
x_train_predict = model_3.predict(X_train)
accuracy = accuracy_score(x_train_predict,Y_train)
print('the accuracy of the train data is',accuracy)
X_test_prediction = model_3.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy on Test data : ', test_data_accuracy)

########################################## ==> model 4 (Decision Tree Classification) <==########################################################

#by using Holdout Method

from sklearn.tree import DecisionTreeClassifier
X_train, X_test, Y_train, Y_test=train_test_split(X, Y,test_size=0.3)
model_4 =clf = DecisionTreeClassifier(criterion="entropy")
model_4.fit(X_train,Y_train)
x_train_predict = model_4.predict(X_train)
accuracy = accuracy_score(x_train_predict,Y_train)
print('the accuracy of the train data is',accuracy)
X_test_prediction = model_4.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy on Test data : ', test_data_accuracy)

########################################## ==> model 5 (Random Forest) <==###########################################################

#by using Holdout Method


from sklearn.ensemble import RandomForestClassifier as RF
X_train, X_test, Y_train, Y_test=train_test_split(X, Y,test_size=0.3)
model_5 =clf =RF(n_estimators= 5,criterion="entropy")
model_5.fit(X_train,Y_train)
x_train_predict = model_5.predict(X_train)
accuracy = accuracy_score(x_train_predict,Y_train)
print('the accuracy of the train data is',accuracy)
X_test_prediction = model_5.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy on Test data : ', test_data_accuracy)
from sklearn import tree
import matplotlib.pyplot as plt
plt.figure(figsize=(20, 25))
tree.plot_tree(model_5.estimators_[0], feature_names=X.columns)
tree.plot_tree(model_5.estimators_[1], feature_names=X.columns)
plt.show()