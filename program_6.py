# Linear Regression using Decision Tree, Random Forest

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


# df = pd.read_csv('dataset/Housing.csv')

# X = df[['area']]
# y = df[['price']]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# model = DecisionTreeRegressor()

# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)

# plt.scatter(X_test, y_test, color="blue", label="Actual")
# plt.scatter(X_test, y_pred, color="red", label="Predicted")
# plt.xlabel("Average area")
# plt.ylabel("Median value of Home")
# plt.title("Decision Tree regresssion")
# plt.legend()
# plt.show()

# mse = mean_squared_error(y_test, y_pred)

# print(mse)

# r2 = r2_score(y_test, y_pred)

# print(r2)


# using random forest

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("dataset/housing.csv")

X = df[['area']]
y = df[['price']]

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.2, random_state=42)

model = RandomForestRegressor()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

plt.scatter(X_test, y_test, color='blue', label='actuel')
plt.scatter(X_test, y_pred, color="red", label="actual")
plt.xlabel("Actual")
plt.ylabel("price")
plt.title("Random forest Regression")
plt.legend()
plt.show()

mse = mean_squared_error(y_test, y_pred)

print(mse)

r2 = r2_score(y_test, y_pred)
print(r2)

