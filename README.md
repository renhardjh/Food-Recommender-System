# Food Recommender System

## Latar Belakang

Dalam era modern, dimana kita memiliki akses yang melimpah terhadap berbagai jenis makanan dan minuman, serta kebutuhan yang semakin kompleks seperti diet khusus, preferensi pribadi, dan kondisi kesehatan, penting bagi kita untuk memiliki panduan yang akurat dan personal dalam memilih makanan yang tepat. Ketika datang ke berbagai resto tempat makan, preferensi dan kebutuhan tiap individu sangat beragam. Beberapa orang mungkin memiliki preferensi vegetarian atau vegan, sedangkan yang lain mungkin memiliki preferensi terhadap makanan tertentu seperti makanan Asia, makanan organik, atau makanan tanpa gluten. Selain itu, kondisi kesehatan seperti alergi makanan, intoleransi, atau penyakit tertentu juga dapat mempengaruhi pilihan makanan seseorang.

Dalam konteks ini, Sistem Rekomendasi Makanan menjadi penting karena dapat membantu pengguna dalam menavigasi pilihan makanan yang luas dan memilih makanan yang sesuai dengan preferensi dan kebutuhan tiap individu. "Pendekatan rekomendasi berbasis konten dalam domain makanan berfokus pada analisis karakteristik item makanan seperti bahan, rasa, dan informasi nutrisi untuk menghasilkan rekomendasi personal untuk pengguna" (Almahmeed & Alshammari, 2016). Sistem ini dapat menghemat waktu dan usaha pengguna dalam mencari dan memilih makanan yang cocok, serta meningkatkan kepuasan dan kualitas pengalaman kuliner mereka.

## Business Understanding

Dalam industri makanan, pengguna seringkali dihadapkan pada banyak pilihan makanan yang tersedia. Namun, pengguna dapat mengalami kesulitan dalam memilih makanan yang sesuai dengan preferensi dan kebutuhan mereka. Oleh karena itu, pengembangan Sistem Rekomendasi Makanan dapat membantu pengguna dalam menemukan makanan yang sesuai dengan preferensi mereka. Pemahaman bisnis ini untuk mengembangkan sebuah Sistem Rekomendasi Makanan yang dapat memberikan rekomendasi makanan yang personal dan relevan kepada pengguna. Sistem ini akan menggunakan teknik-teknik seperti filtrasi kolaboratif, filtrasi berbasis konten, atau kombinasi dari keduanya untuk menghasilkan rekomendasi yang akurat dan memuaskan.

Sistem rekomendasi ini juga memiliki manfaat bisnis seperti meningkatkan pengalaman pengguna, dengan adanya sistem rekomendasi, pengguna dapat dengan mudah menemukan makanan yang cocok dengan preferensi mereka, meningkatkan kepuasan dan pengalaman pengguna. Meningkatkan penjualan dan retensi pelanggan, dengan memberikan rekomendasi yang relevan, sistem ini dapat membantu meningkatkan penjualan makanan dan mempertahankan pelanggan yang loyal. Meningkatkan efisiensi operasional,ndengan memanfaatkan teknologi otomatisasi dalam sistem rekomendasi, proses pengambilan keputusan makanan dapat ditingkatkan, sehingga mengurangi waktu yang dihabiskan dalam pencarian makanan.

Pengguna utama sistem ini adalah konsumen atau pengguna akhir yang mencari rekomendasi makanan. Stakeholder lainnya termasuk pemilik bisnis makanan, penyedia layanan makanan, dan pemasar makanan yang ingin mempromosikan produk mereka. Dengan pemahaman bisnis yang jelas, pengembangan Sistem Rekomendasi Makanan dapat difokuskan pada mencapai tujuan bisnis yang telah ditetapkan dan memberikan manfaat yang signifikan bagi pengguna dan stakeholder terkait.

### Problem Statement and Goals

