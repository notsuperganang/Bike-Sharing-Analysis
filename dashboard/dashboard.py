import streamlit as st
import pandas as pd
import plotly.express as px
import os
from pathlib import Path

# Config
st.set_page_config(
    page_title="Bike Sharing Analysis Dashboard",
    page_icon="🚲",
    layout="wide"
)

# Function to load data with proper path handling
@st.cache_data
def load_data():
    # Get the directory where the script is located
    script_dir = Path(__file__).parent
    
    # Define paths to the data files
    hour_file = script_dir / "hourly_cleaned.csv"
    day_file = script_dir / "daily_cleaned.csv"
    
    # Try different path options if files aren't found
    if not hour_file.exists():
        # Try relative to the current working directory
        hour_file = Path("dashboard/hourly_cleaned.csv")
        if not hour_file.exists():
            hour_file = Path("hourly_cleaned.csv")
    
    if not day_file.exists():
        # Try relative to the current working directory
        day_file = Path("dashboard/daily_cleaned.csv")
        if not day_file.exists():
            day_file = Path("daily_cleaned.csv")
    
    # Load the data
    try:
        df_hour = pd.read_csv(hour_file)
        df_day = pd.read_csv(day_file)
        # st.success(f"Data loaded successfully from {hour_file} and {day_file}")
    except FileNotFoundError as e:
        st.error(f"Error loading data: {e}")
        # Create empty DataFrames as fallback
        df_hour = pd.DataFrame()
        df_day = pd.DataFrame()
    
    return df_hour, df_day

# Load data
df_hour, df_day = load_data()

# Display warning if data is empty
if df_hour.empty or df_day.empty:
    st.warning("⚠️ Data could not be loaded. Please check file paths in the deployment.")
    st.info(f"Current working directory: {os.getcwd()}")
    st.info(f"Files in current directory: {[f for f in os.listdir('.') if os.path.isfile(f)]}")
    st.stop()

# Dashboard title
st.title("🚲 Bike Sharing Analysis Dashboard")
st.markdown("Dashboard untuk analisis pola penyewaan sepeda berdasarkan waktu, musim, dan cuaca.")

# Sidebar - Filters
st.sidebar.header("Filters")
year_filter = st.sidebar.multiselect(
    "Pilih Tahun",
    options=df_hour['year'].unique(),
    default=df_hour['year'].unique()
)

season_filter = st.sidebar.multiselect(
    "Pilih Musim",
    options=df_hour['season_desc'].unique(),
    default=df_hour['season_desc'].unique()
)

# Filter data
filtered_hour = df_hour[df_hour['year'].isin(year_filter) & df_hour['season_desc'].isin(season_filter)]
filtered_day = df_day[df_day['year'].isin(year_filter) & df_day['season_desc'].isin(season_filter)]

# Create tabs
tab1, tab2 = st.tabs(["Pola Waktu & Musim", "Pola berdasarkan Cuaca"])

