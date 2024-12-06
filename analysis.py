import pandas as pd #importing pandas library

# Load data
data = pd.read_csv('data.csv') #`data.csv` is the file containing the data

# Basic statistics
summary = data.describe()

# Correlation matrix
correlation_matrix = data.corr() #correlation matrix

# Save results to files
summary.to_csv('summary.csv')
correlation_matrix.to_csv('correlation_matrix.csv')

print("Analysis complete. Summary and correlation matrix saved.")