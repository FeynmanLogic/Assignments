import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model  
df=pd.read_csv('student.csv')
X = df['Study Hours']
y=df['Exam Score']
X_reshaped = X.values.reshape(-1, 1)
plt.scatter(X, y, color='red')


model = linear_model.LinearRegression()

model.fit(X_reshaped, y)

y_pred = model.predict(X_reshaped) 
study_hours_input = float(input("Enter the number of study hours: "))

predicted_score = model.predict([[study_hours_input]])
print(f"Predicted Exam Score for {study_hours_input} study hours: {predicted_score[0]}")
plt.plot(X, y_pred) 

plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.title('Study Hours vs Exam Score')
plt.show()





