# PERT 11 - Rekayasa Perangkat Lunak Berorientasi Service

## Service Oriented Architectures

Aplikasi zaman sekarang umumnya berupa aplikasi klien server, yang merequest layanan layanan yang disediakan oleh server, dan juga server dapat menjadi sangat fleksibel, karena dapat menangani berbagai jenis aplikasi sekaligus. 

Ada berbagai jenis layanan web yaitu dalam bentuk standar SOAP dalam XML dan juga REST/GraphQL dalam JSON.  Pada awalnya data dalam web didistribusikan dalam format XML, yang sangat mirip dengan HTML namun jauh lebih fleksibel dan didesain untuk transfer data. 

Arsitektur dari standar SOAP meliputi

* SOAP (Standar transfer data), REST pada sistem modern
* WSDL (struktur umum respons), WADL untuk REST
* WS-BPEL (Flowchart untuk WSDL)
* UDDI (Pencari layanan layanan web, sudah digantikan oleh Google)

Standar SOAP/REST berperan agar suatu sistem dapat menyediakan pesan yang sesuai kualitas yang ada yaitu

* Hanya perlu 1x mengirim pesan
* Standar keamanan
* Standar informasi alamat
* Standar penanganan transaksi database

### Service Components in a SOA

URI (Uniform Resource Identifier) digunakan untuk mengidentifikasikan layanan web yang berbasis SOAP. Aplikasi SOAP ditulis dengan WSDL yang memiliki struktur interface, binding dan endpoint

Struktur WSDL dapat dijabarkan sebagai berikut

* Namespace SML (dokumentasi dan layanan)
* Penjelasan bentuk pesan
* Penjalasan antarmuka layanan 
* Penjelasan bentuk input dan output
* Penjelasan standar yang digunakan dalam dalam sistem dalam transfer data maupun transfer informasi pendukung
* Spesifikasi endpoint 

Pertukaran pesan dalam WSDL dapat mendukung operasi ini

* In out
* In only
* Out only
* In optional Out
* Out in

 > 
 > \[!info\]
 > WSDL jarang ditulis manual, pada umumnya digenerate oleh program

## RESTful Services

XML memiliki kompleksitas tersendiri, karena memiliki opening tag dan closing tag, hal ini membuat pesan-pesan sangatlah besar dan pemrosesan sangat tidak efisien. REST dibuat untuk memecahkan masalah ini. REST menggunakan format JSON yang jauh lebih simpel.

REST memiliki pengenal yaitu URL (bukan URI) yang digunakan pada situs web API modern. REST memiliki operasi yang menyerupai CRUD (Create Read Update Delete) Database yaitu 

* (C) POST
* (R) GET
* (U) PUT
* (D) DELETE 

REST juga memiliki desain yang ringan, server tidak dianjurkan untuk menyertakan informasi statusnya kecuali HTTP code, sehingga aplikasi hanya mendapatkan data yang penting penting saja. Desain ringan REST ini membuatnya banyak digunakan untuk aplikasi HP dan perangkat seluler lainnya.

REST juga tidak luput dengan masalah yaitu

1. Sulit untuk mendesain API untuk server yang kompleks
1. Tidak ada deskripsi interface yang terstandar seperti WSDL
1. Sulit memantau kualitas layanan

Oleh karena itu, banyak server-server yang mendukung SOAP dan REST sekaligus.

## Service Engineering

 > 
 > \[!abstract\] Definisi
 > Yaitu proses mengembangkan layanan untuk mendukung aplikasi berbasis layanan dengan mendesain lapisan lapisan abstraksinya

Langkah langkahnya adalah

* Menemukan persyaratan layanan
* Mendesain layanan
* Implementasi layanan

3 jenis layanan yang umum dalam aplikasi berbasis layanan adalah (Erl 2005). Layanan ini juga dapat berupa entitas (berupa Software As A Service)

* Layanan Utilitas (converter, downloader, dll)
* Layanan bisnis (pembelian, pembayaran, pendaftaran)
* Koordinasi (sistem pemesanan dalam sebuah aplikasi kompleks)

Meskipun ada banyak jenis layanan yang dapat disediakan, namun menyesuaikan dengan fakta dan keadaan yang ada tetap sulit, karena beberapa faktor ini

* Kompleksitas dunia nyata
* Kebersediaan dari calon pengguna
* Ketergantungan satu layanan dengan layanan lain
* State management, binding dan endpoint yang ada
* Fleksibilitas dari layanan terhadap persyaratan dan pengguna
  Jika masalah masalah ini dapat dipecahkan, maka dapat ditemukan layanan yang tepat untuk dikembangkan