Berdasarkan kondisi yang telah diuraikan sebelumnya, sistem rekomendasi makanan ini dibuat untuk menjawab permasalahan berikut:
1. Bagaimana cara mengatasi kesulitan pengguna dalam memilih makanan yang sesuai dengan preferensi dan kebutuhan mereka di tengah banyaknya pilihan yang tersedia?
2. Bagaimana caranya meningkatkan pengalaman pengguna dalam menemukan makanan yang sesuai dengan preferensi mereka?
3. Bagaimana pemilik bisnis makanan dapat mempromosikan produk mereka kepada target pasar yang tepat secara efektif?

Serta untuk menjawab pertanyaan tersebut, sistem rekomendasi makanan ini dibuat dengan tujuan atau goals sebagai berikut:

1. Mengembangkan Sistem Rekomendasi Makanan yang dapat memberikan rekomendasi makanan yang personal dan relevan kepada pengguna.
2. Meningkatkan pengalaman pengguna dalam menemukan makanan yang sesuai dengan preferensi mereka.
3. Membantu pemilik bisnis makanan untuk mempromosikan produk mereka kepada target pasar yang tepat.

### Solution Statement

Untuk mencapai tujuan tersebut, kami mengajukan dua pendekatan solusi menggunakan metode _content-based filtering_ dengan menggunakan _cosine similarity_ dan _jaccard similarity_ dengan pertimbangan sebagai berikut:

1. _Content-Based Filtering_ dengan Metode _Cosine Similarity_:
   - Pendekatan ini akan menggunakan analisis konten dari makanan, seperti deskripsi, bahan, dan karakteristik lainnya, untuk membangun profil preferensi pengguna.
   - Metode _cosine similarity_ akan digunakan untuk mengukur sejauh mana kesamaan antara makanan yang ada dalam dataset dengan preferensi pengguna.
   - Dengan membandingkan preferensi pengguna dengan makanan yang ada, sistem akan memberikan rekomendasi makanan yang memiliki kesamaan konten tertinggi.

2. _Content-Based Filtering_ dengan Metode _Jaccard Similarity_:
   - Pendekatan ini juga akan menggunakan analisis konten makanan untuk membangun profil preferensi pengguna.
   - Metode _jaccard similarity_ akan digunakan untuk mengukur kesamaan antara himpunan kata-kata kunci dalam deskripsi makanan dengan preferensi pengguna.
   - Dengan menggunakan metode ini, sistem akan memberikan rekomendasi makanan yang memiliki kesamaan kata-kunci tertinggi dengan preferensi pengguna.

Dengan mengadopsi pendekatan content-based filtering menggunakan metode cosine similarity dan jaccard similarity, diharapkan sistem rekomendasi makanan dapat memberikan rekomendasi yang lebih personal dan relevan kepada pengguna, meningkatkan pengalaman pengguna dalam menemukan makanan, serta membantu pemilik bisnis makanan untuk mempromosikan produk mereka secara efektif.

## Data Understanding

Dataset yang digunakan merupakan data kumpulan makanan bersumber dari Kaggle. Dataset ini mewakili data terkait dengan sistem rekomendasi makanan. Terdapat dua dataset yang disertakan dalam file dataset ini. Yang pertama berisi dataset terkait makanan, bahan-bahan, dan masakan yang terlibat. Yang kedua, berisi dataset _rating_ untuk sistem rekomendasi. 

