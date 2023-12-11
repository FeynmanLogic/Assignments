from sklearn.linear_model import Lasso, Ridge
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn import linear_model
df=pd.read_csv('income.data.csv')
X = df.drop(columns=["happiness"])
y = df["happiness"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
lasso_reg = Lasso(alpha=0.1) 
lasso_reg.fit(X_train_scaled, y_train)
y_pred_lasso = lasso_reg.predict(X_test_scaled)
ridge_reg = Ridge(alpha=0.1)  
ridge_reg.fit(X_train_scaled, y_train)
y_pred_ridge = ridge_reg.predict(X_test_scaled)
linear_reg = linear_model.LinearRegression()
linear_reg.fit(X_train_scaled, y_train)
y_pred_linear = linear_reg.predict(X_test_scaled)
print("Lasso Mean Squared Error:", mean_squared_error(y_test, y_pred_lasso))
print("Ridge Mean Squared Error:", mean_squared_error(y_test, y_pred_ridge))
print("MSE in Linear Regression",mean_squared_error(y_test,y_pred_linear))