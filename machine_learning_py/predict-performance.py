# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd

# Create a sample dataset
data = {
    'Hours_Studied': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Test_Score': [20, 25, 30, 35, 40, 50, 55, 60, 65, 75]
}
df = pd.DataFrame(data)

# Split data into features and target variable
X = df[['Hours_Studied']]  # Features (independent variables)
y = df['Test_Score']       # Target (dependent variable)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)

# Display the coefficients
print("Model Coefficient (Slope):", model.coef_[0])
print("Model Intercept:", model.intercept_)
