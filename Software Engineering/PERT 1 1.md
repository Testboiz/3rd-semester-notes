# Gambaran Umum Rekayasa Perangkat Lunak

## Pengenalan

Rekayasa Perangkat Lunak (RPL) adalah bidang yang mempelajari pengembangan perangkat lunak yang berkualitas dan sesuai kebutuhan pengguna

 > 
 > \[!note\]
 > RPL selalu berubah sejalan zaman, sehingga metedologi yang ada pada saat ini belum tentu sama dalam beberapa tahun kedepan

## Definisi Perangkat Lunak

Perangkat Lunak juga dinamakan sistem perangkat lunak

 > 
 > \[!abstract\] Definition
 > Software adalah program yang diberikan dokumentasi. Software tidak dapat disebut perangkat lunak tanpanya
 > <cite> Rosa </cite>

Software dibangun dengan rekayasa, bukan manufaktur
Software tidak usang, namun diperbaharui

Contoh Aplikasi Perangkat Lunak

1. **Perangkat Lunak Sistem**, yaitu perangkat lunak yang mengelola perangkat lunak lain
1. **Perangkat lunak waktu nyata**, yaitu perangkat lunak yang memproses data secara waktu nyata/sangat cepat
1. **Perangkat lunak bisnis**, yaitu perangkat lunak yang mendukung berjalannya bisnis
1. **Perangkat lunak rekayasa & keilmuan**, yaitu perangkat lunak yang mengimplementasi algoritma/prosedur keilmuan
1. **Perangkat lunak tambahan (embedded)**, yaitu perangkat lunak yang membantu mengerjakan perangkat lunak/perangkat keras yang ada
1. **Perangkat lunak personal**, adalah perangkat lunak yang digunakan oleh user secara keseharian
1. **Perangkat lunak berbasis web**, adalah perangkat lunak yang menggunakan web browser untuk dijalankan
1. **Perangkat lunak kecerdasan buatan**, adalah pengaplikasian Machine Learning maupun algoritma dalam AI untum mengelola data dan mensimulasikan kecerdasan

## Definisi RPL

Ada 3 fase dalam RPL yaitu **what**, **how** dan **error**, Fase pendukung yaitu *correction*, *adaptation*, *enhancement*, dan *prevention*

Ada 2 jenis perangkat lunak yang dibuat yaitu 

* **Generic Product** yaitu produk yang berdiri sendiri dan dapat dijalankan oleh pengguna yang akan mendownloadnya
* **Customized Product** yaitu perangkat lunak yang didesain berdasarkan permintaan hardware, software ataupun use case

 > 
 > \[! abstract\] Definition
 > RPL adalah pembangunan dengan prinsip/konsep rekayasa agar dapat membuat perangkat lunak yang dapat dipercaya dan efisien
 > <cite>Rosa</cite>

 > 
 > \[!abstract\] Definition
 > RPL adalah disiplin teknik yang berkaitan dengan aspek produksi perangkat lunak dari spesifikasi hingga pemeliharaan
 > <cite>Sommerville</cite>

Ada dua poin penting dari kedua definisi berikut yaitu 

* Rekayasa adalah menerapkan teori/metode yang ada untuk mencari solusi berdasarkan batasan yang ada
* Aspeknya juga mencakup manajemen proyek, dan juga pengembangan semua hal yang mendukung

## Rekayasa Perangkat Lunak

Karakteristik produk yang dibuat adalah 

* **Akseptibilitas**, yang berarti perangkat lunak harus kompartibel dan dapat digunakan dengan mudah
* **Ketergantungan dan keamanan**, yang berarti perangkat lunak diusahakan untuk tidak berdampak secara fisik dan ekonomi ketika terjadi malfungsi, dan aman dari serangan yang ada
* **Efisiensi**, yang berarti suatu perangkat lunak harus menggunakan sumber daya secara baik
* **Pemeliharaan**, yaitu perangkat lunak harus dapat beradaptasi dengan perubahan zaman 

