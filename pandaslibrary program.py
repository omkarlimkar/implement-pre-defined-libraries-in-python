import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Emily', 'Kate', 'Sam'],
        'Age': [25, 30, 28, 32],
        'City': ['New York', 'London', 'Paris', 'Tokyo']}
df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Accessing columns
print("\nAccessing the 'Name' column:")
print(df['Name'])

# Adding a new column
df['Country'] = ['USA', 'UK', 'France', 'Japan']
print("\nUpdated DataFrame with a new 'Country' column:")
print(df)

# Filtering rows
print("\nFiltering rows where Age is greater than 28:")
filtered_df = df[df['Age'] > 28]
print(filtered_df)

# Basic statistics
print("\nStatistics:")
print(df.describe())
