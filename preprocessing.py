import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from joblib import load

# Load the selected features
selected_features = load('model/selected_features.joblib')

def preprocess_input(input_data):
    df = pd.DataFrame([input_data])
    # Encode categorical variables
    le_fat_content = LabelEncoder()
    le_fat_content.fit(['Low Fat', 'Regular'])
    df['Item_Fat_Content'] = le_fat_content.transform(df['Item_Fat_Content'])

    le_outlet_size = LabelEncoder()
    le_outlet_size.fit(['Small', 'Medium', 'High'])
    df['Outlet_Size'] = le_outlet_size.transform(df['Outlet_Size'])

    # One-hot encode 'Item_Type'
    item_type_dummies = pd.get_dummies(df['Item_Type'], drop_first=True)
    df = pd.concat([df, item_type_dummies], axis=1).drop('Item_Type', axis=1)

    # Standardize numerical features
    scaler = StandardScaler()
    numerical_features = ['Item_Visibility', 'Item_MRP', 'Outlet_Establishment_Year']
    df[numerical_features] = scaler.fit_transform(df[numerical_features])

    # Ensure the new data has the same columns as the training data
    df = df[selected_features]
    return df
