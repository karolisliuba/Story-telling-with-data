import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file into a DataFrame
rawdf = pd.read_excel("Juicy Fruit Corporation final v2.xlsx",sheet_name='Purchasing')


def Delivery_Reliability_per_supplier (x,y,z):
    plt.figure(figsize=(12, 6))

    # Plot delivery reliability for each supplier
    for supplier, group in rawdf.groupby(x):
        plt.plot(group[y], group[z], label=f'{supplier}', linewidth=2)

    plt.title('Delivery Reliability Over Time for Each Supplier', fontsize=16)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Reliability (%)', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.tight_layout()
    plt.show()

Delivery_Reliability_per_supplier ('Supplier name','Year/Months', 'Delivery reliability (%)') 


rawdf['Year/Months'] = pd.to_datetime(rawdf['Year/Months'])


def Delivery_Reliability_average(x, y, z):
    plt.figure(figsize=(12, 6))

    # Use seaborn for enhanced styling
    sns.set(style="whitegrid")
    
    # Plot delivery reliability for each supplier in grey with increased linewidth and transparency
    for supplier, group in rawdf.groupby(x):
        plt.plot(group[y], group[z], color='grey', linewidth=6, alpha=0.3)

    # Plot average line in orange and add it to the legend with orange color
    avg_reliability = rawdf.groupby(y)[z].mean()
    plt.plot(avg_reliability.index, avg_reliability, color='orange', linewidth=7, label='Average Reliability')

    plt.title('More Reliable Suppliers', fontsize=16)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Reliability (%)', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.tight_layout()
    
    # Show legend in the bottom right corner with only the 'Average Reliability' in orange
    legend = plt.legend(loc='lower right', fontsize=12)
    legend.get_lines()[0].set_linestyle('-')  # Set the legend line style to solid
    legend.get_lines()[0].set_linewidth(7)   # Set the legend line width to match the average line
    legend.get_lines()[0].set_color('orange') # Set the legend line color to orange

    plt.show()

Delivery_Reliability_average('Supplier name', 'Year/Months', 'Delivery reliability (%)')



def stock_value_tetrapack (x, y, z):
    # Convert 'Year/Months' to datetime for proper plotting
    rawdf[x] = pd.to_datetime(rawdf[x], format='%Y %B')
    
    # Filter for a specific product
    product_df = rawdf[rawdf[y] == 'Tetra Packaging BV']
    
    # Plotting the line chart
    plt.figure(figsize=(10, 6))
    plt.plot(product_df[x], product_df[z], marker='o', linestyle='-', color='orange')
    
    # Adding titles and labels
    plt.title('Stock Value Over Time - Tetrapack 1 liter')
    plt.xlabel('Date')
    plt.ylabel('Stock Value')
    
    # Display the plot
    plt.grid(True)
    plt.show()
    
stock_value_tetrapack('Year/Months', 'Supplier name', 'Stock value')

def stock_value_3M_bottles (x, y, z):
    # Convert 'Year/Months' to datetime for proper plotting
    rawdf[x] = pd.to_datetime(rawdf[x], format='%Y %B')
    
    # Filter for a specific product
    product_df = rawdf[rawdf[y] == '3M bottles']
    
    # Plotting the line chart
    plt.figure(figsize=(10, 6))
    plt.plot(product_df[x], product_df[z], marker='o', linestyle='-', color='orange')
    
    # Adding titles and labels
    plt.title('Stock Value Over Time - 300ml bottle')
    plt.xlabel('Date')
    plt.ylabel('Stock Value')
    
    # Display the plot
    plt.grid(True)
    plt.show()
    
stock_value_3M_bottles('Year/Months', 'Supplier name', 'Stock value')

