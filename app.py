import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import openpyxl
import plotly as plt

st.set_page_config(page_title="Juicy Fruit Corporation dashboards", page_icon="bar_chart", layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)

from SCM_KPI_visuals import ObsoletesKPI, ServiceLevelPiecesandOrderlinesKPI, AverageRejectionsStartupBatches, ProductionAdherenceKPI, CubeUtilizationandOverflowKPI
from production_KPI import bottling_oee_figure, run_time_trends_figure, utilization_rate_trends_figure, lot_size_trends_figure, cleaning_time_trends_figure, cleaning_efficiency_lot_size_correlation_figure, overtime_rate_bar_chart_figure, capacity_overtime_comparison_figure
from Sales_Product_final import OSAPerformanceKPI, GrossmarginperweekKPI
from Sales_Customer_final import ServicelevelorderlinesKPI, AttainedshelflifeKPI, GrossMarginKPI
from Purchasing import Delivery_Reliability_per_supplier, Delivery_Reliability_average, stock_value_tetrapack, stock_value_3M_bottles, stock_value_orange, stock_value_mango, stock_value_citrus_syrup, total_stock_value, Transport_costs_tetrapack, Transport_costs_3M_bottles, Transport_costs_orange, Transport_costs_mango, Transport_costs_citrus_syrup, total_Transport_costs
from Distributor import average_distribution_costs



df = 'Juicy Fruit Corporation final v2.xlsx'

def get_sheet_data(df, sheet_name):
    try:
        df = pd.read_excel(df, sheet_name=sheet_name)
        return df
    except Exception as e:
        st.write(e)
        return None

xls = pd.ExcelFile(df)
sheet_names = xls.sheet_names

def get_kpis_for_department(selected_department):
    # Define KPIs for each department
    kpi_mapping = {
        'SCM(Inventory)': ['ObsoletesKPI', 
                           'ServiceLevelPiecesandOrderlinesKPI', 
                           'AverageRejectionsStartupBatches',
                           'ProductionAdherenceKPI'
                           ],
        'Bottling(Operations)': ['OEE', 
                                 'Run time trends', 
                                 'Utilization rates',
                                 'Overtime rate',
                                 'Overtime vs Unused Capacity'
                                 ],
        'Mixer(Operations)':[ 'Lot Size Trends',
                             'Cleaning Time Trend',
                             'Cleaning Efficiency and Lot Size Correlation'
                            ],
        'Sales (Customer - Product)':[
                            'OSAPerformanceKPI',
                            'GrossmarginperweekKPI'
                            ],
        'Sales(Customer)': [
                            'ServicelevelorderlinesKPI',
                            'AttainedshelflifeKPI',
                            'GrossMarginKPI'
                            ],            
        'Purchasing':[
            'Delivery_Reliability_per_supplier', 
            'Delivery_Reliability_average', 
            'stock_value_tetrapack', 
            'stock_value_3M_bottles', 
            'stock_value_orange', 
            'stock_value_mango', 
            'stock_value_citrus_syrup', 
            'total_stock_value', 
            'Transport_costs_tetrapack', 
            'Transport_costs_3M_bottles', 
            'Transport_costs_orange', 
            'Transport_costs_mango', 
            'Transport_costs_citrus_syrup', 
            'total_Transport_costs'
        ],
        'Distributor':[
            'Distribution Costs per Pallet'
        ],
        'Warehouse(Raw and fin. goods)':[
            'CubeUtilizationandOverflowKPI'
        ]
    }

    # Return KPIs based on the selected department
    return kpi_mapping.get(selected_department, [])


# H1
st.title(':bar_chart: Juicy Fruit Corporation dashboards')
st.markdown('##')

# Create sidebars to select department and KPI
st.sidebar.header('Select department:')
selected_department = st.sidebar.selectbox('Select department:', sheet_names)

