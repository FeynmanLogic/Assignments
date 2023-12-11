import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,f1_score


data = pd.read_csv("./Datasets/Diabetes data.csv")


X = data.drop(columns=["Outcome"])  # Features
y = data["Outcome"]  # Target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=100)


clf = DecisionTreeClassifier(random_state=42)


clf.fit(X_train, y_train)


y_pred = clf.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
f1 = f1_score(y_test, y_pred)
print(f"F1 Score: {f1:.2f}")