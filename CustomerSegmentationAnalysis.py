import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import plotly.express as px
#=======================================================
df = pd.read_csv("Dataset/Segmentasi Customer Analysis.csv")

#-------------------------------------------------------
st.header("Fauzan Ikhsan Badri")
st.subheader("Data Enthusiast | Data Analyst in Progress")
st.write("Saya memiliki ketertarikan pada bidang Data Analysis dan Machine Learning, khususnya dalam memahami perilaku pelanggan melalui metode seperti RFM (Recency, Frequency, Monetary) Analysis. "
         "Proyek ini merupakan implementasi sederhana segmentasi pelanggan untuk memberikan gambaran bagaimana data dapat digunakan dalam mendukung strategi bisnis. ")
st.markdown("📧 **Email:** fauzanikhsanbadri@gmail.com") 

#Judul
st.title('Analisis Segmentasi Toko Super Store')

#h2 Pendahuluan
st.header('Pendahuluan')
st.write(" Dalam dunia bisnis, tidak semua pelanggan memiliki perilaku belanja yang sama. "
         "Beberapa pelanggan belanja secara rutin dan memberikan profit besar, sementara yang lain hanya belanja sekali lalu tidak kembali."
         "Oleh karena itu, penting bagi perusahaan untuk melakukan segmentasi pelanggan agar dapat menerapkan strategi yang tepat untuk setiap jenis pelanggan."
         "Pada proyek ini, analisis segmentasi dilakukan dengan metode RFM (Recency, Frequency, Monetary) menggunakan data transaksi dari dataset Superstore."
         "Hasil dari segmentasi ini akan digunakan untuk memberikan rekomendasi strategi bisnis yang lebih terarah dan efisien.")

#h2 Data Understanding
st.header("Data Understanding")
st.image("https://images.unsplash.com/photo-1604066867775-43f48e3957d8?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
         caption="Super Store",
         use_container_width=True
         )
st.dataframe(df)
st.write("Dataset yang digunakan dalam analisis ini adalah Superstore, yang berisi data transaksi pelanggan dengan total 9.994 baris data pada periode 2014 hingga 2017."
         "Untuk keperluan exploratory data analysis (EDA) dan segmentasi pelanggan.")
st.markdown("###### kolom utama yang digunakan antara lain :")
st.markdown("""
- Customer ID: Identitas unik setiap pelanggan. Digunakan untuk mengelompokkan transaksi dan menghitung metrik individu.
- Order Date: Tanggal pelanggan melakukan transaksi. Digunakan untuk menghitung nilai Recency.
- Profit: Keuntungan yang dihasilkan dari setiap transaksi. Digunakan untuk menghitung nilai Monetary.
            """)

#h2 Metodologi
st.header("Metologi – RFM (RECENCY, FREQUENCY, MONETARY)")
st.write("Untuk mengelompokkan pelanggan berdasarkan perilaku belanja, saya menggunakan metode RFM (Recency, Frequency, Monetary)."
         "RFM adalah metode yang umum digunakan dalam customer segmentation, karena "
         "mampu mengukur seberapa baru, sering, dan besar nilai transaksi pelanggan.")
proses_scoring = {
    "Komponen" : ["Recency", "Frequency", "Monetary"],
    "Definisi" : ["Seberapa baru pelanggan terakhir kali melakukan pembelian",
                  "Seberapa sering pelanggan melakukan transaksi",
                  "Seberapa banyak nilai uang (dalam hal ini profit) yang dibelanjakan"]
}
proses_scoring = pd.DataFrame(proses_scoring)
st.table(proses_scoring)

st.write("###### Proses Scoring")
st.write("Setiap pelanggan diberi skor RFM dari 1–3, berdasarkan kuartil distribusi data."
         "tinggi skor → semakin baik perilaku belanjanya.")
st.markdown("###### Contoh :")
st.markdown("""
            - Skor 3 untuk pelanggan dengan Recency pendek, Frequency tinggi, dan Monetary besar.
            - Skor 1 untuk pelanggan yang jarang dan kecil nilai belanjanya.
            """)

