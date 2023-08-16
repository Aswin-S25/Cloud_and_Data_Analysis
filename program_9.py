

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.cluster import KMeans

df = pd.read_csv('dataset/Housing.csv')
sns.scatterplot(x='area', y='price', data=df)
reg_model = LinearRegression()
reg_model.fit(df[['area']], df['price'])

sns.scatterplot(x='area', y='price', hue='furnishingstatus', data=df)
plt.xlabel('Area')
plt.ylabel('Price')
plt.title('Classification (Logistic Regression)')
plt.show()
X = df[['area', 'price']]