Tautan Datasets: ![all text](https://www.kaggle.com/datasets/schemersays/food-recommendation-system)

Dataset ini yang berisi fitur sebagai berikut:

Dataset Makanan:

- **Food_ID:** data ID makanan
- **Name:** Nama-nama makanan
- **C_Type:** Type atau jenis makanan
- **Veg_Non:** Kategori makanan vegetarian atau non-vegatarian
- **Describe:** Deskripsi bahan-bahan dasar makanan

Dataset _Rating_:

- **User_ID:** data ID pengguna
- **Food_ID:** data ID makanan yang telah diberi _rating_
- **Rating:** penilaian yang diberikan pengguna terhadap makanan

### Membaca Data

Datasets makanan yang digunakan ini mempunyai data sebanyak 400 baris dan 5 kolom, sedangkan data _rating_ mempunyai 512 baris dan 3 kolom.

Tabel 1. Data table makanan

|index|Food\_ID|Name|C\_Type|Veg\_Non|Describe|
|---|---|---|---|---|---|
|0|1|summer squash salad|Healthy Food|veg|white balsamic vinegar, lemon juice, lemon rind, red chillies, garlic cloves \(crushed\), olive oil, summer squash \(zucchini\), sea salt, black pepper, basil leaves|
|1|2|chicken minced salad|Healthy Food|non-veg|olive oil, chicken mince, garlic \(minced\), onion, salt, black pepper, carrot, cabbage, green onions, sweet chilli sauce, peanut butter, ginger, soy sauce, fresh cilantro, red pepper flakes \(crushed\), tarts|
|2|3|sweet chilli almonds|Snack|veg|almonds whole, egg white, curry leaves, salt, sugar \(fine grain\), red chilli powder|
|3|4|tricolour salad|Healthy Food|veg|vinegar, honey/sugar, soy sauce, salt, garlic cloves \(minced\), chilli pepper \(sliced\), green papaya, carrot \(peeled\), cucumbers, mint leaves, toasted peanuts|
|4|5|christmas cake|Dessert|veg|christmas dry fruits \(pre-soaked\), orange zest, lemon zest, jaggery syrup, almond flour, apple, butter \(softened\), eggs|

Dataset mempunyai total 4 fitur kategori dengan 1 tipe data _integer_ dan 4 fitur lainnya mempunyai tipe data _object_.

Tabel 1. Data table _rating_

|index|User\_ID|Food\_ID|Rating|
|---|---|---|---|
|0|1\.0|88\.0|4\.0|
|1|1\.0|46\.0|3\.0|
|2|1\.0|24\.0|5\.0|
|3|1\.0|25\.0|4\.0|
|4|2\.0|49\.0|1\.0|

Dataset mempunyai total 3 fitur kategori dimana semuanya mempunyai tipe data _float64_.

### Data Cleansing

Datasets yang ada saat ini perlu dilakukan pembersihan terlebih dahulu sebelum digunakan, sehingga data tidak bias dan bisa dieksplorasi secara maksimal. Metode pembersihan yang dilakukan ialah dengan mengecek data kosong (NaN) dan kemudian data kosong tersebut hapus. Selain itu lakukan juga pengecekan data duplikat yang mungkin ada. Dari hasil pengecekan dataset makanan, tidak ditemukan adanya data kosong ataupun duplikat. Sedangkan pada dataset _rating_ terdapat 1 data kosong pada baris ke 511. Jalankan fungsi drop kemudian dataset kita sudah bersih.

### Univariate Analysis

Untuk memahami dan menganalisis satu variabel tunggal dalam sebuah dataset kita bisa menggunakan metode analisis statistik _univariate analysis_, fokus diberikan pada karakteristik dan distribusi variabel tersebut secara individual, tanpa mempertimbangkan hubungan dengan variabel lainnya. Tujuan utama utamanya ialah untuk menggambarkan, meringkas, dan memahami data pada variabel tunggal tersebut. Pertama-tama gabungkan dataset makanan dan _rating_ menggunakan fungsi merge pada pandas. Gabungkan kedua dataframe berdasarkan Food_ID, penggabungan dilakukan dengan metode 'left' yang berarti semua data dari _rating_ akan tetap ada dalam hasil penggabungan, sedangkan data dari _makanan_ yang memiliki Food_ID yang cocok akan ditambahkan, sehingga data sekarang berisi 512 baris dan 8 kolom. Setelah itu data diurutkan menggunakan fungsi _sort_ diurutkan dalam dataframe berdasarkan nilai Food_ID secara _ascending_.

Setelah itu, lakukan pengecekan lagi terhadap data kosong dan duplikat, hasilnya tidak ditemukan data tetap bersih. Langkah selanjutnya, barulah bisa melakukan visualisasi terhadap data, sehingga data bisa dianalysis secara individual. Lakukan perhitungan persentasi data, kemudian lakukan _count plot bar_ menggunakan matplotlib.pyplot, berikut hasilnya:
