import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Load data from the csv file
dataFrame   =   pd.read_csv('Data/NVDA.csv')

#Convert dates to columns
dataFrame['date'] = pd.to_datetime(dataFrame['date'])

#Prepare data for linear regression
X = dataFrame['position'].values.reshape(-1,1)
y = dataFrame['adjClose'].values

#Create linear regression model to fit the data
model = LinearRegression()
model.fit(X,y)

#Generate predictions for the next 100 steps
futurePositions = np.arange(dataFrame['position'].max() + 1, dataFrame['position'].max() + 101).reshape(-1,1)
futurePredictions = model.predict(futurePositions)

#Plotting the data and predictions
plt.figure(figsize=(12,6))
plt.scatter(dataFrame['date'],dataFrame['adjClose'], color='orange', label='Actual Data')
plt.plot(dataFrame['date'], model.predict(X), color='orange', label='Regression Line')
plt.plot(pd.date_range(start=dataFrame['date'].max(), periods=100, closed='right'),futurePredictions,color='blue',label='Predictions')
plt.xlabel('Dates')
plt.ylabel('Adjusted Close')
plt.title('Stock Data with Linear Regression')
plt.legend()
plt.xsticks(rotation=45)
plt.show()
