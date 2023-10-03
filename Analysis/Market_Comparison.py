import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

DATA_DIR = '/Users/toni/Desktop/Portfolio/Camera Case Python/Data'

def load_and_clean_data(filename, drop_columns, market_name):
    """Loads CSV, cleans data and adds a Market column."""
    data = pd.read_csv(os.path.join(DATA_DIR, filename))
    data = data.drop(drop_columns, axis=1)
    data['Market'] = market_name
    return data

def add_product_level_column(df):
    """Adds a Level column to the dataframe based on Price."""
    conditions = [
        (df['Price'] < 100),
        (df['Price'].between(100, 999)),
        (df['Price'].between(1000, 2999)),
        (df['Price'] > 3000)
    ]
    choices = ['Low', 'Middle', 'High', 'Luxury']
    df['Level'] = np.select(conditions, choices, default='Unknown')

def top_10(df):
    """Displays top 10 most and least expensive products."""
    most_expensive = df.nlargest(10, 'Price')[['Name', 'Price']]
    least_expensive = df.nsmallest(10, 'Price')[['Name', 'Price']]
    print("Most expensive:\n", most_expensive)
    print("\nLeast expensive:\n", least_expensive)

def price_differences(df, col):
    """Displays and plots mean prices grouped by a column."""
    means = df.groupby(col)['Price'].mean().sort_values(ascending=False)
    print(means.to_frame(), '\n')
    means.plot(kind='bar', title=col, ylabel='Price (£)', figsize=(6, 5))
    plt.show()

def quant_differences(df, col):
    """Displays and plots quantity of values in a column."""
    unique_vals = df[col].nunique()
    value_counts = df[col].value_counts()
    print(f"Number of Unique Values: {unique_vals}\n")
    print(value_counts.to_frame(), '\n')
    
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    plt.title(col)
    plt.show()

def price_diff_by_market(col):
    """Displays and plots mean price by market and a column."""
    df_grouped = cam_market.groupby(['Market', col])['Price'].mean().unstack()
    df_grouped.T.plot(kind='bar', figsize=(18, 9))
    plt.title(f"Mean Price Across Competitor Platforms as a function of {col}")
    plt.ylabel('Price (£)')
    plt.show()

def price_comparison(df, category):
    """Compares products of a category across markets."""
    subset = df[df['category'] == category].copy()
    subset['ShortName'] = subset['Name'].str.split().str[:5].str.join(" ")
    value_counts = subset['ShortName'].value_counts()
    common_products = value_counts[value_counts > 1].index
    return subset[subset['ShortName'].isin(common_products)].sort_values(by='ShortName')

# Load and merge data
c_world = load_and_clean_data('camera_world_processed.csv', ['Unnamed: 0'], 'Camera World')
castle = load_and_clean_data('castle_cameras_processed.csv', ['Code', 'Unnamed: 0'], 'Castle')
jessops = load_and_clean_data('jessops_processed.csv', ['Code', 'Unnamed: 0'], 'Jessops')

cam_market = pd.concat([jessops, castle, c_world])

# Add product level column
add_product_level_column(cam_market)

# Save combined dataframe
cam_market.to_csv('/Users/toni/Desktop/Camera Case Study/Data/market_data.csv', index=False)

# Analysis
print("Total Jessops products:", len(jessops))
top_10(jessops)
quant_differences(jessops, 'category')

jessops_filtered = cam_market[cam_market['Market'] == 'Jessops']
quant_differences(jessops_filtered, 'Level')

# Price Comparison
price_diff_by_market('category')
price_diff_by_market('brand')

# Mirrorless Cameras Comparison
mirrorless_comparison = price_comparison(cam_market, 'Mirrorless')
print(mirrorless_comparison)

# DSLR Cameras Comparison
dslr_comparison = price_comparison(cam_market, 'DSLR')
print(dslr_comparison)
