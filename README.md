# Food Recommender System

## Latar Belakang

Dalam era modern, dimana setiap orang memiliki akses yang melimpah terhadap berbagai jenis makanan dan minuman, serta kebutuhan yang semakin kompleks seperti diet khusus, preferensi pribadi, dan kondisi kesehatan, penting untuk memiliki panduan yang akurat dan personal dalam memilih makanan yang tepat. Ketika datang ke berbagai resto tempat makan, preferensi dan kebutuhan tiap individu sangat beragam. Beberapa orang mungkin memiliki preferensi vegetarian atau vegan, sedangkan yang lain mungkin memiliki preferensi terhadap makanan tertentu seperti makanan Asia, makanan organik, atau makanan tanpa gluten. Selain itu, kondisi kesehatan seperti alergi makanan, intoleransi, atau penyakit tertentu juga dapat mempengaruhi pilihan makanan seseorang.

Dalam konteks ini, Sistem Rekomendasi Makanan menjadi penting karena dapat membantu pengguna dalam menavigasi pilihan makanan yang luas dan memilih makanan yang sesuai dengan preferensi dan kebutuhan tiap individu. "Pendekatan rekomendasi berbasis konten dalam domain makanan berfokus pada analisis karakteristik item makanan seperti bahan, rasa, dan informasi nutrisi untuk menghasilkan rekomendasi personal untuk pengguna" (Almahmeed & Alshammari, 2016). Sistem ini dapat menghemat waktu dan usaha pengguna dalam mencari dan memilih makanan yang cocok, serta meningkatkan kepuasan dan kualitas pengalaman kuliner mereka.

## Business Understanding

Dalam industri makanan, pengguna seringkali dihadapkan pada banyak pilihan makanan yang tersedia. Namun, pengguna dapat mengalami kesulitan dalam memilih makanan yang sesuai dengan preferensi dan kebutuhan mereka. Oleh karena itu, pengembangan Sistem Rekomendasi Makanan dapat membantu pengguna dalam menemukan makanan yang sesuai dengan preferensi mereka. Pemahaman bisnis ini untuk mengembangkan sebuah Sistem Rekomendasi Makanan yang dapat memberikan rekomendasi makanan yang personal dan relevan kepada pengguna. Sistem ini akan menggunakan teknik-teknik seperti filtrasi kolaboratif, filtrasi berbasis konten, atau kombinasi dari keduanya untuk menghasilkan rekomendasi yang akurat dan memuaskan.

Sistem rekomendasi ini juga memiliki manfaat bisnis seperti meningkatkan pengalaman pengguna, dengan adanya sistem rekomendasi, pengguna dapat dengan mudah menemukan makanan yang cocok dengan preferensi mereka, meningkatkan kepuasan dan pengalaman pengguna. Meningkatkan penjualan dan retensi pelanggan, dengan memberikan rekomendasi yang relevan, sistem ini dapat membantu meningkatkan penjualan makanan dan mempertahankan pelanggan yang loyal. Meningkatkan efisiensi operasional dengan memanfaatkan teknologi otomatisasi dalam sistem rekomendasi, proses pengambilan keputusan makanan dapat ditingkatkan, sehingga mengurangi waktu yang dihabiskan dalam pencarian makanan.

Pengguna utama sistem ini adalah konsumen atau pengguna akhir yang mencari rekomendasi makanan. Stakeholder lainnya termasuk pemilik bisnis makanan, penyedia layanan makanan, dan pemasar makanan yang ingin mempromosikan produk mereka kepada target pasar yang tepat secara efektif. Dengan menggunakan teknik-teknik seperti filtrasi kolaboratif dan filtrasi berbasis konten, sistem ini dapat menganalisis preferensi pengguna dan karakteristik makanan untuk memberikan rekomendasi yang relevan. Pemilik bisnis makanan dapat memanfaatkan rekomendasi ini untuk mempromosikan produk mereka kepada pengguna yang memiliki minat dan preferensi serupa. Hal ini akan membantu pemilik bisnis makanan meningkatkan efektivitas kampanye promosi mereka dengan mengarahkan upaya pemasaran mereka kepada audiens yang berpotensi tertarik dan berpeluang tinggi untuk membeli produk mereka. Dengan pemahaman bisnis yang jelas, pengembangan Sistem Rekomendasi Makanan dapat difokuskan pada mencapai tujuan bisnis yang telah ditetapkan dan memberikan manfaat yang signifikan bagi pengguna dan stakeholder terkait.

### Problem Statement and Goals

Berdasarkan kondisi yang telah diuraikan sebelumnya, sistem rekomendasi makanan ini dibuat untuk menjawab permasalahan berikut:
1. Bagaimana cara mengatasi kesulitan pengguna dalam memilih makanan yang sesuai dengan preferensi dan kebutuhan mereka di tengah banyaknya pilihan yang tersedia?
2. Bagaimana caranya meningkatkan pengalaman pengguna dalam menemukan makanan yang sesuai dengan preferensi mereka?
3. Bagaimana pemilik bisnis makanan dapat mempromosikan produk mereka kepada target pasar yang tepat secara efektif?

Serta untuk menjawab pertanyaan tersebut, sistem rekomendasi makanan ini dibuat dengan tujuan atau goals sebagai berikut:

1. Mengembangkan sistem rekomendasi makanan yang mencapai tingkat akurasi rekomendasi sebesar 80% berdasarkan penilaian pengguna dalam waktu 3 bulan.
2. Meningkatkan tingkat kepuasan pengguna dalam menemukan makanan yang sesuai sebesar 15% dalam 4 bulan pertama setelah implementasi sistem.
3. Meningkatkan tingkat konversi promosi produk makanan sebesar 15% dengan mengarahkan promosi kepada target pasar yang tepat berdasarkan rekomendasi sistem dalam 1 tahun.

### Solution Statement

Solution Statement

Untuk mencapai tujuan tersebut, sistem akan menerapkan dua pendekatan solusi menggunakan metode content-based filtering dengan menggunakan cosine similarity dan jaccard similarity dengan pertimbangan sebagai berikut:

1. Content-Based Filtering dengan Metode Cosine Similarity:
   - Pendekatan ini akan menggunakan analisis konten makanan untuk membangun profil preferensi pengguna.
   - Pertama, fitur-fitur penting dari makanan seperti deskripsi, bahan, dan atribut lainnya akan diekstraksi dan diwakili dalam bentuk vektor.
   - Representasi vektor makanan dan preferensi pengguna akan dibuat dengan menggunakan teknik seperti CountVectorizer atau TF-IDFVectorizer.
   - Selanjutnya, menggunakan metode cosine similarity, akan dihitung sejauh mana kesamaan antara vektor representasi makanan dengan vektor representasi preferensi pengguna.
   - Semakin tinggi nilai cosine similarity, semakin mirip makanan dengan preferensi pengguna, dan makanan tersebut akan direkomendasikan.

2. Content-Based Filtering dengan Metode Jaccard Similarity:
   - Pendekatan ini juga menggunakan analisis konten makanan untuk membangun profil preferensi pengguna.
   - Kata-kata kunci penting dari deskripsi makanan dan preferensi pengguna akan diekstraksi dan dijadikan sebagai himpunan kata-kunci.
   - Himpunan kata-kunci makanan dan preferensi pengguna akan digunakan untuk menghitung kesamaan menggunakan metode jaccard similarity.
   - Semakin tinggi nilai jaccard similarity, semakin mirip kata-kunci makanan dengan kata-kunci preferensi pengguna, dan makanan tersebut akan direkomendasikan.

Dengan mengadopsi pendekatan content-based filtering menggunakan metode cosine similarity dan jaccard similarity, diharapkan sistem rekomendasi makanan dapat memberikan rekomendasi yang lebih personal dan relevan kepada pengguna. Fitur-fitur penting dari makanan diekstraksi dan diwakili dalam bentuk vektor, sementara kata-kunci penting dari deskripsi makanan dan preferensi pengguna digunakan untuk menghitung kesamaan. Metode cosine similarity dan jaccard similarity digunakan untuk mengukur tingkat kesamaan antara makanan dan preferensi pengguna. Hal ini memungkinkan sistem untuk merekomendasikan makanan yang memiliki kesamaan konten atau kata-kunci tertinggi dengan preferensi pengguna.

Dengan demikian, sistem rekomendasi ini diharapkan dapat membantu pengguna dalam menemukan makanan yang sesuai dengan preferensi mereka, meningkatkan pengalaman pengguna, serta membantu pemilik bisnis makanan dalam mempromosikan produk mereka kepada target pasar yang tepat secara efektif.

## Data Understanding

Dataset yang digunakan merupakan data kumpulan makanan bersumber dari Kaggle. Dataset ini mewakili data terkait dengan sistem rekomendasi makanan. Terdapat dua dataset yang disertakan dalam file dataset ini. Yang pertama berisi dataset terkait makanan, bahan-bahan, dan masakan yang terlibat. Yang kedua, berisi dataset _rating_ untuk sistem rekomendasi. 

