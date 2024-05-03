from sklearn.neighbors import KNeighborsRegressor 
from sklearn.model_selection import train_test_split 
from sklearn.datasets import load_iris 
from sklearn.metrics import mean_squared_error
from sklearn.datasets import fetch_california_housing
import pandas as pd
df=pd.read_csv('housing.csv')
X=df.drop(columns=['median_house_value','ocean_proximity']).fillna(method='bfill')
y=df['median_house_value']
# irisData = load_iris() 
# X = irisData.data 
# y = irisData.target 

X_train, X_test, y_train, y_test = train_test_split( 
			X, y, test_size = 0.2, random_state=42) 
knn = KNeighborsRegressor(n_neighbors=7,weights='distance') 
knn.fit(X_train, y_train) 
Y_predict=knn.predict(X_test)
print("Error is",mean_squared_error(Y_predict,y_test))
# not working with California Dataset ,weights='distance'