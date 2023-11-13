

# SCM(Inventory) KPI's``````````````````````````````````````````````````````````

import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file into a DataFrame
df = pd.read_excel("Juicy Fruit Corporation final v2.xlsx",sheet_name='SCM(Inventory)')


def ObsoletesKPI(x, y, z):
    df[x] = pd.to_datetime(df[x], format='%Y %B')

    obsoletes_by_date = df.groupby(x)[z].mean()
    max_obsoletes = df.groupby(x)[z].max()
    min_obsoletes = df.groupby(x)[z].min()

    plt.figure(figsize=(12, 6))
    plt.fill_between(max_obsoletes.index, min_obsoletes, max_obsoletes, color='lightgray', label='Obsoletes Range')
    plt.plot(obsoletes_by_date.index, obsoletes_by_date, marker='o', color='orange', linewidth=2, label='Average Obsoletes')

    plt.title('Obsoletes show great decrease ', fontsize=16)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Obsoletes (%)', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.tight_layout()
    plt.show()

# Example usage of the function
ObsoletesKPI('Year/Months', 'Year/Months', 'Obsoletes (%)')



# KPI: Average Service Level (Pieces) & (Order Lines)

def ServiceLevelPiecesandOrderlinesKPI(x, y, z):
    # Filter the data to get the last three dates
    last_three_dates = df['Year/Months'].sort_values().unique()[-3:]
    filtered_data = df[df['Year/Months'].isin(last_three_dates)]

    # Group data by Product and calculate the mean of each service level metric
    avg_service_pieces = filtered_data.groupby(x)[y].mean()
    avg_service_order_lines = filtered_data.groupby(x)[z].mean()

    # Create a grouped bar chart with colors and value labels on top of the bars
    plt.figure(figsize=(9, 6))

    bar_width = 0.30
    index = range(len(avg_service_pieces.index))

    pieces_bars = plt.bar(index, avg_service_pieces * 100, bar_width, color='orange', label='Service Level (Pieces)')
    order_lines_bars = plt.bar([i + bar_width + 0.1 for i in index], avg_service_order_lines * 100, bar_width, color='green', label='Service Level (Order Lines)')

    # Display the values as percentages on top of the bars (formatted to one decimal)
    for bar in pieces_bars + order_lines_bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f"{height:.1f}%", ha='center', va='bottom')

    # Set labels, title, and ticks
    plt.xlabel('Products')
    plt.ylabel('Average Service Level (%)')
    plt.title('Average Service Level for Each Product 2020-2021')
    plt.xticks([i + bar_width / 2 for i in index], avg_service_pieces.index, rotation=45)

    # Move the legend outside the plot (without box)
    plt.legend(loc='lower left', bbox_to_anchor=(0, 0), fancybox=True, shadow=False)

    # Show the plot
    plt.tight_layout()
    plt.show()

ServiceLevelPiecesandOrderlinesKPI("Product", "Service level (pieces)", "Service level (order lines)")



def AverageRejectionsStartupBatches(x, y, z):
    # Group data by 'Year/Months' and calculate the mean of 'Rejects (value)' and 'Start up productivity loss (value)'
    Total_rejects = df.groupby('Year/Months')[x].sum()
    Total_startup_loss = df.groupby('Year/Months')[y].sum()

    # Calculate the mean of 'Production batches previous round'
    avg_production_batches = df.groupby('Year/Months')[z].mean()

    # Create the figure and axis objects
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Calculate the bar width and gap to display the bars with space between them
    bar_width = 50  # Adjust this value based on the desired width of bars
    bar_gap = 23  # Adjust this value to set the space between the bars

    # Plot the Rejects and Start-up Productivity Loss as bars side by side with a gap
    reject_bars = ax1.bar(Total_rejects.index - pd.to_timedelta(bar_width + bar_gap / 2, unit='D'), Total_rejects, width=bar_width, alpha=0.8, label='Total Rejects Value', color='orange')
    startup_loss_bars = ax1.bar(Total_startup_loss.index + pd.to_timedelta(bar_gap / 2, unit='D'), Total_startup_loss, width=bar_width, alpha=0.8, label='Total Startup Loss Value', color='green')

    # Create the second y-axis for 'Production batches previous round'
    ax2 = ax1.twinx()
    ax2.plot(avg_production_batches.index, avg_production_batches, linestyle='-', marker='o', color='black', label='Average Production Batches')

    # Set labels, title, and ticks
    ax1.set_xlabel('Year/Months')
    ax1.set_ylabel('Total Rejects / Startup Productivity Loss (value)')
    ax2.set_ylabel('Average Production Batches')
    ax1.set_title('Rejects & startup productivity loss caused by increase in production batches')

    
    ax2.set_ylim(0, 22)

    # Annotate values on top of the bars
    for bar, value in zip(reject_bars, Total_rejects):
        ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"{value:.0f}", ha='center', va='bottom')

    for bar, value in zip(startup_loss_bars, Total_startup_loss):
        ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"{value:.0f}", ha='center', va='bottom')

    # Combining the legends
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc='upper left')

    # Show the plot
    plt.show()

