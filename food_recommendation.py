# -*- coding: utf-8 -*-
"""Food Recommendation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xX86jGJEVgiayHiUeXb_17UBIWXEUkMI

## File Preparation
**Instal kaggle and upload kaggle.json file**
"""

! pip install -q kaggle

from google.colab import files
files.upload()

"""**Download datasets from kaggle**"""

! mkdir ~/.kaggle
! cp kaggle.json ~/.kaggle/
! chmod 600 ~/.kaggle/kaggle.json
! kaggle datasets list

! kaggle datasets download -d schemersays/food-recommendation-system

"""**Create datasets directory and unzip file**"""

! mkdir datasets
! unzip food-recommendation-system.zip -d datasets

"""## Data Understanding
**Import main lib**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""**Load data file**"""

food_df = pd.read_csv('datasets/1662574418893344.csv')
rating_df = pd.read_csv('datasets/ratings.csv')

"""**Liat data food**"""

food_df.head()

"""**Liat food dataframe info dan unik data berdasarkan Food_ID dan C_Type**"""

food_df.info()
print('Banyak data makanan: ', len(food_df.Food_ID.unique()))
print('Banyak tipe makanan: ', len(food_df.C_Type.unique()))
print('Tipe makanan: ', food_df.C_Type.unique())
print('Jenis makanan: ', food_df.Veg_Non.unique())

"""**Cek jika ada data null atau duplikat pada data food**"""

# Cek jika ada data null pada data food
food_df.isnull().sum()

# Cek jika ada data duplikat pada data food
food_df.duplicated().sum()

"""**Liat deskripsi data food**"""

food_df.describe()

"""**Liat data rating**"""

rating_df.head()

"""**Liat rating dataframe info dan jumlah unik data berdasarkan User_ID**"""

rating_df.info()
print('Jumlah data rating: ', len(rating_df))
print('Jumlah user yang memberi review: ', len(rating_df.User_ID.unique()))
print('Nilai rating min: ', rating_df.Rating.min())
print('Nilai rating max: ', rating_df.Rating.max())

"""**Cek jika ada data null atau duplikat pada data rating**"""

# Cek jika ada data null pada rating
rating_df.isnull().sum()

# Liat data null
rating_df.tail()

# Drop data null di row terakhir 511 pada data rating
rating_df = rating_df.dropna()
rating_df.isnull().sum()

# cek jika ada data duplicate pada rating
rating_df.duplicated().sum()

"""## Univariate Analysis

**Menggabungkan data food dan rating**
"""

# Merge rating_df dan food_df berdasarkan Food_ID
fix_food_df = pd.merge(rating_df, food_df, on='Food_ID', how='left')

# Sort Berdasarkan Food_ID
fix_food_df = fix_food_df.sort_values('Food_ID', ascending=True)
fix_food_df

# Cek jika terdapat data null pada fix_food_df
fix_food_df.isnull().sum()

# Mengecek berapa jumlah fix_food_df berdasarkan preferensi user
len(fix_food_df.Food_ID.unique())

# Mengecek kategori C_Type yang unik
fix_food_df.C_Type.unique()

"""**Persentase dan visualisasi data food berdasarkan preferensi user**"""

# buat fungsi visualisasi fitur
def visualization_feature(df, feature):
  count = df[feature].value_counts()
  percent = 100*df[feature].value_counts(normalize=True)
  df = pd.DataFrame({'Total sample':count, 'percentage':percent.round(1)})
  print(df)
  count.plot(kind='bar', title=feature);

# visualisasi fitur C_Type
visualization_feature(fix_food_df, 'C_Type')

# visualisasi fitur Veg_Non
visualization_feature(fix_food_df, 'Veg_Non')

# visualisasi fitur Rating
visualization_feature(fix_food_df, 'Rating')

"""## Data Preparation"""

# Membuang data yang duplicate
food_content_df = fix_food_df.drop_duplicates('Food_ID')
food_content_df

# Buat fitur baru gabungan content yang relevan
relevan_features = ['C_Type', 'Veg_Non', 'Describe']

