# Laporan Proyek Machine Learning - Indah Dwi Sulistiyawati
# Project Overview

![image](https://user-images.githubusercontent.com/79253590/138224597-e5bb8e4e-ae65-4c87-b2b9-0d6c50b41c2f.png)

Membaca adalah melihat serta memahami isi dari apa yang tertulis, dengan melisankan atau hanya melafalkan dalam hati. Membaca yang dimaksudkan dalam penelitian ini adalah kegiatan yang mewujudkan lahirnya komunikasi antara seseorang dan bahan-bahan bacaan sebagai salah satu bentuk upaya pemenuhan kebutuhan dan tujuan tertentu. Sehingga dalam hal ini yang dimaksud dengan minat baca adalah keinginan yang kuat yang timbul dalam diri seseorang untuk melakukan kegiatan membaca sebagai bentuk upaya dalam pemenuhan kebutuhan dan tujuan tertentu [[1]](http://lib.unnes.ac.id/2202/1/4308.pdf). 

Menurut data statistik [picodi.com](https://www.picodi.com/id/mencari-penawaran/pembelian-buku-di-indonesia-dan-di-seluruh-dunia) menunjukkan bahwa permintaan buku di toko buku online meningkat paling tinggi di bulan Desember (12% dari semua transaksi tahunan) dimana angka tersebut dilakukan melalui survei tren *customer*. Sebanyak 47% menyatakan bahwa mereka membeli buku di toko buku konvensional, lebih sedikit pembaca sekitar 31% meminjam dari perpustakaan, serta hanya 12% yang meminjam dari teman. Sisanya sebanyak 10% mengakui bahwa mereka tidak banyak membaca atau sama sekali tidak tertarik pada buku.

Salah satu faktor yang membuat seseorang tidak banyak membaca adalah kebingungan dalam menentukan buku mana saja yang sesuai dengan jenis yang disuka dan buku apa saja yang cocok berdasarkan judul buku yang dibaca. Oleh karena itu, dalam hal ini akan dibuat sistem rekomendasi buku berdasarkan preferensi pengguna dan rating yang telah diberikan oleh pengguna sebelumnya. Sistem rekomendasi saat ini telah banyak digunakan dalam memberikan rekomendasi kepada seseorang sehingga dapat mempermudah seseorang dalam mengambil keputusannya. Sistem rekomendasi merupakan salah satu sistem yang mampu mengelola informasi dari data historis pengguna seperti jumlah beli, rating,
lainnya dan memberi saran atau rekomendasi kepada pengguna [[2]](https://d1wqtxts1xzle7.cloudfront.net/35130578/216-222-knsi2010-037-analisis-dan-implementasi-metode-item-based-clustering-hybrid-pada-recommender-system-with-cover-page-v2.pdf?Expires=1634801276&Signature=ckV~k210NzS5aQVM9SyB~YoyeXNt2w2JsuPigoWOy84Qm~CA83O4wqv5OZLybbqKL10tD32wPe~0lROCcvOptvOY6J-Y5DcWfYLzKbzDtegB5CcV7~ZwBHjY~XHGUQPFQKB7vFFb7NZ9SI58D5VBxNqpsiP~S7m0~PzMG7pm-xtFZgP84oYsVsfL3PqEoEZAL09NmKEXq1FFnj2hzGo0cKRP8kAEC3X0GW1ZUvK6WL0HetXbJAYMbZPmro5e4r2oyuUNrIsF~0Dur4w7XudJ2WA6pCaVg~JcMloWV9W0HHSAgNWLuarH6RHneh0WWKwv4PC2AlMMoQyC8JiU7nPriQ__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA). 

# Business Understanding
# Problem Statements

Setelah mengetahui beberapa masalah diatas, berikut ini merupakan rincian masalah yang perlu diselesaikan di proyek ini:
* Bagaimana mengolah data buku, user, dan rating untuk digunakan sebagai informasi dalam sistem rekomendasi?
* Bagaimana cara membuat sistem rekomendasi buku ?

# Goals

Berikut adalah tujuan dari dibuatnya proyek ini:
* Mengetahui cara mengolah data buku, user, dan rating untuk digunakan pada sistem rekomendasi.
* Membuat sistem rekomendasi buku.

# Solution approach

Solusi yang dapat dilakukan untuk memenuhi tujuan dari proyek ini diantaranya :
* Pra-pemrosesan data 
  Dalam hal ini akan dilakukan analisis karakteristik dari ketiga data (books, users, ratings) sebelum masuk ke dalam tahap *preparation*
  * *books*
  
    ![image](https://user-images.githubusercontent.com/79253590/138228844-f7fb87b9-5b1d-4b9b-ad79-1acc98e8527a.png)
  
  * *ratings*
    
    ![image](https://user-images.githubusercontent.com/79253590/138228932-31f9dbdf-aeb0-4d80-a1ef-310dd552f253.png)
    
  * *users*
    
    ![image](https://user-images.githubusercontent.com/79253590/138229003-7cc2bfe1-f351-48b7-86d7-a132ef44db2c.png)
    
* Persiapan data

  Dalam hal ini akan dilakukan seleksi fitur-fitur yang diperlukan.
  * *books* : mengisi data kosong pada publisher dan author
  * *ratings* : menghapus data dengan rating 0
  * *users* : mengisi *missing value* menggunakan modus *Age*
  
*  Solusi yang diberikan bergantung dengan hasil rekomendasi yang ingin dicapai dan data yang dimiliki, yaitu : 

   *  *Popularity based recommendation* 
      
      Sistem rekomendasi berdasarkan Popularitas bekerja dengan tren. Ini pada dasarnya menggunakan item yang sedang tren saat ini. Misalnya, jika ada produk yang biasanya dibeli oleh setiap pengguna baru, maka ada kemungkinan produk tersebut akan menyarankan item tersebut kepada pengguna yang baru saja mendaftar [[3]](https://medium.com/the-owl/recommender-systems-f62ad843f70c). Teknik yang akan digunakan adalah *weighted rating*. Teknik ini dapat berguna untuk merekomendasikan buku kepada seluruh pengguna baik yang belum memiliki riwayat transaksi maupun yang sudah.
      
   * *Content-Based Recommendation*
      
      Merekomendasikan buku berdasarkan kemiripan Author terhadap pengguna yang melakukan transaksi pada buku tersebut. Kelebihan teknik ini tidak membutuhkan data transaksi dari user lain karena rekomendasi spesifik untuk user tersebut. Sehingga mempermudah merekomendasikan buku pada jumlah pengguna yang sangat besar. Sedangkan kekurangannya, rekomendasi hanya terbatas pada interest dari pengguna dan tidak bisa memperluas interest tersebut.  
      
   * *Model-Based Collaborative filtering Recommendation*
      
      Merekomendasikan buku berdasarkan riwayat transaksi (rating) pengguna untuk memprediksi dan menghitung rating yang akan diberikan pengguna pada buku lain menggunakan model machine learning SVD. Algoritma berbasis matrix factorization ini dipopulerkan oleh Simon Funk pada Netflix Prize. Kekurangan dari collaborative filtering tidak bisa merekomendasikan item yang tidak memiliki riwayat transaksi.
      
# Data Understanding

![image](https://user-images.githubusercontent.com/79253590/138232232-5c0e24cd-af12-4d65-9fd1-c9fcd7cd082f.png)

Tabel dibawah ini merupakan informasi dari dataset yang digunakan :
|           Jenis         |  Keterangan |
| ----------------------- | ----------- |
|           Sumber        | [Kaggle Dataset : Book Recommendation Dataset](https://www.kaggle.com/arashnic/book-recommendation-dataset)|
|         Usability       | 10.0 |
|          Lisensi        | CC0: Public Domain |
| Jenis dan Ukuran Berkas | zip (107MB) |

Dalam dataset tersebut berisi 3 file csv, yaitu:

* *Books* 
  
  Berisi informasi buku: 
  * *Book-Title*: judul
  * *Book-Author*: penulis
  * *Year-Of-Publication*: Tahun terbit
  * *Publisher*: Penerbit
  * *Image-URL-S*, *Image-URL-M, Image-URL-L* : link sampul buku
  
* *Ratings*
  
  Berisi informasi rating buku dari user
  * *Book-Rating*: rating buku 
  
* *Users*
  
  Berisi informasi user
  * *UserID*: identitas unik user berupa integer agar user anonymous
  * *Location*: lokasi tempat tinggal use
  * *Age*: umur user

# Data Preparation

Dalam tahap  ini akan dilakukan proses transformasi pada data sehingga menjadi bentuk yang cocok untuk proses pemodelan. Ada beberapa tahapan yang dilakukan pada data preparation, antara lain :

* *Handling Missing Value*
  
  Proses mengolah missing value (ex: data umur yang null, data rating 0) dengan menghapus atau mengganti data tersebut dengan value lain.
  
* *Encoding* 
  
   Melakukan encoding data UserID dan Book Title agar dapat dibaca model dengan baik.
   
* Transformasi Data
  
  Mentransformasikan book author menjadi matrix dengan TF-IDF Vectorizer untuk mengidentifikasi korelasi antara buku dan authornya.
  
* *Merge* Data
 
  Menggabungkan data rating dan buku untuk dijadikan dataset.

# Modelling

   * *Popularity based recommendation* 
      
      Digunakan untuk menggabungkan informasi rata-rata rating dan jumlah rating yang diterima per buku dengan menerapkan *weighted rating*, kemudian memilih 10 produk terbaik . Berikut rumus dari *weighted rating* :
      
      *Weighted Rating* = (Rv + Cm) / (v + m), 
      keterangan :
      * v adalah jumlah rating diterima per buku 
      * R adalah rata-rata rating per buku
      * C adalah rata-rata rating seluruh buku
      * m adalah minimal jumlah rating yang diterima. 
      
      ![image](https://user-images.githubusercontent.com/79253590/138235856-811f8ac7-2233-4ac9-a3f0-59e4e96527b2.png)
      
      Plot hasil rekomendasi dengan menerapkan *weighted rating* sebagai berikut:
      
      ![image](https://user-images.githubusercontent.com/79253590/138238337-6f7a03f5-38d0-45cb-8181-afcff0c6863f.png)
      
   * *Content-Based Recommendation*
      
      Akan dilakukan perhitungan skor kesamaan menggunakan kesamaan kosinus untuk menghitung kuantitas numerik yang menunjukkan kesamaan antara dua kategori. Dalam hal ini menerapkan skor kesamaan kosinus karena tidak tergantung pada besarnya dan relatif mudah dan cepat untuk dihitung. Secara matematis, didefinisikan sebagai berikut:

      ![image](https://user-images.githubusercontent.com/79253590/138236911-1336b352-e704-4c66-bdb4-e3905200916a.png)
      
      Hasil rekomendasinya adalah sebagai berikut:
      
      ![image](https://user-images.githubusercontent.com/79253590/138238613-62c04673-02d5-4537-870b-c042ece8d2f0.png)
      
   * *Model-Based Collaborative filtering Recommendation*
      
      Akan dilakukan *training data user* buku dengan model SVD dari library Surprise yang selanjutnya 10 buku dengan prediksi rating tertinggi akan diurutkan.
      Hasil rekomendasinya sebagai berikut:
      
      ![image](https://user-images.githubusercontent.com/79253590/138238871-364eb510-d58d-4097-a957-4c58acce83f3.png)
      
# Evaluasi

Pada *content-based recommendation* akan digunakan *precision* sebagai metrik evaluasi. *Precision* adalah jumlah item rekomendasi yang relevan. Secara matematis dapat dituliskan dengan rumus sebagai berikut.

![image](https://user-images.githubusercontent.com/79253590/138541659-204c6de6-dbab-446e-a052-3356fd6671be.png)

Berdasarkan hasil rekomendasi menggunakan *content-based recommendation* yakni sebagai berikut

![image](https://user-images.githubusercontent.com/79253590/138238613-62c04673-02d5-4537-870b-c042ece8d2f0.png)
 
Diperoleh *precision* = 10/10 . Sehingga presisinya adalah sebesar 100 %.

Selanjutnya, untuk hasil evaluasi dari model SVD menggunakan metode *k-fold cross validation*. Metode ini adalah salah satu dari jenis pengujian *cross validation* yang berfungsi untuk menilai kinerja proses sebuah metode algoritme dengan membagi sampel data secara acak dan mengelompokkan data tersebut sebanyak nilai *K fold*. Dimana data training adalah K-1 fold dan sisanya digunakan sebagai data testing. Kemudian hasil testing dihitung dengan matriks:

1. *Mean Absolute Error* (MAE)
    
    Merepresentasikan rata-rata perbedaan mutlak antara nilai aktual dan prediksi pada dataset. MAE mengukur rata-rata residu dalam dataset. MAE lebih intuitif dalam memberikan rata-rata error dari keseluruhan data.
    
    ![image](https://user-images.githubusercontent.com/79253590/138239741-58eadce7-8fbf-462e-88d9-8b954b22403f.png)
    
2. *Root Mean Squared Error* (RMSE)

    Cara menghitungnya yaitu dengan mengkuadratkan error (prediksi – observasi) dibagi dengan jumlah data (= rata-rata), lalu diakarkan. 
    
    ![image](https://user-images.githubusercontent.com/79253590/138239899-3ce11efc-09c7-4889-904e-fff9a1ea7265.png)
    
 
Dalam proses analisis kali ini, data user buku akan di training dengan model SVD dari library surprise dan mengevaluasi dengan 10-fold cross validation menggunakan matriks RMSE dan MAE. Validasi silang 10 kali lipat akan melakukan prosedur pemasangan sebanyak sepuluh kali, dengan masing-masing pemasangan dilakukan pada set pelatihan yang terdiri dari 90% dari total set pelatihan yang dipilih secara acak, dengan 10% sisanya digunakan sebagai set penahan untuk validasi. 10 fold CV adalah salah satu K fold CV yang direkomendasikan untuk pemilihan model terbaik karena cenderung memberikan estimasi akurasi yang kurang bias dibandingkan dengan CV biasa, leave-one-out CV dan bootstrap.
Hasil dari perhitungannya adalah sebagai berikut:

![image](https://user-images.githubusercontent.com/79253590/138240014-7455c6f4-6f94-44ef-be92-62158d1c9446.png)

Dalam perhitungan ini, diperoleh nilai rata-rata *Mean Absolute Error* (MAE) sebesar 1.63 dan nilai rata-rata *Root Mean Squared Error* (RMSE) sebesar 1.26 . Sehinggan dapat kita buat kesimpulan bahwa pada model ini nilai error nya cukup kecil sehingga menandakan model tersebut sudah baik. Hal ini dibuktikan juga dengan hasil rekomendasi buku yang cukup baik dan sesuai kategorinya.

   
# Referensi

[[1]](http://lib.unnes.ac.id/2202/1/4308.pdf) Hayati, N. (2009). Faktor-Faktor Yang Mempengaruhi Minat Baca Buku Referensi Mata Pelajaran Sosiologi (Kaus Siswa SMA Negeri 1 Sukorejo Kendal Tahun Ajaran 2008/2009). Faktor-Faktor Yang Mempengaruhi Minat Baca Buku Referensi Mata Pelajaran Sosiologi (Kaus Siswa SMA Negeri 1 Sukorejo Kendal Tahun Ajaran 2008/2009), 3(2), 94.

[[2]](https://d1wqtxts1xzle7.cloudfront.net/35130578/216-222-knsi2010-037-analisis-dan-implementasi-metode-item-based-clustering-hybrid-pada-recommender-system-with-cover-page-v2.pdf?Expires=1634801276&Signature=ckV~k210NzS5aQVM9SyB~YoyeXNt2w2JsuPigoWOy84Qm~CA83O4wqv5OZLybbqKL10tD32wPe~0lROCcvOptvOY6J-Y5DcWfYLzKbzDtegB5CcV7~ZwBHjY~XHGUQPFQKB7vFFb7NZ9SI58D5VBxNqpsiP~S7m0~PzMG7pm-xtFZgP84oYsVsfL3PqEoEZAL09NmKEXq1FFnj2hzGo0cKRP8kAEC3X0GW1ZUvK6WL0HetXbJAYMbZPmro5e4r2oyuUNrIsF~0Dur4w7XudJ2WA6pCaVg~JcMloWV9W0HHSAgNWLuarH6RHneh0WWKwv4PC2AlMMoQyC8JiU7nPriQ__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA) Djamal, R.A., Maharani, W. & Kurniati, P. 2010. Analisis Dan Implementasi Metode Item-Based Clustering Hybrid Pada Recommender System. Konferensi Nasional Sistem dan Informatika, (November): 216–222.

[[3]](https://medium.com/the-owl/recommender-systems-f62ad843f70c) Saumyadeepta, Sen. (2020, July 06). Recommender Systems. Medium. https://medium.com/the-owl/recommender-systems-f62ad843f70c

[[4]](https://scikit-learn.org/stable/modules/metrics.html#cosine-similarity) scikit-learn.Cosine-Similarity.https://scikit-learn.org/stable/modules/metrics.html#cosine-similarity


