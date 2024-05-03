from sklearn.neighbors import KNeighborsRegressor 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import RobustScaler
import pandas as pd

df = pd.read_csv('housing.csv')
X = df.drop(columns=['median_house_value', 'ocean_proximity']).fillna(method='bfill')
y = df['median_house_value']

# Use RobustScaler to scale features, which is less sensitive to outliers
scaler = RobustScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

knn = KNeighborsRegressor(n_neighbors=7)
knn.fit(X_train, y_train)
y_predict = knn.predict(X_test)

print("Error is", mean_squared_error(y_predict, y_test))