# Only get and display data when a specific department is selected
if selected_department in sheet_names:
    # Get data based on the selected department
    selected_data = get_sheet_data(df, selected_department)
    st.write(selected_data)

    # Populate KPI dropdown based on the selected department
    kpis = get_kpis_for_department(selected_department)
    st.sidebar.header('Select KPI')
    select_kpi = st.sidebar.selectbox('Select KPI from department:', kpis)

    # SCM kpis to select
    if select_kpi == 'ObsoletesKPI':
        st.write('Obsoletes KPI')
        st.pyplot(ObsoletesKPI('Year/Months', 'Year/Months', 'Obsoletes (%)'))
    elif select_kpi == 'ServiceLevelPiecesandOrderlinesKPI':
        st.write('Service Level Pieces and Order lines')
        st.pyplot(ServiceLevelPiecesandOrderlinesKPI("Product", "Service level (pieces)", "Service level (order lines)"))
    elif select_kpi == 'AverageRejectionsStartupBatches':
        st.write('Average Rejections Startup Batches')
        st.pyplot(AverageRejectionsStartupBatches('Rejects (value)', 'Start up productivity loss (value)', 'Production batches previous round'))
    elif select_kpi == 'ProductionAdherenceKPI':
        st.write('Production Adherence KPI')
        st.pyplot(ProductionAdherenceKPI('Year/Months', 'Year/Months', 'Production plan adherence (%)'))
    elif select_kpi == 'CubeUtilizationandOverflowKPI':
        st.write('Cube Utilization and Overflow KPI')
        st.pyplot(CubeUtilizationandOverflowKPI(['Finished goods warehouse', 'Raw materials warehouse'], 'Cube utilization (%)', 'Overflow (%)'))
    #operations KPIs
    elif select_kpi == 'OEE' and selected_department == 'Bottling(Operations)':
        st.write('Overall Equipment Effectiveness (OEE) Over Time')
        st.plotly_chart(bottling_oee_figure)
    elif select_kpi == 'Run time trends' and selected_department == 'Bottling(Operations)':
        st.write('Run time trends')
        st.plotly_chart(run_time_trends_figure)
    elif select_kpi == 'Utilization rates' and selected_department == 'Bottling(Operations)':
        st.write('Utilization rate')
        st.plotly_chart(utilization_rate_trends_figure)
    elif select_kpi == 'Overtime rate' and selected_department == 'Bottling(Operations)':
        st.write('Overtime rate')
        st.plotly_chart(overtime_rate_bar_chart_figure)
    elif select_kpi == 'Overtime vs Unused Capacity' and selected_department == 'Bottling(Operations)':
        st.write('Overtime vs Unused Capacity')
        st.plotly_chart(capacity_overtime_comparison_figure)
    elif select_kpi == 'Lot Size Trends' and selected_department == 'Mixer(Operations)':
        st.write('Lot Size trends')
        st.plotly_chart(lot_size_trends_figure)
    elif select_kpi == 'Cleaning Time Trend' and selected_department == 'Mixer(Operations)':
        st.write('Cleaning Time Trends')
        st.plotly_chart(cleaning_time_trends_figure)
    elif select_kpi == 'Cleaning Efficiency and Lot Size Correlation' and selected_department == 'Mixer(Operations)':
        st.write('Cleaning Efficiency and Lot Size Correlation')
        st.plotly_chart(cleaning_efficiency_lot_size_correlation_figure)  
    #sales KPI
    elif select_kpi == 'OSAPerformanceKPI':
        st.write('OSA Performance KPI')
        st.pyplot(OSAPerformanceKPI('Year/Months', 'Customer', 'OSA'))
    elif select_kpi == 'GrossmarginperweekKPI':
        st.write('Gross margin per week KPI')
        st.pyplot(GrossmarginperweekKPI('Year/Months', 'Product ', 'Gross margin per week'))
    elif select_kpi == 'ServicelevelorderlinesKPI':
        st.write('Service level order lines KPI')
        st.pyplot(ServicelevelorderlinesKPI('Year/Months', 'Customer', 'Service level (order lines)'))
    elif select_kpi == 'AttainedshelflifeKPI':
        st.write('Attained shelf life KPI')
        st.pyplot(AttainedshelflifeKPI('Year/Months', 'Customer', 'Attained shelf life (%)'))
    elif select_kpi == 'GrossMarginKPI':
        st.write('Gross Margin KPI')
        st.pyplot(GrossMarginKPI('Customer', 'Year/Months', 'Gross margin per week'))
    #purchasing KPI
    elif select_kpi == 'Delivery_Reliability_per_supplier':
        st.write('Delivery Reliability per supplier')
        st.pyplot(Delivery_Reliability_per_supplier ('Supplier name','Year/Months', 'Delivery reliability (%)'))
    elif select_kpi == 'Delivery_Reliability_average':
        st.write('Delivery Reliability average')
        st.pyplot(Delivery_Reliability_average('Supplier name', 'Year/Months', 'Delivery reliability (%)'))
    elif select_kpi == 'stock_value_tetrapack':
        st.write('Stock value tetrapack')
        st.pyplot(stock_value_tetrapack('Year/Months', 'Supplier name', 'Stock value'))
    elif select_kpi == 'stock_value_3M_bottles':
        st.write('Stock value 3M bottles')
        st.pyplot(stock_value_3M_bottles('Year/Months', 'Supplier name', 'Stock value')) 
    elif select_kpi == 'stock_value_orange':
        st.write('Stock value orange')
        st.pyplot(stock_value_orange('Year/Months', 'Supplier name', 'Stock value')) 
    elif select_kpi == 'stock_value_mango':
        st.write('Stock value mango')
        st.pyplot(stock_value_mango('Year/Months', 'Supplier name', 'Stock value'))
    elif select_kpi == 'stock_value_citrus_syrup':
        st.write('Stock value citrus syrup')
        st.pyplot(stock_value_citrus_syrup('Year/Months', 'Supplier name', 'Stock value'))
    elif select_kpi == 'total_stock_value':
        st.write('Total stock value')
        st.pyplot(total_stock_value('Year/Months' , 'Stock value'))
    elif select_kpi == 'Transport_costs_tetrapack':
        st.write('Transport costs tetrapack')
        st.pyplot(Transport_costs_tetrapack('Year/Months', 'Supplier name', 'Transport costs'))
    elif select_kpi == 'Transport_costs_3M_bottles':
        st.write('Transport costs 3M bottles')
        st.pyplot(Transport_costs_3M_bottles('Year/Months', 'Supplier name', 'Transport costs'))
    elif select_kpi == 'Transport_costs_orange':
        st.write('Transport costs orange')
        st.pyplot(Transport_costs_orange('Year/Months', 'Supplier name', 'Transport costs'))
    elif select_kpi == 'Transport_costs_mango':
        st.write('Transport costs mango')
        st.pyplot(Transport_costs_mango('Year/Months', 'Supplier name', 'Transport costs'))
    elif select_kpi == 'Transport_costs_citrus_syrup':
        st.write('Transport costs citrus syrup')
        st.pyplot(Transport_costs_citrus_syrup('Year/Months', 'Supplier name', 'Transport costs'))
    elif select_kpi == 'total_Transport_costs':
        st.write('Total transport costs')
        st.pyplot(total_Transport_costs('Year/Months' , 'Transport costs'))
    elif select_kpi == 'Distribution Costs per Pallet':
        st.write('Distribution Costs per Pallet')
        st.plotly_chart(average_distribution_costs)
    else:
        st.write('No KPI is selected')