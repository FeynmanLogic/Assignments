from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import pandas as pd
df = pd.read_csv('housing.csv')
X = df.drop(columns=['median_house_value', 'ocean_proximity']).fillna(method='bfill')
y = df['median_house_value']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
knn = KNeighborsRegressor(n_neighbors=7, weights='distance')
knn.fit(X_train, y_train)
y_predict_before = knn.predict(X_test)
mse_before = mean_squared_error(y_predict_before, y_test)
print("Mean Squared Error before dropping outliers:", mse_before)
scaler = StandardScaler()
X_standardized = scaler.fit_transform(X)
X_standardized = pd.DataFrame(X_standardized, columns=X.columns)
z_scores = (X_standardized - X_standardized.mean()) / X_standardized.std()
outliers = (z_scores > 3) | (z_scores < -3)
cleaned_data = df[~outliers.any(axis=1)]
X_cleaned = cleaned_data.drop(columns=['median_house_value', 'ocean_proximity']).fillna(method='bfill')
y_cleaned = cleaned_data['median_house_value']
X_train_cleaned, X_test_cleaned, y_train_cleaned, y_test_cleaned = train_test_split(
    X_cleaned, y_cleaned, test_size=0.2, random_state=42)
knn.fit(X_train_cleaned, y_train_cleaned)
y_predict_after = knn.predict(X_test_cleaned)
mse_after = mean_squared_error(y_predict_after, y_test_cleaned)
print("Mean Squared Error after dropping outliers:", mse_after)