#h2 Proses Logika
st.header("Proses Segmentasi & Logika Kustom")
st.write("Segmentasi pelanggan tidak hanya dilakukan berdasarkan total skor RFM (3–9), tapi juga berdasarkan pola kombinasi individual R, F, dan M."
         "Beberapa pelanggan memiliki karakteristik unik yang penting untuk diperhatikan,")
st.markdown("###### misalnya :")
st.markdown("""
- Best Spending: Pelanggan dengan nilai Monetary tinggi, tapi hanya sekali
belanja. Ini bisa jadi peluang jika mereka diberikan pengalaman belanja yang
lebih baik.
- Potential Loyalist: Pelanggan yang mulai rutin berbelanja (F tinggi), meskipun nilai transaksi belum besar.
""")
st.write("Strategi ini membantu perusahaan untuk tidak mengabaikan peluang tersembunyi dari pola transaksi yang tidak konvensional.")
st.subheader("Super Store Dataset")
filtered_df = df[df["Customer Segment"] == "Big Spenders"]
st.dataframe(filtered_df[["RFM Class", "RFM Score", "Customer Segment"]])
st.write("Dataset diatas pada kolom ‘RFM CLass’ meliki skor R=1,F=1,M=3. dari sini kita tahu bahwa ada kemungkinan pelanggan mendapat "
         "pengalaman buruk ketika berbelanja sehingga tidak melakukan pembelian ulang. tapi dengan perbaikan sedikit customer seperti ini menjadi "
         "potential Loyal ataupun Best Customer")

#h2 Visualisasi Segmentasi Pelanggan
st.header("Visualisasi Segmentasi Pelanggan")
st.write("Dashboard berikut menampilkan hasil segmentasi pelanggan berdasarkan analisis RFM."
         "Visualisasi dibuat menggunakan Power BI untuk memudahkan pemahaman distribusi dan karakteristik setiap segmen pelanggan."
         )
segment_counts = df["Customer Segment"].value_counts()
fig = px.pie(
    df,
    names="Customer Segment",
    title="Proporsi Customer Berdasarkan Segmentasi",
    hole=0
)
st.plotly_chart(fig, use_container_width=True)

#h2 Insight Pelanggan Berdasarkan Segmentasi RFM
st.header("Insight Pelanggan Berdasarkan Segmentasi RFM")
st.markdown("###### 🟢 Best Customer (R:3, F:3, M:3)")
st.write("Pelanggan terbaik yang sudah loyal dan royal — mereka sering berbelanja, baru saja melakukan pembelian, dan selalu mengeluarkan uang besar.")
st.markdown("###### Strategi :")
st.markdown("""
- Berikan pengalaman eksklusif (early
access, preview produk baru)
- Gunakan promo yang tidak terdengar
“murahan”
- Kirimkan ucapan terima kasih
personal atau loyalty reward
""")
#----------------------------
st.markdown("###### 🔵 Loyal Customer (R:3, F:2)")
st.write("Pelanggan yang sering kembali dan baru saja bertransaksi, namun nilai pembelian mereka belum terlalu besar.")
st.markdown("###### Strategi :")
st.markdown("""
- Gunakan promo bertingkat seperti
beli 3 gratis 1
- Upsell produk bernilai lebih tinggi
- Tawarkan bundling hemat agar
mereka belanja lebih besar
""")
#-----------------------------
st.markdown("###### 🔴 At Risk (R:1, F:3)")
st.write("Pelanggan yang dulu sering belanja tapi sudah lama tidak kembali. Bisa jadi karena hilang trust atau pindah ke kompetitor.")
st.markdown("###### Strategi :")
st.markdown("""
- Buat program reaktivasi, seperti
Kartu Member Baru
- Kirim penawaran “Kami Merindukan
Anda”
- Tambahkan insentif agar mereka
kembali (diskon personal, cashback)
""")
#----------------------------
st.markdown("###### 🟠 Big Spender (M:3)")
st.write("Pelanggan yang melakukan pembelian dengan nilai tinggi, meskipun tidak sering atau tidak baru-baru ini.")
st.markdown("###### Strategi :")
st.markdown("""
- Prioritaskan kualitas pengalaman
belanja
- Tawarkan membership dengan benefit
eksklusif
- Arahkan ke produk premium dengan
layanan personal
""")
#----------------------------
st.markdown("⚪ Cold Customer (R:1, F:1, M:1)")
st.write("Pelanggan yang sudah lama tidak berbelanja, hanya pernah satu kali, dan dengan nilai kecil. Mereka kemungkinan tidak akan kembali.")
st.markdown("###### Strategi :")
st.markdown("""
- Jangan jadi fokus utama campaign
- Namun bisa dimasukkan dalam promo
massal seperti “comeback offer”
- Anggap mereka seperti “pelanggan
lewat” (low priority)
""")
#---------------------------
st.markdown("🟡 Potential Customer (Total Score ≥ 4)")
st.write("Pelanggan dengan skor kombinasi menengah. Belum bisa disebut loyal, tapi punya potensi jika didekati dengan strategi yang tepat.")
st.markdown("###### Strategi :")
st.markdown("""
- Campaign kartu member & pengalaman
belanja lebih nyaman
- Kirim promo terpersonalisasi
- Dorong engagement via email atau
media sosial
""")