def stock_value_orange (x, y, z):
    # Convert 'Year/Months' to datetime for proper plotting
    rawdf[x] = pd.to_datetime(rawdf[x], format='%Y %B')
    
    # Filter for a specific product
    product_df = rawdf[rawdf[y] == 'Orange Supplies BV']
    
    # Plotting the line chart
    plt.figure(figsize=(10, 6))
    plt.plot(product_df[x], product_df[z], marker='o', linestyle='-', color='orange')
    
    # Adding titles and labels
    plt.title('Stock Value Over Time - orange')
    plt.xlabel('Date')
    plt.ylabel('Stock Value')
    
    # Display the plot
    plt.grid(True)
    plt.show()
    
stock_value_orange('Year/Months', 'Supplier name', 'Stock value')

def stock_value_mango (x, y, z):
    # Convert 'Year/Months' to datetime for proper plotting
    rawdf[x] = pd.to_datetime(rawdf[x], format='%Y %B')
    
    # Filter for a specific product
    product_df = rawdf[rawdf[y] == 'Star Hoku']
    
    # Plotting the line chart
    plt.figure(figsize=(10, 6))
    plt.plot(product_df[x], product_df[z], marker='o', linestyle='-', color='orange')
    
    # Adding titles and labels
    plt.title('Stock Value Over Time - mango')
    plt.xlabel('Date')
    plt.ylabel('Stock Value')
    
    # Display the plot
    plt.grid(True)
    plt.show()
    
stock_value_mango('Year/Months', 'Supplier name', 'Stock value')

def stock_value_citrus_syrup (x, y, z):
    # Convert 'Year/Months' to datetime for proper plotting
    rawdf[x] = pd.to_datetime(rawdf[x], format='%Y %B')
    
    # Filter for a specific product
    product_df = rawdf[rawdf[y] == 'Lemon concentrate']
    
    # Plotting the line chart
    plt.figure(figsize=(10, 6))
    plt.plot(product_df[x], product_df[z], marker='o', linestyle='-', color='orange')
    
    # Adding titles and labels
    plt.title('Stock Value Over Time - citrus syrup')
    plt.xlabel('Date')
    plt.ylabel('Stock Value')
    
    # Display the plot
    plt.grid(True)
    plt.show()
    
stock_value_citrus_syrup('Year/Months', 'Supplier name', 'Stock value')


def total_stock_value(x,y):
    # Convert 'Year/Months' to datetime for proper plotting
    rawdf[x] = pd.to_datetime(rawdf[x], format='%Y %B')
    
    # Group by 'Year/Months' and sum the stock values
    total_stock_df = rawdf.groupby(x)[y].sum().reset_index()
    
    # Plotting the line chart for total stock development
    plt.figure(figsize=(10, 6))
    plt.plot(total_stock_df[x], total_stock_df[y], marker='o', linestyle='-', color='orange')
    
    # Adding titles and labels
    plt.title('Overall decrease in Stock Value Over Time')
    plt.xlabel('Date')
    plt.ylabel('Stock Value')
    
    # Display the plot
    plt.grid(True)
    plt.show()

total_stock_value('Year/Months' , 'Stock value')

def Transport_costs_tetrapack (x, y, z):
    # Convert 'Year/Months' to datetime for proper plotting
    rawdf[x] = pd.to_datetime(rawdf[x], format='%Y %B')
    
    # Filter for a specific product
    product_df = rawdf[rawdf[y] == 'Tetra Packaging BV']
    
    # Plotting the line chart
    plt.figure(figsize=(10, 6))
    plt.plot(product_df[x], product_df[z], marker='o', linestyle='-', color='orange')
    
    # Adding titles and labels
    plt.title('Transport Costs Over Time - Tetrapack 1 liter')
    plt.xlabel('Date')
    plt.ylabel('Transport costs')
    
    # Display the plot
    plt.grid(True)
    plt.show()
    
Transport_costs_tetrapack('Year/Months', 'Supplier name', 'Transport costs')

