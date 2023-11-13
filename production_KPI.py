# Bottling kpis
#1 OEE
import pandas as pd
import plotly.express as px
import streamlit as st

df_bottling = pd.read_excel('Juicy Fruit Corporation final v2.xlsx', sheet_name='Bottling(Operations)')
df_mixer = pd.read_excel('Juicy Fruit Corporation final v2.xlsx', sheet_name='Mixer(Operations)')

def plot_oee(x, y, z, df):
    df[x] = pd.to_datetime(df[x], format='%Y %B')

    # Calculate OEE
    availability = (df['Run time (%)'] - df['Breakdown time (%)']) / df['Run time (%)']
    performance = (df['Run time (%)'] - df['Changeover time (%)']) / df['Run time (%)']
    quality = (df['Run time (%)'] - df['Unused capacity (%)']) / df['Run time (%)']
    oee = availability * performance * quality

    # Create a Plotly figure
    fig = px.line(df, x=x, y=oee * 100, markers=True, line_shape='linear', labels={x: 'Year/Months', 'value': 'OEE'})
    
    # Update layout for better display
    fig.update_layout(
        title='Bottling Line Overall Equipment Effectiveness (OEE) Over Time',
        xaxis_title='Year/Months',
        yaxis_title='Percentage (%)',
        yaxis_range=[0, 100],  # Set the y-axis range to ensure percentages are displayed correctly
        hovermode='x',
        showlegend=True
    )

    # Return the Plotly figure
    return fig

# Example usage of the function
bottling_oee_figure = plot_oee('Year/Months', 'Year/Months', 'Production plan adherence (%)', df_bottling)

# Display the figure in Streamlit app
st.plotly_chart(bottling_oee_figure)


#2.Run Time Trends
#-Analyzing the trend in run time over different periods.
def display_run_time_trends(x, y, df):
    # Convert the date column to datetime format
    df[x] = pd.to_datetime(df[x], format='%Y %B')

    # Create a Plotly figure for run time trends
    fig = px.line(df, x=x, y=y, markers=True, line_shape='linear', labels={x: 'Year/Months', y: 'Run Time (%)'})

    # Update layout for better display
    fig.update_layout(
        title='Run Time Trends Over Time',
        xaxis_title='Year/Months',
        yaxis_title='Run Time Percentage (%)',
        yaxis_range=[0, 1],
        hovermode='x',
        showlegend=True
    )

    # Return the Plotly figure
    return fig

# Example usage of the function
run_time_trends_figure = display_run_time_trends('Year/Months', 'Run time (%)', df_bottling)

# Display the figure in Streamlit app
st.plotly_chart(run_time_trends_figure)




# Utilization rate
df_bottling = pd.read_excel('Juicy Fruit Corporation final v2.xlsx', sheet_name='Bottling(Operations)')

def display_utilization_rate_trends(x, y, df):
    # Convert the date column to datetime format
    df[x] = pd.to_datetime(df[x], format='%Y %B')

    # Calculate Utilization Rate
    df['Utilization Rate (%)'] = (df['Run time per week (hours)'] / 
                                   (df['Run time per week (hours)'] + 
                                    df['Changeover time per week (hours)'] + 
                                    df['Breakdown time per week (hours)'] + 
                                    df['Unused capacity per week (hours)'] + 
                                    df['Overtime per week (hours)']) * 100)

    # Create a Plotly figure for utilization rate trends
    fig = px.line(df, x=x, y=y, markers=True, line_shape='linear', labels={x: 'Year/Months', y: 'Utilization Rate (%)'})

    # Highlight drawbacks in the figure
    drawbacks = df[df['Unused capacity per week (hours)'] > 10]  # Adjust the condition based on your criteria
    fig.add_trace(px.scatter(drawbacks, x=x, y='Utilization Rate (%)',
                             color='Unused capacity per week (hours)', size=[10]*len(drawbacks)).update_traces(mode='markers').data[0])

    # Update layout for better display
    fig.update_layout(
        title='Utilization Rate Trends Over Time with Drawbacks Highlighted',
        xaxis_title='Year/Months',
        yaxis_title='Utilization Rate Percentage (%)',
        hovermode='x',
        showlegend=True
    )

    # Return the Plotly figure
    return fig

# Example usage of the function
utilization_rate_trends_figure = display_utilization_rate_trends('Year/Months', 'Utilization Rate (%)', df_bottling)

# Display the figure in Streamlit app
st.plotly_chart(utilization_rate_trends_figure)

def display_overtime_rate_bar_chart(df):
    # Calculate Overtime Rate
    df['Overtime Rate (%)'] = (df['Overtime per week (hours)'] / 
                                (df['Run time per week (hours)'] + 
                                 df['Changeover time per week (hours)'] + 
                                 df['Breakdown time per week (hours)'] + 
                                 df['Unused capacity per week (hours)'] + 
                                 df['Overtime per week (hours)']) * 100)

    # Create a bar chart for Overtime Rate
    fig = px.bar(df, x='Year/Months', y='Overtime Rate (%)',
                 labels={'Year/Months': 'Year/Months', 'Overtime Rate (%)': 'Overtime Rate (%)'},
                 title='Bottling Line Overtime Rate Over Time')

    # Update layout for better display
    fig.update_layout(
        xaxis_title='Year/Months',
        yaxis_title='Overtime Rate Percentage (%)',
        hovermode='x',
        showlegend=False  # We don't need a legend for a single bar chart
    )

    # Return the Plotly figure
    return fig

# Example usage of the function
overtime_rate_bar_chart_figure = display_overtime_rate_bar_chart(df_bottling)

# Display the figure in Streamlit app
st.plotly_chart(overtime_rate_bar_chart_figure)

