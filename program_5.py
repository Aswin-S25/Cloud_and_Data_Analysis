# Linear regression with using function

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('dataset/housing.csv')

X = df[['area']]
y = df[['price']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (MSE): {mse}")

# Calculate R-squared (Coefficient of Determination)
r2 = r2_score(y_test, y_pred)
print(f"R-squared (Coefficient of Determination): {r2}")

plt.scatter(X_test, y_test, color="blue", label="Actual")
plt.plot(X_test, y_pred, color='red', label="Predicted")
plt.xlabel("Average area")
plt.ylabel("price")
plt.title("Linear regression: Housing Price")
plt.legend()
plt.show()