# Mix relevan_features menjadi fitur baru
# Dengan cara menggabung setiap string fitur
def join_features_content(df):
    return df[relevan_features[0]] + " " + df[relevan_features[1]] + " " + df[relevan_features[2]]

# Terapkan penggabungan string fitur ke feature baru 'content'
food_content_df['Description'] = food_content_df.apply(join_features_content, axis=1)

# Cek hasil data food_content_df
food_content_df.head()

import string

# Buat fungsi untuk menghapus tanda baca pada text
def punctuation_cleaning(text):
    clear_text  = "".join([char for char in text if char not in string.punctuation])
    return clear_text

# Hapus text tanda baca pada fitur Content
# Replace fitur Content dengan text yang sudah di bersihkan
food_content_df['Description'] = food_content_df['Description'].apply(punctuation_cleaning)
food_content_df['Description']

# Mengonversi data series Food_ID ke bentuk list
food_id = food_content_df['Food_ID'].tolist()

# Mengonversi data series Name ke bentuk list
food_name = food_content_df['Name'].tolist()

# Mengonversi data series Description ke bentuk list
food_description = food_content_df['Description'].tolist()

print(len(food_id))
print(len(food_name))
print(len(food_description))

# Membuat dataframe baru yang hanya ada fitur yang relevan saja
final_food = pd.DataFrame({
    'id': food_id,
    'food_name': food_name,
    'food_description': food_description
})
final_food

"""## Content Based Filtering

**Menggunakan CountVectorizer untuk mengonversi kumpulan dokumen teks menjadi matriks jumlah token**
"""

from sklearn.feature_extraction.text import CountVectorizer

# Inisialisasi CountVectorizer
cv = CountVectorizer(stop_words='english', ngram_range=(1, 3))

# Melakukan fit lalu ditransformasikan ke bentuk matrix pada data Content
cv_matrix = cv.fit_transform(final_food['food_description'])

# Mapping array dari fitur index integer ke fitur nama
cv.get_feature_names_out()

# Lihat dimensi tfidf_matrix
cv_matrix.shape

# Mengubah vektor countvectorizer dalam bentuk matriks dengan fungsi todense()
cv_matrix.todense()

# Melihat tf-idf matrix dalam bentuk dataframe
# Kolom diisi dengan nama makanan
# Baris diisi dengan content makanan

pd.DataFrame(
    cv_matrix.todense(),
    columns=cv.get_feature_names_out(),
    index=final_food.food_name
).sample(22, axis=1).sample(10, axis=0)

"""**Menghitung kesamaan konten menggunakan Cosine Similiarity**"""

from sklearn.metrics.pairwise import cosine_similarity

# Meggunakan cosine_similarity untuk membuat menghitung kesamaan konten
cosine_similiarities = cosine_similarity(cv_matrix, cv_matrix)
cosine_similiarities

"""**Menghitung kesamaan konten menggunakan Cosine Similiarity**"""

from sklearn.metrics.pairwise import pairwise_distances

# Meggunakan jaccard similarity untuk membuat menghitung kesamaan konten
# Ubah data sparse matrix ke array
cv_array = cv_matrix.toarray()
jaccard_sim = 1 - pairwise_distances(cv_array, metric="jaccard")

# Menyetel ulang indeks dan menarik keluar nama makanan dari dataframe food_content_df
indices = pd.Series(final_food.index, index=final_food['food_name'])
print(indices)

# Buat fungsi untuk mendapatkan rekomendasi
def get_recommendations(name, method_sim):
  food_index = indices[name]
  sim_weight = list(enumerate(method_sim[food_index]))
  sim_weight = sorted(sim_weight, key=lambda x: x[1], reverse=True)

  # Mendapatkan skor similiarity top-n
  sim_weight = sim_weight[1:6]

  # Kumpulkan index top-n similiarity weight
  food_indices = [i[0] for i in sim_weight]

  # Show hasil dataframe berdasarkan index top-n similiarity weight
  return final_food.iloc[food_indices]

"""**Mendapatkan top 5 rekomendasi makanan menggunakan cosine similiarity**"""

