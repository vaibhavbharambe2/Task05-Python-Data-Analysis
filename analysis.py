import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sales_df = pd.read_csv('sales_data.csv', low_memory=False)

# Ensure 'Sales' column is numeric, coercing errors to NaN
sales_df['Sales'] = pd.to_numeric(sales_df['Sales'], errors='coerce')

# Drop rows with NaN in 'Sales' if necessary
sales_df = sales_df.dropna(subset=['Sales'])

# Convert 'Order Date' to datetime
sales_df['Order Date'] = pd.to_datetime(sales_df['Order Date'], errors='coerce')

# Drop rows with invalid dates if any
sales_df = sales_df.dropna(subset=['Order Date'])

# Display the first few rows to understand the structure
sales_df.head()

print(sales_df.info())

# 2. Group by 'Product' and sum 'Sales'
product_sales = sales_df.groupby('Product')['Sales'].sum().reset_index()

# 3. Sort the results for better visualization
product_sales = product_sales.sort_values(by='Sales', ascending=False)

# Prepare data
x_pos = np.arange(len(product_sales))
sales = product_sales['Sales'].values
labels = product_sales['Product']

fig, ax = plt.subplots(figsize=(12,6))
ax.bar(x_pos, sales, color='skyblue')

ax.set_xlabel('Product')
ax.set_ylabel('Total Sales')
ax.set_title('Total Sales per Product')

# Set x-ticks at the positions of the bars, with labels
ax.set_xticks(x_pos)
ax.set_xticklabels(labels, rotation=45, ha='right')  # Rotate labels for readability, align right

plt.tight_layout()
#plt.show()

# 5. Additional analysis: sales over time

# Ensure 'Order Date' is in datetime format
sales_df['Order Date'] = pd.to_datetime(sales_df['Order Date'])

# Create a 'Month-Year' period for grouping
sales_df['Month-Year'] = sales_df['Order Date'].dt.to_period('Y')

# Group by 'Month-Year' and sum sales
monthly_sales = sales_df.groupby('Month-Year')['Sales'].sum().reset_index()

# Convert 'Month-Year' back to timestamp for plotting (start of the month)
monthly_sales['Month-Year'] = monthly_sales['Month-Year'].dt.to_timestamp()

# Plot sales trend over time
plt.figure(figsize=(12,6))
plt.plot(monthly_sales['Month-Year'], monthly_sales['Sales'], marker='o')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales Trend')

max_sales = monthly_sales['Sales'].max()  # Determine the maximum sales value
tick_values = np.linspace(0, max_sales, num=5)  # 5 evenly spaced ticks
plt.yticks(tick_values)  # Set the y-ticks to these values

plt.grid(True)
plt.show()