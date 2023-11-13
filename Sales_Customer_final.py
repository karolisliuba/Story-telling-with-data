#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 15:33:59 2023

@author: nguyenhaihung
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_excel('Juicy Fruit Corporation final v2.xlsx', sheet_name='Sales(Customer)')

# Convert the 'Year/Months' column to datetime
df['Year/Months'] = pd.to_datetime(df['Year/Months'], format='%Y %B')
df.info()

#Service level (order lines)
def ServicelevelorderlinesKPI (x,y,z):

    #Pivot the data to have 'Year/Months' as columns and 'Customer' as index
    pivot_table = df.pivot(index=x, columns=y, values=z)
    # Calculate the average, maximum, and minimum service levels
    average_service_level = pivot_table.mean(axis=1)
    max_service_level = pivot_table.max(axis=1)
    min_service_level = pivot_table.min(axis=1)
    plt.figure(figsize=(12, 6))
    # Fill the area between the maximum and minimum service levels in gray
    plt.fill_between(max_service_level.index, min_service_level, max_service_level, color='lightgray', label='Service Level Range')
    # Plot the average service level line in red with markers
    plt.plot(average_service_level.index, average_service_level, marker='o', color='orange', linewidth=2, label='Average Service Level')
    plt.title('Service Level Over Time (Range) with Average', fontsize=16)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Service Level (order lines)', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.tight_layout()
    plt.show()

ServicelevelorderlinesKPI('Year/Months', 'Customer', 'Service level (order lines)')


#Attained shelf life
def AttainedshelflifeKPI (x,y,z):
    
    #Pivot the data to have 'Year/Months' as columns and 'Customer' as index
    pivot_table = df.pivot(index=x, columns=y, values=z)
    # Calculate the average, maximum, and minimum service levels
    average_attained_shelf_life = pivot_table.mean(axis=1)
    max_attained_shelf_life = pivot_table.max(axis=1)
    min_attained_shelf_life = pivot_table.min(axis=1)
    # Create a filled area chart to represent the range
    plt.figure(figsize=(12, 6))
    plt.fill_between(max_attained_shelf_life.index, min_attained_shelf_life, max_attained_shelf_life, color='lightgray', label='Attained shelf life range')
    # Plot the average service level line in red with markers
    plt.plot(average_attained_shelf_life.index, average_attained_shelf_life, marker='o', color='orange', linewidth=2, label='Attained shelf life')
    # Set plot titles and labels
    plt.title('Attained shelf life Over Time (Range) with Average', fontsize=16)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Attained shelf life (%)', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.tight_layout()
    plt.show()

AttainedshelflifeKPI('Year/Months', 'Customer', 'Attained shelf life (%)')


#GrossMarginKPI
def GrossMarginKPI(x, y, z):
    # Group by 'Customer' and 'Year/Months' and calculate the mean of 'Gross Margin KPI'
    pivot_table = df.groupby([y, x])[z].mean().unstack()

    # Set a custom color palette for lines
    colors = sns.color_palette('husl', n_colors=len(pivot_table.columns))

    # Plot a line chart for each customer
    plt.figure(figsize=(14, 7))  # Adjust the size of the figure

    # Use Seaborn lineplot for better control of line grouping
    sns.lineplot(data=df, x=y, y=z, hue=x, ci=None, estimator='mean', palette=colors)

    # Set plot titles and labels
    plt.title('Gross Margin Over Time for Each Customer', fontsize=16)
    plt.xlabel('Year/Months', fontsize=14)
    plt.ylabel('Average Gross Margin Per Week', fontsize=14)

    # Adjust the legend size
    plt.legend(title='Customer', fontsize=8, title_fontsize=8, bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.tight_layout()
    plt.show()

# Call the function with relevant parameters
GrossMarginKPI('Customer', 'Year/Months', 'Gross margin per week')