food_name = 'roast turkey with cranberry sauce'
cosine_sim_recommend = get_recommendations(food_name, cosine_similiarities)
cosine_sim_recommend

"""**Mendapatkan top 5 rekomendasi makanan menggunakan Jaccard Similarity**"""

jaccard_recommend = get_recommendations(food_name, jaccard_sim)
jaccard_recommend

"""## Evaluasi Model

**Melihat detail makanan yang akan dicari rekomendasinya**
"""

user_food = final_food.loc[final_food['food_name'] == food_name]
user_food

# Dari sampel makanan yang disukai diatas, kita dapat liat attributnya
attributes = user_food['food_description'].iloc[0].split(' ')
count = len(attributes)
attr_df = pd.DataFrame({'food_description':attributes})
attr_df

"""### Bandingkan attribute dari user_food dengan hasil rekomendasi untuk menentukan kriteria
- True Positive (TP): Item yang benar-benar disukai dan direkomendasikan dengan benar.
- False Positive (FP): Item yang tidak disukai tetapi direkomendasikan.
- True Negative (TN): Item yang tidak disukai dan tidak direkomendasikan.
- False Negative (FN): Item yang benar-benar disukai tetapi tidak direkomendasikan.

**- Pembuktian hasil rekomendasi Cosine similiarity**

Bandingkan atribut-atribut dari hasil rekomendasi cosine similiarity dengan atribut user_food 'roast turkey with cranberry sauce'
Kita lihat minimal dari **2 attribut awal** yaitu **Healthy Food, nonveg**, dll

Dari Hasil 5 rekomendasi, terdapat 4 data yang sesuai dan 1 data yang tidak sesuai yaitu makanan 'carrot ginger soup' dengan atribut **Healthy Food, veg**, ...

Setelah itu hasilnya kita masukan pada fitur baru actual_item
"""

# Buat kolom baru 'outcome' untuk menampung nilai hasil Cosine similiarity
conf_matrix_cosine_sim = cosine_sim_recommend
conf_matrix_cosine_sim['actual_item'] = [
    'chicken minced salad',
    'roasted spring chicken with root veggies',
    'microwave chicken steak',
    'half roast chicken',
    'fish andlouse']
conf_matrix_cosine_sim

"""**- Pembuktian hasil rekomendasi Jaccard similiarity**

Bandingkan atribut-atribut dari hasil rekomendasi cosine similiarity dengan atribut user_food 'roast turkey with cranberry sauce'
Kita lihat minimal dari **2 attribut awal** yaitu **Healthy Food, nonveg**, dll

Dari Hasil 5 rekomendasi, terdapat 3 data yang sesuai dan 2 data yang tidak sesuai yaitu makanan 'carrot ginger soup' dan 'fish andlouse' yang mempunyai atribut **Healthy Food, veg**, ...

Setelah itu hasilnya kita masukan pada fitur baru actual_item
"""

# Buat kolom baru 'outcome' untuk menampung nilai hasil Jaccard similiarity
conf_matrix_jaccard_sim = jaccard_recommend
conf_matrix_jaccard_sim['actual_item'] = [
    'roasted spring chicken with root veggies',
    'chicken minced salad',
    'microwave chicken steak',
    'half roast chicken',
    'fish andlouse']
conf_matrix_jaccard_sim

"""### Menilai performa indikator menggunakan Precision, Recall dan F1 Score"""

# Fungsi untuk menghitung precision
def precision(actual_items, recommended_items):
    # Ubah list menjadi set untuk menghitung irisan dengan mudah
    actual_set = set(actual_items)
    recommended_set = set(recommended_items)

    # Hitung jumlah item yang direkomendasikan dengan benar
    true_positives = len(actual_set.intersection(recommended_set))

    # Hitung precision
    precision = true_positives / len(recommended_set)

    return precision

# Fungsi untuk menghitung recall
def recall(actual_items, recommended_items):
    # Ubah list menjadi set untuk menghitung irisan dengan mudah
    actual_set = set(actual_items)
    recommended_set = set(recommended_items)

    # Hitung jumlah item yang direkomendasikan dengan benar
    true_positives = len(actual_set.intersection(recommended_set))

    # Hitung recall
    recall = true_positives / len(actual_set)

    return recall

