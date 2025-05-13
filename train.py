import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import RFE
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from data_preprocessing import feature_engineering_pipeline
from joblib import dump

df = feature_engineering_pipeline()

# Encode 'Item_Type' using LabelEncoder
le = LabelEncoder()
df['Item_Type'] = le.fit_transform(df['Item_Type'])

# One-hot encode 'Item_Type'
df = pd.get_dummies(df, columns=['Item_Type'], drop_first=True)

# Define features and target variable
X = df.drop('Item_Outlet_Sales', axis=1)
y = df['Item_Outlet_Sales']

# Check for missing values in features and target
if X.isnull().any().any() or y.isnull().any():
    print("Warning: Missing values detected. Filling missing values...")
    X = X.fillna(X.mean())  # Fill missing values in features with the mean
    y = y.fillna(y.mean())  # Fill missing values in target with the mean

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform Recursive Feature Elimination (RFE)
model = LinearRegression()
selector = RFE(model, n_features_to_select=15)
selector = selector.fit(X_scaled, y)

# Get the selected features
selected_features = X.columns[selector.support_]
print("Selected Features:", selected_features)

# Save the selected features
dump(selected_features, 'model/selected_features.joblib')

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X[selected_features], y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)


from joblib import dump
# Assuming 'model' is your trained Linear Regression model
dump(model, 'model/linear_regression_model.joblib')

# # Make predictions
# y_pred = model.predict(X_test)

# # Evaluate the model
# from sklearn.metrics import mean_squared_error, r2_score
# print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
# print("R-squared:", r2_score(y_test, y_pred))

# import numpy as np
# importances = np.abs(model.coef_[0])

# # Create a DataFrame for better visualization
# feature_names = X_train.columns
# importance_df = pd.DataFrame({
#     'Feature': feature_names,
#     'Coefficient': importances
# }).sort_values(by='Coefficient', ascending=False)

# print(importance_df)