st.write("💡 Catatan Umum:")
st.write(" ini tidak hanya berdasarkan total skor RFM, tetapi juga kombinasi nilai individu dari Recency, Frequency, dan Monetary untuk menangkap nuansa perilaku"
         "pelanggan yang lebih akurat.")

#h2 Kesimpulan
st.header("Kesimpulan & Rekomendasi Strategi")
st.write("Kesimpulan Utama dari Segmentasi")
st.markdown("###### Dari total 793 pelanggan:")
st.markdown("""
            - 44.5% adalah Potential Customer
            - 27.3% adalah Loyal Customer
            - Sisanya terbagi di Cold, At Risk, Big Spender, dan Best Customer""")
st.markdown("Artinya, kita punya fondasi kuat untuk tumbuh jika bisa:")
st.markdown("""
            - Menjaga pelanggan loyal
            - Mengubah potential menjadi loyal/best""")

#h2 Strategi Fokus
st.header("🧠 Strategi Fokus:")

st.header("🎯 1. Fokus Utama: Potential Customer")
st.write("Mereka masih “menggantung”, tapi punya potensi besar jadi pelanggan loyal.")
st.markdown("###### Aksi :")
st.markdown("""
            - Bangun aplikasi mobile → supaya kita selalu dekat (HP = device paling personal)
            - Branding sebagai “Member”, bukan cuma “pelanggan”
            - Kirim notifikasi promo, event, loyalty point langsung ke HP Kembangkan koneksi emosional dan kemudahan akses
            """)
st.write("💬 'Kita tidak menjual barang, kita membangun hubungan.'")

st.header("💜 2. Loyal Customer: Dorong jadi Best")
st.markdown("###### Aksi:")
st.markdown("""
- Gunakan promo bertingkat:
- Contoh: “Belanja min. 100 ribu = Tebus Murah produk eksklusif”
- Buat kelas loyalitas:
- Silver → Gold → Platinum → Diamond
- Berdasarkan total akumulasi belanja
- Hadiah loyalitas tahunan, ucapan ulang tahun, atau benefit privat
            """)

st.header("🧊 3. Cold & At Risk: Jangan Fokus Terlalu Besa")
st.markdown("###### Aksi:")
st.markdown("""
- Masukkan ke promo massal (broadcast)
- Kirim “Kami Rindu Anda” campaign (sekali-sekali)
- Jangan alokasikan banyak anggaran
            """)

st.header("💰 4. Big Spenders : Bangun Kembali Hubungan")
st.markdown("###### Aksi:")
st.markdown("""
- Kirim undangan spesial member (karena mereka pernah belanja besar)
- Buat mereka merasa eksklusif, bukan cuma pembeli satu kali
- Tawarkan reward untuk kembali berbelanja
            """)

st.header("🏁 Penutup:")
st.write("Dengan strategi ini, bisnis bisa menumbuhkan pelanggan berkualitas tinggi, "
         "mempertahankan yang terbaik, dan membangun loyalitas jangka panjang melalui "
         "pendekatan personal & digital.")