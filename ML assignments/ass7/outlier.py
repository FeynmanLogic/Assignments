from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import pandas as pd

# Load your dataset
df = pd.read_csv('housing.csv')

# Extract features and target variable
X = df.drop(columns=['median_house_value', 'ocean_proximity']).fillna(method='bfill')
y = df['median_house_value']

# Standardize the features to have zero mean and unit variance
scaler = StandardScaler()
X_standardized = scaler.fit_transform(X)

# Convert the standardized features back to a DataFrame
X_standardized = pd.DataFrame(X_standardized, columns=X.columns)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X_standardized, y, test_size=0.2, random_state=42)

# Train the KNeighborsRegressor model
knn = KNeighborsRegressor(n_neighbors=7, weights='distance')
knn.fit(X_train, y_train)

# Make predictions on the test set
y_predict = knn.predict(X_test)

# Calculate mean squared error
mse = mean_squared_error(y_predict, y_test)
print("Mean Squared Error:", mse)

# Identify outliers using Z-score
z_scores = (X_standardized - X_standardized.mean()) / X_standardized.std()
outliers = (z_scores > 3) | (z_scores < -3)
outlier_indices = outliers.any(axis=1)
outlier_count = outlier_indices.sum()
print("Number of outliers:", outlier_count)
