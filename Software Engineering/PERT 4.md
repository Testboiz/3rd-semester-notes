# PERT 4

# RANCANGAN ARSITEKTUR PERANGKAT LUNAK

## KEPUTUSAN DESAIN ARSITEKTUR

 > 
 > \[!info\] 
 > Desain arsitektur adalah desain keseluruhan dari suatu perangkat lunak. Desain ini adalah step pertama dalam merancang perangkat lunak

Proses ini menghasilkan model arsitektur yang menggambarkan bagaimana komponen sistem berkomunikasi. 

 > 
 > \[!warning\] Ingat
 > Proses ini harus dilakukan secara maksimal. Proses ini sebaiknya dilakukan secara langsung, bukan bertahap, dan kesalahan di fase ini jauh lebih berisiko daripada pada fase lainnya.

Desain ini bersifat open ended, dengan banyak potensi desain untuk memenuhi persyaratan fungsional dan non fungsional.

Desain arsitektur dibagi menjadi berbagai subkomponen yang membentuk model umum terhadap bagian bagian sistem dan bagaimana eksekusinya

Poin Poin Penting dalam gaya arsitektur sistem adalah

1. **Kinerja**, Komponen perlu didistribusikan dalam seluruh sistem. Gunakan komponen besar untuk menyederhanakan sistem
1. **Keamanan**, Membutuhkan lapisan keamanan yang sangat baik baik agar mencegah hal yang tidak diinginkan secara digital maupun fisik
1. **Redundansi**, yaitu sistem harus tetap bekerja meskipun 1 atau 2 komponen gagal
1. **Pemeliharaan**, yaitu menghindari campuran data konsumen dan produsen

Desain arsitektur dapat dievaluasi dengan referensi arsitektur/ generik, namun lebih umum diuji atas pemenuhan kebutuhannya. 

## Pandangan Arsitektur

 > 
 > \[!info\]
 > Model arsitektur memfokuskan proses desain perangkat lunak, agar lebih mudah untuk memenuhi persyaratan dan desain yang ada, juga membantu dalam dokumentasi 

Arsitektur perlu digambarkan dengan berbagai perspektif, tidak hanya dengan suatu diagram saja, dikarenakan diagram menggambarkan bagaimana sistem terpecah menjadi modul, dan pendistribusiannya dalam sistem.

Arsitektur sistem menurut Krutchen (Krutchen 1995) menyebutkan bahwa suatu model arsitektur harus ada 4 pespektif dalam suatu arsitektur sistem yaitu :

1. Tampilan logis (Gambaran sistem sebagai objek dan kelas) untuk menggambarkan persyaratan sistem
1. Tampilan proses (Gambaran interaksi sistem) untuk menggambarkan persyaratan non fungsional
1. Tampilan pengembangan (Gambaran bagaimana suatu sistem diimplementasi ) untuk developer
1. Tampilan fisik (gambaran perangkat keras dan penggunaan perangkat lunak) untuk teknisi

## Pola Pola Arsitektur

 > 
 > \[!abstrak\] Definisi
 > Merupakan suatu gambaran akan arsitektur yang telah digunakan untuk mendesain arsitektur lainnya

MVC adalah desain dimana Logic, GUI dan Database dipisah dimana mereka bekerja secara independen.  
\>\[!success\] Pros  
\>MVC menguntungkan pada projek yang besar karena skalabilitas yang baik dan komponen yang independen

 > 
 > \[!fail\] Cons  
 > MVC dapat cukup kompleks untuk aplikasi yang sederhana

* Model adalah DB, data dan state dari aplikasi
* View adalah GUI, dan interaksinya
* Controller adalah logic bagaimana suatu sistem bekerja

Pola Aristektur seperti MVC adalah pola yang menggambarkan *best practice* dari membangun suatu arsitektur

### Layered Architecture

Arsitektur ini memiliki 4 layer yaitu

* UI
* UI Logic
* System Logic
* System support (OS, DB, etc)

Contohnya

* Web Frontend
* App Management
* Utilities (Email, Word Processing, dll)
* Utility (Storage, logs, auth)

Perubahan pada layer yang ada hanya merubah implementasi layer dibawahnya

### Repository Architecture

Arsitektur ini menggambarkan struktur dimana komponen dikelompokan ke suatu tempat, dimana output satu komponen digunakan dalam komponen lainnya. Arsitektur ini cukup efisien ketika mengelola data yang banyak. Digunakan pada aplikasi Open Source (*Git* maupun *Github*), sistem kontrol, dll

 > 
 > \[!success\] Pros  
 > Arsitektur ini menguntungkan dalam sisi performa karena semua pemrosesan ada pada 1 repositori, komponen lebih modular

 > 
 > \[!fail\] Cons  
 > Perlu banyak penyalinan data, dan kegagalan dalam 1 bagian repositori memengaruhi seluruh repositori

### Client Server Architecture

Client Server merupakan sebuah arsitektur sistem saat runtime. Struktur ini umumnya digunakan pada sistem terdistribusi. Struktur ini memiliki 1 atau lebih server, dengan berbagai klien yang berkomunikasi dalam suatu jaringan (internet, intranet ataupun `localhost`)

Contohnya adalah Web Apps yang memiliki banyak server untuk hosting data, dan kliennya menggunakan browser

 > 
 > \[!success\] Pros
 > Load mudah untuk didistribusi, dan perubahan pada klien maupun server tidak memengaruhi satu sama lain

 > 
 > \[!fail\] Cons
 > DDOS, server failure dapat melumpuhkan server, masalah pada jaringan juga dapat menggangu performa sistem. Konflik kepentingan dapat terjadi ketika server dikelola oleh banyak pihak

