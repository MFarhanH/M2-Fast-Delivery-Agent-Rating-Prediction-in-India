import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from PIL import Image
import matplotlib.pyplot as plt


def run():

    # Membuat Title
    st.title('Aplikasi Prediksi Rating Agent dari data Fast Delivery Agent (India)')

    # Membuat Sub Header
    st.subheader(
        'Page ini mengenai Exploratory Data Analysis dari dataset Fast Delivery Agent (India)')
    st.write('\n')
    st.write('\n')

    # # Menambahkan Gambar
    image1 = Image.open(
        'D:\Hacktiv8\Phase 1\Milestone 1\p1-ftds027-hck-m2-MFarhanH\Deployment\Foto Delivery.png')
    st.image(
        image1, caption='Prediksi Rating Agent dari data Fast Delivery Agent (India)')

    # Menambahkan Teks
    st.write('# Page ini dibuat oleh: \n # Muhammad Farhan Hendriyanto')
    st.write('# HCK-027')
    st.write('\n')
    st.write('\n')
    st.write('\n')

    # Menampilkan Dataframe
    df = pd.read_csv(
        'D:/Hacktiv8/Phase 1/Milestone 1/p1-ftds027-hck-m2-MFarhanH/Fast Delivery Agent Reviews.csv')
    st.dataframe(df)
    st.write('\n')
    st.write('\n')

    # Soal 1
    st.write('## 1. Bagaimana distribusi data numeriknya?')
    
    # melihat summary statistik deskriptif data numerik
    st.dataframe(df.describe().T)
    st.write('Berdasarkan data tersebut, dapat dilihat bahwa nilai mean dan median pada data hampir sama, ini berarti data memiliki distribusi data yang bisa dibilang mendekati distribusi normal. Lebih detailnya akan dicek pada bagian outlier.')
    st.write('\n')
    st.write('\n')
    # buat function untuk memudahkan pembuatan chart
    '''  
    Function ini bertujuan untuk membuat histogram untuk merepresentasikan distribusi data.
    '''
    def create_data_distribution(df, variable):
        # Define figure size

        fig = plt.figure(figsize=(6, 4))
        sns.boxplot(y=df[variable])
        plt.title(f'Distribusi {variable}')
        plt.xlabel(f'{variable}')
        plt.ylabel('Frekuensi')
        st.pyplot(fig)

    list_numerik = ['Rating', 'Delivery Time (min)', 'Customer Service Rating']
    for i in list_numerik:
        create_data_distribution(df, i)
    st.write('Berdasarkan hasil visualisasi, bisa dilihat bahwa semua data numeriknya tidak ditemukan outlier, sehingga bisa dikatakan jika data terdistribusi normal.')
    st.write('\n')
    st.write('\n')

    #cek distribusi
    listItem= []

    for col in list_numerik:
        listItem.append([col, round(df[col].skew(),1), np.where(
            (round(df[col].skew(),1) <= 0.5) & (round(df[col].skew(),1) >= -0.5),
            'normal','skewed')])

        skewness = pd.DataFrame(columns=['nama kolom', 'nilai skewness', 'distribution'], data= listItem)
    st.dataframe(skewness)
    st.write('\n')
    st.write('\n')

    st.write('Berdasarkan hasil pengecekan skewness, ditemukan bahwa datanya memiliki nilai skewness 0 atau sangat mendektai nol yang dimana bisa dikatakn bahwa data terdistribusi normal. Ini sesuai juga dari hasil summary of statistic description dan visualiasasi box plot yang menyatakan bahwa data terdistribusi normal.')
    st.write('\n')
    st.write('\n')

    # Soal 2
    st.write('## 2. Siapa agen yang paling banyak melakukan pengantaran?')
    # Menghitung jumlah pengantaran per agen
    agent_counts = df['Agent Name'].value_counts().reset_index()
    agent_counts.columns = ['Agent Name', 'Jumlah Pengantaran']

    # Plot barplot top 10 agen dengan pengantaran terbanyak
    fig = plt.figure(figsize=(10, 6))
    sns.barplot(data=agent_counts, x='Agent Name',
                y='Jumlah Pengantaran', palette='Blues_d')
    plt.title('Agen dengan Jumlah Pengantaran Terbanyak')
    plt.xlabel('Agent Name')
    plt.ylabel('Jumlah Pengantaran')
    plt.tight_layout()
    st.pyplot(fig)
    st.write('Berdasaran visualisasi di atas, bisa dilihat bahwa Zepto merupakan agen dengan jumlah pengantaran terbanyak, sedangkan Swiggy Instamart merupakan agent dengan pengantaran terendah.')
    st.write('\n')
    st.write('\n')

    # Soal 3
    st.write(
        '## 3. Apakah terdapat perbedaan rata-rata rating pelanggan berdasarkan jenis Order Type?')
    image2 = Image.open("D:\Hacktiv8\Phase 1\Milestone 1\p1-ftds027-hck-m2-MFarhanH\Deployment\SS_PERBEDAAN_RATA-RATA_RATING_BERDASARKAN_ORDER_TYPE.png")
    st.image(
    image2, caption='Uji Hipotesis Annova')
    st.write('\n')
    st.write('\n')


    # Soal 4
    st.write('## 4. Siapa agen yang memiliki rating terbaik?')

    # Menghitung rata-rata rating tiap agen
    avg_rating = df.groupby('Agent Name')['Rating'].mean().reset_index()

    # Mengurutkan dari rating tertinggi ke terendah
    top_agents = avg_rating.sort_values(by='Rating', ascending=False)

    # Visualisasikan agen berdasarkan ratingnya
    fig = plt.figure(figsize=(10, 6))
    sns.barplot(data=top_agents, x='Rating', y='Agent Name', palette='Greens_d')
    plt.title('Agen dengan Rata-rata Rating Tertinggi')
    plt.xlabel('Rata-rata Rating')
    plt.ylabel('Agent Name')
    plt.xlim(0, 5)
    plt.tight_layout()
    st.pyplot(fig) 
    st.write('Berdasarkan data hasil dari visualisasi di atas, ditemukan bahwa agen yang memiliki rating terbaik adalah Swiggy instamart, sedangkan agen dengan rating terendah adalah Jio Mart.') 
    st.write('\n')
    st.write('\n')


    # Soal 5
    st.write('## 5. Lokasi mana yang memiliki rata-rata delivery time terlama?')
    # Hitung rata-rata delivery time per lokasi
    avg_delivery_by_location = df.groupby('Location')['Delivery Time (min)'].mean().reset_index()

    # Urutkan dari yang paling lama ke paling cepat
    avg_delivery_by_location = avg_delivery_by_location.sort_values(by='Delivery Time (min)', ascending=False)

    # Visualisasikan
    fig = plt.figure(figsize=(10, 6))
    sns.barplot(data=avg_delivery_by_location, x='Delivery Time (min)', y='Location', palette='Reds_r')
    plt.title('Rata-rata Delivery Time Tertinggi per Lokasi')
    plt.xlabel('Rata-rata Waktu Pengantaran (menit)')
    plt.ylabel('Lokasi')
    plt.tight_layout()
    st.pyplot(fig)  
    st.write('Berdasarkan hasil visualisasi di atas, dapat dilihat bahwa hyderabad merupakan lokasi yang rata-rata waktu pengantarannya terlama, yaitu > 35 mnt. Chennai merupakan lokasi yang rata-rata waktu pengirimannya terendah.')
    st.write('\n')
    st.write('\n')


    st.write('## 6. Apakah ada hubungan antara Customer Service Rating dengan Delivery Time?')
    # cek korelasi fitur numerik

    corr_matrix = df[['Customer Service Rating','Delivery Time (min)']].corr(method='spearman')

    fig = plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Customer Service Rating dengan Delivery Time")
    st.pyplot(fig)
    st.write('Di sini saya menggunakan uji korelasi spearman karena data yang ingin diuji keduanya adalah data numerik. Berdasarkan hasil visualiasi tersebut, dapat dilihat bahwa customer service rating bisa dikatan hampir tidak memiliki korelasi sama sekali, -0.00 menandakan bahwa korelasinya adalah negatif, namun sangat kecil.')
    st.write('\n')
    st.write('\n')


    st.write('## 7. Apakah terdapat perbedaan rata-rata waktu pengantaran (Delivery Time) di antara lokasi yang berbeda?')
    image2 = Image.open("D:\Hacktiv8\Phase 1\Milestone 1\p1-ftds027-hck-m2-MFarhanH\Deployment\jawaban_no7.png")
    st.image(
    image2, caption='Uji Hipotesis Annova')
    fig = plt.figure(figsize=(12, 6))
    sns.boxplot(x='Location', y='Rating', hue='Agent Name', data=df)
    plt.title('Perbandingan Rating Agen di Setiap Lokasi')
    plt.xlabel('Lokasi')
    plt.ylabel('Rating')
    plt.legend(title='Agen', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    st.pyplot(fig)
    st.write('''' Berdasarkan hasil visualisasi di atas, didapatkan bahwa:
- Setiap lokasi memiliki persebaran rating yang relatif sama, yakni rentang 1-5
- Hampir semua agen di setiap lokasi memiliki persebaran rating yang seimbang (ga ada yang terlalu mendominasi).

Hal ini tentunya sesuai dengan hasil uji annova yang mengatakan tidak terdapat perbedaan signifikan pada rating berdasarkan lokasi.''')
    st.write('\n')
    st.write('\n')

    image2 = Image.open("D:\Hacktiv8\Phase 1\Milestone 1\p1-ftds027-hck-m2-MFarhanH\Deployment\Rekomendasi Bisnis.png")
    st.image(
    image2, caption='Uji Hipotesis Annova')

    st.write('# ==== Sekian dan Terimakasih ! ====')
if __name__ == '__main__':
    run()
