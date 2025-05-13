import numpy as np
import pandas as pd

# Load the dataset
def feature_engineering_pipeline(file_path=None):
    df = pd.read_csv(file_path or r'.\data\Train.csv')
    # Handle missing values
    df['Item_Weight'] = df['Item_Weight'].fillna(df['Item_Weight'].mean())
    df['Outlet_Size'] = df['Outlet_Size'].fillna(df['Outlet_Size'].mode()[0])
    # Handle missing values
    df['Item_Weight'] = df['Item_Weight'].fillna(df['Item_Weight'].mean())
    df['Outlet_Size'] = df['Outlet_Size'].fillna(df['Outlet_Size'].mode()[0])


    # Convert categorical variables to numeric
    df['Item_Fat_Content'] = df['Item_Fat_Content'].map({'Low Fat': 0, 'Regular': 1})
    df['Outlet_Size'] = df['Outlet_Size'].map({'Small': 0, 'Medium': 1, 'High': 2})
    df['Outlet_Location_Type'] = df['Outlet_Location_Type'].map({'Tier 1': 0, 'Tier 2': 1, 'Tier 3': 2})
    df['Outlet_Type'] = df['Outlet_Type'].map({'Grocery Store': 0, 'Supermarket Type1': 1, 'Supermarket Type2': 2, 'Supermarket Type3': 3})

    # Encode Item_Identifier and Outlet_Identifier
    df['Item_Identifier'] = df['Item_Identifier'].apply(lambda x: x[:2])
    df['Item_Identifier'] = df['Item_Identifier'].map({'FD': 0, 'NC': 1, 'DR': 2})
    df['Outlet_Identifier'] = df['Outlet_Identifier'].map({'OUT049': 0, 'OUT018': 1, 'OUT027': 2, 'OUT045': 3, 'OUT046': 4, 'OUT010': 5, 'OUT013': 6, 'OUT017': 7, 'OUT035': 8, 'OUT019': 9})

    # Drop unnecessary columns
    df.drop(['Item_Identifier', 'Outlet_Identifier'], axis=1, inplace=True)
    return df


def feature_engineering_pipeline_churn(file_path=None):
    df = pd.read_csv(file_path or r'.\data\synthetic_customer_churn_data.csv')
    # Convert 'Churn' to numeric
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    # Encode 'Contract' as categorical variables
    df = pd.get_dummies(df, columns=['Contract'], drop_first=True)

    # Split the data into features and target
    df = df.drop(['customerID'], axis=1)
    return df 

# print(feature_engineering_pipeline_churn(file_path=None))