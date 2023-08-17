

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression


df = pd.read_csv('dataset/Housing.csv')
sns.scatterplot(x='area', y='price', data=df)
reg_model = LogisticRegression()
reg_model.fit(df[['area']], df['price'])

sns.scatterplot(x='area', y='price', hue='furnishingstatus', data=df)
plt.xlabel('Area')
plt.ylabel('Price')
plt.title('Classification (Logistic Regression)')
plt.show()
X = df[['area', 'price']]