# Tab 1: Pola Waktu & Musim
with tab1:
    st.header("Bagaimana faktor waktu dan musim mempengaruhi permintaan rental sepeda?")
    
    # Row 1
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Pola Penyewaan Berdasarkan Jam")
        hourly_stats = filtered_hour.groupby('hr').agg({
            'casual': 'sum',
            'registered': 'sum',
            'cnt': 'sum'
        }).reset_index()
        
        fig = px.line(hourly_stats, x='hr', y=['cnt', 'registered', 'casual'],
                     labels={'hr': 'Jam', 'value': 'Jumlah Penyewaan', 'variable': 'Tipe Pengguna'},
                     color_discrete_sequence=['#0088FE', '#00C49F', '#FFBB28'],
                     title='Pola Penyewaan Sepeda Berdasarkan Jam')
        fig.update_layout(xaxis=dict(tickmode='linear', dtick=1))
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Pola Penyewaan Berdasarkan Hari")
        weekday_stats = filtered_hour.groupby(['weekday']).agg({
            'casual': 'sum',
            'registered': 'sum',
            'cnt': 'sum'
        }).reset_index()
        
        # Map weekday numbers to names
        day_names = {0: 'Minggu', 1: 'Senin', 2: 'Selasa', 3: 'Rabu', 4: 'Kamis', 5: 'Jumat', 6: 'Sabtu'}
        weekday_stats['day_name'] = weekday_stats['weekday'].map(day_names)
        
        fig = px.bar(weekday_stats, x='day_name', y=['registered', 'casual'],
                    labels={'day_name': 'Hari', 'value': 'Jumlah Penyewaan', 'variable': 'Tipe Pengguna'},
                    color_discrete_sequence=['#00C49F', '#FFBB28'],
                    title='Pola Penyewaan Sepeda Berdasarkan Hari', barmode='stack')
        fig.update_xaxes(categoryorder='array', categoryarray=['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'])
        st.plotly_chart(fig, use_container_width=True)
    
    # Row 2
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("Pola Penyewaan Berdasarkan Bulan")
        monthly_stats = filtered_day.groupby(['mnth']).agg({
            'casual': 'sum',
            'registered': 'sum',
            'cnt': 'sum'
        }).reset_index()
        
        # Map month numbers to names
        month_names = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'Mei', 6: 'Jun', 
                       7: 'Jul', 8: 'Agt', 9: 'Sep', 10: 'Okt', 11: 'Nov', 12: 'Des'}
        monthly_stats['month_name'] = monthly_stats['mnth'].map(month_names)
        
        fig = px.line(monthly_stats, x='month_name', y=['cnt', 'registered', 'casual'],
                     labels={'month_name': 'Bulan', 'value': 'Jumlah Penyewaan', 'variable': 'Tipe Pengguna'},
                     color_discrete_sequence=['#0088FE', '#00C49F', '#FFBB28'],
                     title='Pola Penyewaan Sepeda Berdasarkan Bulan')
        fig.update_xaxes(categoryorder='array', categoryarray=list(month_names.values()))
        st.plotly_chart(fig, use_container_width=True)
    
    with col4:
        st.subheader("Pola Penyewaan Berdasarkan Musim")
        season_stats = filtered_day.groupby(['season_desc']).agg({
            'casual': 'sum',
            'registered': 'sum',
            'cnt': 'sum'
        }).reset_index()
        
        fig = px.bar(season_stats, x='season_desc', y=['registered', 'casual'],
                    labels={'season_desc': 'Musim', 'value': 'Jumlah Penyewaan', 'variable': 'Tipe Pengguna'},
                    color_discrete_sequence=['#00C49F', '#FFBB28'],
                    title='Pola Penyewaan Sepeda Berdasarkan Musim', barmode='stack')
        st.plotly_chart(fig, use_container_width=True)
        
