# Analisis Sentimen Ulasan Aplikasi Gojek 🛵

Proyek ini adalah implementasi alur kerja *Data Science* *end-to-end* yang berfokus pada analisis sentimen ulasan pengguna aplikasi Gojek di Google Play Store. Proyek ini mengekstraksi ulasan, melakukan pembersihan teks, dan mengklasifikasikan sentimen pengguna ke dalam tiga kategori (Positif, Netral, dan Negatif) menggunakan algoritma **Logistic Regression**.

## 📌 Fitur Utama
1. **Data Scraping**: Pengambilan ulasan terbaru secara otomatis dari halaman Google Play Store.
2. **Text Preprocessing Lengkap**: Pembersihan data (*Case folding*, pembersihan URL/simbol), normalisasi kata gaul/slang Indonesia, tokenisasi, *stopword removal*, dan *stemming* (menggunakan NLTK & Sastrawi).
3. **Exploratory Data Analysis (EDA)**: Visualisasi dengan *WordCloud* dan distribusi proporsi sentimen.
4. **Machine Learning Modeling**: Pembobotan kata menggunakan metode TF-IDF lalu dilatih menggunakan algoritma *Logistic Regression* (Multinomial).
5. **Evaluasi Komprehensif**: Evaluasi metrik akurasi, *Classification Report* (Precision, Recall, F1-Score), kurva ROC-AUC, dan pemetaan kesalahan menggunakan *Confusion Matrix*.
6. **Feature Importance**: Penarikan kata-kata yang paling berpengaruh (*Top 10 Features*) pada masing-masing sentimen.

## 🛠️ Teknologi yang Digunakan
- **Bahasa Pemrograman**: Python
- **Data Manipulation**: Pandas, NumPy
- **Natural Language Processing (NLP)**: NLTK, Sastrawi
- **Machine Learning**: Scikit-Learn
- **Visualisasi**: Matplotlib, Seaborn, WordCloud
- **Environment**: Jupyter Notebook

## 📂 Struktur Direktori
```text
.
├── data/
│   ├── raw/                 # Data ulasan mentah hasil scraping
│   └── processed/           # Data teks bersih hasil tahapan preprocessing
├── Tubes_DIP_LogisticRegression.ipynb  # Kode sumber / Notebook utama 
├── requirements.txt         # Daftar spesifikasi dependensi library Python
└── README.md                # Dokumentasi proyek
```

## 🚀 Cara Menjalankan Proyek Secara Lokal

1. **Clone repository ini**
   ```bash
   git clone https://github.com/username-anda/nama-repo.git
   cd nama-repo
   ```

2. **Buat Virtual Environment (Opsional namun sangat direkomendasikan)**
   ```bash
   python -m venv venv
   venv\Scripts\activate     # Untuk Windows
   # source venv/bin/activate  # Untuk Linux/Mac
   ```

3. **Install Dependensi Library**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan Jupyter Notebook**
   ```bash
   jupyter notebook Tubes_DIP_LogisticRegression.ipynb
   ```

## 📝 Catatan Tambahan
Data yang dihasilkan berupa CSV akan secara otomatis tersimpan di folder `data/raw` dan `data/processed` saat Anda mengeksekusi semua sel (cell) di dalam *notebook*. 

Proyek ini dibuat untuk pemenuhan Tugas Besar. Silakan pelajari dan kembangkan lebih lanjut!