# Example usage
AverageRejectionsStartupBatches('Rejects (value)', 'Start up productivity loss (value)', 'Production batches previous round')


def ProductionAdherenceKPI(x, y, z):
    df[x] = pd.to_datetime(df[x], format='%Y %B')

    adherence_by_date = df.groupby(x)[z].mean()
    plt.plot(adherence_by_date.index, adherence_by_date * 100, marker='o', color='orange')
    plt.xlabel('Year/Months')
    plt.ylabel('Average Production Plan Adherence (%)')
    plt.title('Small decrease in Average Production Plan Adherence since 2020')
    plt.grid(True)
    plt.xticks(rotation=45)
    

    plt.ylim(70, 100)

    # Annotate the last two dates
    last_two_dates = adherence_by_date.index[-2:]
    last_two_adherence = adherence_by_date[-2:] * 100
    
    for date, adherence in zip(last_two_dates, last_two_adherence):
        plt.annotate(f'{adherence:.1f}%', (date, adherence), 
                     xytext=(-20, 10), textcoords='offset points',
                     arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5'))
    
    plt.show()

# Example usage of the function
ProductionAdherenceKPI('Year/Months', 'Year/Months', 'Production plan adherence (%)')




# Warehouse(Raw and fin. goods) KPI`````````````````````````````````````````````

# Cube Utilization rate and overflow rate KPI

def CubeUtilizationandOverflowKPI(x, y, z):
    import pandas as pd
    import matplotlib.pyplot as plt

    # Load the data from the Excel file
    warehouse_df = pd.read_excel('Juicy Fruit Corporation final v2.xlsx', sheet_name='Warehouse(Raw and fin. goods)')

    
    # Load the data from the Excel file
    warehouse_df = pd.read_excel('Juicy Fruit Corporation final v2.xlsx', sheet_name='Warehouse(Raw and fin. goods)')

    # Filter data for the provided warehouses
    selected_data = warehouse_df[warehouse_df['Warehouse'].isin(x)]

    # Convert percentage columns to numeric values
    selected_data[y] = selected_data[y].replace({'%': ''}, regex=True).astype(float)
    selected_data[z] = selected_data[z].replace({'%': ''}, regex=True).astype(float)

    # Plot Cube Utilization and Overflow rates over time for the specified warehouses
    plt.figure(figsize=(10, 6))

    for warehouse in x:
        warehouse_data = selected_data[selected_data['Warehouse'] == warehouse]
        cube_utilization = warehouse_data[y]
        overflow = warehouse_data[z]

        plt.plot(warehouse_data['Year/Months'], cube_utilization, marker='o', label=f'{warehouse} - Cube Utilization')
        plt.plot(warehouse_data['Year/Months'], overflow, marker='o', label=f'{warehouse} - Overflow')

    plt.xlabel('Year/Months')
    plt.ylabel('Rate (%)')
    plt.title('Cube Utilization and Overflow Rates over Time')
    plt.legend(prop={'size': 8})  # Adjust the font size here
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

CubeUtilizationandOverflowKPI(['Finished goods warehouse', 'Raw materials warehouse'], 'Cube utilization (%)', 'Overflow (%)')



