import pandas as pd


dataset = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv')

# print(dataset)

# print("Dataset Description")
# print(dataset.describe())


#Splitting datas as x and y values
y = dataset['logS']
# print('Y field values\n', y)

x = dataset.drop('logS', axis='columns')
# print('X field values\n', x)


from sklearn.model_selection import train_test_split

#Building training and testing models
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=100)

#Building ML model
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(x_train, y_train)


y_lr_train_prediction = lr.predict(x_train)
y_lr_test_prediction = lr.predict(x_test)

# print('Prediction on training model')
# print(y_lr_train_prediction)

# print("Prediction on testing model")
# print(y_lr_test_prediction)



# Model performance evaluation
from sklearn.metrics import mean_squared_error, r2_score


lr_train_mean = mean_squared_error(y_train, y_lr_train_prediction)
lr_train_r2 = r2_score(y_train, y_lr_train_prediction)

lr_test_mean = mean_squared_error(y_test, y_lr_test_prediction)
lr_test_r2 = r2_score(y_test, y_lr_test_prediction)


print("Training: ", [lr_train_mean, lr_train_r2])
print("Testing: ", [lr_test_mean, lr_test_r2])

frame = pd.DataFrame(['Linear Regression', lr_train_mean, lr_train_r2, lr_test_mean, lr_test_r2]).transpose()
frame.columns = ['Method', 'Training MSE', 'Training R2', "Test MSE", 'Test R2']

print(frame)

#Model training
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(max_depth=2, random_state=100)
rf.fit(x_train, y_train)

# Make Predictions
y_rf_train_prediction = rf.predict(x_train)
y_rf_test_prediction = rf.predict(x_test)

# Performance Evaluation
rf_train_mean = mean_squared_error(y_train, y_rf_train_prediction)
rf_train_r2 = r2_score(y_train, y_rf_train_prediction)

rf_test_mean = mean_squared_error(y_test, y_rf_test_prediction)
rf_test_r2 = r2_score(y_test, y_rf_test_prediction)

rf_frame = pd.DataFrame(['Random Forest', rf_train_mean, rf_train_r2, rf_test_mean, rf_test_r2]).transpose()
rf_frame.columns = ['Method', 'Training MSE', 'Training R2', "Test MSE", 'Test R2']
print(frame)


global_results_frame = pd.concat([frame, rf_frame], axis=0)
global_results_frame.reset_index(drop=True)



import matplotlib.pyplot as plt
import numpy as np


r = np.polyfit(y_train, y_lr_train_prediction, 1)
p = np.poly1d(r)

plt.ylabel('Predicted logS')
plt.xlabel('Experimental logS')

plt.scatter(x=y_train, y=y_lr_train_prediction, alpha=0.4)
plt.plot(y_train, p(y_train), 'red')

plt.show()