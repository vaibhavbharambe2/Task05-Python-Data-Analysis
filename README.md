# Sales Data Analysis

This repository contains a Python script for analyzing sales data from a CSV file. The code performs data cleaning, aggregation, and visualization to provide insights into sales performance per product and over time.

---

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [License](#license)

---

## Introduction

The script reads a sales dataset, cleans the data, and generates visualizations to understand sales distribution across products and trends over time.

---

## Requirements

This script requires the following Python libraries:

- pandas
- numpy
- matplotlib

You can install these using pip:

```bash
pip install pandas numpy matplotlib
```

---

## Usage

1. Place your sales data CSV file named `sales_data.csv` in the same directory as the script.
2. Run the script:

```bash
python sales_analysis.py
```

> Ensure that your CSV includes at least the columns: `Order Date`, `Product`, and `Sales`.

---

## Code Explanation

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

**Import necessary libraries** for data manipulation and visualization.

---

```python
sales_df = pd.read_csv('sales_data.csv', low_memory=False)
```

**Load data** from CSV into a pandas DataFrame.

---

```python
# Ensure 'Sales' column is numeric, coercing errors to NaN
sales_df['Sales'] = pd.to_numeric(sales_df['Sales'], errors='coerce')

# Drop rows with NaN in 'Sales' if necessary
sales_df = sales_df.dropna(subset=['Sales'])
```

**Clean 'Sales' data** by converting to numeric and removing invalid entries.

---

```python
# Convert 'Order Date' to datetime
sales_df['Order Date'] = pd.to_datetime(sales_df['Order Date'], errors='coerce')

# Drop rows with invalid dates if any
sales_df = sales_df.dropna(subset=['Order Date'])
```

**Convert 'Order Date'** to datetime format for temporal analysis.

---

```python
# Display the first few rows to understand the structure
sales_df.head()

print(sales_df.info())
```

**Inspect data structure** and confirm data types.

---

```python
# 2. Group by 'Product' and sum 'Sales'
product_sales = sales_df.groupby('Product')['Sales'].sum().reset_index()

# 3. Sort the results for better visualization
product_sales = product_sales.sort_values(by='Sales', ascending=False)
```

**Aggregate total sales per product** and sort descending for visualization.

---

```python
# Prepare data for bar chart
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
# plt.show()
```

**Create a bar chart** showing total sales per product with rotated labels for readability.

---

```python
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

# Set y-axis ticks based on max sales
max_sales = monthly_sales['Sales'].max()
tick_values = np.linspace(0, max_sales, num=5)
plt.yticks(tick_values)

plt.grid(True)
plt.show()
```

**Analyze sales over time:**

- Group data by year.
- Plot monthly sales trend with a line chart.
- Dynamic y-axis ticks based on maximum sales for clarity.

---

## License

This project is for educational purposes. Feel free to adapt and expand the code for your own datasets.

---

**Note:** Remember to replace `'sales_data.csv'` with your actual data file if different, and ensure your dataset contains the necessary columns.
