import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
import statsmodels.formula.api as smf
from sklearn.impute import KNNImputer


with st.sidebar:
    selected = option_menu(
        menu_title = "Tubes Pemgrograman Dasar Data Science",
        options = ["Biodata", "Data Understanding", "Business Understanding", "Data Pre-Processing", "EDA (Exploratory Data Analysis)"],
        icons = ["people","database-check","activity", "envelope-arrow-down", "bar-chart"],
        menu_icon = "cast",
        default_index = 0,
    )
    
if selected == "Biodata":
    st.title('Tugas Besar Pemrograman Dasar Sains Data')
    st.write('Kelompok 6')
    anggota = """
    1. 10121018 - Andika Dwi Putra  
    2. 10121025 - Alif Munawar  
    3. 10123200 - Fadhilah Dwi Febrianto  
    4. 10123201 - Muhammad Fauzi Mugni  
    5. 10123912 - Muhammad Rizal Al Multazzam  
    6. 10124907 - M. Fatur Maulidan Azzahra  
    """
    st.write(anggota)
    
elif selected == "Data Understanding":
    st.title('Penjelasan Mengenai Setiap Fitur')
    fitur ="""
        **Year** : Tahun pengukuran kualitas udara, direpresentasikan sebagai bilangan bulat (contoh: 2020, 2021).
        
        **Month** : Bulan pengukuran (1–12), yang menunjukkan bulan dalam setahun.
        
        **Day** : Hari pengukuran (1–31), sesuai dengan tanggal tertentu dalam bulan.
        
        **Hour** : Jam pengukuran (0–23), menunjukkan waktu pengambilan data dalam format 24 jam.
        
        **PM2.5** : Konsentrasi partikel udara halus berukuran ≤2,5 mikrometer dalam udara, diukur dalam mikrogram per meter kubik (µg/m³). Partikel ini berbahaya bagi kesehatan karena dapat masuk jauh ke dalam paru-paru.
        
        **PM10** : Konsentrasi partikel udara kasar berukuran ≤10 mikrometer, diukur dalam µg/m³.
        
        **SO₂ (Sulfur Dioksida)** : Gas polutan yang biasanya berasal dari pembakaran bahan bakar fosil, diukur dalam µg/m³.
        
        **NO₂ (Nitrogen Dioksida)** : Polutan gas yang dihasilkan oleh kendaraan bermotor dan pembakaran industri, diukur dalam µg/m³.
        
        **CO (Karbon Monoksida)** : Gas tidak berwarna dan tidak berbau yang dihasilkan dari pembakaran tidak sempurna, diukur dalam µg/m³.
        
        **O₃ (Ozon)** : Gas ozon di udara, yang berperan dalam kualitas udara dan tingkat polusi, diukur dalam µg/m³.
        
        **TEMP (Temperature)** : Suhu udara di lokasi pengukuran, diukur dalam derajat Celsius (°C).
        
        **PRES (Pressure)** : Tekanan atmosfer pada lokasi pengukuran, diukur dalam hektopascal (hPa).
        
        **DEWP (Dew Point)** : Titik embun, yaitu suhu di mana udara menjadi jenuh dengan uap air, diukur dalam derajat Celsius (°C).
        
        **RAIN (Rainfall)** : Curah hujan pada saat pengukuran, diukur dalam milimeter (mm).
        
        **WD (Wind Direction)** : Arah angin saat pengukuran, biasanya dinyatakan dalam arah kardinal (seperti N, NE, E, dsb.).
        
        **WSPM (Wind Speed)•• : Kecepatan angin pada lokasi pengukuran, diukur dalam meter per detik (m/s).
        
        **Station** : Nama atau kode stasiun pengukuran yang mengidentifikasi lokasi data diambil.
    """
    st.write(fitur)
    