### Pipe and Filter Architecture

Pipe and Filter juga merupakan suatu arsitektur runtime. Arsitektur ini mengambil analogi air dalam suatu pipa yang dapat diproses maupun difilter. Pipa dapat bercabang dan pemrosesan dapat dilakukan secara sekuensial maupun paralel. Pipa merupakan aliran data, dan Filter adalah pemrosesan data.

Sistem ini lebih cocok untuk pemrosesan batch dengan interaktivitas yang terbatas. Sistem ini juga sangat scalable dan fleksibel. Namun overhead sistem dan kebutuhan pemrosesan membuat data bentuk baru sulit untuk didukung

 > 
 > \[!success\] Pros
 > Mudah dimengerti dan mudah diimplementasikan pada kegunaan praktikal. Sistem lebih scalable

 > 
 > \[!fail\] Cons
 > Format data tidak fleksibel dan harus ada format yang disetujui, sehingga support untuk berbagai jenis data sulit

## Arsitektur Aplikasi

Aplikasi digunakan untuk memenuhi kebutuhan user berdasarkan fungsionalitas yang diberikan. Berbagai jenis aplikasi memiliki prinsip yang sama. Hal ini menghasilkan suatu pengembangan arsitektur bersifat umum. Arsitektur ini adalah gambaran bagaimana suatu aplikasi baru akan diimplementasikan

Model arsitektur aplikasi dapat digunakan untuk hal berikut :

1. Sebagai fondasi awal aplikasi yang dibuat pertama kali
1. Sebagai referensi dari arsitektur yang telah dibuat
1. Framework untuk mengelola pekerjaan dari tim
1. Pembanding untuk menilai komponen yang sudah jadi
1. Bentuk istilah untuk membahas konsep aplikasi

Aplikasi yang berbeda mungkin saja memiliki arsitektur yang mirip, hanya saja lapisan lapisan abstraksi dan obsfukasi (penutupan) yang ada menutup source code dari pengguna.

### TPS (Transaction Processing System)

 > 
 > \[!abstract\] Definisi
 > Adalah aplikasi yang memroses informasi dalam basis data, TPS digunakan dalam perbankan, ecommerce, sistem informasi, dsb

TPS didesain untuk memproses permintaan pengguna maupun sistem itu sendiri untuk mengelola database. Pemrosesan ini harus selesai sebelum database dibuat permanen agar menghindari inkonsistensi

Transaksi merupakan operasi yang memenuhi tujuan seperti menarik uang di ATM.  Sinyal secara asinkron diberikan agar interaksi lebih interaktif.

Transaksi diproses dengan Application Logic yang dimana akan diteruskan ke proses pada DBMS.  [Pipe and Filter Architecture](PERT%204.md#pipe-and-filter-architecture) dapat digunakan untuk mengimplementasikan sistem tersebut

### Sistem Informasi

 > 
 > \[!abstract\] Definisi
 > Sistem Informasi adalah sistem yang memberikan akses terkontrol ke basis informasi seperti katalog, jadwal keberangkatan dan catatan pasien yang umumnya menggunakan basis data

Sistem ini memiliki arsitektur berlapis yang mengelola akses dan batasan bagaimana suatu fitur dapat mengakses basis data. Contoh lapisannya dapat seperti berikut

1. User Interface (Browser)
1. UI Logic (login, UX, dsb)
1. System Logic (security, database query, dsb)
1. DBMS dan penyimpanan datanya
   Perlu diperhatikan skalabilitas agar dapat menangani transaksi dengan jumlah besar dalam waktu singkat

### LPS (Language Processing System)

 > 
 > \[!abstract\] Definisi
 > Adalah sistem yang memroses suatu bahasa ataupun data menjadi bahasa lainnya. Contohnya adalah compiler dan parser

LPS digunakan untuk berbagai bahasa data atau bahkan kode. Bahasa yang umumnya digunakan adalah JSON, XML, YAML dan Assembly (machine language).

LPS juga digunakan pada bahasa intrepreted (Contohnya Python, Ruby, Javascript) dan bahasa virtual machine (Java) untuk "mengkompile" bahasa pemograman tersebut agar dijalankan oleh mesin abstrak (intrepreter/virtual machine)

Komponen dari LPS kompiler adalah :

1. Penganalisis Leksikal (keyword parser dan simbol)
1. Tabel Simbol (Identifier/nama variabel/kelas)
1. Penganalsis sintaks (mengecek kebenaran sintaks dengan AST)
1. AST (Abstract Syntax Tree)
1. Penganalisis semantik (memeriksa kebenaran AST)
1. Generator Kode (menggunakan AST)

Untuk LPS seperti penerjemah maka akan memerlukan kamus. Selain itu LPS dapat menyematkan informasi tambahan terhadap kata kata, simbol maupun tata bahasa dalam repositorinya. Editor dapat memamfaatkan LPS agar dapat mengecek sintaks maupun pemformatan bahasa yang ada secara baik

LPS dapat menggunakan arsitektur repositori dan pipa & filter. Menggunakan Pipa & filter LPS akan efektif jika tidak terjadi interaksi dengan pengguna. Contohnya adalah parser HTML. Namun untuk LPS seperti kompiler, perubahan perlu direfleksikan dalam komponen lain dengan arsitektur repositori