Perakayasa dapat menghabiskan waktu sebanyak yang ia mau untuk menyempurnakan suatu program untuk mencapai tingkat kualitas yang diinginkan. Memilih teknik yang tepat sangat penting agar dapat menghasilkan perangkat lunak berkualitas dalam waktu cepat. Juga perangkat lunak berubah sangat cepat dewasa ini sehingga metedologi sifatnya sangat fluid

RPL penting karena dapat menghasilkan perangkat lunak secara ekonomis, cepat, dan murah

Proses perancangan perangkat lunak adalah proses yang sistematis yang mengarah ke produksi perangkat lunak. Aktifitasnya adalah 

1. Spesifikasi (pembatasan) perangkat lunak
1. Pengembangan perangkat lunak
1. Validasi perangkat lunak (testing)
1. Evolusi perangkat lunak (software increment)

Dalam barbagai kasus tahap-tahap ini dapat dilakukan dengan urutan yang berbeda-beda tergantung [situasi](PERT%201%202.md#sdlc)

RPL membahas sisi praktis dalam pengembangan perangkat lunak agar dapat digunakan dalam kasus dunia nyata.  RPL fokus dalam aspek pengembangan dan evolusi terhadap sistem perangkat lunak tersebut. 

 > 
 > \[!note\]
 > Tidak seperti Algoritma, Machine Learning, maupun framework, RPL fokus kepada komunikasi, desain, dan bagaimana kita bekerja sama dalam menghasilkan suatu *software*

Masalah yang ada di RPL adalah 

1. Heterogenitas (greater support) (How you will **support** those stuff?)
1. Perubahan dunia dan perkembangan teknologi (How would you deal with **changes**?)
1. Keamanan perangkat lunak (How would you **handle security issues**?)
1. Scale (How would you scale to **millions or even billions**?)

Berbagai jenis aplikasi yang dapat dikembangkan adalah

1. **Stand-Alone**, yaitu aplikasi yang berdiri sendiri tanpa server/internet
1. **Transaction-based**, yaitu aplikasi yang dapat diakses secara remote seperti e commerce
1. **Embedded control system**, adalah sistem kontrol perangkat lunak yang mengelola perangkat keras
1. **Pemrosesan Batch**, yaitu aplikasi yang memroses data dalam jumlah besar seperti sistem penagihan
1. **Entertainment System**, adalah sistem yang dibuat untuk hiburan (game, musik, dll)
1. **Modelling and simulation system**, adalah sistem yang digunakan untuk mensimulasikan model matematika
1. **Sistem pengumpulan dan analisis data**, adalah sistem yang mengekstrak big data untuk diproses 
1. **System of Systems**, adalah sistem yang mengelola sistem lain

Dasar dasar rekayasa yang universal ialah :

1. Sistematis dan mudah dipahami
1. Menghindari error
1. Memenuhi requirement
1. Efisien

Web zaman sekarang semakin terintegrasi dalam kehidupan, termasuk dalam perangkat lunak. Contohnya adalah Web App dan Cloud App.
Pengembangan Web dilakukan secara bertahap dan perangkat lunaknya memiliki orientasi layanan

Jenis aplikasi yang mendominasi dunia saat ini adalah :

1. **WebApp** yaitu aplikasi yang berjalan dalam internet
1. **Mobile App** adalah aplikasi yang berjalan di HP
1. **Cloud Computing** adalah infrastruktur yang memudahkan pengguna untuk mendapat akses komputasi skala besar dengan mudah
1. **Product Line Software** adalah pengembangan produk yang memamfaatkan kesamaan dari tiap produk tersebut

## Etika RPL

Perilaku etis, menghargai kode etik, kejujuran, integritas sangat penting dalam RPL karena RPL juga adalah bagian dari kehidupan bermasyarakat

Hal hal yang tak begitu terikat dengan hukum namun dengan kode etik adalah :

* Kerahasiaan dan privasi
* Menerima pekerjaan dalam kompetensi
* Menghargai HAKI
* Tidak menyalahgunakan komputer