elif selected == "Business Understanding":
    st.title('Pertanyaan yang akan dijawab oleh analisis dari hasil di result')
    pertanyaan = """
    - Bagaimana perbandingan rata-rata tingkat polutan PM2.5 dan PM10 di setiap stasiun? - 10121018 - Andika Dwi Putra

    - Bagaimana distribusi polutan NO2 dalam sehari di setiap stasiun? - 10121025 - Alif Munawar

    - Bagaimana Polutan CO pada setiap stasiun yang ada, dan faktor apa yang mungkin memengaruhi stasiun tersebut bisa memiliki polutan CO yang sangat besar? - 10124907 - M. Fatur Maulidan Azzahra

    - Bagaimana Pertumbuhan gas Ozon dari Tahun 2013 - 2017? - 10123200 - Fadhilah Dwi Febrianto

    - Bagaimana pengaruh suhu udara (TEMP) terhadap konsentrasi PM2.5 di setiap stasiun pengukuran udara? - 10123912 - Muhammad Rizal Al Multazzam

    - Bagaimana variasi harian CO dibandingkan dengan polutan lainnya - 10123201 - M. Fauzi Mugni
    """
    st.write(pertanyaan)
    
elif selected == "Data Pre-Processing":
    st.title('Data Pre-Processing')
    # Result Code Here
    
    st.subheader('Package dan Library yang digunakan')
    with st.echo():
        import numpy as np
        import pandas as pd
        import os
        import matplotlib.pyplot as plt
        import seaborn as sns
        from scipy.stats import zscore
        import statsmodels.formula.api as smf
        from sklearn.impute import KNNImputer
        
        
    st.subheader('Data Gathering')
    with st.echo():
        file_paths = [
            "PRSA_Data_Aotizhongxin_20130301-20170228.csv",
            "PRSA_Data_Changping_20130301-20170228.csv",
            "PRSA_Data_Dingling_20130301-20170228.csv",
            "PRSA_Data_Dongsi_20130301-20170228.csv",
            "PRSA_Data_Guanyuan_20130301-20170228.csv",
            "PRSA_Data_Gucheng_20130301-20170228.csv",
            "PRSA_Data_Huairou_20130301-20170228.csv",
            "PRSA_Data_Nongzhanguan_20130301-20170228.csv",
            "PRSA_Data_Shunyi_20130301-20170228.csv",
            "PRSA_Data_Tiantan_20130301-20170228.csv",
            "PRSA_Data_Wanliu_20130301-20170228.csv",
            "PRSA_Data_Wanshouxigong_20130301-20170228.csv"
        ]
        
    file_paths = [
        "PRSA_Data_20130301-20170228/PRSA_Data_Aotizhongxin_20130301-20170228.csv",
        "PRSA_Data_20130301-20170228/PRSA_Data_Changping_20130301-20170228.csv",
        "PRSA_Data_20130301-20170228/PRSA_Data_Dingling_20130301-20170228.csv",
        "PRSA_Data_20130301-20170228/PRSA_Data_Dongsi_20130301-20170228.csv",
        "PRSA_Data_20130301-20170228/PRSA_Data_Guanyuan_20130301-20170228.csv",
        "PRSA_Data_20130301-20170228/PRSA_Data_Gucheng_20130301-20170228.csv",
        "PRSA_Data_20130301-20170228/PRSA_Data_Huairou_20130301-20170228.csv",
        "PRSA_Data_20130301-20170228/PRSA_Data_Nongzhanguan_20130301-20170228.csv",
        "PRSA_Data_20130301-20170228/PRSA_Data_Shunyi_20130301-20170228.csv",
        "PRSA_Data_20130301-20170228/PRSA_Data_Tiantan_20130301-20170228.csv",
        "PRSA_Data_20130301-20170228/PRSA_Data_Wanliu_20130301-20170228.csv",
        "PRSA_Data_20130301-20170228/PRSA_Data_Wanshouxigong_20130301-20170228.csv"
    ]

    with st.echo():
        dfs = {}
        # Membaca semua file dan menyimpannya dalam dictionary
        for file in file_paths:
            dfs[file] = pd.read_csv(file)


        # Menampilkan beberapa baris pertama dari setiap dataframe
        for name, df in dfs.items():
            print(f"\nData dari: {name}")
            print(df)
            print("\n" + "-"*50 + "\n")
    
    # Membaca semua file dan menyimpannya dalam dictionary
    dfs = {}
    for file in file_paths:
        dfs[file] = pd.read_csv(file)


    # Menampilkan beberapa baris pertama dari setiap dataframe
    for name, df in dfs.items():
        print(f"\nData dari: {name}")
        print(df.head())
        print("\n" + "-"*50 + "\n")
        st.write(f"\nData dari: {name}")
        st.write(df.head())
        st.write("\n" + "-"*50 + "\n")
        

    st.subheader('Data Cleaning (Check Missing Value)')
    with st.echo():
        for file in file_paths:
            # Memeriksa Missing Value dari setiap dataset
            try:
                df = pd.read_csv(file)
                missing_values = df.isnull().sum()
                print(f"Missing values in {file}:")
                print(missing_values)
                print("-" * 40)
                st.write(f"Missing values in {file}:")
                st.write(missing_values)
                st.write("-" * 40)
            except Exception as e:
                print(f"Error processing {file}: {e}")
                
    for file in file_paths:
        # Memeriksa Missing Value dari setiap dataset
        try:
            df = pd.read_csv(file)
            missing_values = df.isnull().sum()
            print(f"Missing values in {file}:")
            print(missing_values)
            print("-" * 40)
            st.write(f"Missing values in {file}:")
            st.write(missing_values)
            st.write("-" * 40)
        except Exception as e:
            print(f"Error processing {file}: {e}")
        
    # st.subheader('Data Cleaning (Handle Missing Values)')
    # with st.echo():
    #     # Folder tempat menyimpan hasil
    #     output_folder = "processed_files"
    #     os.makedirs(output_folder, exist_ok=True)
            
    #     # Loop untuk memproses setiap file
    #     for file in file_paths:
    #         file_path = f"{file}"
    #         folder, filename = os.path.split(file_path)

    #         try:
    #             # Load dataset
    #             df = pd.read_csv(file_path)

    #             # Konversi kolom waktu menjadi format datetime
    #             df['datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])

    #             # Hapus kolom year, month, day, hour karena sudah tergabung dalam datetime
    #             df = df.drop(columns=['year', 'month', 'day', 'hour'])

    #             # Set datetime sebagai index untuk interpolasi time series
    #             df = df.set_index('datetime')

    #             # 1. Mengisi kolom dengan missing value 1-3% menggunakan interpolasi berbasis waktu
    #             columns_interpolation = ["PM2.5", "PM10", "SO2", "O3","TEMP", "PRES", "DEWP", "RAIN", "WSPM"]
    #             df[columns_interpolation] = df[columns_interpolation].interpolate(method="time")

    #             # 2. Mengisi kolom dengan missing value >3% menggunakan KNN Imputer
    #             columns_knn_impute = ["CO", "NO2"]
    #             imputer = KNNImputer(n_neighbors=5)
    #             df[columns_knn_impute] = imputer.fit_transform(df[columns_knn_impute])

    #             # 3. Mengisi kolom kategorikal "wd" dengan mode (nilai yang paling sering muncul)
    #             df['wd'] = df['wd'].fillna(df['wd'].mode()[0])

    #             # Reset index kembali ke format semula
    #             df = df.reset_index()

    #             # Simpan hasil dengan nama baru
    #             output_file_path = os.path.join(output_folder, f"processed_{filename}")
    #             df.to_csv(output_file_path, index=False)
    #             print(f"Processed and saved: {output_file_path}")

    #         except Exception as e:
    #             print(f"Error processing {file}: {e}")

    #     print("Semua file telah diproses dan disimpan di folder processed_files.")
        
    # # Folder tempat menyimpan hasil
    # output_folder = "processed_files"
    # os.makedirs(output_folder, exist_ok=True)
    
    # # Loop untuk memproses setiap file
    # for file in file_paths:
    #     file_path = f"{file}"
    #     folder, filename = os.path.split(file_path)

    #     try:
    #         # Load dataset
    #         df = pd.read_csv(file_path)

    #         # Konversi kolom waktu menjadi format datetime
    #         df['datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])

    #         # Hapus kolom year, month, day, hour karena sudah tergabung dalam datetime
    #         df = df.drop(columns=['year', 'month', 'day', 'hour'])

    #         # Set datetime sebagai index untuk interpolasi time series
    #         df = df.set_index('datetime')

    #         # 1. Mengisi kolom dengan missing value 1-3% menggunakan interpolasi berbasis waktu
    #         columns_interpolation = ["PM2.5", "PM10", "SO2", "O3","TEMP", "PRES", "DEWP", "RAIN", "WSPM"]
    #         df[columns_interpolation] = df[columns_interpolation].interpolate(method="time")

    #         # 2. Mengisi kolom dengan missing value >3% menggunakan KNN Imputer
    #         columns_knn_impute = ["CO", "NO2"]
    #         imputer = KNNImputer(n_neighbors=5)
    #         df[columns_knn_impute] = imputer.fit_transform(df[columns_knn_impute])

    #         # 3. Mengisi kolom kategorikal "wd" dengan mode (nilai yang paling sering muncul)
    #         df['wd'] = df['wd'].fillna(df['wd'].mode()[0])

    #         # Reset index kembali ke format semula
    #         df = df.reset_index()

    #         # Simpan hasil dengan nama baru
    #         output_file_path = os.path.join(output_folder, f"processed_{filename}")
    #         df.to_csv(output_file_path, index=False)
    #         print(f"Processed and saved: {output_file_path}")

    #     except Exception as e:
    #         print(f"Error processing {file}: {e}")

    # print("Semua file telah diproses dan disimpan di folder processed_files.")
    
    
    with st.echo():
        folder_path = "processed_files/"  # Ganti dengan path folder yang sesuai
        # Variabel diatas adalah Folder yang berisi file CSV

        # Mengambil semua file CSV dalam folder
        csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

        # Membaca dan menggabungkan semua file CSV menjadi satu DataFrame
        combined_df = pd.concat([pd.read_csv(os.path.join(folder_path, file)) for file in csv_files], ignore_index=True)

        # Menampilkan beberapa data awal
        combined_df
    
    folder_path = "processed_files/"  # Ganti dengan path folder yang sesuai
    # Variabel diatas adalah Folder yang berisi file CSV

    # Mengambil semua file CSV dalam folder
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

    # Membaca dan menggabungkan semua file CSV menjadi satu DataFrame
    combined_df = pd.concat([pd.read_csv(os.path.join(folder_path, file)) for file in csv_files], ignore_index=True)

    # Menampilkan beberapa data awal
    combined_df
    
    with st.echo():
        combined_df.isnull().sum()
        
    combined_df.isnull().sum()
    
    st.subheader('Menangani Outlier')
    with st.echo():
        # Daftar kolom numerik
        numeric_cols = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3", "RAIN", "WSPM"]

        # Menghitung Z-score
        df_zscore = combined_df[numeric_cols].apply(zscore)

        # Menentukan threshold untuk outlier
        threshold = 3

        # Menampilkan jumlah outlier per kolom
        outliers_count = (np.abs(df_zscore) > threshold).sum()
        print("Jumlah Outlier per Kolom:")
        print(outliers_count)
        
    # Daftar kolom numerik
    numeric_cols = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3", "RAIN", "WSPM"]

    # Menghitung Z-score
    df_zscore = combined_df[numeric_cols].apply(zscore)

    # Menentukan threshold untuk outlier
    threshold = 3

    # Menampilkan jumlah outlier per kolom
    outliers_count = (np.abs(df_zscore) > threshold).sum()
    print("Jumlah Outlier per Kolom:")
    print(outliers_count)
    
    with st.echo():
        # Membuang outlier
        df_cleaned = combined_df[(np.abs(df_zscore) < threshold).all(axis=1)]

        # Menampilkan jumlah data sebelum dan sesudah pembersihan
        print(f"Jumlah data sebelum pembersihan: {len(combined_df)}")
        print(f"Jumlah data setelah pembersihan: {len(df_cleaned)}")
    
    st.write(f"Jumlah data sebelum pembersihan: {len(combined_df)}")
    st.write(f"Jumlah data setelah pembersihan: {len(df_cleaned)}")
    
    # Menyaring data dengan membuang outlier
    df_cleaned = combined_df[(np.abs(df_zscore) < threshold).all(axis=1)]

    # Menampilkan jumlah data sebelum dan sesudah pembersihan
    print(f"Jumlah data sebelum pembersihan: {len(combined_df)}")
    print(f"Jumlah data setelah pembersihan: {len(df_cleaned)}")
    
    with st.echo():
        df_cleaned.describe()
    
    df_cleaned.describe()
    
    df_cleaned.to_csv("df_cleaned_temp.csv", index=False)
    combined_df.to_csv("combined_df_temp.csv", index=False)
    
