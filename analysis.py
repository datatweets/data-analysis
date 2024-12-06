import pandas as pd

# Load data
data = pd.read_csv('data.csv')

# Basic statistics
summary = data.describe()

# Correlation matrix
correlation_matrix = data.corr()

# Save results to files
summary.to_csv('summary.csv')
correlation_matrix.to_csv('correlation_matrix.csv')

print("Analysis complete. Summary and correlation matrix saved.")