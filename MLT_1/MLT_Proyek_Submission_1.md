# Laporan Proyek Machine Learning - Indah Dwi Sulistiyawati
# Domain Proyek
Domain Proyek pada proyek ini adalah mengenai kesehatan yang di buat untuk mengetahui apakah kita mendapati penyakit stroke atau tidak. Stroke adalah penyebab kematian ketiga dan penyebab utama kecacatan jangka panjang yang serius [[1]](https://dl.acm.org/doi/abs/10.1145/1835804.1835830). Prediksi risiko stroke dapat memberikan kontribusi yang signifikan untuk pencegahan dan pengobatan dini. Sejumlah penelitian medis dan analisis data telah dilakukan untuk mengidentifikasi prediktor stroke yang efektif. 
* Latar Belakang 
![24059463_1254289268050706_637254001679480115_o](https://user-images.githubusercontent.com/79253590/137060561-cd7e599f-821e-42b9-a1cc-691b8debcbc3.jpg)

Stroke adalah sindroma klinis yang awal timbulnya mendadak dan cepat, yang berupa defisit neurologis fokal dan atau global, yang terkadang berlangsung 24 jam atau nantinya akan   langsung   menimbulkan   kematian,   dan semata-mata      disebabkan      oleh      gangguan peredaran darah otak non traumatik[[2]](https://jurnal.unimus.ac.id/index.php/JKJ/article/view/3932). Berdasarkan data Sample registrasion survey (SRS) tahun 2014, diketahui bahwa tiga besar penyebab kematian di Indonesia adalah penyakit tidak menular dengan stroke sebagai penyebab tertinggi yang diikuti oleh penyakit jantung dan pembuluh darah serta diabetes dengan komplikasi.
Sedangkan Menurut    data    yang    dikumpulkan    oleh Yayasan   Stroke   Indonesia,   masalah   stroke semakin   penting   dan   mendesak   karena   kini jumlah   penderita   stroke   di   Indonesia   adalah terbanyak  dan  menduduki  urutan  pertama  di Asia.  Jumlah  kematian  yang  disebabkan  oleh stroke menduduki urutan kedua pada usia diatas 60  tahun  dan  urutan  kelima  pada  usia  15-59 tahun[[3]](https://books.google.co.id/books?hl=id&lr=&id=_JXagiMVRykC&oi=fnd&pg=PA1&dq=Solusi+Sehat+Mengatasi+Stroke.+Tangerang:+Agro+Media&ots=tITi22j2BQ&sig=D2wboLkxsM4itV0FOUHN8IWQEnQ&redir_esc=y#v=onepage&q=Solusi%20Sehat%20Mengatasi%20Stroke.%20Tangerang%3A%20Agro%20Media&f=false). Dengan adanya model machine learning ini diharapkan dapat memudahkan ahli dalam mengetahui apakah seseorang terkena penyakit stoke atau tidak. 
# Business Understanding
# Problem Statements
Berangkat dari latar belakang diatas, rincian masalah yang dapat diselesaikan pada proyek ini adalah apakah model machine learning dapat membantu memprediksi penyakit stroke ?
# Goals
Untuk memprediksi apakah seseorang mengalami penyakit stroke atau tidak
# Solution Statements
Dalam hal ini akan didbandingan empat metode machine learning, antara lain:
* Support Vector Machine

Support Vector Machine (SVM) adalah salah satu metode diskriminatif yang paling tepat yang digunakan dalam klasifikasi.   Metode   inibekerja   berdasarkan   pada Structural Risk Minimization, yang merupakan prinsip induktif  penggunaan  dalam  pembelajaran  mesin[[4]](https://ejournal.st3telkom.ac.id/index.php/infotel/article/view/312/209). 

![svm](https://user-images.githubusercontent.com/79253590/137062345-158b3329-e0a5-48bd-90eb-b4fab6a3250d.png)

* Decision Tree

Decision    tree    merupakan    algoritma    yang    umum    digunakan    untuk   pengambilan  keputusan.  Decision  tree  akan  mencari  solusi  permasalahan  dengan  menjadikan  kriteria sebagai node yang saling berhubungan membentuk seperti struktur pohon. Decision tree adalah model prediksi terhadap suatu keputusan menggunakan struktur hirarki atau pohon.  Setiap  pohon  memiliki  cabang,  cabang  mewakili  suatu  atribut  yang  harus  dipenuhi  untuk  menuju cabang selanjutnya hingga berakhir di daun (tidak ada cabang lagi)[[5]](https://jurnal.mdp.ac.id/index.php/jatisi/article/view/78/50). 

![dt](https://user-images.githubusercontent.com/79253590/137063693-c7acb491-6ebb-41b7-923c-a74d15d477ef.png)


* Logistic Regression

Logistic Regression merupakan salah satu metode statistika yang sering digunakan untuk menganalisisdata yang mendeskripsikan antara variabel respon dengan satu atau lebih variabel prediksi. Variabel respon dari Logistic Regression bersifat dikotomi yang hanya bernilai 1 (ya) dan 0 (tidak)[[6]](https://seminar.ilkom.unsri.ac.id/index.php/ars/article/view/1932/920).

![lr](https://user-images.githubusercontent.com/79253590/137063706-51824633-bdf9-4cba-8738-381c212c2ea4.png)

* Random Forest

Metode Random Forest (RF) merupakan metode yang
dapat meningkatkan hasil akurasi, karena dalam membangkitkan simpul anak untuk setiap node dilakukan secara acak. Metode ini digunakan untuk membangun pohon keputusan yang terdiri dari root node, internal node, dan leaf node dengan mengambil atribut dan data secara acak sesuai ketentuan yang diberlakukan[[7]](https://journal.unnes.ac.id/nju/index.php/jte/article/view/10452/6660). 

![rf](https://user-images.githubusercontent.com/79253590/137063712-170bbeaf-1129-4b7a-94b5-38847c5b45d9.png)

# Data Understanding
Dataset ini diperoleh dari Kaggle [Stroke Prediction Dataset](https://www.kaggle.com/fedesoriano/stroke-prediction-dataset) yang terdiri atas 5110 data obeservasi dengan 12 atribut.

![kaggle](https://user-images.githubusercontent.com/79253590/137064097-866b822c-1632-4f76-a4e1-0b3740f27c44.png)

dimana berisi variabel-variabel berikut ini:
1. id : identifikasi pasien 

![image](https://user-images.githubusercontent.com/79253590/137066107-0683b11e-6534-4647-b484-2a4844cb77d4.png)

2. gender : berisi jenis kelamin pasien 

![image](https://user-images.githubusercontent.com/79253590/137066285-7bde5bcb-378d-44ed-9785-64e942107093.png)

3. age : umur pasien 

![image](https://user-images.githubusercontent.com/79253590/137066348-01d5befc-ae5a-4bbf-8238-590a24bcb1a4.png)

4. hypertension : 0 jika tidak memiliki hipertensi dan 1 jika memiliki hipertensi

![image](https://user-images.githubusercontent.com/79253590/137066399-8fa46ac0-0a1d-40cf-8c30-a9252a53fff2.png)

5. heart_disease: 0 jika tidak memiliki serangan jantung, 1 jika memiliki serangan jantung 

![image](https://user-images.githubusercontent.com/79253590/137066423-832404b9-3f9b-4ba7-a397-34b6726ca5a3.png)

6. ever_married: apakah pasien sudah menikah (No/Yes) 

![image](https://user-images.githubusercontent.com/79253590/137066539-70c47e48-a1f2-40b4-bdcf-2e42c958ed35.png)

7. work_type: jenis pekerjaan 

![image](https://user-images.githubusercontent.com/79253590/137066576-7c5112ea-9c53-4d3a-8225-00d7caf95a2e.png)

8. Residence_type: jenis empat tinggal 

![image](https://user-images.githubusercontent.com/79253590/137066614-a40082be-724b-4b91-bb2e-2824a83dbf05.png)

9. avg_glucose_level: rata-rata nilai gula dalam darah 

![image](https://user-images.githubusercontent.com/79253590/137066674-e6522599-0379-4985-80e6-76be39c23236.png)

10. bmi: Index massa tubuh

![image](https://user-images.githubusercontent.com/79253590/137066701-7c6b2721-b4e8-4982-8aac-df933448705f.png)

11. smoking_status: status merokoknya 

![image](https://user-images.githubusercontent.com/79253590/137066756-7cc18ef7-f79d-4cc9-ad61-97323d9dc5fa.png)

12. stroke: 0 jika tidak memiliki stroke dan 1 jika memiliki punya stroke

![image](https://user-images.githubusercontent.com/79253590/137066788-cac15bcd-0981-4b6a-81a7-35f78b05517f.png)


# Data Preparation
1. Langkah pertama yang akan dilakukan adalah proses persiapan data.
2. Penghapusan sama dan mengganti semua kolom data yang kosong dengan rata-rata nilai dari kolom tersebut.
3. Menghapus beberapa kolom yang tidak dibutuhkan yaitu id dam avg_glucose_level karena kolom tersebut tidak berkorelasi dengan kolom manapun.
4. Menghapus outliers data dimana outlier dapat mengganggu performa model.
5. Merubah semua kolom kategorikal menjadi kolom numerik.
6. Standarisasi data, dilakukan agar perbandingan jarak antar kolom satu dengan yang lain tidaklah jauh. Dalam hal ini digunakan StandardScaler pada scikit-learn.
7. Split data menjadi data train dan data test.

# Modeling
Disini akan dilakukan perbandingan 4 model, yaitu:
1. Support Vector Machine: Popular pada masalah klasifikasi
2. Decision Tree: Proses pengambilan keputusan yang kompleks menjadi lebih simple, sehingga pengambil keputusan akan lebih menginterpretasikan solusi dari permasalahan.
3. Logistic Regression: Dapat mendeskripsikan hubungan antara peubah respon (dependent variable) yang bersifat kualitatif memiliki dua kategori atau lebih dengan satu atau lebih peubah penjelas (independent variable) berskala kategori atau interval
4. Random Forest: Kombinasi dari masing – masing tree yang baik kemudian dikombinasikan ke dalam satu model dimana bergantung pada sebuah nilai vector random dengan distribusi yang sama pada semua pohon yang masing masing decision tree memiliki kedalaman yang maksimal

# Evaluasi 
Dalam hal ini akan digunakan metrik evaluasi akurasi. Dimana tabel akan mempresentasikan nilai akurasi dari masing-masing model hasil akurasi train dan test. Berikut tabelnya :

![image](https://user-images.githubusercontent.com/79253590/137066835-13bd1aba-89d8-4410-bf86-5ae53c7c5151.png)

Akan ditampilkan juga hasil plot dari tiap-tiap model

![image](https://user-images.githubusercontent.com/79253590/137066870-11b42b05-f653-4fb9-b364-fb7f8d7ce81e.png)

![image](https://user-images.githubusercontent.com/79253590/137066962-fe6671b9-813a-44f3-82fd-ea7349617154.png)

Kesimpulan dari analisis tersebut adalah dari keempat model tersebut dapat melakukan prediksi dengan baik namun, dapat dilihat berdasarkan grafik plot model Logistic Regression (LR) dan Support Vector Machine (SVM) lah yang memiliki performa hampir mirip.

# Referensi
[[1]](https://dl.acm.org/doi/abs/10.1145/1835804.1835830) Khosla, A., Cao, Y., Lin, C. C. Y., Chiu, H. K., Hu, J., & Lee, H. (2010). An integrated machine learning approach to stroke prediction. Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 183–191. https://doi.org/10.1145/1835804.1835830

[[2]](https://jurnal.unimus.ac.id/index.php/JKJ/article/view/3932) Oktamiati,  H.  (2014).  Analisis  Praktik  Klinik Keperawatan      Kesehatan      Masyarakat Perkotaan Pada Pasien Stroke Hemoragik  Di  Ruang  Rawat  Melati  Atas RSUP Persahabatan. Depok: Fakultas Ilmu Keperawatan UI. 

[[3]](https://books.google.co.id/books?hl=id&lr=&id=_JXagiMVRykC&oi=fnd&pg=PA1&dq=Solusi+Sehat+Mengatasi+Stroke.+Tangerang:+Agro+Media&ots=tITi22j2BQ&sig=D2wboLkxsM4itV0FOUHN8IWQEnQ&redir_esc=y#v=onepage&q=Solusi%20Sehat%20Mengatasi%20Stroke.%20Tangerang%3A%20Agro%20Media&f=false) Yastroki. (2012). Solusi Sehat Mengatasi Stroke. Tangerang: Agro Media

[[4]](https://ejournal.st3telkom.ac.id/index.php/infotel/article/view/312/209) Widiastuti, N. I., Rainarli, E., & Dewi, K. E. (2017). Peringkasan dan Support Vector Machine pada Klasifikasi Dokumen. Jurnal Infotel, 9(4), 416. https://doi.org/10.20895/infotel.v9i4.312

[[5]](https://jurnal.mdp.ac.id/index.php/jatisi/article/view/78/50) Sartika, D., & Indra, D. (2017). Perbandingan Algoritma Klasifikasi Naive Bayes, Nearest Neighbour, dan Decision Tree pada Studi Kasus Pengambilan Keputusan Pemilihan Pola Pakaian. Jurnal Teknik Informatika Dan Sistem Informasi, 1(2), 151–161.

[[6]](https://seminar.ilkom.unsri.ac.id/index.php/ars/article/view/1932/920) (Bimantara & Dina, 2019)Bimantara, A., & Dina, T. A. (2019). Klasifikasi Web Berbahaya Menggunakan Metode Logistic Regression. Annual Research Seminar (ARS), 4(1), 173–177.

[[7]](https://journal.unnes.ac.id/nju/index.php/jte/article/view/10452/6660) Komunikasi, F., Surakarta, U. M., Yani, J. A., & Pos, T. (2017). Sistem Klasifikasi Variabel Tingkat Penerimaan Konsumen Terhadap Mobil Menggunakan Metode Random Forest. Jurnal Teknik Elektro, 9(1), 24–29. https://doi.org/10.15294/jte.v9i1.10452