# Function to display Unused Capacity Rate and Overtime Rate comparison as a line chart
def unused_capacity_overtime_comparison(df):
    # Calculate Unused Capacity Rate
    df['Unused Capacity Rate (%)'] = (df['Unused capacity per week (hours)'] / 
                                      (df['Run time per week (hours)'] + 
                                       df['Changeover time per week (hours)'] + 
                                       df['Breakdown time per week (hours)'] + 
                                       df['Unused capacity per week (hours)'] + 
                                       df['Overtime per week (hours)']) * 100)

    # Calculate Overtime Rate
    df['Overtime Rate (%)'] = (df['Overtime per week (hours)'] / 
                                (df['Run time per week (hours)'] + 
                                 df['Changeover time per week (hours)'] + 
                                 df['Breakdown time per week (hours)'] + 
                                 df['Unused capacity per week (hours)'] + 
                                 df['Overtime per week (hours)']) * 100)

    # Create a line chart for Unused Capacity Rate and Overtime Rate comparison
    fig = px.line(df, x='Year/Months', y=['Unused Capacity Rate (%)', 'Overtime Rate (%)'],
                  labels={'Year/Months': 'Year/Months', 'value': 'Percentage (%)'},
                  title='Bottling Line Unused Capacity Rate and Overtime Rate Over Time',
                  color_discrete_sequence=['blue', 'orange'])

    # Update layout for better display
    fig.update_layout(
        xaxis_title='Year/Months',
        yaxis_title='Percentage (%)',
        hovermode='x',
        showlegend=True
    )

    # Return the Plotly figure
    return fig

# Example usage of the function
capacity_overtime_comparison_figure = unused_capacity_overtime_comparison(df_bottling)

# Display the figure in Streamlit app
st.plotly_chart(capacity_overtime_comparison_figure)

### Mixer KPIs:
#4. **Lot Size Trends**
#  - Analyzing the trend in average lot size over different periods.
def display_lot_size_trends(x, y, df):
    # Convert the date column to datetime format
    df[x] = pd.to_datetime(df[x], format='%Y %B')

    # Create a Plotly figure for lot size trends
    fig = px.line(df, x=x, y=y, markers=True, line_shape='linear', labels={x: 'Year/Months', y: 'Average Lot Size'})

    # Update layout for better display
    fig.update_layout(
        title='Lot Size Trends Over Time',
        xaxis_title='Year/Months',
        yaxis_title='Average Lot Size',
        hovermode='x',
        yaxis_range=[5000, 15000],
        showlegend=True
    )

    # Return the Plotly figure
    return fig

# Example usage of the function
lot_size_trends_figure = display_lot_size_trends('Year/Months', 'Average lot size', df_mixer)

# Display the figure in Streamlit app
st.plotly_chart(lot_size_trends_figure)


#Cleaning time trend 5
def display_cleaning_time_trends(x, y, df):
    # Convert the date column to datetime format
    df[x] = pd.to_datetime(df[x], format='%Y %B')

    # Create a Plotly figure for Cleaning Time Trends
    fig = px.line(df, x=x, y=y, markers=True, line_shape='linear', labels={x: 'Year/Months', y: 'Cleaning Time (%)'})

    # Update layout for better display
    fig.update_layout(
        title='Cleaning Time Trends Over Time',
        xaxis_title='Year/Months',
        yaxis_title='Cleaning Time Percentage (%)',
        hovermode='x',
        showlegend=True
    )

    # Return the Plotly figure
    return fig

# Example usage of the function
cleaning_time_trends_figure = display_cleaning_time_trends('Year/Months', 'Cleaning time (%)', df_mixer)

# Display the figure in Streamlit app
st.plotly_chart(cleaning_time_trends_figure)


def display_cleaning_efficiency_lot_size_correlation(df):
    # Create a scatter plot with color gradient
    fig = px.scatter(df, x='Cleaning time (%)', y='Average lot size', color='Average lot size',
                     labels={'Cleaning time (%)': 'Cleaning Time (%)', 'Average lot size': 'Average Lot Size'},
                     title='Cleaning Efficiency and Lot Size Correlation',
                     hover_name='Year/Months', size_max=20,
                     color_continuous_scale=px.colors.sequential.Plasma)  # You can choose a different color scale

    # Update layout for better display
    fig.update_layout(
        hovermode='closest',
        showlegend=True
    )

    # Return the Plotly figure
    return fig

# Example usage of the function
cleaning_efficiency_lot_size_correlation_figure = display_cleaning_efficiency_lot_size_correlation(df_mixer)

# Display the figure in Streamlit app
st.plotly_chart(cleaning_efficiency_lot_size_correlation_figure)

### Cross-Functional KPIs (Both Tables):
df_merged = pd.merge(df_bottling, df_mixer, on='Year/Months')

#Cleaning Efficiency and Utilization:
def display_cleaning_efficiency_utilization_correlation(df):
    # Create a scatter plot with color gradient
    fig = px.scatter(df, x='Cleaning time (%)', y='Run time (%)', color='Average lot size',
                     labels={'Cleaning time (%)': 'Cleaning Time (%)', 'Run time (%)': 'Bottling Utilization Rate (%)'},
                     title='Cleaning Efficiency and Utilization Correlation',
                     hover_name='Year/Months', size_max=20,
                     color_continuous_scale=px.colors.sequential.Plasma)  # You can choose a different color scale

    # Update layout for better display
    fig.update_layout(
        hovermode='closest',
        showlegend=True
    )

    # Return the Plotly figure
    return fig

# Example usage of the function with the merged dataframe
cleaning_efficiency_utilization_correlation_figure = display_cleaning_efficiency_utilization_correlation(df_merged)

# Display the figure in Streamlit app
st.plotly_chart(cleaning_efficiency_utilization_correlation_figure)


