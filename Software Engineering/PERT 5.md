# PERT 5

# DESAIN dan IMPLEMENTASI

## Rancangan Berorientasi Objek

Pada sistem sederhana proses desain dan implementasi dan aktifitas lainnya non coding dapat diimplementasikan disini. 

Namun untuk sistem besar, ini hanyalah suatu proses kecil dari banyak proses lainnya

 > 
 > \[!definition\] Definisi
 > Desain Perangkat lunak adalah proses mengidentifikasi komponen dan interaksinya berdasarkan kebutuhan. Implementasi adalah proses mewujudkan desain tersebut. 

Desain dapat digambarkan secara langsung di kertas maupun dalam UML. UML umumnya digunakan untuk desain OOP. Pada sistem agile, desain merupakan sketsa kasar yang dimana akan direfine oleh programmer. 

UML tidak perlu digunakan ketika program akan menggunakan paket off the shelf. Aplikasi ini akan lebih mudah untuk dikustomisasi untuk memenuhi kebutuhan

Dalam pemograman OOP state merupakan atribut lokal objek. Desain OOP menggunakan kelas dan objek untuk sebagai media interaksi. Objek dibuat secara dinamis dalam runtime. Objek memiliki atribut dan method yang menggambarkan sifat dan perilaku dari objek tersebut.

Objek bersifat independen, sehingga perubanan dalam suatu objek tidak memengaruhi objek lainnaya. Sehingga pemetaan interaksi terhadap tiap objek sangat mudah dilakukan.

Hal yang dilakukan untuk membuat konsep dan desain OOP diperlukan :

* Menentukan konteks dan interaksi sistem
* Merancang arsitektur
* Identifikasi objek dalam sistem
* Kembangkan desain
* Buat UI UX

Proses ini adalah proses kreatif yang tidak bersifat sekuensial. Risiko kegagalan cukup tinggi. Gambaran desain dapat dibantu dengan diagram UML. 

Penjabaran langkah langkah desain tersebut adalah berikut

### Menentukan konteks dan interaksi sistem

* Menentukan batasan sistem, dan hubungan hardware dan software
* Menentukan functional dan non functional requirement
* Menggambarkan use case diagram
* Menentukan interaksi antar sistem yang masih ada

### Merancang arsitektur

* Identifikasi komponen yang berinteraksi satu sama lain
* Menentukan pola pola arsitektur
* Menjabarkan subsistem yang ada
* Mereview keputusan desain agar menghindari kesalahan desain

### Identifikasi objek dalam sistem

* Mengembangkan ide objek dari use case diagram
* Menggambarkan objek abstrak yang merepresentasikan logika sistem
* Menggambarkan kelas dan objek umum 

Cara identifikasi objek dalam sistem adalah :

* Menganalsis requirement bahasa manusia (Objek adalah noun, dan method adalah verb)
* Menggunakan analogi entitas benda, peran aktor, acara, interaksi, lokasi, unit organisasi, dsb.
* Analisis skenario penggunaan dari perangkat lunak
* Domain knowledge (landasan teori) dari bagaimana sistem akan diimplementasi
* Menentukan apakah ada objek implementasi untuk penelusuran dan validitas

Cara cara tersebut digabungkan untuk menentukan  kelas yang tepat sesuai kegunaan dan keadaan

Objek pada fase ini masih bersifat umum, tidak memperhatikan implementasi dari objek tersebut. Kemudian mulai mengorganisir objek tersebut dalam hireaki inheritance

### Model Desain

Model desain adalah gambaran objek dan kelas dalam sistem, yang memperhatikan hubungan antarkelasnya. Sifatnya adalah abstrak tidak memperhatikan implementasi namun cukup detil. Model desain tersedia dalam UML. Ada model struktural (compile time) seperti class diagram dan model dinamis (runtime) seperti subsistem, sequence dan state diagram.

Harap untuk bijak dalam membuat model desain. Model tidak perlu untuk didetail kalau info tersebut merupakan penerapan sistem, karena hal tersebut akan dilakukan pada proses coding

istilahnya lo gosa tulis hal2 yang programmer doang yang ngerti

### Interface Specification

UI UX akan menjadi jembatan akan objek objek dalam sistem kepada pengguna. Dalam UML digunakan `<<interface>>` . UI UX tidak mengenal atribut, namun hanya method. UI UX harus mengexpos objek untuk menggambarkan apa yang terjadi.

Banyak pendekatan untuk menggambarkan objek dalam UI UX. Dalam Java UI `implements` Objek dan UI dapat bekerja secara independen

## Pola Pola Rancangan

Pola Pola Rancangan adalah gambaran akan desain yang sudah ada dan dapat diimplementasikan pada rancangan dan desain perangkat lunak. Hal yang dapat dideskripsikan adalah :

