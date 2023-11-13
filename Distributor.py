import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st

df_distributor = pd.read_excel('Juicy Fruit Corporation final v2.xlsx', sheet_name='Distributor')

def average_distribution_costs_per_pallet(x, y, z_list, df):
    # Convert 'Year/Months' to datetime format
    df['Year/Months'] = pd.to_datetime(df['Year/Months'], format='%Y %B')

    # Create a new DataFrame for plotly express
    df_plotly = pd.DataFrame()

    # Prepare data for plotly
    for distributor, group in df.groupby(x):
        for z in z_list:
            average_cost_per_pallet = group[y] / group[z]
            df_plotly = pd.concat([df_plotly, pd.DataFrame({
                'Date': group['Year/Months'],
                'Average Cost per Pallet': average_cost_per_pallet,
                'Distributor': distributor,
                'Shipment Size': z
            })])

    # Create an interactive line chart with hover information
    fig = px.line(df_plotly, x='Date', y='Average Cost per Pallet', color='Shipment Size',
                  line_dash='Distributor',
                  line_group='Shipment Size', hover_name='Shipment Size',
                  labels={'Average Cost per Pallet': 'Average Cost per Pallet ($)'},
                  title='Average Distribution Costs per Pallet Over Time for Each Distributor',
                  template='plotly_dark')

    # Show the interactive chart
    return fig

# Specify all shipment sizes you want to compare
shipment_sizes = ['Pallets in small shipments', 'Pallets in medium shipments', 'Pallets in large shipments']
# Example usage:
average_distribution_costs = average_distribution_costs_per_pallet('Distributor', 'Distribution costs', shipment_sizes, df_distributor)
st.plotly_chart(average_distribution_costs)



