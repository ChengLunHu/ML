# import python packages
import pandas as pd
#import statsmodels.formula.api as sm
from sklearn import metrics
from sklearn.cross_validation import train_test_split
import numpy as np
import matplotlib.pyplot as plt

# allow plots to appear directly in the notebook
#matplotlib inline

from sklearn.datasets import load_boston
Boston = load_boston()

Boston.keys()


print Boston.DESCR

Boston.data.shape

boston = pd.DataFrame(Boston.data)
boston.head(3)

from sklearn.preprocessing import scale
boston = scale(boston)

bos = pd.DataFrame(boston)
bos.head(3)

bos.columns = Boston.feature_names
bos.head(3)


# Linear Regression Model
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(bos, Boston.target, train_size=0.8)
#print X_train.shape, X_test.shape, Y_train.shape, Y_text.shape

from sklearn.linear_model import LinearRegression
lm_model = LinearRegression()
lm_model.fit(X_train,Y_train)

pd.DataFrame(zip(Boston.feature_names, lm_model.coef_), columns = ['Feature', 'Coefficient'])

print round(lm_model.score(X_train,Y_train),3)

Predicted_price= lm_model.predict(X_test)

Result = pd.DataFrame({"Observed":Y_test,"Predicted":Predicted_price})
Result.head()

print round(lm_model.score(X_test,Y_test),3)

# calculate MAE using scikit-learn
print metrics.mean_absolute_error(Y_test, Predicted_price)

plt.scatter(lm_model.predict(X_test), (Predicted_price - Y_test), c='r', s=30)
plt.title("Residual plot on the testing data")
plt.ylabel("Residuals")

