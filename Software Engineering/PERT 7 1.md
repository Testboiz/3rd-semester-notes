# PERT 7 - SOFTWARE EVOLUTION

## Evolution Process

Software memiliki masa pakainya tersendiri, mulai dari beberapa bulan untuk aplikasi sosial media, hingga puluhan tahun untuk sistem penerbangan dan militer. Software yang berevolusi adalah software yang telah dirilis dan masih diupdate seiring waktu berjalan. 

Update umumnya digunakan untuk memenuhi persyaratan baru, maupun memperbaiki suatu masalah/bug yang ada. 

Proses ini merupakan proses yang paling lama dan mahal dalam siklus hidup software. Terkadang software ternyata merupakan bagian dari sistem yang lebih besar, alhasil evolusi harus dilakukan pada seluruh sistem. Pengembangan ini dinamakan pengembangan Brownfield

[SDLC Spiral](PERT%201%202.md#spiral) umumnya digunakan pada proses ini. Setiap 1 update, engineer akan mengurusi update berikutnya. Update juga dinamakan increment. 

Ada pembedaan akan software evolution dan servicing

* Pada Windows, ketika sedang berada pada mainstream support, maka akan diberikan update fitur-fitur yang ada, dan penambahan kapabilitas. Fase ini adalah fase software evolution
* Pada fase Extended Support, hanya ada update security patch yang akan diberikan

Proses untuk melakukan evolusi merupakan subset dari RDCTM yaitu

* Cari persyaratan baru dan analisa risiko
* Buat proposal (dokumentasi)
* Coding & testing
* Increment

Persyaratan baru dapat berasal dari request user maupun juga analisis requirement baru. 
Kemudian desain dan persyaratan harus diupdate juga, dan divalidasi sebelum diimplementasi. Dokumentasi dan prototipe baru harus dibuat
Lalu pada proses implementasi (coding), perlu pemahaman akan bagaimana aplikasi bekerja, dan bagaimanakah perubahan dapat diimplementasi dengan risiko yang seminimal mungkin

Perubahan mendesak dapat muncul ketika ada bug kritikal, glitch yang menggangu, maupun perubahan yang terjadi secara tiba tiba
Berbeda dengan evolusi biasa, tidak diperlukan dokumentasi pada perubahan ini, langsung saja coding, testing dan increment.
Hanya saja ada risiko kalau nantinya dokumentasi menjadi inkonsisten, yang akan berdampak pada update berikutnya.
Update seperti ini cenderung tidak optimal, dan memperpendek umur software. Penanganannya dapat dengan refactoring, namun sering tidak cukup waktu untuk itu

SDLC agile diuntungkan dalam transisi pengembangan ke evolusi. Namun tetap saja ada risiko ketika tim pengembang dan evolusi tidak sepakat dalam metedologi yang ada (agile/plan based).
SDLC agile hampir tidak membedakan evolusi dengan development. Tim pengembang tidak direkomendasikan untuk fase ini karena perbedaan spesialisasinya

## Legacy Systems

Terkadang masih ada saja sistem yang harus dijalankan pada sistem lawas seperti Windows 95,98,NT maupun XP. Sistem tersebut jauh lebih sulit untuk dikelola.

Elemen sistem lawas terdiri atas

* Hardware lama yang tua dan tak tersedia lagi
* Library / support software yang tidak diupdate lagi
* Aplikasi yang usang
* Data yang mulai berantakan dan anomali
* Proses aplikasi yang belum berubah dan beradaptasi

Selain itu, juga dapat digambarkan dengan layer yaitu

* Proses
* Aplikasi
* Library dan driver
* Hardware
  Setiap komponen bergantung dengan komponen dibawahnya
  Gambaran ini agak terlalu sederhana dan kurang merepresentasikan kenyataan yang ada.

Sistem lawas juga banyak dikembangkan dalam bahasa COBOL yang tidak lagi digunakan pada sistem baru. Namun sistem ini tetap dijalankan dan digunakan, karena risiko evolusi yang tinggi dan mahal. Hal tersebut disebabkan karena

* Requirement kurang jelas
* Pengoperasian yang terikat erat dengan software
* Mungkin cara bekerjanya suatu organisasi bergantung pada kode program software tersebut
* Risiko sistem baru yang kurang stabil
  Hal yang menyebabkan mahalnya maintainence sistem baru adalah
* Kode program yang inkonsisten seiring waktu
* Bahasa pemograman usang
* Dokumentasi usang atau tidak memadai
* Optimisasi yang sangat spesifik untuk suatu hardware
* Inkompartibilitas data

### Manajemen Sistem Lawas

Ada berbagai pendekatan dengan organisasi yang memiliki sistem lama yaitu

* Hapus sistem sepenuhnya jika tidak terlalu berguna
* Biarkan sistem dan lanjutkan maintainence yang ada
* Update sistem 
* Upgrade sistem

Ada 2 dimensi dalam pengelolaan sistem lawas yaitu dimensi value dan quality. Value ditentukan dengan berapa banyak penghematan biaya dibandingkan dengan proses manual, jumlah pengguna software, kontribusi terhadap organisasi.

Rubrik yang dapat digunakan untuk menilai kualitas dan value dari sistem lawas adalah

|Pengkajian Lingkungan|Pengkajian aplikasi|
|---------------------|-------------------|
|Keberadaan maintainer|Kemudahan untuk dimengerti|
|Risiko kegagalan|Dokumentasi yang ada|
|Umur aplikasi dan hardware|Standardisasi dan interoperabilitas data|
|Performa|Support bahasa pemograman|
|Biaya support aplikasi|Adanya manajemen konfigurasi|
|Biaya pengelolaan hardware|Data untuk testing|
|Pengaruh terhadap sistem lain|Kemampuan tim pengkaji|

## Software Maintenance

Pada perangkat lunak khusus (custom made) maupun sistem besar seperti Windows, evolusi lebih dikenal sebagai Maintenance. Maintenance sedikit berbeda karena aplikasi yang telah dikembangkan akan tetap seperti demikian, namun akan ada perubahan perubahan berdasarkan kebutuhan yang ada

Umumnya perubahan dapat berupa, dengan distribusi biayanya (Davidsen dan Krogstie 2010)

* bugfix (24%)
* platform expansion (19%)
* penambahan fitur baru (58%)

Fitur baru lebih mahal untuk diimplementasi karena umumnya tim maintenance berbeda dengan tim development, yang membuat program jarang maintainable dan juga pengetahuan yang kurang.
Pemisahan ini umumnya dilakukan karena secara lebih murah secara jangka pendek

### Maintenance Prediction

Untuk memahami perubahan yang harus dilakukan, perlu memahami bagaimana sistem berinteraksi dengan lingkungan sekitar dan kompleksitasnya. Hal yang perlu diperhatikan adalah

* Kompleksitas sistem tersendiri
* Persyaratan yang berubah-ubah
* Perubahan zaman yang menuntut perubahan sistem
  Metrik yang dapat diperhatikan untuk menilai maintainabilitas sistem adalah
* Jumlah laporan bug maupun update emergency
* Waktu rata rata untuk risk analysis maupun implementasi

### Software Reengineering

Software lawas lebih sulit untuk dipahami, maka software tersebut dapat direkayasa ulang. Rekayasa ini digunakan untuk meningkatkan struktur dan pemahaman dengan menghindari perubahan besar terhadap arsitektur sistem. Dampaknya adalah **risiko dan biaya yang dikurangi**

Software Reengineering dimulai dari tahapan 

1. **Source Code Translation**, yaitu proses memahami dan menerjemah bahasa pemograman lawas ke bahasa baru
1. **Reverse Engineering**, yaitu proses analisa ulang untuk memahami struktur dan organisasi program
1. **Program Structure Improvement**, yaitu perbaikan struktur program agar lebih mudah dipahami
1. **Program Modularization**, yaitu pemisahan maupun pengelompokan program dan penghapusan redundansi
1. **Data Reengineering**, yaitu perubahan data agar dapat digunakan pada program baru

![Pasted image 20231111130721.png](Pasted%20image%2020231111130721.png)

Semakin banyak yang diubah, dan semakin banyak pekerjaan manual yang dilakukan, semakin mahal proses ini

### Refactoring

 > 
 > \[!abstract\] Definisi
 > Refactoring adalah proses memodifikasi source code agar lebih dipahami. Tidak ada fungsionalitas yang ditambahkan maupun dikurangi

Refactoring sangat penting karena dapat memperlambat degradasi program yang akan membuat program semakin sulit untuk di maintainence. Hal ini merupakan tindakan preventif yang menghindari potensi masalah dalam maintainence

Refactoring merupakan bagian dari agile, terutama XP. Hal tersebut terjadi karena perubahan program terjadi sangat cepat, dan degradasi berpotensi jauh lebih cepat. 

Pengujian regresi ([TDD](PERT%206.md#test-driven-development)) mengurangi risiko kesalahan pada refactoring. Kesalahan harus dideteksi karena akan menginvalidasi kesalahan pada pengetesan sebelumnya.

Perbedaan Refactoring terhadap [Software Reengineering](PERT%207%201.md#software-reengineering) adalah

|Refactoring|Software Reengineering|
|-----------|----------------------|
|Ideal pada fase development|Ideal pada fase Maintainence|
|Inheren pada SDLC Agile|Universal|
|Menekankan perubahan kode|Menekankan perubahan sistem|
