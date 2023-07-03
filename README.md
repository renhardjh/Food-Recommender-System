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
