# PERT 10 - Rekayasa Perangkat Lunak Terdistribusi

## Distributed Systems

 > 
 > \[!abstract\] Definisi
 > Sistem terdistribusi adalah sistem dimana banyak komputer terpisah bekerja menjadi 1 kesatuan. Contoh : superkomputer 

Komponen individual dari komputer tersebut disebut node. Tiap node merupakan satu bagian kecil dari kesatuan sistem terdistribusi.

Harus dicapai poin poin berikut

1. Transparan
1. Terbuka
1. Scalable
1. Aman
1. Quality
1. Failure management

Sebuah sistem terdistribusi sulit untuk dikelola sebagai sebuah 1 sistem utuh. Namun sistem ini sangat mudah untuk diskalakan untuk demand yang sangat tinggi. Sistem ini dapat mengelola jutaan user dengan data sebesar jutaan TB secara real time

Sistem ini harus tahan dari hal hal berikut

1. Sadapan hacker
1. DDOS
1. Perubahan data secara unauthorized

Ada tantangan tersendiri ketika sistem memiliki kebutuhan kualitas layanan meskipun beban kerja yang tinggi. Apalagi kalau data yang ada merupakan data audiovisual

Interaksi dapat berdasarkan prosedural (siapa cepat dia dapat), maupun model pesan (klien server) dengan Remote Procedure Calls.

Middleware dapat digunakan sebagai software yang menjembatani antara sistem terdistribusi dengan klien. Umumnya aplikasi ini bersifat sebagai sebuah front end dari sistem. Aplikasi akan memberikan layanan API dari server dan membuat user biasa dapat berinteraksi dengan sistem secara terbatas

## Client Server Computing

 > 
 > \[!info\]
 > Internet merupakan sistem klien server terdistribusi terbesar didunia, menggunakan middleware browser

Aplikasi dalam klien server merupakan sebuah penyedia layanan, hal ini dapat berupa seperti web app [Google](http://www.google.com). Pada sistem ini, tidak mungkin semua request dapat dihandle oleh 1 komputer, namun dengan berbagai server menggunakan load balancing, agar menghindari high load dan meningkatkan performa

Dapat menggunakan struktur MVC juga dalam arsitektur softwarenya

## Pola Pola Arsitektural Untuk Sistem Terdistribusi

1. Master Slave, yaitu adanya node yang bertanggung jawab terhadap node lainnya
1. Two tier, yaitu sistem klien server. 
   1. Thin client dimana pemrosesan dilakukan di server. Sistem ini memiliki beban tinggi di server, namun dapat mensupport banyak user. Contoh Web app
   1. Fat client yang dimana pemrosesan dilakukan di klien. Sistem ini lebih ringan di server, namun end user biasa memerlukan sistem khusus untuk mengakses server Contoh. Game client / ATM
1. Multi tier, dimana tiap bagian MVC merupakan tiernya tersendiri. Menggunakan middleware middleware untuk menghandle komponen yang ada. Sistem ini banyak digunakan pada sistem terintegrasi yang scalable.

### Distributed Component Architectures

Adapun pendekatan lainnya adalah menggunakan sebuah communication middleware yang dapat berupa sebuah superapp. Superapp akan menjembatani terhadap berbagai layanan layanan yang ada secara terpisah. Contoh standarnya adalah CORBA, EJB, .NET

Kelebihannya adalah 

1. Node nodenya fleksibel dan multifungsi
1. Sangat scalable
1. Mudah dikonfigurasi ketika kebutuhan berubah

Kekurangannya adalah

1. Sangat sulit untuk dirancang
1. Tidak ada standar universal

### Peer to Peer Architectures

 > 
 > \[!info\]
 > Peer to peer adalah arsitektur dimana user adalah node dari sistem terdistribusi, tidak ada server maupun klien

Sistem ini populer pada sistem pribadi seperti pinjol, torrent, sms, kripto, VoIP, dsb

Pada arsitektur ini, setiap user adalah node dari bagian sistem yang besar. Oleh karena itu, seperti dalam sebuah torrent, ketika tidak ada yang seeding, maka file tidak tersedia

Kelebihannya adalah redundansi dan toleransi terhadap kegagalan. Hanya saja risiko dari overhead yang tinggi karena semua node harus bekerja sebagaimana sebuah klien dan server. 

Ada arsitektur semisentralisasi dimana ada superpeer yang membantu dalam komunikasi. Superpeer akan menjadi prosesor, dan peer biasa akan sekedar mendistribusikan apa yang telah diproses oleh superpeer. Sering ada pada seeding torrent

Sistem ini mendistribusikan komputasi dalam node node independen, dan juga mengurangi risiko terhadap kehilangan data. Hanya saja karena sifatnya desentralisasi, sulit untuk dikelola oleh 1 atau beberapa organisasi 

## Software As A Service

 > 
 > \[!abstract\] Definisi
 > SaaS merupakan software yang diinstal dalam server (cloud) yang diakses dengan browser. SaaS dikelola oleh vendor, dan user perlu membayar fee / menerima iklan. Contohnya adalah YT downloader, Google Docs, ChatGPT

Tantangannya adalah overhead transfer data untuk mengupload dan download. SaaS tidak harus merupakan layanan web, namun dapat berupa sebuah layanan yang diakses dengan implementasi komponen. 

Faktor yang harus perhatikan adalah

1. Software harus dapat diconfig berdasarkan kebutuhan user
1. Kemananan data user harus dijaga
1. Skalabilitas harus baik
1. Mendukung tools dari user seperti database
1. Access control

Untuk menangani masalah yang dapat muncul karena banyaknya pengguna, dapat dibuat database pribadi untuk setiap user, dengan identifikasi pengguna yang unik

Tips dalam membuat SaaS scalable

1. Layanan harus stateless dan sederhana
1. Menggunakan interaksi asynchronous
1. Kelola sumber daya dengan baik
1. Granularitas akses database yang baik
1. Gunakan PaaS