### Implementasi dan Desain Antarmuka Layanan

Setelah mengidentifikasikan layanan yang akan dikembangkan, maka kita akan merancangnya.

 > 
 > \[!note\]
 > Pemilihan SOAP dan REST berpengaruh besar dalam pembuatan layanan. SOAP menuntut kita untuk mendesain struktur pesan XML menggunakan WSDL, sedangkan REST juga menuntut pemetaannya sendiri

Exception (Error) perlu didefinisikan agar teknisi dapat mengerti apa masalah yang terjadi. Error harus didesain secara jelas untuk menuntun user/teknisi untuk mengetahui masalah yang terjadi. Salah satu contoh error yang sering ada adalah HTTP 404

UML juga dapat digunakan dalam mendesain arsitektur sistem, pada umumnya menggunnakan Class Diagram

Salah satu contoh kasus layanan adalah **wrapper layanan sistem lawas**. Wrapper ini dapat didesain dengan WSDL pada sistem SOAP. Banyak framework dan IDE yang mendukung penerjemahan secara otomatis kode program ke WSDL

Pengimplementasian sistem layanan umumnya digunakan pada bahasa "backend" seperti C#, JavaScript dan Java. Implementasi ini juga dapat membuat interface baru yang menggunakan implementasi sistem lawas. 

Testing dapat dilakukan menggunakan syntax checking menggunakan IDE yang tersedia, serta menggunakan aplikasi dengan Postman.

Penginstalan aplikasi cukup mudah, cukup menggunakan 1 file yang dapat langsung digunakan.

Dokumentasi dapat dibuat jika akan banyak pengguna yang ada. Dapat menggunakan Swagger

## Service Composition

Berbagai Web Service seperti API dapat dikomposisikan satu sama lain untuk mengembangkan aplikasi kita. Contohnya adalah seperti aplikasi perpustakaan dengan fitur sign in dengan KTP. Maka aplikasi itu selain membutuhkan layanan server dari perpustakaan, namun juga dapat menambah layanan dari pemerintah (DukCapil)

Gabungan akan layanan-layanan tersebut dapat digambarkan dalam diagram alur kerja yang mirip dengan diagram data flow (activity) pada UML

Merancang layanan berbasis reuse hampir selalu menggunakan Service Composition. Persyaratan dan desain harus saling kerja sama dan menyesuaikan terhadap kenyataan yang ada. 

Tahapan Utama dalam membangun aplikasi komposisi adalah :

1. Menggambarkan alur kerja
1. Menentukan layanan yang tersedia baik di server kita maupun cloud
1. Menyesuaikan alur kerja dari layanan yang ada, dan perjelas diagramnya
1. Membuat aplikasi
1. Mengetes aplikasi

 > 
 > \[!warn\]
 > Namun terkadang beberapa layanan tidak dapat diintegrasi dengan mudah. Oleh karena itu, dapat menggunakan *web scraping*

### Desain & Implementasi Alur Kerja

Mendesain alur kerja mengharuskan kita untuk meniliki gambaran terhadap bagaimana aplikasi akan bekerja, dan tidak semua alur kerja akan dijalankan secara otomatis. Desain ini dapat dibuat dalam UML maupun BPMN (Business Process Modelling Notation)

Notasi yang digunakan adalah

* Persegi panjang merupakan sistem/aktivitas (mirip terhadap Use case dan Activity)
* Oval adalah peristiwa yang terjadi
* Belah ketupat adalah kondisi if else
* Panah adalah akhir aktifitas
* Lingkaran adalah start/stop

Modelkan ini tiap use case 

Setelah model telah dibuat, maka layanan dapat diprogram. Sebagian jenis model alur dapat diproses menjadi model API menggunakan WS-BPEL maupun spesifikasi REST. 

### Menguji Komponen Layanan

Kemudian sama dengan software lain, komponen layanan juga perlu diuji. Pendekatan uji yang dapat dilakukan adalah dengan White Box untuk layanan yang kita kembangkan maupun Interaksi Black Box untuk layanan yang berasal dari penyedia lain

Tantangan pengujian komponen layanan adalah

* Aplikasi bergantung pada server, sehingga masalah server akan menggangu penggunaan aplikasi
* Terkadang aplikasi tidak selalu menggunakan layanan yang sama
* Persyaratan non fungsional seperti performa baru dapat diamati pada saat deployment
* API dengan rate limit / pembayaran per call membuat pengetesan menjadi mahal
* Simulasi error pada beberapa aspek mungkin sulit
