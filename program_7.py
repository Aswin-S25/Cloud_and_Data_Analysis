import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




df = pd.read_csv("dataset/Iris1.csv", low_memory=False)

df.info()


for label, content in df.items() :
    if not pd.api.types.is_numeric_dtype(content):
        df[label] = content.astype('category').cat.as_ordered()

df.info()


for label, content in df.items() :
    if not pd.api.types.is_numeric_dtype(content):
        df[label] = pd.Categorical(content).codes + 1
        
print(df)






from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
model = LogisticRegression()
model

x = df.drop('Species',axis=1)
y = df['Species']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

model.fit(x_train,y_train)

y_predicted = model.predict(x_test)

y_predicted

model.score(x_test,y_test)*100

from sklearn.metrics import mean_absolute_error,mean_squared_error

mae = mean_absolute_error(y_test,y_predicted)

mae


# Create a scatter plot of actual vs. predicted labels
# plt.scatter(range(len(y_test)), y_test, label='Actual', color='blue')
# plt.scatter(range(len(y_test)), y_predicted, label='Predicted', color='red', marker='x')
# plt.xlabel('Data Point')
# plt.ylabel('Class Label')
# plt.title('Scatter Plot: Actual vs. Predicted Labels')
# plt.legend()
# plt.show()
print(x_test['PetalLengthCm'])

plt.scatter(x_test['PetalLengthCm'], y_test, color="black", )
plt.scatter(x_test['PetalLengthCm'], y_predicted, color='red', marker= "x")
plt.legend()
plt.show()