import pandas as pd
import numpy as np
import random
import string

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Define the number of samples
num_samples = 2000

# Helper function to generate random customer IDs
def generate_customer_id():
    return ''.join(random.choices(string.digits, k=4)) + '-' + ''.join(random.choices(string.ascii_uppercase, k=4))

# Generate synthetic data
data = {
    'customerID': [generate_customer_id() for _ in range(num_samples)],
    'tenure': np.random.randint(1, 73, num_samples),  # Tenure between 1 and 72 months
    'MonthlyCharges': np.random.uniform(20, 120, num_samples).round(2),  # Monthly charges between $20 and $120
    'TotalCharges': np.random.uniform(100, 8000, num_samples).round(2),  # Total charges between $100 and $8000
    'Contract': np.random.choice(['Month-to-month', 'One year', 'Two year'], num_samples),
    'Churn': np.random.choice(['Yes', 'No'], num_samples, p=[0.26, 0.74])  # 26% churn rate
}

# Create a DataFrame
df = pd.DataFrame(data)
print(len(df))
# Save to CSV
df.to_csv('synthetic_customer_churn_data.csv', index=False)

print("Synthetic customer churn dataset with 2,000 records has been saved as 'synthetic_customer_churn_data.csv'.")