def Transport_costs_3M_bottles (x, y, z):
    # Convert 'Year/Months' to datetime for proper plotting
    rawdf[x] = pd.to_datetime(rawdf[x], format='%Y %B')
    
    # Filter for a specific product
    product_df = rawdf[rawdf[y] == '3M bottles']
    
    # Plotting the line chart
    plt.figure(figsize=(10, 6))
    plt.plot(product_df[x], product_df[z], marker='o', linestyle='-', color='orange')
    
    # Adding titles and labels
    plt.title('Transport Costs Over Time - 300ml bottle')
    plt.xlabel('Date')
    plt.ylabel('Transport costs')
    
    # Display the plot
    plt.grid(True)
    plt.show()
    
Transport_costs_3M_bottles('Year/Months', 'Supplier name', 'Transport costs')

def Transport_costs_orange (x, y, z):
    # Convert 'Year/Months' to datetime for proper plotting
    rawdf[x] = pd.to_datetime(rawdf[x], format='%Y %B')
    
    # Filter for a specific product
    product_df = rawdf[rawdf[y] == 'Orange Supplies BV']
    
    # Plotting the line chart
    plt.figure(figsize=(10, 6))
    plt.plot(product_df[x], product_df[z], marker='o', linestyle='-', color='orange')
    
    # Adding titles and labels
    plt.title('Transport Costs Over Time - orange')
    plt.xlabel('Date')
    plt.ylabel('Transport costs')
    
    # Display the plot
    plt.grid(True)
    plt.show()
    
Transport_costs_orange('Year/Months', 'Supplier name', 'Transport costs')

def Transport_costs_mango (x, y, z):
    # Convert 'Year/Months' to datetime for proper plotting
    rawdf[x] = pd.to_datetime(rawdf[x], format='%Y %B')
    
    # Filter for a specific product
    product_df = rawdf[rawdf[y] == 'Star Hoku']
    
    # Plotting the line chart
    plt.figure(figsize=(10, 6))
    plt.plot(product_df[x], product_df[z], marker='o', linestyle='-', color='orange')
    
    # Adding titles and labels
    plt.title('Transport Costs Over Time - mango')
    plt.xlabel('Date')
    plt.ylabel('Transport costs')
    
    # Display the plot
    plt.grid(True)
    plt.show()
    
Transport_costs_mango('Year/Months', 'Supplier name', 'Transport costs')

def Transport_costs_citrus_syrup (x, y, z):
    # Convert 'Year/Months' to datetime for proper plotting
    rawdf[x] = pd.to_datetime(rawdf[x], format='%Y %B')
    
    # Filter for a specific product
    product_df = rawdf[rawdf[y] == 'Lemon concentrate']
    
    # Plotting the line chart
    plt.figure(figsize=(10, 6))
    plt.plot(product_df[x], product_df[z], marker='o', linestyle='-', color='orange')
    
    # Adding titles and labels
    plt.title('Transport costs Over Time - citrus syrup')
    plt.xlabel('Date')
    plt.ylabel('Transport costs')
    
    # Display the plot
    plt.grid(True)
    plt.show()
    
Transport_costs_citrus_syrup('Year/Months', 'Supplier name', 'Transport costs')


def total_Transport_costs(x,y):
    # Convert 'Year/Months' to datetime for proper plotting
    rawdf[x] = pd.to_datetime(rawdf[x], format='%Y %B')
    
    # Group by 'Year/Months' and sum the stock values
    total_stock_df = rawdf.groupby(x)[y].sum().reset_index()
    
    # Plotting the line chart for total stock development
    plt.figure(figsize=(10, 6))
    plt.plot(total_stock_df[x], total_stock_df[y], marker='o', linestyle='-', color='orange')
    
    # Adding titles and labels
    plt.title('Overall decrease in Transport Costs Over Time')
    plt.xlabel('Date')
    plt.ylabel('Transport costs')
    
    # Display the plot
    plt.grid(True)
    plt.show()

total_Transport_costs('Year/Months' , 'Transport costs')


