# Bike Sharing Data Analysis

## 📌 Project Overview
Analisis ini bertujuan untuk memahami pola penggunaan layanan berbagi sepeda dengan mempertimbangkan berbagai faktor, termasuk waktu, musim, cuaca, dan jenis pengguna. Dengan dataset ini, kita dapat menjawab pertanyaan utama:

1️⃣ Bagaimana faktor waktu dan musim mempengaruhi permintaan rental sepeda?

2️⃣ Apa perbedaan pola penggunaan antara pengguna kasual dan terdaftar berdasarkan kondisi cuaca?

## 📂 Dataset
Dataset yang digunakan berasal dari **Bike Sharing Dataset**, yang berisi informasi tentang jumlah penyewaan sepeda harian dan jam-jam tertentu dengan berbagai variabel pendukung, termasuk:
- **Datetime Features**: Hari, bulan, musim, dan waktu dalam sehari.
- **Weather Features**: Kondisi cuaca seperti suhu, kelembaban, dan kecepatan angin.
- **User Type**: Perbedaan antara pengguna kasual dan terdaftar.
- **Count**: Jumlah sepeda yang disewa.

## 📁 Project Structure
Struktur folder dalam proyek ini sebagai berikut:
```
Bike-Sharing-Analysis/
├── dashboard/           # Folder untuk dashboard interaktif
│   ├── daily_cleaned.csv   # Data harian yang sudah dibersihkan
│   ├── dashboard.py       # Script untuk menjalankan dashboard
│   └── hourly_cleaned.csv # Data per jam yang sudah dibersihkan
├── dataset/            # Folder dataset mentah
│   ├── day.csv          # Data harian sebelum preprocessing
│   ├── hour.csv         # Data per jam sebelum preprocessing
│   └── Readme.txt       # Deskripsi dataset
├── main.ipynb          # Notebook utama untuk eksplorasi dan analisis
├── README.md           # Dokumentasi proyek
└── requirements.txt     # Daftar dependensi Python
```

## 🔍 Exploratory Data Analysis (EDA)
Sebelum melakukan analisis lebih dalam, dilakukan eksplorasi dataset untuk memahami pola dan distribusi data:
1. **Visualisasi tren penggunaan sepeda berdasarkan waktu** (harian, bulanan, dan musiman).
2. **Analisis hubungan cuaca dan jumlah penyewaan**.
3. **Perbedaan perilaku antara pengguna kasual dan terdaftar**.
4. **Pembersihan data** seperti menangani missing values dan outliers.

## 📊 Data Processing & Feature Engineering
Setelah eksplorasi awal, dilakukan preprocessing untuk memastikan data siap digunakan dalam analisis lebih lanjut:
- **Normalisasi variabel cuaca** agar lebih mudah diinterpretasikan.
- **Ekstraksi fitur waktu** untuk mendapatkan informasi lebih rinci.
- **Encoding variabel kategorikal** untuk memudahkan analisis statistik dan machine learning.

## 📈 Analysis & Insights
Beberapa analisis utama yang dilakukan:
- **Tren musiman**: Bagaimana pola penggunaan berubah dari musim ke musim.
- **Pengaruh jam dalam sehari**: Kapan permintaan rental sepeda paling tinggi.
- **Perbedaan pengguna kasual vs terdaftar**: Siapa yang lebih sering menyewa berdasarkan faktor cuaca dan waktu.

## 📊 Dashboard & Data Visualization
Hasil analisis ditampilkan dalam bentuk visualisasi interaktif menggunakan **Matplotlib, Seaborn, dan Plotly** untuk mempermudah interpretasi:
- **Heatmap korelasi antara variabel**.
- **Time series plot tren penyewaan**.
- **Bar chart perbandingan pengguna kasual dan terdaftar**.
- **Dashboard interaktif** menggunakan **Dash atau Streamlit** untuk memvisualisasikan tren secara real-time dan memungkinkan eksplorasi data berdasarkan filter yang dipilih pengguna. Dashboard ini berjalan melalui `dashboard.py` yang memanfaatkan data dari `daily_cleaned.csv` dan `hourly_cleaned.csv`.

## 🚀 Conclusion
Hasil analisis menunjukkan bahwa:
- Permintaan sepeda meningkat pada musim panas dan menurun saat musim dingin.
- Pengguna kasual lebih sensitif terhadap kondisi cuaca dibanding pengguna terdaftar.
- Jam sibuk terjadi di pagi dan sore hari, terutama untuk pengguna terdaftar yang kemungkinan besar adalah pekerja atau pelajar.

## 🛠️ Tools & Technologies
- **Python** (Pandas, NumPy, Matplotlib, Seaborn, Plotly)
- **Jupyter Notebook** untuk eksplorasi interaktif
- **Scikit-learn** untuk preprocessing dan analisis tambahan
- **Dash/Streamlit** untuk membangun dashboard interaktif

## 📜 How to Use
1. Clone repository ini:  
   ```bash
   git clone https://github.com/notsuperganang/bike-sharing-analysis.git
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan notebook untuk melihat analisis:  
   ```bash
   jupyter notebook
   ```
4. Jalankan dashboard interaktif:  
   ```bash
   streamlit run dashboard/dashboard.py
   ```

## 📌 Future Work
- Membangun model prediktif untuk estimasi jumlah penyewaan.
- Menambahkan data eksternal seperti event atau kebijakan kota.
- Meningkatkan interaktivitas dashboard untuk eksplorasi yang lebih dalam.

---
📧 Jika ada pertanyaan atau saran, silakan hubungi [ganangsetyohadi@gmail.com](mailto:ganangsetyohadi@gmail.com).