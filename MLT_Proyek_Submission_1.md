# Laporan Proyek Machine Learning - Indah Dwi Sulistiyawati
# Domain Proyek
Domain Proyek pada proyek ini adalah mengenai bidang ekonomi dan bisnis yang di buat untuk mengetahui prediksi harga smartphone untuk mencegah penipuan.  
* Latar Belakang 
![image](https://user-images.githubusercontent.com/79253590/137494141-83e84912-54c6-4395-9416-e8c670668f75.png)

Cukup banyak modus penipuan yang memakan korban akhir-akhir ini. Salah satu yang sering dijumpai adalah penipuan berkedok menjual smartphone mahal dengan harga murah. Pola penipu ini hampir sama. Mereka menjual smartphone, biasanya iPhone (karena banyak peminatnya) dengan harga seperlima bahkan seperenam lebih murah dari harga pasar. Untuk meyakinkan calon korban, mereka berdalih jika smartphone yang dijual adalah original HP blackmarket. Artinya, smartphone tersebut memang asli buatan perusahaan Apple akan tetapi imeinya tidak terdaftar dan dilegalisasi negara.[[1]](https://www.hitekno.com/gadget/2021/10/14/073000/curhat-korban-penipuan-hp-blackmarket-tergiur-iphone-murah-uang-melayang).
Hal tersebut yang memicu calon korban percaya kemudian melakukan transaksi jual beli. "Korban-korbannya tergiur karena harganya murah. Ditambah diskon besar. Padahal itu hanya jebakan. Setelah korban mentransfer uang, pelaku tidak mengirim ponsel tersebut," tutur Faisal. Kasat Reskrim Polres Karawang AKP Oliestha Ageng Wicaksana mengungkapkan, selama beraksi, YTW meraup uang Rp 25 juta dari para korbannya. "Untuk menghilangkan jejak, pelaku kerap mengganti kartu SIM card ponselnya. Kami temukan delapan kartu ponsel yang pernah ia gunakan," kata Oliestha [[2]](https://news.detik.com/berita-jawa-barat/d-5268472/polres-karawang-bongkar-aksi-penipu-berkedok-jual-smartphone-murah). 

Untuk memininalisir permasalahan serupa, didalam proyek ini akan dibuat model machine learning dengan mengklasifikasikan kategori smartphone mulai dari biaya rendah hingga biaya paling tinggi. Dengan adanya model ini, pembeli dapat mengecek spesifikasi smartphone dan memperkirakan apakah smartphone termasuk dalam kategori biaya rendah, biaya sedang, biaya tinggi, dan biaya sangat tinggi sebagai tahapan pertimbangan untuk mengurangi terjadinya terjerumus kedalam pasar gelap. Implementasi model ini dapat dijalankan pada aplikasi web atau android maupun ios.

# Business Understanding
# Problem Statements
Berangkat dari latar belakang diatas, rincian masalah yang dapat diselesaikan pada proyek ini adalah sebagai berikut :
* Bagaimana cara melakukan pra-pemrosesan data agar dapat digunakan pada model machine learning?
* Bagaimana cara membuat model machine learning untuk mengklasifikasikan kisaran harga smartphone?

# Goals
* Melakukan *pra-pemrosesan* data agar dapat digunakan pada model machine learning.
* Membuat model machine learning untuk mengklasifikasikan kisaran harga ponsel yang memiliki tingkat akurasi > 75%.

# Solution Statements
Solusi yang dapat dilakukan untuk memenuhi tujuan dari proyek ini diantaranya :
* *Pra-pemrosesan* dapat dilakukan beberapa teknik sebagai berikut.
   * Melakukan *Categorical Encoding* sebagai proses mengubah data kategori menjadi data numerik menggunakan One-Hot Encoding
   * Melakukan *Split Data* dengan membagi 2 dataset sebagai data latih (train data) dan data test (test data) dengan perbandingan rasio 80% : 20%.
   * Melakukan standardisasi data pada fitur numerik dengan *StandarScaler*.

* Untuk pembuatan model akan digunakan algoritma *Support Vector Machine* (SVM) sebagai model baseline. Konsep SVM dapat dijelaskan secara sederhana sebagai usaha mencari
hyperplane terbaik yang berfungsi sebagai pemisah dua buah kelas pada input space. Pattern merupakan anggota dari dua buah kelas: +1 dan -1 dan berbagi alternatif garis pemisah (discrimination boundaries). Margin adalah jarak antara hyperplane tersebut dengan pattern terdekat dari masing-masing kelas. Pattern yang paling dekat ini disebut sebagai support vector. Usaha untuk mencari lokasi hyperplane ini merupakan inti dari proses pembelajaran pada SVM[[3]](https://books.google.co.id/books?hl=id&lr=&id=_PXJn_cxv0AC&oi=fnd&pg=PR9&dq=Cristianini+dan+Tayor,+S.+(2000)+An+introduction+to+Support+Vector+Machines.+Cambridge+University+Press.+El-Halees,&ots=xTPh4JYu_f&sig=7NLoE51Zx2Y22-r7POyBFEre7VY&redir_esc=y#v=onepage&q&f=false). 
![image](https://user-images.githubusercontent.com/79253590/137500672-d9e0aabc-3f8f-4f63-88ec-e45eff657a59.png)

  Dalam proyek kali ini akan digunakan SVM Klasifikasi Non-Linier. Adapun cara kerjanya yaitu : 
  * Data dimuat
  * Mentransformasikan data menjadi ruang baru
  * Memisahkan data dengan mengimplementasikan beberapa fungsi kernel, antara lain:
    1. Polynomial
    
       ![image](https://user-images.githubusercontent.com/79253590/137501979-e4b8b51a-9bcf-4810-a556-be1267b785be.png)
       
    2. Gaussian 
    
       ![image](https://user-images.githubusercontent.com/79253590/137502045-834543da-150e-4688-ae25-6c466d0e57e8.png)
       
    3. Sigmoid 
    
       ![image](https://user-images.githubusercontent.com/79253590/137502112-75606447-d3d0-430a-8981-26fae3988344.png)
   
   Adapun kelebihan dan kekurangan dari SVM, antara lain [[4]](http://learningbox.coffeecup.com/SVM.html) , [[5]](https://www.dqlab.id/perbandingan-support-vector-machine-dan-decision-tree):
   * Kelebihan :
     * Pengklasifikasi SVM menawarkan akurasi tinggi dan bekerja dengan baik dengan ruang dimensi tinggi. SVM pengklasifikasi pada dasarnya menggunakan subset dari poin pelatihan sehingga hasilnya menggunakan memori yang sangat sedikit.
     * Landasan teori Sebagai metode yang berbasis statistik, SVM memiliki landasan teori yang dapat dianalisa dengan jelas, dan tidak bersifat black box.
     * Feasibility SVM dapat diimplementasikan relatif mudah, karena proses penentuan support vector dapat dirumuskan dalam QP problem.
   * Kekurangan :
     * Sulit dipakai dalam problem berskala besar. Skala besar dalam hal ini dimaksudkan dengan jumlah sample yang diolah.
     * SVM secara teoritik dikembangkan untuk problem klasifikasi dengan dua class
     * Memiliki waktu pelatihan yang tinggi sehingga dalam praktiknya tidak cocok untuk kumpulan data yang besar

# Data Understanding
![image](https://user-images.githubusercontent.com/79253590/137503484-8496c1c0-8170-421f-be79-89e248615799.png)

Informasi terkait dataset dapat dilihat dalam tabel berikut
|             Jenis	          |       Keterangan       |
|             Sumber       	  |Kaggle Dataset : [Mobile Price Classification](https://www.kaggle.com/iabhishekofficial/mobile-price-classification) |
|            Kategori         |Bisnis dan Klasifikasi|
|        Rating Penggunaan    |	7.1 (Gold)|
| Jenis dan Ukuran Berkas	    | CSV (122.4 kB)|

Pada berkas yang diunduh yakni [train.csv](https://www.kaggle.com/iabhishekofficial/mobile-price-classification) terdapat 2.000 baris (jumlah pengamatan) dan 21 kolom dalam dataset. Berdasarkan informasi dari dataset, variabel pada Mobile Price Classification sebagai berikut.
1. battery_power	: energi total yang dapat disimpan baterai dalam satu waktu diukur dalam mAh
2. blue	: memiliki bluetooth atau tidak memiliki bluetooth
3. clock_speed :	kecepatan mikroprosesor mengeksekusi instruksi
4. dual_sim	: ya atau tidak
5. fc	: resolusi kamera depan (mega piksels)
6. four_g :	4G atau tidak
7. int_memory	: memori internal (Gigabytes)
8. m_dep : ketebalan ponsel (cm)
9. mobile_wt : berat ponsel
10. n_cores : jumlah core dalam processor
11. pc : resolusi kamera utama (mega pixels)
12. px_height : tinggi resolusi piksel
13. px_width : lebar resolusi piksel
14. ram :	Random Access Memory (mega byte)
15. sc_h	: tinggi layar ponsel (cm)
16. sc_w	: lebar layar ponsel (cm)
17. talk_time	: waktu terlama satu kali pengisian baterai akan bertahan saat Anda berada
18. three_g	: 3G atau tidak
19. touch_screen: layar sentuh atau tidak
20. wifi	: memiliki wifi atau tidak
21. price_range	: variabel target dengan nilai 0 (low cost), 1 (medium cost), 2 (high cost) dan 3 (very high cost)

![image](https://user-images.githubusercontent.com/79253590/137505060-51cba8bb-8f9b-4bf4-8c80-5c1961aba80c.png)

Dari gambar diatas dijelaskan bahwa didalam data terdapat 7 data kategori bertipe object dan 14 data numerik bertipe int64 dan float64. Visualisasi data kategori sebagai berikut.
![image](https://user-images.githubusercontent.com/79253590/137505346-630b2691-9a43-455f-bd87-65c497625a9a.png)
![image](https://user-images.githubusercontent.com/79253590/137505370-3dac5116-9fa2-4981-a82f-cadd79e0702c.png)
![image](https://user-images.githubusercontent.com/79253590/137505393-b83ffb15-43ef-4262-ba1c-f2a04b5e78d9.png)
![image](https://user-images.githubusercontent.com/79253590/137505421-5fbc2fef-24b7-49f8-b873-70d177765b24.png)
![image](https://user-images.githubusercontent.com/79253590/137505440-5597947a-05bd-4e8d-9ffd-678a3726a00d.png)
![image](https://user-images.githubusercontent.com/79253590/137505454-1d6e9f8f-2280-47ca-a439-92dd03079792.png)
![image](https://user-images.githubusercontent.com/79253590/137505474-0d40a59c-aae0-4204-b60a-0c9b4fbd54a9.png)

Sementara itu, untuk visualisasi numeriknya adalah:
![image](https://user-images.githubusercontent.com/79253590/137505672-33254a5a-04be-4135-a7d1-5a7019900278.png)

Untuk visualisasi distribusi data pada kolom dengan numeric features dan antar numeric features sebagai berikut.
![image](https://user-images.githubusercontent.com/79253590/137505858-d075fb56-3ca1-43f4-902e-f8da2d9fd16a.png)

Untuk visualisasi heatmap (korelasi numeric features) adalah sebagai berikut.
![image](https://user-images.githubusercontent.com/79253590/137506034-8935d742-c0c8-44e3-8260-181b3e20cfb5.png)

# Data Preparation
Seperti yang sudah disebutkan sebelumnya pada bagian Solution statements, berikut adalah tahapan-tahapan dalam melakukan pra-pemrosesan data :
1. Melakukan Categorical Encoding 
Digunakan sebagai proses mengubah data kategori menjadi data numerik. Untuk teknik Encoding fitur kategori menggunakan One-Hot Encoding. One-Hot Encoding untuk data nominal. Data nominal diklasifikasikan tanpa urutan atau peringkat.
2. Split Data
Split data adalah pembagian dataset menjadi 2, yaitu data latih (train data) dengan rasio 80% dan data test (test data) dengan rasio 20%. data latih (train data) berguna untuk pelatihan model dan data test (test data) untuk menguji model. Pembagian dataset dilakukan modul [train_test_split](https://scikit-learn.org/0.24/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split) dari scikit-learn.
3. Standardisasi data pada numeric features
Tujuannya adalah untuk membuat numerical data pada varibel independen memiliki rentang nilai (scale) yang sama. Untuk melakukan standardisasi data, digunakan fungsi [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html). [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html) membuat mean menjadi 0 atau mendekati 0 dan 68% dari rentang data diantara -1 dan 0. 

# Modeling
Setelah melakukan pra-pemrosesan data yang baik pada tahap modeling akan dilakukan dua hal, yakni tahap pembuatan model baseline dan pembuatan model yang dikembangkan.
* Model *baseline*
  Model baseline pada tahap ini, akan dibuat model dasar dengan menggunakan modul dari scikit-learn yaitu SVC dengan parameter default. Kemudian dilakukan prediksi pada data test.
  
  ![image](https://user-images.githubusercontent.com/79253590/137507945-d7e2f017-8472-42b6-a3cf-7d34dcf4a940.png)

* Model yang dikembangkan
  Model yang dikembangkan Setelah melihat kinerja dari model *baseline*, untuk model dapat bekerja lebih optimal maka diperlukan *Hyper Parameter Tuning*.* Hyper Parameter Tuning* digunakan untuk mencari parameter terbaik yang akan diterapkan pada model *baseline*.
  
  ![image](https://user-images.githubusercontent.com/79253590/137507999-7ebb7f19-702d-45bb-8b5c-ab192c3836d8.png)
  
  Pada model baseline memiliki nilai akurasi yang cukup baik yaitu 96,25% dan nilai f1 score, recall, serta precision cukup baik. Setelah dilakukan Hyper Parameter Tuning nilai akurasinya menjadi 83,75% dan nilai f1 score, recall, serta precision yang cukup baik. Untuk membuktikan nilai akurasi, f1 score, recall, dan precision menggunakan visualisasi pada confusion matriks sebagai berikut.
  
![image](https://user-images.githubusercontent.com/79253590/137508657-b3f63fc0-74f0-43ec-a821-6671c06cb527.png)

![image](https://user-images.githubusercontent.com/79253590/137508684-288cf148-b1d5-495a-8140-8d4f74195cb0.png)

Dari hasil diatas, maka model yang dipilih adalah model awal.

# Evaluasi
Dalam proses evaluasi akan digunakan *confusion matriks* dan *classification report* dalam mengevalusasi model.
* *Confusion Matriks*
  Confusion matriks adalah pengukuran performa untuk masalah klasifikasi machine learning dimana keluaran dapat berupa dua kelas atau lebih. 
  ![image](https://user-images.githubusercontent.com/79253590/137509262-23d32427-5c2e-4f7b-808b-4da51bd0a6a6.png)
  
  Keterangan:
  * True Positif: Ini mengacu pada jumlah prediksi di mana pengklasifikasi dengan benar memprediksi kelas positif sebagai positif.
  * False Positive: Ini mengacu pada jumlah prediksi di mana pengklasifikasi salah memprediksi kelas negatif sebagai positif.
  * False Negative: Ini mengacu pada jumlah prediksi di mana pengklasifikasi salah memprediksi kelas positif sebagai negatif.
  * True Negative: Ini mengacu pada jumlah prediksi di mana pengklasifikasi dengan benar memprediksi kelas negatif sebagai negatif.

* *Classification Report*
  *Classification report* digunakan untuk mengukur kualitas prediksi dari algoritma klasifikasi. Classification report menampilkan nilai akurasi, f1 score, recall, dan precision untuk model.
  
  ![image](https://user-images.githubusercontent.com/79253590/137509646-e4a98801-48be-4c9c-ae21-1909452ff1ba.png)


# Referensi
[1] https://www.hitekno.com/gadget/2021/10/14/073000/curhat-korban-penipuan-hp-blackmarket-tergiur-iphone-murah-uang-melayang

[2] https://news.detik.com/berita-jawa-barat/d-5268472/polres-karawang-bongkar-aksi-penipu-berkedok-jual-smartphone-murah

[[3]](https://books.google.co.id/books?hl=id&lr=&id=_PXJn_cxv0AC&oi=fnd&pg=PR9&dq=Cristianini+dan+Tayor,+S.+(2000)+An+introduction+to+Support+Vector+Machines.+Cambridge+University+Press.+El-Halees,&ots=xTPh4JYu_f&sig=7NLoE51Zx2Y22-r7POyBFEre7VY&redir_esc=y#v=onepage&q&f=false) Cristianini dan Tayor, S. (2000) An introduction to Support Vector Machines. Cambridge University Press.
El-Halees,

[4] http://learningbox.coffeecup.com/SVM.html 

[5] https://www.dqlab.id/perbandingan-support-vector-machine-dan-decision-tree






