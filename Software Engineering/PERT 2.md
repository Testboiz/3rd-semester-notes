# PERT 2

## Persyaratan Fungsional dan Non Fungsional

### Pendahuluan

 > 
 > \[!abstrak\] Definisi
 > Persyaratan adalah deskripsi layanan yang harus dipenuhi oleh sistem dan batasannya.

Requirement Engineering adalah proses mencari tahu, analisis, dokumentasi, pemeriksaan layanan dan kendala dari suatu persyaratan

Ada berbagai jenis persyaratan yaitu 

* **Persyaratan pengguna / user requirement**, yaitu persyaratan secara umum akan bagaimana perangkat lunak bekerja dan batasannya secara terperinci
* **Persyaratan Sistem / System requirement**, yaitu persyaratan akan bagaimana sistem harus bekerja. Persyaratan ini jauh lebih rinci dan jelas daripada persyaratan pengguna
* **Persyaratan fungsional** adalah persyaratan terhadap apa yang sistem harus mampu/tidak dan sediakan
* **Persyaratan non fungsional**, adalah persyaratan yang mendukung sistem seperti performa, UI, dsb
  alias:
* elo maunya apa
* komputer maunya apa
* aplikasi harus bisa apa
* aplikasi seharusnya bisa gmn

## Persyaratan Proses Rekayasa

Dalam rekayasa persyaratan diawali dengan memahami secara high level apa yang akan dihandle, dan persyaratan-persyaratannya. Kemudian seiring waktu persyaratan akan menjadi semakin rinci

Perubahan persyaratan hampir menjadi suatu keniscayaan, perbuahan ini harus dikelola agar dampak dan implikasinya dapat dikelola juga.

## Memunculkan Persyaratan (Elisitasi)

 > 
 > \[!note\]
 > Gunanya persyaratan adalah dapat memahami bagaimana sistem akan mendukung operasi yang sudah ada atau merubahnya 

Selama proses ini developer akan berdiskusi akan bagaimana perangkat lunak akan disesuaikan berdasarkan kegunaan yang diminta

Proses Elisitasi secara umum adalah :

1. **Penemuan dan pemahaman**, yaitu proses diskusi dengan klien untuk menemukan persyaratan, persyaratan domain dan dokumentasi yang dibutuhkan
1. **Klasifikasi dan organisasi**, Yaitu pengelompokan dan penyortiran persyaratan yang terstruktur maupun tidak
1. **Prioritas dan Negosiasi**, Yaitu untuk menangulangi konflik dengan kompromi akan persyaratan yang ada
1. **Dokumentasi**, Yaitu proses pendokumentasian akan proses yang sudah berlangsung
   irl be like:
1. bilang ma klien lu monnya apa
1. temukan dan sortir persyaratan yang ditemukan
1. nego atau berantem
1. catet (ga tralu guna)

## Spesifikasi Kebutuhan

 > 
 > \[!abstract\] Definisi
 > Spesifikasi kebutuhan adalah proses penulisan persyaratan dalam dokumen persyaratan secara sistematis dan mudah dipahami

Hal ini ternyata sulit karena kebutuhan sering berbeda beda dan bahkan terjadi konflik

### Spesifikasi Bahasa Alami (Manusia)

Spesifikasi ini mudah dipahami namun juga berisiko ambigu. Walau demikian spesifikasi ini adalah spesifikasi yang paling mudah untuk semua

Tips menggunakan bahasa sehari hari dalam spesifikasi ;

1. Menggunakan kalimat dan istilah standar
1. Bahasa konsisten. Contoh "harus" untuk kewajiban, dan "seharusnya" untuk opsional
1. Menggunakan pemformatan teks
1. Hindari jargon, singkatan dan akronim
1. Tambahkan alasan kepada tiap requirement

### Structured Specification

 > 
 > \[!info\]
 > Yaitu bentuk terstruktur dari [Spesifikasi Bahasa Alami (Manusia)](PERT%202.md#spesifikasi-bahasa-alami-manusia)

Untuk merincikan [Persyaratan Fungsional](PERT%202.md#persyaratan-fungsional-dan-non-fungsional) butuh menspesifikasikan hal berikut 

1. Penjelasan akan fungsi, aktor dan entitas
1. Penjelasan akan masukan dan asalnya
1. Penjelasan akan keluarannya dan tujuannya
1. Informasi terhadap apa yang perlu dikomputasi dan sistem yang diperlukan
1. Penjelasan akan tindakan yang diambil
1. Prasyarat akan cara kerja komponen
1. Efek samping dari operasi

### Use Case

 > 
 > \[!info\]
 > Digunakan untuk menggambarkan Use Case secara umum antara aktor, sistem dan database. Use Case diagram ada dalam UML

%%Insert image%%
![Use Case 1.png](Use%20Case%201.png)

![Use Case 2.png](Use%20Case%202.png)

### Software Requirements Document

 > 
 > \[!info\]
 > Yaitu dokumen yang diberikan kepada pihak pihak berkepentingan untuk mendapatkan gambaran akan apa yang ada dalam perangkat lunak

%% insert image here %%

## Validasi Persyaratan

 > 
 > \[!info\] Kegunaannya
 > Untuk memastikan bahwa requirement sudah benar, agar menghindari kesalahan yang dapat berdampak besar dan mahal

Hal yang dilakukan meliputi :

* Pemeriksaan Validitas (memastikan persyaratan sesuai dengan kenyataan)
* Pemeriksaan Konsistensi (memastikan dokumen tidak bertentangan)
* Pemeriksaan Kelengkapan (memastikan kelengkapan dokumen)
* Pemeriksaan Realisme (memastikan seberapa realistis requirement itu)
* Verifiability (pengujian akan persyaratan yang ada)

Teknik validasi yang dapat dilakukan adalah :

1. Tinjauan kebutuhan oleh tim peninjau
1. Pembuatan prototipe sistem untuk dites
1. Pengujian dengan kasus uji

## Perubahan Persyaratan

Hal yang perlu dilakukan untuk menghadapinya adalah :

1. Idenitifkasi Persyaratan
1. Kelola perubahan
1. Tentukan hubungan antara tiap persyaratan
1. Gunakan alat pendukung untuk
   1. Penyimpanan Persyaratan
   1. Visualisasi Manajemen Perubahahan dan ketelusuran dengan diagram yang sesuai

Ada 3 tahapan dalam manajemen perubahan

1. Analisis Masalah dan Spesifikasi Perubahan
1. Analisis Perubahan dan tetapkan biaya pengaruh perubahan
1. Ubah implementasi dokumen persyaratan, desain, dan implementasi sistem
