import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca dataset
df_day = pd.read_csv("dataset/day.csv", delimiter=",")
df_hour = pd.read_csv("dataset/hour.csv", delimiter=",")

# Menggabungkan DataFrame
bike_df = pd.merge(df_hour, df_day, on='dteday', how='inner', suffixes=('_hour', '_day'))

# Menambahkan label cuaca
label_cuaca = {
    1: 'Cerah',
    2: 'Berawan',
    3: 'Hujan Ringan',
    4: 'Hujan Lebat'
}
bike_df['weather_label'] = bike_df['weathersit_day'].map(label_cuaca)

# Pertanyaan 1
def question_1():
    st.subheader('Pertanyaan 1:')
    st.write('Menghitung rata-rata peminjaman sepeda untuk setiap jam')
    rental_jam = bike_df.groupby('hr')['cnt_hour'].mean()
    plt.bar(rental_jam.index, rental_jam.values, color='#ff7f0e')  
    plt.title('Rata-Rata Peminjaman per Jam')
    plt.xlabel('Jam')
    plt.ylabel('Rata-Rata Peminjaman')
    st.pyplot()

# Pertanyaan 2
def question_2():
    st.subheader('Pertanyaan 2:')
    st.write('Menghitung rata-rata peminjaman sepeda berdasarkan kondisi cuaca')
    avg_weather = bike_df.groupby('weather_label')['cnt_day'].mean().reset_index().sort_values(by="cnt_day")
    plt.figure(figsize=(10, 6))
    sns.barplot(x='cnt_day', y='weather_label', data=avg_weather, palette='rocket_r')  
    plt.title('Rata-Rata Peminjaman Sepeda berdasarkan Kondisi Cuaca')
    plt.xlabel('Rata-Rata Peminjaman')
    plt.ylabel('Kondisi Cuaca')
    st.pyplot()

# Pertanyaan 3
def question_3():
    st.subheader('Pertanyaan 3:')
    st.write('Menghitung rata-rata peminjaman sepeda pada hari libur dan bukan hari libur')
    avg_holiday = bike_df.groupby('holiday_day')['cnt_day'].mean().reset_index().sort_values(by="cnt_day")
    avg_holiday['holiday_day'] = avg_holiday['holiday_day'].apply(lambda x: 'Libur' if x == 1 else 'Tidak Libur')
    plt.figure(figsize=(8, 5))
    sns.barplot(x='holiday_day', y='cnt_day', data=avg_holiday, palette='husl')  
    plt.title('Rata-rata Peminjaman Sepeda pada Hari Libur')
    plt.xlabel('Hari Libur')
    plt.ylabel('Rata-rata Peminjaman')
    plt.xticks([0, 1], ['Tidak Libur', 'Libur'])
    st.pyplot()

def main():
    st.title('Dashboard Analisis Data: Bike Sharing Dataset')
    st.sidebar.title('Menu')
    menu = st.sidebar.radio('Pilih Menu:', ('Pertanyaan 1', 'Pertanyaan 2', 'Pertanyaan 3'))

    if menu == 'Pertanyaan 1':
        question_1()
    elif menu == 'Pertanyaan 2':
        question_2()
    elif menu == 'Pertanyaan 3':
        question_3()

if __name__ == "__main__":
    main()