Tautan Datasets: [Kaggle: Food Dataset](https://www.kaggle.com/datasets/schemersays/food-recommendation-system)

Dataset ini yang berisi fitur sebagai berikut:

Dataset Makanan:

- **Food_ID:** data ID makanan
- **Name:** Nama-nama makanan
- **C_Type:** Type atau jenis makanan
- **Veg_Non:** Kategori makanan vegetarian atau non-vegetarian
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

Tabel 2. Data table _rating_

|index|User\_ID|Food\_ID|Rating|
|---|---|---|---|
|0|1\.0|88\.0|4\.0|
|1|1\.0|46\.0|3\.0|
|2|1\.0|24\.0|5\.0|
|3|1\.0|25\.0|4\.0|
|4|2\.0|49\.0|1\.0|

Dataset mempunyai total 3 fitur kategori dimana semuanya mempunyai tipe data _float64_.

### Data Cleansing

Datasets yang ada saat ini perlu dilakukan pembersihan terlebih dahulu sebelum digunakan, sehingga data tidak bias dan bisa dieksplorasi secara maksimal. Metode pembersihan yang dilakukan ialah dengan mengecek data kosong (NaN) dan kemudian data kosong tersebut hapus. Selain itu lakukan juga pengecekan data duplikat yang mungkin ada. Dari hasil pengecekan dataset makanan, tidak ditemukan adanya data kosong ataupun duplikat. Sedangkan pada dataset _rating_ terdapat 1 data kosong pada baris ke 511. Jalankan fungsi drop kemudian dataset sekarang sudah bersih.

### Univariate Analysis

Untuk memahami dan menganalisis satu variabel tunggal dalam sebuah dataset, bisa menggunakan metode analisis statistik _univariate analysis_, fokus diberikan pada karakteristik dan distribusi variabel tersebut secara individual, tanpa mempertimbangkan hubungan dengan variabel lainnya. Tujuan utama utamanya ialah untuk menggambarkan, meringkas, dan memahami data pada variabel tunggal tersebut. Pertama-tama gabungkan dataset makanan dan _rating_ menggunakan fungsi merge pada pandas. Gabungkan kedua dataframe berdasarkan Food_ID, penggabungan dilakukan dengan metode 'left' yang berarti semua data dari _rating_ akan tetap ada dalam hasil penggabungan, sedangkan data dari _makanan_ yang memiliki Food_ID yang cocok akan ditambahkan, sehingga data sekarang berisi 512 baris dan 8 kolom. Setelah itu data diurutkan menggunakan fungsi _sort_ diurutkan dalam dataframe berdasarkan nilai Food_ID secara _ascending_.

Setelah itu, lakukan pengecekan lagi terhadap data kosong dan duplikat, hasilnya tidak ditemukan data tetap bersih. Langkah selanjutnya, barulah bisa melakukan visualisasi terhadap data, sehingga data bisa dianalysis secara individual. Lakukan perhitungan persentasi data, kemudian lakukan _count plot bar_ menggunakan matplotlib.pyplot, berikut hasilnya:

Tabel 3. Persentasi Fitur C_Type

|              | Total sample | percentage |
|--------------|--------------|------------|
| Indian       | 112          | 21.9       |
| Dessert      | 102          | 20.0       |
| Healthy Food | 73           | 14.3       |
| Snack        | 46           | 9.0        |
| Japanese     | 36           | 7.0        |
| Italian      | 35           | 6.8        |
| French       | 27           | 5.3        |
| Mexican      | 25           | 4.9        |
| Thai         | 21           | 4.1        |
| Chinese      | 20           | 3.9        |
| Beverage     | 14           | 2.7        |

Gambar 1. Visualisasi Fitur C_Type

![C_Type](https://github.com/renhardjh/Food-Recommender-System/assets/24643123/801929b5-49d0-4ad0-a775-ec10c561ba02)
)

Tabel 4. Persentasi Fitur Veg_Non

|       | Total sample | percentage |
|-------|--------------|------------|
| veg   |    347       |    67.9    |
| non-veg |   164       |    32.1    |

Gambar 2. Visualisasi Fitur Veg_Non

![Veg_Non](https://github.com/renhardjh/Food-Recommender-System/assets/24643123/abeaa973-221e-46e6-9522-b16368b8da6a)


Tabel 5. Persentasi Fitur Rating

|   | Total sample | percentage |
|---|--------------|------------|
| 3.0 |     63       |    12.3    |
| 10.0 |    61       |    11.9    |
| 5.0 |     61       |    11.9    |
| 4.0 |     53       |    10.4    |
| 7.0 |     49       |    9.6     |
| 1.0 |     48       |    9.4     |
| 6.0 |     48       |    9.4     |
| 2.0 |     47       |    9.2     |
| 9.0 |     42       |    8.2     |
| 8.0 |     39       |    7.6     |


Gambar 3. Visualisasi Fitur Rating

![Rating](https://github.com/renhardjh/Food-Recommender-System/assets/24643123/66166279-af37-47eb-8b08-514f84e054f5)


Dari hasil visualisasi tersebut, kesimpulan informasi yang bisa didapat sebagai berikut:

- Terdapat 11 kategori tipe atau jenis makanan
- Tiga tipe makanan tertinggi ialah _Indian_, _Dessert_ dan _Healthy Food_
- Jumlah jenis makanan vegetarian lebih besar daripada jenis makanan non vegetarian
- Penilaian rating berkisar antara 1 - 10
- Makanan dengan rating rendah lebih banyak dibandingkan makanan dengan rating tinggi
- Makanan dengan rating 3.0 paling banyak

## Data Preparation

Sebelum mempersiapkan model, perlu dilakukan persiapan data terlebih dahulu, agar data yang digunakan pada model bisa sesuai. Pertama, buang data duplikat pada Food_ID, karena sistem rekomendasi yang akan dibuat berdasarkan nama-nama makanan, untuk mendapatkan nama-nama makanan yang valid bisa menggunakan nilai unik berdasarkan ID. 

Tabel 6. Dataframe Sebelum Pembersihan

|index|User\_ID|Food\_ID|Rating|Name|C\_Type|Veg\_Non|Describe|
|---|---|---|---|---|---|---|---|
|376|71\.0|1\.0|10\.0|summer squash salad|Healthy Food|veg|white balsamic vinegar, lemon juice, lemon rind, red chillies, garlic cloves \(crushed\), olive oil, summer squash \(zucchini\), sea salt, black pepper, basil leaves|
|253|49\.0|1\.0|5\.0|summer squash salad|Healthy Food|veg|white balsamic vinegar, lemon juice, lemon rind, red chillies, garlic cloves \(crushed\), olive oil, summer squash \(zucchini\), sea salt, black pepper, basil leaves|
|200|39\.0|2\.0|10\.0|chicken minced salad|Healthy Food|non-veg|olive oil, chicken mince, garlic \(minced\), onion, salt, black pepper, carrot, cabbage, green onions, sweet chilli sauce, peanut butter, ginger, soy sauce, fresh cilantro, red pepper flakes \(crushed\), tarts|
|50|9\.0|2\.0|3\.0|chicken minced salad|Healthy Food|non-veg|olive oil, chicken mince, garlic \(minced\), onion, salt, black pepper, carrot, cabbage, green onions, sweet chilli sauce, peanut butter, ginger, soy sauce, fresh cilantro, red pepper flakes \(crushed\), tarts|
|116|22\.0|2\.0|5\.0|chicken minced salad|Healthy Food|non-veg|olive oil, chicken mince, garlic \(minced\), onion, salt, black pepper, carrot, cabbage, green onions, sweet chilli sauce, peanut butter, ginger, soy sauce, fresh cilantro, red pepper flakes \(crushed\), tarts|
|456|89\.0|3\.0|7\.0|sweet chilli almonds|Snack|veg|almonds whole, egg white, curry leaves, salt, sugar \(fine grain\), red chilli powder|
|396|77\.0|3\.0|1\.0|sweet chilli almonds|Snack|veg|almonds whole, egg white, curry leaves, salt, sugar \(fine grain\), red chilli powder|
|457|90\.0|4\.0|6\.0|tricolour salad|Healthy Food|veg|vinegar, honey/sugar, soy sauce, salt, garlic cloves \(minced\), chilli pepper \(sliced\), green papaya, carrot \(peeled\), cucumbers, mint leaves, toasted peanuts|
|210|41\.0|4\.0|6\.0|tricolour salad|Healthy Food|veg|vinegar, honey/sugar, soy sauce, salt, garlic cloves \(minced\), chilli pepper \(sliced\), green papaya, carrot \(peeled\), cucumbers, mint leaves, toasted peanuts|
|144|28\.0|5\.0|10\.0|christmas cake|Dessert|veg|christmas dry fruits \(pre-soaked\), orange zest, lemon zest, jaggery syrup, almond flour, apple, butter \(softened\), eggs|

Hasilnya dataframe berisi 309 kolom yang berarti ada 309 dari 400 jenis makanan yang sesuai dengan data makanan preferensi penilaian pengguna. Selanjutnya, karena sistem rekomendasi yang akan dibuat merupakan _content-based filtering_ maka makanan yang akan diberi rekomendasi berdasarkan kesamaan kontennya, dalam penerapannya bisa menggunakan salah satu fitur baik itu **C_Type**, **Veg_Non** ataupun **Describe**, namun untuk hasil yang lebih baik bisa melakukan mixed pada ketiga fitur tersebut. Ketiga fitur ini dilakukan _join text_ menjadi satu konten agar lebih mudah dalam menentukan _similiarity_ atau kesamaannya. 

Setelah melakukan penggabungan konten, data hasil penggabungan ini masih memiliki tanda baca seperti titik, koma, dan sebagainya, lakukan penghapusan tanda baca pada text, penghapusan bisa dilakukan dengan melakukan perulangan dan melakukan pengecekan terhadap _string_ yang mengadung tanda baca menggunakan metode _string punctuation_. 

Setelah data konten bersih yang berisi kumpulan kata-kata yang bisa disebut sebagai atibut-atribut yang di cek kesamaannya menggunakan _cosine similiarity_ dan _jaccard similiarity_. Lakukan konversi data series Food_ID, Name dan Description ke bentuk list untuk kemudian buatkan _dataframe_ baru, sehingga data yang digunakan hanya fitur yang relevan saja. Hasil dataframenya menjadi seperti ini:

Tabel 7. Dataframe Setelah Pembersihan dan Melakukan Mixed Fitur

|index|id|food\_name|food\_description|
|---|---|---|---|
|0|1\.0|summer squash salad|Healthy Food veg white balsamic vinegar lemon juice lemon rind red chillies garlic cloves crushed olive oil summer squash zucchini sea salt black pepper basil leaves|
|1|2\.0|chicken minced salad|Healthy Food nonveg olive oil chicken mince garlic minced onion salt black pepper carrot cabbage green onions sweet chilli sauce peanut butter ginger soy sauce fresh cilantro red pepper flakes crushed tarts|
|2|3\.0|sweet chilli almonds|Snack veg almonds whole egg white curry leaves salt sugar fine grain red chilli powder|
|3|4\.0|tricolour salad|Healthy Food veg vinegar honeysugar soy sauce salt garlic cloves minced chilli pepper sliced green papaya carrot peeled cucumbers mint leaves toasted peanuts|
|4|5\.0|christmas cake|Dessert veg christmas dry fruits presoaked orange zest lemon zest jaggery syrup almond flour apple butter softened eggs|
|5|6\.0|japanese curry arancini with barley salsa|Japanese veg japanese curry sticky rice cheese inside rice barley salsa wasabi mayo red capsicum cube cut yellow capsicum cube cut green capsicum cube cut green chili barley butter white pepper light soya salt|
|6|7\.0|chocolate nero cookies|Dessert veg almonds eggs granulated sugar bittersweet chocolate unsalted butter flour baking powder castor sugar icing sugar|
|7|8\.0|lamb and chargrilled bell pepper soup|Healthy Food nonveg lamb bones preferably shank and shoulder onions celery ginger garlic carrot chargrilled redyellowgreen bell peppers quartered whole spices mix black pepper cinnamon cardamom clove bay leaf salt water warm oil sunflower or olive|
|8|9\.0|cream of almond soup|Healthy Food veg vegetable stock skimmed milk toasted almonds powdered butter flour salt and pepper nutmeg almond essence toasted almond flakes|
|9|10\.0|broccoli and almond soup|Healthy Food veg vegetable stock broccoli ground almonds toasted skimmed milk salt freshly ground black pepper|

## Pengembangan Model

Setelah data selesai dipersiapkan, sudah bersih dan hanya berisi fitur-fitur yang relevan saja, sekarang saatnya membuat model sistem rekomendasi makanan menggunakan pendekatan _content based filtering_. Pertama mulai dari melakukan pemrosesan teks yang digunakan pada sistem rekomendasi untuk menemukan representasi fitur penting dari setiap kategori makanan. Dalam kasus ini, pemrosesan teks menggunakan CountVectorizer yang merupakan salah satu teknik dalam pemrosesan teks yang digunakan untuk mengubah teks menjadi representasi numerik berdasarkan frekuensi kemunculan kata-kata. Dalam konteks model sistem rekomendasi makanan, CountVectorizer digunakan untuk mengubah deskripsi makanan atau kata-kata terkait menjadi fitur numerik yang dapat digunakan dalam pemodelan machine learning. Kemudian untuk menghitung kesamaan dari konten setiap kategori makanan dalam sistem ini akan menggunakan cosine similiarity dan jaccard similiarity. Lalu bandingkan performa dan hasil dari kedua model tersebut untuk menemukan mana yang lebih baik.

### Tokenisasi

CountVectorizer menghitung frekuensi kemunculan setiap kata dalam teks dan menghasilkan vektor numerik berdasarkan frekuensi tersebut. Setiap kata dalam teks akan menjadi fitur dalam vektor, dan nilai dalam vektor tersebut menunjukkan berapa kali kata tersebut muncul dalam teks. CountVectorizer memungkinkan sistem untuk mengubah teks menjadi representasi numerik yang dapat digunakan oleh algoritma machine learning untuk melatih model rekomendasi. Alasannya sistem ini menggunakan CountVectorizer karena kemudahan implementasi dan interpretasi hasilnya. CountVectorizer hanya berfokus pada frekuensi kemunculan kata dalam teks tanpa memperhitungkan bobot kata tersebut. Dalam konteks sistem rekomendasi makanan, frekuensi kemunculan kata dapat memberikan informasi penting tentang preferensi pengguna terhadap jenis makanan atau bahan-bahan tertentu.

Berikut langkah-langkah mengimplementasi CountVectorizer:

1. Menginisialisasi CountVectorizer dengan parameter stop_words='english' dan ngram_range=(1, 3). 
   - stop_words='english' digunakan untuk menghapus kata-kata umum dalam bahasa Inggris, seperti "the", "and", "is", dsb.
   - ngram_range=(1, 3) menunjukkan bahwa ingin mempertimbangkan unigram, bigram, dan trigram dalam teks. Misalnya, "chicken", "fried chicken", "spicy fried chicken".

2. Menggunakan metode fit_transform pada CountVectorizer untuk melakukan proses fitting dan transformasi teks ke dalam bentuk matriks fitur. Data yang digunakan adalah kolom 'food_description' dari dataframe final_food.

3. Menggunakan metode get_feature_names_out() pada CountVectorizer untuk mendapatkan daftar fitur (kata-kata) yang terkait dengan matriks fitur.
   - cv.get_feature_names_out() akan mengembalikan array yang berisi daftar fitur (kata-kata) yang dihasilkan oleh CountVectorizer. Setiap elemen dalam array ini mewakili satu fitur (kata) dalam teks.

Hasil CountVectorizer tersebut berupa matriks fitur yang merepresentasikan teks (deskripsi makanan) dalam bentuk numerik berisi matriks dengan dimensi (309, 11083). Setiap kolom dalam matriks fitur menunjukkan frekuensi kemunculan kata-kata dalam teks, sesuai dengan konfigurasi CountVectorizer yang telah ditentukan.

### Cosine Similiarity

Cosine similarity merupakan sebuah metode yang digunakan untuk mengukur kesamaan antara dua vektor dalam ruang berdimensi banyak. Metode ini menghitung kosinus sudut antara dua vektor, dan hasilnya adalah nilai antara 0 hingga 1. Semakin tinggi nilai cosine similarity, semakin mirip atau serupa dua vektor tersebut. Dalam konteks sistem rekomendasi makanan, cosine similarity digunakan untuk mengukur kesamaan konten antara dua atau lebih makanan berdasarkan fitur-fitur yang dimiliki oleh makanan tersebut. Fitur-fitur ini dapat berupa kata-kata atau atribut lain yang dianggap relevan, seperti bahan-bahan, jenis masakan, atau deskripsi makanan.

Berikut langkah-langkah implementasinya dalam sistem ini:

1. Mengimport fungsi cosine_similarity dari sklearn.metrics.pairwise. Fungsi ini digunakan untuk menghitung kesamaan kosinus antara dua matriks atau vektor.

2. Menggunakan cosine_similarity dengan parameter cv_matrix, cv_matrix. 
   - cv_matrix adalah matriks fitur yang dihasilkan oleh CountVectorizer pada langkah sebelumnya. Matriks ini berisi representasi numerik dari deskripsi makanan.
   - cv_matrix, cv_matrix berarti menghitung kesamaan kosinus antara setiap baris pada cv_matrix dengan setiap baris lainnya. Dalam konteks ini, akan dicari kesamaan antara deskripsi makanan satu dengan yang lain.

3. Hasil dari cosine_similarity adalah matriks similiaritas kosinus, di mana setiap elemen menunjukkan tingkat kesamaan antara dua deskripsi makanan berdasarkan representasi numeriknya. Semakin tinggi nilai similiaritas kosinus, semakin mirip atau serupa dua deskripsi makanan tersebut.

Hasil dari model tersebut berupa matriks similiaritas kosinus yang dapat digunakan dalam sistem rekomendasi makanan untuk mencari makanan yang memiliki kesamaan konten dengan makanan lainnya berdasarkan deskripsinya.

### Jaccard Similiarity

Jaccard similarity merupakan sebuah metode yang digunakan untuk mengukur kesamaan antara dua set atau himpunan data. Metode ini menghitung persentase kesamaan antara elemen-elemen yang ada di dalam dua himpunan, dibandingkan dengan jumlah total elemen yang unik dari kedua himpunan tersebut. Pendekatan ini didefinisikan sebagai rasio dari ukuran irisan (intersection) antara dua himpunan terhadap ukuran gabungan (union) dari kedua himpunan tersebut. Pendekatan ini menghasilkan nilai antara 0 hingga 1. Nilai 0 menunjukkan ketidakserupaan total antara kedua himpunan, sedangkan nilai 1 menunjukkan kesamaan sempurna antara kedua himpunan. Dalam konteks sistem rekomendasi makanan ini, Pendekatan ini digunakan untuk mengukur kesamaan antara dua makanan berdasarkan fitur-fitur yang dimiliki, seperti bahan-bahan, kategori makanan, atau sifat-sifat tertentu. Semakin tinggi nilai Jaccard similarity antara dua makanan, semakin mirip atau serupa makanan-makanan tersebut dalam hal fitur-fitur yang dimiliki.

Berikut langkah-langkah dalam menghitung kesamaan Jaccard similarity dalam sistem ini:

1. Mengubah matriks sparse yang diperoleh dari CountVectorizer ke dalam bentuk array menggunakan metode `.toarray()`. Hal ini dilakukan agar dapat menggunakan metode pairwise_distances.
2. Menggunakan fungsi `pairwise_distances` dari library `sklearn.metrics` dengan parameter `metric="jaccard"`. Fungsi ini akan menghitung jarak pairwise antara vektor-vektor dalam array menggunakan metode Jaccard.
3. Nilai jarak yang diperoleh dari pairwise_distances akan dikonversi menjadi Jaccard similarity dengan melakukan operasi 1 dikurangi dengan nilai jarak. Hal ini karena nilai jarak Jaccard adalah komplementer dari Jaccard similarity.

Hasil dari model tersebut berupa matriks di mana setiap elemen matriks menunjukkan tingkat kesamaan antara dua makanan berdasarkan fitur-fitur yang dimiliki. Nilai Jaccard similarity berkisar antara 0 hingga 1, di mana nilai 1 menunjukkan kesamaan sempurna antara dua makanan dalam hal fitur-fitur yang dimiliki, sedangkan nilai 0 menunjukkan ketidakserupaan total antara dua makanan.

### Mendapatkan Rekomendasi

Selanjutnya buat sebuah fungsi untuk mendapatkan rekomendasi makanan berdasarkan nama makanan yang diberikan dan matriks kesamaan antar makanan yang telah dihitung sebelumnya menggunakan model _cosine similarity_ dan _Jaccard similarity_.

Berikut langkah-langkah implementasinya:

1. `indices = pd.Series(final_food.index, index=final_food['food_name'])`: Membuat objek `Series` dengan menggunakan `food_name` sebagai indeks dan `index` dari `final_food` sebagai nilai. Hal ini dilakukan untuk memudahkan pencarian indeks berdasarkan nama makanan.

2. `def get_recommendations(name, method_sim)`: Membuat fungsi `get_recommendations` yang menerima dua parameter, yaitu `name` yang merupakan nama makanan yang ingin direkomendasikan, dan `method_sim` yang merupakan matriks kesamaan (similarity matrix) antar makanan berdasarkan metode tertentu.

3. `food_index = indices[name]`: Menggunakan objek `indices` untuk mencari indeks makanan berdasarkan nama makanan yang diberikan sebagai input.

4. `sim_weight = list(enumerate(method_sim[food_index]))`: Mengambil baris matriks kesamaan (similarity matrix) yang berkaitan dengan makanan yang dipilih, lalu mengubahnya menjadi daftar yang terdiri dari pasangan indeks makanan dan bobot kesamaan.

5. `sim_weight = sorted(sim_weight, key=lambda x: x[1], reverse=True)`: Mengurutkan daftar bobot kesamaan secara menurun, sehingga makanan dengan kesamaan tertinggi akan muncul di bagian atas.

6. `sim_weight = sim_weight[1:6]`: Memotong daftar bobot kesamaan sehingga hanya menyisakan top 5 makanan teratas dengan kesamaan tertinggi (kecuali makanan itu sendiri).

7. `food_indices = [i[0] for i in sim_weight]`: Mengumpulkan indeks makanan dari daftar bobot kesamaan yang telah dipotong sebelumnya.

8. `return final_food.iloc[food_indices]`: Mengembalikan dataframe `final_food` yang berisi rekomendasi makanan berdasarkan indeks makanan yang telah dikumpulkan sebelumnya.

Setelah membuat fungsi untuk mendapatkan rekomendasinya, panggil fungsi tersebut dengan input nama makanan dan modelnya satu persatu. Mari coba untuk mendapatkan preferensi rekomendasi dari makanan _roast turkey with cranberry sauce_ Berikut hasilnya:

Tabel 8. Hasil top 5 rekomendasi mengngunakan model cosine similiarity

|index|id|food\_name|food\_description|
|---|---|---|---|
|1|2\.0|chicken minced salad|Healthy Food nonveg olive oil chicken mince garlic minced onion salt black pepper carrot cabbage green onions sweet chilli sauce peanut butter ginger soy sauce fresh cilantro red pepper flakes crushed tarts|
|86|87\.0|roasted spring chicken with root veggies|Healthy Food nonveg whole chicken thyme garlic lemon orange salt black pepper butter to rub extra olive oil carrot turnip beetroot chipotle powder parsley|
|246|247\.0|microwave chicken steak|Healthy Food nonveg chicken breasts boneless eggs slightly whisked ginger paste garlic paste onions coriander leaves green chillies black pepper powder flour vinegar salt oil|
|70|71\.0|carrot ginger soup|Healthy Food veg Carrots Olive Oil Salt Vegetable Stock Ginger Thyme Onion Garlic Buds Pepper Freshly Picked|
|150|151\.0|fish andlouse|French nonveg white wine and water mix to cover onion salt bay leaf black pepper corns olive oil onion garlic tomatoes peeled and seeded basil leaves spring fresh thyme  optional 1 bay leaf salt and pepper olive oil wine vinegar prepared mustard salt and pepper assorted garden herbs  parsley basil etc|

Dari hasil output yang terlihat, bisa dikatakan model dengan _cosine similiarity_ sistem sudah berhasil memberikan rekomendasi yang sesuai secara keseluruhan. Hal ini bisa dilihat dari kolom `food_description` ada beberapa kesamaan.

Tabel 9. Hasil top 5 rekomendasi mengngunakan model jaccard similiarity

|index|id|food\_name|food\_description|
|---|---|---|---|
|86|87\.0|roasted spring chicken with root veggies|Healthy Food nonveg whole chicken thyme garlic lemon orange salt black pepper butter to rub extra olive oil carrot turnip beetroot chipotle powder parsley|
|1|2\.0|chicken minced salad|Healthy Food nonveg olive oil chicken mince garlic minced onion salt black pepper carrot cabbage green onions sweet chilli sauce peanut butter ginger soy sauce fresh cilantro red pepper flakes crushed tarts|
|246|247\.0|microwave chicken steak|Healthy Food nonveg chicken breasts boneless eggs slightly whisked ginger paste garlic paste onions coriander leaves green chillies black pepper powder flour vinegar salt oil|
|70|71\.0|carrot ginger soup|Healthy Food veg Carrots Olive Oil Salt Vegetable Stock Ginger Thyme Onion Garlic Buds Pepper Freshly Picked|
|69|70\.0|shepherds salad \(tamatar-kheera salaad\)|Healthy Food veg 1 cucumber peeled and chopped onion tomato green chillies garlic buds pasarley olive oil lemon juice salt and pepper|

Dari hasil output yang terlihat, bisa dikatakan model dengan _jaccard similiarity_ sistem sudah berhasil memberikan rekomendasi yang sesuai secara keseluruhan. Hal ini bisa dilihat dari kolom `food_description` ada beberapa kesamaan. Hasil rekomendasi dari kedua model menunjukan data yang sesuai memiliki beberapa kesamaan yang sesuai, namun manakah model yang lebih _cosine similiarity_ atau _jaccard similiarity_. Untuk membuktikannya mari lakukan evaluasi pada langkah selanjutnya.

## Evaluasi Model

Evaluasi model sangat penting setelah pembuatan model karena memberikan pemahaman tentang seberapa baik model bekerja dalam memenuhi tujuan yang ditetapkan. Evaluasi model membantu dalam mengukur kinerja dan kualitas model serta memberikan wawasan tentang seberapa akurat dan dapat diandalkan model dalam menghasilkan prediksi atau rekomendasi. Setelah selesai membuat model dengan _cosine similiarity_ dan _jaccard similiarity_, perlu melakukan evaluasi terhadap model-model tesebut untuk mengetahui seberapa akurat dan seberapa presisi predikisi atau rekomendasi yang dihasilkan. Untuk mengevaluasi model, dalam hal ini akan menggunakan _precision_, _recall_ dan _F1 score_, evaluasi model menggunakan ketiga metrik tersebut merupakan cara yang umum digunakan dalam sistem klasifikasi dan rekomendasi untuk mengukur kinerja model. Berikut penjelasan singkat tentang masing-masing metrik:

1. **Precision**: Precision mengukur seberapa akurat model dalam memprediksi kelas positif. Precision dihitung sebagai rasio true positive (TP) dibagi dengan jumlah prediksi positif yang benar (TP + false positive (FP)). Precision memberikan informasi tentang seberapa banyak prediksi positif yang benar dari semua prediksi positif yang dibuat oleh model. Semakin tinggi nilai precision, semakin sedikit false positive, yang berarti model memberikan sedikit kesalahan dalam memprediksi item yang tidak seharusnya direkomendasikan.

2. **Recall**: Recall (juga dikenal sebagai sensitivity atau true positive rate) mengukur seberapa baik model dalam menemukan semua contoh kelas positif yang seharusnya direkomendasikan. Recall dihitung sebagai rasio true positive (TP) dibagi dengan jumlah contoh kelas positif yang benar (TP + false negative (FN)). Recall memberikan informasi tentang seberapa banyak contoh kelas positif yang dapat ditemukan oleh model. Semakin tinggi nilai recall, semakin sedikit false negative, yang berarti model tidak melewatkan banyak contoh kelas positif yang seharusnya direkomendasikan.

3. **F1-score**: F1-score adalah rata-rata harmonik antara precision dan recall. F1-score memberikan pengukuran keseimbangan antara precision dan recall. Hal ini berguna ketika ingin memperhatikan keseimbangan antara memaksimalkan presisi dan recall secara bersamaan. F1-score dihitung sebagai 2 * (precision * recall) / (precision + recall). F1-score memiliki rentang nilai antara 0 hingga 1, di mana nilai 1 menunjukkan kinerja yang sempurna dalam memprediksi kelas positif.

Ketiga metrik ini digunakan bersamaan untuk memberikan gambaran yang lebih lengkap tentang kinerja model. Precision dan recall dapat memberikan informasi yang berguna dalam konteks spesifik, tetapi F1-score menggabungkan kedua metrik ini menjadi satu angka yang mencerminkan kinerja secara keseluruhan.

Pertama mari tentukan aktual item rekomendasinya, untuk menentukannya bisa melakukan uji atau tes pada hasil rekomendasi dengan cara membandingkan atribut-atribut dari hasil rekomendasi model dengan atribut input makanan yang ingin diberi rekomendasi, misalnya melakukan uji menggunakan nama makanan **roast turkey with cranberry sauce**. Amati minimal dari 2 attribut awal memiliki kemiripan, misalnya **Healthy Food, nonveg, dan seterusnya**.

Berikut ini hasil dari pengujian hasil rekomendasi _cosine similiarity_:

Tabel 10. Pengujian hasil rekomendasi cosine similiarity

|index|id|food\_name|food\_description|actual\_item|
|---|---|---|---|---|
|1|2\.0|chicken minced salad|Healthy Food nonveg olive oil chicken mince garlic minced onion salt black pepper carrot cabbage green onions sweet chilli sauce peanut butter ginger soy sauce fresh cilantro red pepper flakes crushed tarts|chicken minced salad|
|86|87\.0|roasted spring chicken with root veggies|Healthy Food nonveg whole chicken thyme garlic lemon orange salt black pepper butter to rub extra olive oil carrot turnip beetroot chipotle powder parsley|roasted spring chicken with root veggies|
|246|247\.0|microwave chicken steak|Healthy Food nonveg chicken breasts boneless eggs slightly whisked ginger paste garlic paste onions coriander leaves green chillies black pepper powder flour vinegar salt oil|microwave chicken steak|
|70|71\.0|carrot ginger soup|Healthy Food veg Carrots Olive Oil Salt Vegetable Stock Ginger Thyme Onion Garlic Buds Pepper Freshly Picked|half roast chicken|
|150|151\.0|fish andlouse|French nonveg white wine and water mix to cover onion salt bay leaf black pepper corns olive oil onion garlic tomatoes peeled and seeded basil leaves spring fresh thyme  optional 1 bay leaf salt and pepper olive oil wine vinegar prepared mustard salt and pepper assorted garden herbs  parsley basil etc|fish andlouse|

Dari hasil pengujian 5 rekomendasi, terdapat 4 data yang sesuai dan 1 data yang tidak sesuai yaitu makanan **carrot ginger soup** dengan atribut Healthy Food, veg, dan seterusnya.

Berikut ini hasil dari pengujian hasil rekomendasi _jaccard similiarity_:

Tabel 11. Pengujian hasil rekomendasi jaccard similiarity

|index|id|food\_name|food\_description|actual\_item|
|---|---|---|---|---|
|86|87\.0|roasted spring chicken with root veggies|Healthy Food nonveg whole chicken thyme garlic lemon orange salt black pepper butter to rub extra olive oil carrot turnip beetroot chipotle powder parsley|roasted spring chicken with root veggies|
|1|2\.0|chicken minced salad|Healthy Food nonveg olive oil chicken mince garlic minced onion salt black pepper carrot cabbage green onions sweet chilli sauce peanut butter ginger soy sauce fresh cilantro red pepper flakes crushed tarts|chicken minced salad|
|246|247\.0|microwave chicken steak|Healthy Food nonveg chicken breasts boneless eggs slightly whisked ginger paste garlic paste onions coriander leaves green chillies black pepper powder flour vinegar salt oil|microwave chicken steak|
|70|71\.0|carrot ginger soup|Healthy Food veg Carrots Olive Oil Salt Vegetable Stock Ginger Thyme Onion Garlic Buds Pepper Freshly Picked|half roast chicken|
|69|70\.0|shepherds salad \(tamatar-kheera salaad\)|Healthy Food veg 1 cucumber peeled and chopped onion tomato green chillies garlic buds pasarley olive oil lemon juice salt and pepper|fish andlouse|

Dari hasil pengujian 5 rekomendasi, terdapat 3 data yang sesuai dan 2 data yang kurang sesuai yaitu makanan **carrot ginger soup** dan **shepherds salad** yang mempunyai atribut Healthy Food, veg, dan seterusnya.

Selanjutnya coba panggil fungsi precision, recall dan F1 score dengan input aktual item dan rekomendasi item, langkah pertama dalam program adalah menyimpan nilai item aktual dari data evaluasi dalam variabel `actual_items_cosine` dan `actual_items_jaccard`. Kemudian, variabel `cosine_recommend_items` dan `jaccard_recommend_items` digunakan untuk menyimpan item rekomendasi yang dihasilkan oleh model menggunakan metode cosine similarity dan jaccard similarity.

Selanjutnya, program membuat DataFrame kosong `eval_df` yang akan digunakan untuk menyimpan hasil evaluasi model, seperti precision, recall, dan F1-score. Kemudian, program menghitung precision, recall, dan F1-score untuk metode cosine similarity dan jaccard similarity menggunakan fungsi `precision`, `recall`, dan `f1_score`. Hasil evaluasi ini disimpan dalam dictionary `cosine_dict` dan `jaccard_dict`. Terakhir, program mengisi nilai-nilai evaluasi ke dalam DataFrame `eval_df` menggunakan loop dan menghasilkan tabel yang berisi evaluasi model untuk kedua metode similiarity tersebut.

Tabel 12. Hasil metrik evaluasi precision, recall dan F1 score

|index|Cosine Similiarity|Jaccard Similiarity|
|---|---|---|
|Precision|0\.8|0\.6|
|Recall|0\.8|0\.6|
|F1-score|0\.8000000000000002|0\.6|

Dapat dilihat bahwa hasil Cosine Similiarity lebih baik dibandingkan Jaccard Similiarity dengan F1-Score 0.8 > 0.6, oleh karena itu sistem ini akan lebih baik jika menggunakan cosine similiarity untuk menentukan rekomendasi makanan yang lebih sesuai. Sistem rekomendasi makanan ini nantinya dapat membantu pengguna dalam menemukan makanan yang sesuai dengan preferensi mereka, memberikan pengalaman kuliner yang lebih kaya, dan memperluas pengetahuan mereka tentang berbagai jenis masakan. Selain itu, sistem ini juga dapat membantu dalam mengurangi kebingungan dalam memilih makanan dan memberikan rekomendasi yang personalisasi sesuai dengan selera dan kebutuhan pengguna

## Kesimpulan

Dalam penelitian ini, telah dikembangkan sebuah sistem rekomendasi makanan menggunakan metode cosine similarity dan jaccard similarity. Sistem ini bertujuan untuk memberikan rekomendasi makanan yang sesuai dengan preferensi pengguna berdasarkan kesamaan konten. Hasil evaluasi model menunjukkan bahwa kedua metode similiarity, yaitu cosine similarity dan jaccard similarity, memberikan performa yang baik dalam memberikan rekomendasi makanan. Precision, recall, dan F1-score yang dihitung pada kedua metode tersebut memberikan indikasi yang positif tentang keakuratan dan kebermanfaatan rekomendasi yang diberikan. Hasil metrik evaluasi precision, recall, dan F1-score pada cosine similiarity masing-masing sebesar 0.8, sedangkan menggunakan jaccard similiarity masing-masing sebesar 0.6, sehingga dapat disimpulkan bahwa menggunakan pendekatan cosine similiarity lebih baik untuk sistem rekomendasi makanan ini.

Melalui penggunaan CountVectorizer untuk menganalisis kesamaan konten, sistem rekomendasi ini dapat mengidentifikasi makanan yang memiliki kemiripan dalam deskripsi dan fitur seperti jenis makanan, bahan-bahan, dan asal masakan. Hal ini memungkinkan pengguna untuk menemukan makanan baru yang sesuai dengan preferensi mereka dan mencoba variasi masakan. Dengan demikian, sistem rekomendasi makanan ini dapat membantu pengguna dalam menemukan makanan yang sesuai dengan preferensi mereka, memberikan pengalaman kuliner yang lebih kaya, dan memperluas pengetahuan mereka tentang berbagai jenis masakan. Selain itu, sistem ini juga dapat membantu dalam mengurangi kebingungan dalam memilih makanan dan memberikan rekomendasi yang personalisasi sesuai dengan selera dan kebutuhan pengguna.

Namun, perlu diperhatikan bahwa sistem rekomendasi ini masih memiliki ruang untuk perbaikan. Pengembangan lebih lanjut dapat dilakukan dengan menggabungkan metode similiarity lainnya, menggali lebih dalam fitur-fitur yang relevan, dan meningkatkan performa model dengan menggunakan teknik-teknik machine learning yang lebih canggih. Secara keseluruhan, sistem rekomendasi makanan ini memiliki potensi besar dalam memberikan pengalaman kuliner yang lebih memuaskan dan membantu pengguna dalam menemukan makanan yang sesuai dengan selera dan preferensi mereka.

## DAFTAR PUSTAKA

- Almahmeed, M., & Alshammari, R. (2016). A content-based food recommendation approach. In 2016 7th International Conference on Information and Communication Systems (ICICS) (pp. 41-46). IEEE.

## Sumber Eksternal

- Dataset: [Kaggle: Food Recommendation System](https://www.kaggle.com/datasets/schemersays/food-recommendation-system)
