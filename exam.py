import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/Housing.csv")
arr=df[['price']]
plt.boxplot(arr)
fig = plt.figure(figsize=(10,7))
plt.show()
df.describe()
q1 = np.quantile(arr, 0.25)
q3 = np.quantile(arr, 0.75)
med = np.median(arr)
iqr = q3-q1
upper_bound = q3+(1.5*iqr)
lower_bound = q1-(1.5*iqr)
print(iqr, upper_bound, lower_bound)
outliers = arr[(arr <= lower_bound) | (arr >= upper_bound)]
print('The following are the outliers in the boxplot:{}'.format(outliers))