# Fungsi untuk menghitung F1-score
def f1_score(actual_items, recommended_items):
    # Hitung precision dan recall
    prec = precision(actual_items, recommended_items)
    rec = recall(actual_items, recommended_items)

    # Hitung F1-score
    f1 = 2 * (prec * rec) / (prec + rec)

    return f1

actual_items_cosine = conf_matrix_cosine_sim['actual_item'].to_numpy()
actual_items_jaccard = conf_matrix_jaccard_sim['actual_item'].to_numpy()
cosine_recommend_items = conf_matrix_cosine_sim['food_name'].to_numpy()
jaccard_recommend_items = conf_matrix_jaccard_sim['food_name'].to_numpy()

eval_df = pd.DataFrame(columns=['Cosine Similiarity', 'Jaccard Similiarity'], index=['Precision','Recall','F1-score'])

# Dictionary untuk setiap hasil evaluasi
cosine_dict = {
    'Precision': precision(actual_items_cosine, cosine_recommend_items),
    'Recall': recall(actual_items_cosine, cosine_recommend_items),
    'F1-score': f1_score(actual_items_cosine, cosine_recommend_items)
    }

jaccard_dict = {
    'Precision': precision(actual_items_jaccard, jaccard_recommend_items),
    'Recall': recall(actual_items_jaccard, jaccard_recommend_items),
    'F1-score': f1_score(actual_items_jaccard, jaccard_recommend_items)
    }

# Kalkulasi precision, recall, dan f1-score pada setiap metode similiarity
for name, model in cosine_dict.items():
    eval_df.loc[name, 'Cosine Similiarity'] = model

for name, model in jaccard_dict.items():
    eval_df.loc[name, 'Jaccard Similiarity'] = model

eval_df

"""Dapat dilihat bahwa hasil **Cosine Similiarity** lebih baik dibandingkan **Jaccard Similiarity** dengan **F1-Score 0.8 > 0.6**

**Kesimpulan**

Kesimpulan hasil dari sistem rekomendasi top-n menggunakan metode cosine similarity dan Jaccard Similarity sebagai berikut:

1. Cosine Similarity:
   - Metode cosine similarity digunakan untuk mengukur kesamaan arah antara dua vektor dalam ruang vektor.
   - Sistem rekomendasi top-n menggunakan cosine similarity dapat memberikan rekomendasi berdasarkan kesamaan konten antara item-item dalam dataset makanan, seperti deskripsi resep makanan.
   - Semakin tinggi nilai cosine similarity antara dua item, semakin mirip mereka dalam hal konten atau atribut yang dimiliki.
   - Hasil rekomendasi berdasarkan cosine similarity dapat membantu pengguna menemukan resep makanan yang serupa atau relevan dengan preferensi mereka.

2. Jaccard Similarity:
   - Jaccard Similarity digunakan untuk mengukur perbedaan antara dua himpunan berdasarkan elemen-elemen yang sama di antara keduanya.
   - Sistem rekomendasi top-n menggunakan Jaccard Similarity dapat memberikan rekomendasi berdasarkan kesamaan himpunan kata-kata atau fitur dalam deskripsi resep makanan.
   - Semakin rendah nilai Jaccard Similarity antara dua item, semakin mirip himpunan kata-kata atau fitur yang dimiliki.
   - Hasil rekomendasi berdasarkan Jaccard Similarity dapat membantu pengguna menemukan resep makanan dengan kata-kata atau fitur yang serupa dengan preferensi mereka.

Kedua metode, cosine similarity dan Jaccard Similarity, dapat memberikan hasil rekomendasi yang bermanfaat dalam sistem rekomendasi makanan berdasarkan konten. Pemilihan metode yang tepat tergantung pada karakteristik dataset dan tujuan rekomendasi yang ingin dicapai. Adapun evaluasi performa dan kualitas rekomendasi dari kedua metode tersebut dapat dilakukan dengan menggunakan metrik evaluasi seperti precision, recall dan F1-Score.
"""