elif selected == "EDA (Exploratory Data Analysis)":
    st.title('EDA (Exploratory Data Analysis)')
    # Membuat fungsi untuk menentukan kategori kualitas udara berdasarkan nilai PM2.5
    try:
        df_cleaned = pd.read_csv("df_cleaned_temp.csv")
    except FileNotFoundError:
        st.write("File belum tersedia. Silakan jalankan Data Pre-Processing terlebih dahulu.")
        
    try:
        combined_df = pd.read_csv("combined_df_temp.csv")
    except FileNotFoundError:
        st.write("File belum tersedia. Silakan jalankan Data Pre-Processing terlebih dahulu.")
        
        
    def kategori_kualitasudara(pm25):
        if pm25 <= 12:
            return 'Baik'
        elif 12 < pm25 <= 35.4:
            return 'Sedang'
        elif 35.4 < pm25 <= 55.4:
            return 'Tidak sehat bagi kelompok sensitif'
        elif 55.4 < pm25 <= 150.4:
            return 'Tidak sehat'
        elif 150.4 < pm25 <= 250.4:
            return 'Sangat tidak sehat'
        else:
            return 'Berbahaya'

    # Menambahkan kolom indeks kualitas udara
    df_cleaned['Level_AQI'] = df_cleaned['PM2.5'].apply(kategori_kualitasudara)
    df_cleaned
    
    st.write(df_cleaned)
    
    # 2. Visualisasi distribusi data numerik
    # Pastikan DataFrame `combined_df` sudah tersedia
    st.title("Visualisasi distribusi data numerik")

    # Daftar kolom numerik
    numeric_cols = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3", "RAIN", "WSPM"]

    # Membuat plot dalam Streamlit
    fig, axes = plt.subplots(3, 3, figsize=(15, 10))

    for i, col in enumerate(numeric_cols):
        row = i // 3
        col_index = i % 3
        sns.histplot(combined_df[col], bins=30, kde=True, ax=axes[row, col_index])
        axes[row, col_index].set_title(f'Distribusi {col}')

    plt.tight_layout()
    st.pyplot(fig)


    st.title("Matriks Korelasi")
    # 3. Korelasi antar fitur numerik    
    # Membuat figure dan plot heatmap
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df_cleaned[numeric_cols].corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
    ax.set_title('Matriks Korelasi')
    # Menampilkan plot di Streamlit
    st.pyplot(fig)
    
    # 5. Tren data waktu untuk PM2.5
    # Pastikan dataframe `df_cleaned` sudah tersedia
    st.title("Tren PM2.5 per Bulan")

    # Mengecek apakah kolom 'datetime' ada dalam dataset
    if 'datetime' in df_cleaned.columns:
        df_cleaned['datetime'] = pd.to_datetime(df_cleaned['datetime'])
        df_cleaned = df_cleaned.set_index('datetime')

        # Membuat figure untuk Streamlit
        fig, ax = plt.subplots(figsize=(12, 6))
        df_cleaned['PM2.5'].resample('M').mean().plot(ax=ax)

        # Menyesuaikan tampilan plot
        ax.set_title('Tren PM2.5 per Bulan')
        ax.set_xlabel('Tanggal')
        ax.set_ylabel('PM2.5')

        # Menampilkan plot di Streamlit
        st.pyplot(fig)

    else:
        st.warning("Kolom 'datetime' tidak ditemukan dalam dataset.")
        
    
    # 6. Visualisasi kualitas udara berdasarkan PM2.5
    # Judul aplikasi Streamlit
    st.title("Variasi Harian CO Dibandingkan dengan Polutan Lainnya")

    available_cols = ['CO', 'NO2', 'SO2', 'O3']
    df_cleaned = df_cleaned.reset_index()
    daily_avg = df_cleaned[available_cols + ['datetime']].resample('D', on='datetime').mean()
    
    if not daily_avg.empty:
        fig, ax = plt.subplots(figsize=(12, 6))
        
        for col, color in zip(available_cols, ['red', 'blue', 'green', 'purple']):
            sns.lineplot(data=daily_avg, x=daily_avg.index, y=col, label=col, color=color, ax=ax)
        
        ax.set_xlabel('Tanggal')
        ax.set_ylabel('Konsentrasi (µg/m³)')
        ax.set_title('Variasi Harian CO Dibandingkan dengan Polutan Lainnya')
        ax.legend()
        plt.xticks(rotation=45)
        
        st.pyplot(fig)
    else:
        st.warning("daily_avg kosong setelah resampling, periksa kembali dataset.")