# Tab 2: Pola berdasarkan Cuaca
with tab2:
    st.header("Apa perbedaan pola penggunaan antara pengguna kasual dan terdaftar berdasarkan kondisi cuaca?")
    
    # Row 1
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Pola Penyewaan Berdasarkan Kondisi Cuaca")
        weather_stats = filtered_hour.groupby(['weather_desc']).agg({
            'casual': 'sum',
            'registered': 'sum',
            'cnt': 'sum',
            'casual_ratio': 'mean'
        }).reset_index()
        
        fig = px.bar(weather_stats, x='weather_desc', y=['registered', 'casual'],
                    labels={'weather_desc': 'Kondisi Cuaca', 'value': 'Jumlah Penyewaan', 'variable': 'Tipe Pengguna'},
                    color_discrete_sequence=['#00C49F', '#FFBB28'],
                    title='Pola Penyewaan Sepeda Berdasarkan Kondisi Cuaca', barmode='stack')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Rasio Pengguna Kasual Berdasarkan Kondisi Cuaca")
        fig = px.bar(weather_stats, x='weather_desc', y='casual_ratio',
                    labels={'weather_desc': 'Kondisi Cuaca', 'casual_ratio': 'Rasio Pengguna Kasual'},
                    color_discrete_sequence=['#FFBB28'],
                    title='Rasio Pengguna Kasual Berdasarkan Kondisi Cuaca')
        fig.update_yaxes(tickformat=".0%")
        st.plotly_chart(fig, use_container_width=True)
    
    # Row 2
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("Korelasi Faktor Cuaca dengan Jumlah Penyewaan")
        corr_data = filtered_hour[['temp_actual', 'hum_actual', 'windspeed_actual', 'casual', 'registered', 'cnt']]
        correlation = corr_data.corr()
        
        fig = px.imshow(correlation, 
                       labels=dict(color="Korelasi"),
                       x=correlation.columns,
                       y=correlation.columns,
                       color_continuous_scale='RdBu_r',
                       title='Korelasi antara Faktor Cuaca dan Jumlah Penyewaan')
        st.plotly_chart(fig, use_container_width=True)
    
    with col4:
        st.subheader("Hubungan Suhu dengan Jumlah Penyewaan")
        # Sample data for better performance
        sample_size = min(5000, len(filtered_hour))
        sampled_data = filtered_hour.sample(sample_size, random_state=42)
        
        fig = px.scatter(sampled_data, x='temp_actual', y=['casual', 'registered'],
                        labels={'temp_actual': 'Suhu (°C)', 'value': 'Jumlah Penyewaan', 'variable': 'Tipe Pengguna'},
                        color_discrete_sequence=['#FFBB28', '#00C49F'],
                        title='Hubungan Suhu dengan Jumlah Penyewaan', opacity=0.6)
        st.plotly_chart(fig, use_container_width=True)
        
    # Row 3
    st.subheader("Rasio Pengguna Kasual Berdasarkan Kombinasi Musim dan Cuaca")
    
    # Create heatmap
    season_weather_stats = filtered_hour.groupby(['season_desc', 'weather_desc']).agg({
        'casual_ratio': 'mean'
    }).reset_index()
    
    pivot_data = season_weather_stats.pivot_table(
        values='casual_ratio', 
        index='season_desc', 
        columns='weather_desc'
    )
    
    fig = px.imshow(pivot_data, 
                   labels=dict(x="Kondisi Cuaca", y="Musim", color="Rasio Pengguna Kasual"),
                   x=pivot_data.columns,
                   y=pivot_data.index,
                   color_continuous_scale='Blues',
                   text_auto='.3f')
    fig.update_layout(title='Rasio Pengguna Kasual Berdasarkan Kombinasi Musim dan Cuaca')
    st.plotly_chart(fig, use_container_width=True)

# Additional KPIs at the bottom
st.markdown("---")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    total_rentals = filtered_day['cnt'].sum()
    st.metric("Total Penyewaan", f"{total_rentals:,}")

with kpi2:
    casual_pct = (filtered_day['casual'].sum() / total_rentals) * 100
    st.metric("Persentase Pengguna Kasual", f"{casual_pct:.1f}%")

with kpi3:
    peak_month = filtered_day.groupby('mnth')['cnt'].sum().idxmax()
    month_name = {1: 'Januari', 2: 'Februari', 3: 'Maret', 4: 'April', 5: 'Mei', 6: 'Juni',
                 7: 'Juli', 8: 'Agustus', 9: 'September', 10: 'Oktober', 11: 'November', 12: 'Desember'}
    st.metric("Bulan Puncak", month_name[peak_month])

with kpi4:
    peak_hour = filtered_hour.groupby('hr')['cnt'].sum().idxmax()
    st.metric("Jam Puncak", f"{peak_hour}:00")

# Footer
st.markdown("---")
st.caption("Dashboard dibuat dengan Streamlit • Data: Capital Bikeshare System, Washington D.C.")