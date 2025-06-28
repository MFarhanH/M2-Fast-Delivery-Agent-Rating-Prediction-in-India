# Judul Project
Fast Delivery Agent Rating Prediction in India

## Repository Outline
```
M2-Fast-Delivery-Agent-Rating-Prediction-in-India/
├── P1M2_MuhammadFarhan_Hendriyanto.ipynb
├── P1M2_MuhammadFarhan_Hendriyanto_Inference.ipynb
├── P1M2_MuhammadFarhan_Hendriyanto.txt - menjawab pertanyaan konseptual
├── exploratory_data_analysis.ipynb
├── url.txt
├── README.md
└── Deployment/
    ├── app.py - sebagai main app
    ├── EDA.py - file untuk store eda yang sudah dibuat
    ├── Predict.py - Prediction tab
    ├── randomforest_regression_grid_best.pkl - model terbaik yang sudah didapatkan
    └── Fast Delivery Agent Reviews.csv
```
## Problem Background
Layanan pengiriman cepat di India berkembang pesat dengan persaingan ketat antar perusahaan seperti Zepto, Blinkit, dan JioMart. Dalam industri ini, kepuasan pelanggan menjadi faktor penting yang memengaruhi loyalitas, dan bisa diukur lewat rating, review, dan feedback. Berdasarkan analisis sebelumnya, informasi dari rating yang diberikan pelanggan untuk agent delivery terbukti memberikan insight yang berguna untuk meningkatkan kinerja agen. Maka dari itu, proyek ini bertujuan memprediksi rating pelanggan berdasarkan fitur-fitur yang ada.

## Project Output
Output dari project ini adalah Machine Learning berbasis regresi yang dimana memiliki fungsi untuk memprediksi agent rating dari agent yang ada pada ekosistem jasa delivery di India.

## Data
Dataset yang digunakan dalam analisis ini terdiri dari 5.000 baris dan 12 kolom, yang mencerminkan berbagai aspek layanan pengantaran oleh beberapa agen seperti Zepto dan JioMart. Data ini mencakup informasi mengenai penilaian layanan (rating), ulasan pelanggan (review text), waktu pengantaran, lokasi pemesanan, jenis pesanan, serta berbagai indikator terkait kepuasan pelanggan seperti ketersediaan produk, akurasi pesanan, dan rating layanan pelanggan.

Karakteristik Data:
Jumlah Baris: 5.000
Jumlah Kolom: 12

- Tipe Data: Kombinasi dari numerik (float, int) dan kategori (object)
- Missing Values: Tidak ditemukan nilai yang hilang (non-null count menunjukkan semua data lengkap)
- Kolom Utama:
    - Agent Name: Nama agen layanan (contoh: Zepto, JioMart)
    - Rating: Penilaian pelanggan dalam skala desimal (misal: 4.5)
    - Review Text: Ulasan pelanggan dalam bentuk teks
    - Delivery Time (min): Waktu pengantaran dalam menit
    - Location: Lokasi pelanggan
    - Order Type: Jenis pesanan (misal: Grocery, Essentials, Pharmacy)
    - Customer Feedback Type: Jenis umpan balik (Positive, Neutral, Negative)
    - Price Range: Kategori harga (High/Low)
    - Discount Applied: Apakah diskon diterapkan (Yes/No)
    - Product Availability: Ketersediaan produk (In Stock/Out of Stock)
    - Customer Service Rating: Penilaian untuk layanan pelanggan (skala 1-5)
    - Order Accuracy: Apakah pesanan sesuai (Correct/Incorrect)

Data ini tidak memiliki nilai kosong sehingga siap untuk dilakukan analisis lebih lanjut tanpa perlu penanganan missing values. Struktur data yang lengkap dan beragam memungkinkan eksplorasi mendalam terhadap faktor-faktor yang memengaruhi pengalaman pelanggan dalam layanan pengantaran.

## Method
Project ini menggunakan pendekatan machine learning supervised learning untuk membangun model prediksi performa agen pengiriman berdasarkan rating dari pelanggan. Beberapa algoritma yang digunakan dalam pemodelan antara lain:

- Random Forest Regressor
- Support Vector Regressor (SVR)
- K-Nearest Neighbors (KNN) Regressor
- Decision Tree Regressor
- XGBoost Regressor

Seluruh proses pemodelan dibangun menggunakan pipeline, yang mencakup tahapan preprocessing seperti standarisasi data numerik dan encoding data kategorikal. Evaluasi performa model dilakukan menggunakan teknik cross-validation (CV) serta metrik evaluasi seperti MAE, RMSE, dan R².

Selain itu, dilakukan juga hyperparameter tuning menggunakan GridSearchCV untuk mendapatkan performa model terbaik.

## Stacks
Proyek ini menggunakan Python sebagai bahasa pemrograman utama. Beberapa library dan modul yang digunakan antara lain:
- pandas dan numpy untuk pengolahan data,
- matplotlib dan seaborn untuk visualisasi data,
- scikit-learn untuk proses machine learning seperti preprocessing, pemodelan, evaluasi, dan tuning,
- xgboost untuk algoritma pemodelan tambahan,
- scipy untuk analisis statistik,
- serta pickle untuk menyimpan model.

## Reference
- (https://huggingface.co/spaces/farhanpaul21/tugas) -> link hugging face (deployment)
- (https://www.kaggle.com/datasets/kanakbaghel/indias-fast-delivery-agents-reviews-and-ratings) -> Link dataset