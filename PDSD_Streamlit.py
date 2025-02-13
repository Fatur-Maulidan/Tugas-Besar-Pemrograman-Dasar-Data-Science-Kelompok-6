import streamlit as st
from streamlit_option_menu import option_menu


with st.sidebar:
    selected = option_menu(
        menu_title = "Biodata",
        options = ["Biodata", "Data Understanding", "Business Understanding", "EDA (Exploratory Data Analysis)", "Result"],
        icons = ["people","database-check","activity","bar-chart"],
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
    st.title('Business Understanding')
    # Business Understanding Code Here
    
elif selected == "EDA (Exploratory Data Analysis)":
    st.title('EDA (Exploratory Data Analysis)')
    # EDA Code Here
    
elif selected == "Result":
    st.title('Result')
    # Result Code Here

