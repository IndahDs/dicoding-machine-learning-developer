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

* Logistic Regression

Logistic Regression merupakan salah satu metode statistika yang sering digunakan untuk menganalisisdata yang mendeskripsikan antara variabel respon dengan satu atau lebih variabel prediksi. Variabel respon dari Logistic Regression bersifat dikotomi yang hanya bernilai 1 (ya) dan 0 (tidak)[[6]](https://seminar.ilkom.unsri.ac.id/index.php/ars/article/view/1932/920).

* Random Forest

Metode Random Forest (RF) merupakan metode yang
dapat meningkatkan hasil akurasi, karena dalam membangkitkan simpul anak untuk setiap node dilakukan secara acak. Metode ini digunakan untuk membangun pohon keputusan yang terdiri dari root node, internal node, dan leaf node dengan mengambil atribut dan data secara acak sesuai ketentuan yang diberlakukan[[7]](https://journal.unnes.ac.id/nju/index.php/jte/article/view/10452/6660). 

# Referensi
[[1]](https://dl.acm.org/doi/abs/10.1145/1835804.1835830) Khosla, A., Cao, Y., Lin, C. C. Y., Chiu, H. K., Hu, J., & Lee, H. (2010). An integrated machine learning approach to stroke prediction. Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 183–191. https://doi.org/10.1145/1835804.1835830
[[2]](https://jurnal.unimus.ac.id/index.php/JKJ/article/view/3932) Oktamiati,  H.  (2014).  Analisis  Praktik  Klinik Keperawatan      Kesehatan      Masyarakat Perkotaan Pada Pasien Stroke Hemoragik  Di  Ruang  Rawat  Melati  Atas RSUP Persahabatan. Depok: Fakultas Ilmu Keperawatan UI. 
[[3]](https://books.google.co.id/books?hl=id&lr=&id=_JXagiMVRykC&oi=fnd&pg=PA1&dq=Solusi+Sehat+Mengatasi+Stroke.+Tangerang:+Agro+Media&ots=tITi22j2BQ&sig=D2wboLkxsM4itV0FOUHN8IWQEnQ&redir_esc=y#v=onepage&q=Solusi%20Sehat%20Mengatasi%20Stroke.%20Tangerang%3A%20Agro%20Media&f=false) Yastroki. (2012). Solusi Sehat Mengatasi Stroke. Tangerang: Agro Media
[[4]](https://ejournal.st3telkom.ac.id/index.php/infotel/article/view/312/209) Widiastuti, N. I., Rainarli, E., & Dewi, K. E. (2017). Peringkasan dan Support Vector Machine pada Klasifikasi Dokumen. Jurnal Infotel, 9(4), 416. https://doi.org/10.20895/infotel.v9i4.312
[[5]](https://jurnal.mdp.ac.id/index.php/jatisi/article/view/78/50) Sartika, D., & Indra, D. (2017). Perbandingan Algoritma Klasifikasi Naive Bayes, Nearest Neighbour, dan Decision Tree pada Studi Kasus Pengambilan Keputusan Pemilihan Pola Pakaian. Jurnal Teknik Informatika Dan Sistem Informasi, 1(2), 151–161.
[[6]](https://seminar.ilkom.unsri.ac.id/index.php/ars/article/view/1932/920) (Bimantara & Dina, 2019)Bimantara, A., & Dina, T. A. (2019). Klasifikasi Web Berbahaya Menggunakan Metode Logistic Regression. Annual Research Seminar (ARS), 4(1), 173–177.
[[7]](https://journal.unnes.ac.id/nju/index.php/jte/article/view/10452/6660) Komunikasi, F., Surakarta, U. M., Yani, J. A., & Pos, T. (2017). Sistem Klasifikasi Variabel Tingkat Penerimaan Konsumen Terhadap Mobil Menggunakan Metode Random Forest. Jurnal Teknik Elektro, 9(1), 24–29. https://doi.org/10.15294/jte.v9i1.10452





