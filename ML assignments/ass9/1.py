from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
df = pd.read_csv('pulsar_stars.csv')
df = df.dropna()
if df.shape[0] == 0:
    print("Dataset is empty after dropping missing values.")
else:
    X = df.drop(['target_class'], axis=1)
    y = df['target_class']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    svc = SVC(C=100.0)
    svc.fit(X_train, y_train)
    y_pred = svc.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print('Model accuracy score with value of hyperparameter as 100: {0:0.4f}'.format(accuracy))
