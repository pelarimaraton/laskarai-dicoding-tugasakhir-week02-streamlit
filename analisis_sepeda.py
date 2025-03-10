import altair as alt
import pandas as pd
import streamlit as st

# Load data
url_day = 'https://raw.githubusercontent.com/pelarimaraton/laskarai-dicoding-tugasakhir-week02/main/Bike-sharing-dataset/day.csv'
url_hour = 'https://raw.githubusercontent.com/pelarimaraton/laskarai-dicoding-tugasakhir-week02/main/Bike-sharing-dataset/hour.csv'
day_df = pd.read_csv(url_day)
hour_df = pd.read_csv(url_hour)

# Judul Aplikasi
st.title("Analisis Penyewaan Sepeda")

# Fungsi untuk membuat grafik Altair
def create_altair_chart(data, x_col, y_col, title, x_title, y_title):
    chart = alt.Chart(data).mark_bar().encode(
        x=alt.X(x_col, title=x_title),
        y=alt.Y(y_col, title=y_title),
        tooltip=[x_col, y_col]
    ).properties(
        title=title
    ).interactive()
    return chart

# Analisis Hari Kerja (Weekday)
st.header("Analisis Penyewaan Sepeda Berdasarkan Hari Kerja")

# Group data by weekday
day_weekday_grouped = day_df.groupby('weekday')[['cnt', 'casual', 'registered']].mean().reset_index()
hour_weekday_grouped = hour_df.groupby('weekday')[['cnt', 'casual', 'registered']].mean().reset_index()

# Konversi weekday ke nama hari
days = ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu']
day_weekday_grouped['weekday'] = day_weekday_grouped['weekday'].map(lambda x: days[x])
hour_weekday_grouped['weekday'] = hour_weekday_grouped['weekday'].map(lambda x: days[x])

# Visualisasi data dengan Altair
st.subheader("Visualisasi Rata-rata Penyewa Sepeda per Hari Kerja")
day_chart = create_altair_chart(day_weekday_grouped, 'weekday', 'cnt', 'Rata-rata Penyewa Sepeda per Hari (day_df)', 'Hari dalam Seminggu', 'Rata-rata Jumlah Penyewa')
st.altair_chart(day_chart, use_container_width=True)

st.subheader("Visualisasi Rata-rata Penyewa Sepeda per Jam Kerja")
hour_chart = create_altair_chart(hour_weekday_grouped, 'weekday', 'cnt', 'Rata-rata Penyewa Sepeda per Jam (hour_df)', 'Hari dalam Seminggu', 'Rata-rata Jumlah Penyewa')
st.altair_chart(hour_chart, use_container_width=True)

# Analisis Kondisi Cuaca (Weathersit)
st.header("Analisis Penyewaan Sepeda Berdasarkan Kondisi Cuaca")

# Group data by weathersit
day_weathersit_grouped = day_df.groupby('weathersit')[['cnt', 'casual', 'registered']].mean().reset_index()
hour_weathersit_grouped = hour_df.groupby('weathersit')[['cnt', 'casual', 'registered']].mean().reset_index()

# Konversi weathersit ke nama kondisi cuaca
weathers = ['Cerah', 'Kabut', 'Hujan Ringan', 'Hujan Lebat']
day_weathersit_grouped['weathersit'] = day_weathersit_grouped['weathersit'].map(lambda x: weathers[x-1])
hour_weathersit_grouped['weathersit'] = hour_weathersit_grouped['weathersit'].map(lambda x: weathers[x-1])

# Visualisasi data dengan Altair
st.subheader("Visualisasi Rata-rata Penyewa Sepeda per Kondisi Cuaca (day_df)")
day_weather_chart = create_altair_chart(day_weathersit_grouped, 'weathersit', 'cnt', 'Rata-rata Penyewa Sepeda per Kondisi Cuaca (day_df)', 'Kondisi Cuaca', 'Rata-rata Jumlah Penyewa')
st.altair_chart(day_weather_chart, use_container_width=True)

st.subheader("Visualisasi Rata-rata Penyewa Sepeda per Kondisi Cuaca (hour_df)")
hour_weather_chart = create_altair_chart(hour_weathersit_grouped, 'weathersit', 'cnt', 'Rata-rata Penyewa Sepeda per Kondisi Cuaca (hour_df)', 'Kondisi Cuaca', 'Rata-rata Jumlah Penyewa')
st.altair_chart(hour_weather_chart, use_container_width=True)
