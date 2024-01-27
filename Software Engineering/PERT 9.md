# PERT 9 - Rekayasa Perangkat Lunak Berbasis Komponen

## Komponen dan Model-Model Komponen

Menurut Countill dan Heineman (2021), komponen adalah

 > 
 > Elemen perangkat lunak yang sesuai dengan modelkomponen standar dan dapat diterapkan dan disusun secara independen tanpa modifikasi sesuai dengan standar komposisi

 > 
 > Komponen perangkat lunak adalah unit komposisi dengan antarmuka yang ditentukan secara kontrak dan hanya ketergantungan konteks eksplisit. Komponen perangkat lunak dapat digunakan secara independen dan diatur oleh pihak ketiga.

Komponen pada definisi ini lebih ditekankan sebagai unit komputasi inti dari sistem. 

Karakteristik komponen adalah :

1. Composable (dapat berada dalam komponen lainnya)
1. Deployable (dapat berjalan sendiri)
1. Documented 
1. Independent (tidak bergantung komponen lain)
1. Standardized (mengikuti model standar)

Komponen juga dapat memberikan layanan kepada komponen lain, sehingga mudah direuse. Contoh `ls` di UNIX merupakan command yang juga berupa sebuah komponen, penggunaannya adalah dengan menggunakan command itu, bukan cara lain.

Interface tersebut dapat berupa API, library, framework maupun dependensi

Interface dalam pemograman sering berupa sebuah Objek, Interface, Library yang umumnya diakses dengan method method yang tersedia. Library tersebut harus dapat berdiri sendiri. Contohnya library matematika tidak harus mengimport kode program untuk database, dsb

### Component Model

 > 
 > \[!abstrak\] Definisi
 > Model komponen adalah definisi standar dari cara menggunakan sebuah komponen. Hal ini meliputi user manual, dependensi yang dibutuhkan, middleware, convention dsb. Contohnya adalah Flutter

Hal hal yang membuat sebuah model komponen yang baik adalah

1. Harus ada pendefinisian interface yang baik. Attribut, method, parameter, cara koding, dsb
1. Menual harus dapat diakses dengan mudah secara jarak jauh
1. Informasi teradap build passing dsb harus dikemas dengan jelas

Middleware yang dapat disediakan dalam komponen tersebut adalah

* Platform service. Hal ini meliputi addressing, interface definition, exception handling dan component communications. Hal ini merupakan middleware yang menghandle interaksi antar komponen
* Support Service, ini meliputi fitur-fitur tambahan untuk memudahkan programmer dalam membuat aplikasi Contoh : security, persistence, concurrence, resource management, dsb

Sering middleware diletakan dalam sebuah container seperti Docker

## CBSE Process

CBSE Processes meningkatkan reuse komponen dengan pembuatan komponen reusable. CBSE sangat menekankan reuse.

Generalisasi cara pakai fungsi agar dapat digunakan secara efektif. Hal ini meliputi membuat interface, membuat parameter baru, wrapper, dsb

Component Acquisition meliputi membeli, mendownload dan menginstal komponen, Component management meliputi pengelolaan komponen agar dapat dijalankan dengan baik dan Component certification adalah proses standardisasi komponen

### CBSE For Reuse

 > 
 > \[!abstract\] Definisi
 > Merupakan proses untuk membuat komponen yang dapat direuse oleh projek-projek masa depan

Komponen dibuat menjadi sebuah package yang dapat diinstal dan di runningkan. Anggap komponen adalah sebuah software tersendiri. Hanya saja biaya dokumentasi untuk ini cukup tinggi karena kebutuhannya cukup menekankan dokumentasi

Exception handling cukup dilematis karena ketika sebuah library mensupport eksepsi tersebut, semakin kompleks librarynya, namun jika tidak, maka library kurang robust. Exception umum harus ditangani secara lokal (pada komponennya)

Pengembangan komponen akan menghemat biaya pengembangan software berikutnya, karena tidak perlu reinventing the wheel. Untuk menilai penghematannya dapat menggunakan model COCOMO.

Perhatikan apakah komponen yang akan direuse sering digunakan tidak. Contoh : CSS themes lebih banyak dipakai, sedangkan kode Javascript umumnya tidak sesering itu

Sistem lawas mungkin memiliki komponen yang dapat digunakan, kita dapat menggunakan wrapper / middleware untuk meningkatkan kompartibilitasnya

## CBSE with Reuse

Menemukan komponen yang tepat dapat memodifikasi persyaratan yang ada. Persyaratan akan diupdate pada saat tools/komponen yang tersedia didapat. Alangkah baiknya untuk memiliki persyaratan yang fleksibel. 

 > 
 > \[!warn\]
 > Tidak selamanya kita dapat menemukan framework yang kita butuhkan, sehingga CBSE dan komponen kustom dapat menjadi solusinya

CBSE meliputi

1. Pencarian komponen (open source/closed source/ API)
1. Pemilihan komponen berdasarkan keamanan, kegunaan,dsb
1. Validasi Komponen

## Komposisi Komponen

Studi Kasus dengan mudah menggambarkan bagaimana komponen komponen terkomposisi. Contohnya di library matematika

1. Sequential (fungsi konversi pecahan ke desimal perlu menyederhanakannya dahulu)
1. Hierarchical (Perhitungan numerik trigonometri dengan fungsi private)
1. Additive (set fungsi trigonometri seperti `sin`,`cos`,`tan`,dsb dalam sebuah objek Lingkaran)

Tidak selamanya interface tiap komponen kompartibel terhadap satu sama lain. Contohnya adalah :

1. Parameter Incomparitbility (parameter mismatch, different order)
1. Operation Incompartibility (no overrides for `+`,`-`,dsb)
1. Operator Incompleteness (tidak `implements` interface, ataupun `extend` kelas)

Sistem berdasarkan komposisi komponen harus memperhatikan hal berikut :

1. Memiliki komposisi yang paling efektif
1. Mudah diubah ketika persyaratan diubah
1. Memiliki sifat yang mudah diprediksi

Terkadang dalam kenyataanya ada trade off yang membuat kita harus mengorbankan salah satu dari poin diatas untuk komponen lain.

Keuntungan terbesar dari rekayasa berbasis komponen adalah **separation of concerns**, dimana tiap komponen fokus pada 1 peran yang tidak dipengaruhi oleh komponen lain dalam sistem
