import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
url_day = 'https://raw.githubusercontent.com/pelarimaraton/laskarai-dicoding-tugasakhir-week02/main/Bike-sharing-dataset/day.csv'
url_hour = 'https://raw.githubusercontent.com/pelarimaraton/laskarai-dicoding-tugasakhir-week02/main/Bike-sharing-dataset/hour.csv'
day_df = pd.read_csv(url_day)
hour_df = pd.read_csv(url_hour)

# Judul Aplikasi
st.title("Analisis Penyewaan Sepeda")

# Analisis Hari Kerja (Weekday)
st.header("Analisis Penyewaan Sepeda Berdasarkan Hari Kerja")

# Group data by weekday
day_weekday_grouped = day_df.groupby('weekday')[['cnt', 'casual', 'registered']].mean()
hour_weekday_grouped = hour_df.groupby('weekday')[['cnt', 'casual', 'registered']].mean()
merged_weekday_data = pd.merge(day_weekday_grouped, hour_weekday_grouped, left_index=True, right_index=True, suffixes=('_day', '_hour'))

# Tampilkan data yang dikelompokkan
st.subheader("Data Agregat per Hari Kerja")
st.write("Data harian:")
st.write(day_weekday_grouped)
st.write("Data per jam:")
st.write(hour_weekday_grouped)
st.write("Data gabungan:")
st.write(merged_weekday_data)

# Visualisasi data
st.subheader("Visualisasi Rata-rata Penyewa Sepeda per Hari Kerja")
fig, ax = plt.subplots(figsize=(12, 6))
day_weekday_grouped.plot(kind='bar', ax=ax)
plt.title('Rata-rata Penyewa Sepeda per Hari (day_df)')
plt.xlabel('Hari dalam Seminggu')
plt.ylabel('Rata-rata Jumlah Penyewa')
plt.xticks(range(7), ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'], rotation=45)
st.pyplot(fig)

st.subheader("Visualisasi Rata-rata Penyewa Sepeda per Jam Kerja")
fig, ax = plt.subplots(figsize=(12, 6))
hour_weekday_grouped.plot(kind='bar', ax=ax)
plt.title('Rata-rata Penyewa Sepeda per Jam (hour_df)')
plt.xlabel('Hari dalam Seminggu')
plt.ylabel('Rata-rata Jumlah Penyewa')
plt.xticks(range(7), ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'], rotation=45)
st.pyplot(fig)


# Analisis Kondisi Cuaca (Weathersit)
st.header("Analisis Penyewaan Sepeda Berdasarkan Kondisi Cuaca")

# Group data by weathersit
day_weathersit_grouped = day_df.groupby('weathersit')[['cnt', 'casual', 'registered']].mean()
hour_weathersit_grouped = hour_df.groupby('weathersit')[['cnt', 'casual', 'registered']].mean()
merged_weathersit_data = pd.merge(day_weathersit_grouped, hour_weathersit_grouped, left_index=True, right_index=True, suffixes=('_day', '_hour'))

# Tampilkan data yang dikelompokkan
st.subheader("Data Agregat per Kondisi Cuaca")
st.write("Data harian:")
st.write(day_weathersit_grouped)
st.write("Data per jam:")
st.write(hour_weathersit_grouped)
st.write("Data gabungan:")
st.write(merged_weathersit_data)

# Visualisasi data
st.subheader("Visualisasi Rata-rata Penyewa Sepeda per Kondisi Cuaca (day_df)")
fig, ax = plt.subplots(figsize=(10, 6))
day_weathersit_grouped.plot(kind='bar', ax=ax)
plt.title('Rata-rata Penyewa Sepeda per Kondisi Cuaca (day_df)')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Rata-rata Jumlah Penyewa')
plt.xticks(range(4), ['Cerah', 'Kabut', 'Hujan Ringan', 'Hujan Lebat'], rotation=0)
st.pyplot(fig)

st.subheader("Visualisasi Rata-rata Penyewa Sepeda per Kondisi Cuaca (hour_df)")
fig, ax = plt.subplots(figsize=(10, 6))
hour_weathersit_grouped.plot(kind='bar', ax=ax)
plt.title('Rata-rata Penyewa Sepeda per Kondisi Cuaca (hour_df)')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Rata-rata Jumlah Penyewa')
plt.xticks(range(4), ['Cerah', 'Kabut', 'Hujan Ringan', 'Hujan Lebat'], rotation=0)
st.pyplot(fig)