1. Nama Pola
1. Rumusan masalah yang kompartibel dengan pola desain
1. Deskripsi solusi yang mengimplementasi pola tersebut, dalam pendekatan template dan UML
1. Konsekuensi dari pola tersebut

Pada suatu kasus pada pola rancangan dapat berupa cara representasi suatu data. Representasi dapat berupa tabel maupun grafik.

4 Pola dalam rancangan dalam Gang of Four adalah :

1. Observer (infokan perubahan objek)
1. Facade (prioritaskan objek yang umum)
1. Iterator (Data harus dapat diakses dalam bentuk koleksi)
1. Dekorator (Memperluas fungsionalitas kelas)

Contoh implementasinya

1. Event
1. Menggunakan Interface atau superclass
1. Menggunakan koleksi objek secara bentuk objek lain, list, array, dsb
1. `@decorator` di Python, atau `@FXML` di JavaFX yang dapat menambah fungsionalitas

Pola memudahkan kita untuk menggunakan ulang konsep dan membatasi terhadap rancangan kita. Pemahaman akan konsep dengan baik akan membantu kita menentukan pola yang ideal

## Masalah Implementasi

### Reuse

Pada awalnya implementasi dari suatu program dapat digunakan ulang dengan menggunakan objek dan fungsi yang ada pada bahasa tersebut. Namun pendekatan ini cukup kompleks dan mahal karena sifat dari pemograman tersendiri

Jauh lebih mudah untuk menggunakan ulang perangkat lunak secara utuh. Reuse menekankan akan menggunakan aplikasi maupun komponen aplikasi yang telah dites dan diimplementasi sebelumnya. 

Namun ada biaya yang terkait dalam pendekatan ini yaitu

1. Biaya waktu untuk mencari, menguji dan mengimplementasinya
1. Biaya Pembelian perangkat lunak
1. Biaya adaptasi dan konfigurasi perangkat lunak sesuai dengan persyaratan yang ada
1. Biaya integrasi elemen dari perangkat lunak yang sudah ada dengan perangkat lunak yang baru

### Host Target Development (Configuration Management)

Dengan mengelola konfigurasi dari IDE, Kompiler dan testing tools kita dapat menghasilkan perangkat lunak yang berbeda beda dan sesuai dengan persyaratan yang ada

Pendekatan ini menggunakan host komputer yang telah mengembangkan perangkat lunak yang sudah ada dan mengembangkan dengan apa  yang disyaratkan.

Hal yang perlu diperhatikan adalah System specs, System Availability dan Komunikasi Komponen.

## Pengembangan Open Source

Pengembangan Open Source adalah pengembangan perangkat lunak yang dimana source codenya terbuka dan bebas dikembangkan oleh siapa saja. Namun pada kenyataannya hanya sebagian kecil dari pengguna maupun developer yang akan mengelola perangkat lunak tersebut. 

Open Source bertumpu pada komunitas yang memberikan sugesti maupun penyelesaian dari suatu masalah pada perangkat lunak. Pengembang inti umumnya akan menentukan apakah sugesti maupun penyelesaian tersebut layak atau tidak

Open source adalah tulang punggung dari pengembangan komputer pada saat ini. Linux, Apache, MariaDB, Android, Git, Firefox, Java, C, C++, dsb adalah produk produk pasaran yang merupakan buah dari Open Source.

Open source umumnya bebas untuk didapatkan dan digunakan. Kualitasnya umumnya baik dan banyak pengguna yang menggunakannya. Bugfix juga jauh lebih cepat

### Open Source Licensing

Merupakan batasan maupun informasi terhadap apa yang dapat dilakukan oleh pengguna terhadap kode. Penggunaan dapat dibatasi untuk tidak menggunakannya untuk melanggar hukum, kegunaan komersil, licensing berbeda, dsb. Contoh dari licensing ini adalah GPL,LGPL, BSD, MIT,dsb

* GPL mewajibkan produk derivatnya harus open source
* LGPL mewajibkan sedikitnya komponen derivatnya open source
* BSD tidak mewajibkan komponen derivatnya open source
* MIT memperbolehkan kode derivatnya digunakan untuk komersil selama memberikan kredit

Hal ini harus diperhatikan karena pelanggaran licensing dapat membuat pengembang maupun entitas untuk dituntut hukum. 

Hal yang diperhatikan dalam projek open source adalah :

1. Kelola Informasi dan lisensi pada perangkat lunak tersebut. Awasi perubahan lisensi
1. Ketahui Lisensi yang tepat untuk projek anda
1. Perhatikan evolusi perangkat lunak
1. Edukasikan prinsip dan nilai terhadap open source
1. Audit terhadap potensi pelanggaran lisensi
1. Mengikuti bagian dari komunitas open source

Monetisasi Open source dapat dilakukan seperti berikut

1. Merilis open source dan menjual layanannya (RHEL)
1. Hosting Open Source di Cloud (AWS)
