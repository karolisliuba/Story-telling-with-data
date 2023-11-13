
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
df = pd.read_excel('Juicy Fruit Corporation final v2.xlsx', sheet_name='Sales (Customer - Product)')

# Convert the 'Year/Months' column to datetime
df['Year/Months'] = pd.to_datetime(df['Year/Months'], format='%Y %B')

# OSA KPI by Product Category
def OSAPerformanceKPI(x, y, z):
    # Group by 'Year/Months' and 'Product Category', and calculate the mean of 'OSA'
    pivot_table = df.groupby([x, y])[z].mean().unstack()

    # Plot the average OSA line by Product Category with different colors
    plt.figure(figsize=(12, 6))
    for category, color in zip(df[y].unique(), sns.color_palette('husl', n_colors=len(df[y].unique()))):
        category_data = df[df[y] == category]
        category_pivot = category_data.groupby([x, y])[z].mean().unstack()
        category_average_OSA = category_pivot.mean(axis=1)
        plt.plot(category_average_OSA.index, category_average_OSA, marker='o', color=color, label=f'{category}')

    # Set plot titles and labels
    plt.title(f'Increase in {z} Performance Over Time ', fontsize=16)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel(z, fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=12, bbox_to_anchor=(1.05, 1), loc='upper left')  # Legend outside the graph
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.tight_layout()
    plt.show()

# Call the function with relevant parameters
OSAPerformanceKPI('Year/Months', 'Product ', 'OSA')



# Gross Margin Per Week KPI
def GrossmarginperweekKPI(x, y, z):
    # Group by 'Year/Months' and 'Product', and calculate the mean of 'Gross margin per week'
    pivot_table = df.groupby([x, y])[z].mean().unstack()

    # Set a custom color palette for better visualization
    colors = sns.color_palette('husl', n_colors=len(df[y].unique()))

    # Plot the average Gross Margin Per Week line with different colors for each product
    plt.figure(figsize=(16, 8))  # Adjust the size of the figure
    for product, color in zip(df[y].unique(), colors):
        plt.plot(pivot_table.index, pivot_table[product], marker='o', color=color, label=f'{product}')

    # Set plot title
    plt.title('Increase in Gross Margin Over Time (Average)', fontsize=16)  # Updated title
    
    # Set plot labels
    plt.xlabel('Date', fontsize=14)
    plt.ylabel(z, fontsize=14)
    
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Place the legend outside of the graph
    plt.legend(fontsize=12, bbox_to_anchor=(1.05, 1), loc='upper left')
    
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.tight_layout()
    plt.show()

# Call the function with relevant parameters
GrossmarginperweekKPI('Year/Months', 'Product ', 'Gross margin per week')





