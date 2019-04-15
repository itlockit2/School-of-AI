import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model

# read data
dataframe = pd.read_csv('challenge_dataset.txt', sep=",", names=['x_value', 'y_value'])
x_values = dataframe[['x_value']]
y_values = dataframe[['y_value']]

# train model on data
body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)

# visualize results
plt.scatter(x_values, y_values)
plt.plot(x_values, body_reg.predict(x_values))
plt.show()
