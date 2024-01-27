# Dependable Systems

## Dependability Properties

Pada zaman sekarang, dimana sistem semakin terintegrasi terhadap sendi sendi kehidupan, kesalahan bug dan glitch pada program dapat berdampak buruk terhadap pengguna, organisasi atau bahkan terjadinya kehilangan nyawa. Sehingga software dituntut untuk dapat dipercaya, harus tersedia saat dibutuhkan dan beroperasi tanpa bug/glitch

Beberapa alasan mengapa ketergantungan sistem ada, yaitu karena

* Kegagalan berdampak pada banyak/seluruh user
* Pengguna tidak ingin software yang cacat
* Biaya kegagalan yang tinggi (materil atau bahkan nyawa)
* Kehilangan informasi/data penting

Penyebab kesalahan yang dapat merusak keandalan software adalah 

* Kesalahan dari perangkat keras yang rusak/cacat
* Kesalahan desain, arsitektur, persyaratan maupun implementasi perangkat lunak yang menyebabkan bug/glitch
* Kesalahan penggunanya sendiri

Ada 5 dimensi ketergantungan user terhadap software yaitu

1. Ketersediaan software (24/7 maupun High Availability)
1. Reliabilitas (Seberapa jarangnya software mengalami kegagalan)
1. Keselamatan pengguna saat menggunakan software
1. Keamanan user dalam software
1. Ketahanan atas kejadian yang dapat merusak seperti bencana alam maupun serangan siber
   Selain itu, software juga perlu memiliki sifat berikut agar menjadi software yang dapat diandalkan
1. Dapat diperbaiki dengan cepat
1. Mudah dipelihara (Maintainable)
1. Toleran terhadap kesalahan input (request ulang/koreksi otomatis)
   Sistem yang aman haruslah andal dalam pengoperasiannya

Dalam rekayasa, kita dapat meningkatkan keandalan sistem dengan berikut 

1. Menghindari kesalahan dalam spesifikasi persyaratan
1. Melakukan verifikasi dan validasi persyaratan secara efektif
1. Merancang sistem yang resilien
1. Merancang perlindungan atas serangan terhadap sistem
1. Memberikan konfigurasi yang tepat
1. Membuat sistem cepat pulih dari serangan tersebut

Redundansi justru baik dalam meningkatkan resiliensi, karena dapat mendeteksi kesalahan yang mungkin terjadi. Hal ini dapat memengaruhi kinerja, sehingga perlu bijak dalam menyeimbangkan kinerja dan reliabilitas. Semakin reliabel suatu sistem, semakin kompleks proses desain, implementasi dan validasi terhadap sistem. Sehingga membuat biaya rekayasa membengkak

## Sociotechnical Systems

Perangkat keras butuh perangkat lunak agar dapat bekerja. Komputer dengan perangkat kerasnya dan perangkat lunaknya terintegrasi kepada lingkungan masyarakat. Sistem yang merupakan  bagian dari masyarakat dinamakan sistem sosioteknik. Dapat digambarkan dalam sebuah lapisan yaitu

1. Masyarakat
1. Organisasi
1. Proses kerja
1. Aplikasi
1. Database dan logic aplikasi
1. Sistem Operasi
1. Hardware

Systems Engineering meliputi lapisan 2-7, sedangkan Software Engineering meliputi lapisan 3-6. Lapisan-lapisan ini berinteraksi satu sama lain dengan suatu kesatuan. Semua lapisan merupakan layer abstraksi dari layer dibawahnya. Adapun risiko interaksi tak terduga seperti update os, perubahan manajemen maupun undang-undang dapat mempengaruhi seluruh sistem

Sistem perlu diperhatikan dalam satu kesatuan penting dalam memperhatikan keamanan dan keandalan sistem. Kerusakan yang terjadi pada perangkat lunak dapat mudah dipulihkan sebelum menembus bagian lain, yang akan meningkatkan biaya dan kompleksitas. Pandangan holistik ini akan membuat perancang software memerhatikan dampak dari software ke masyarakat

Hal yang perlu dipastikan dalam interaksi perangkat lunak dengan lingkungan adalah 

1. Minimalisir kegagalan agar tidak memengaruhi operasi
1. Memahami pengaruh bug maupun glitch pada OS maupun hardware memengaruhi sistem
   Sering kegagalan terjadi karena software banyak menggunakan teknik tambal sulam dalam mengakomodasi persyaratan yang berubah

### Regulasi dan Kepatuhan

Pemerintah meregulasi organisasi organisasi laba maupun nirlaba agar software memiliki standar tertentu sehingga aman dan terjamin. Regulasi tersebut dapat berbentuk undang-undang, peraturan maupun badan pengawas. Pelanggaran dapat disanksi dengan denda, pidana maupun pencabutan izin.

Standar tersebut dapat berupa bentuk lisensi, kontrak yang menjamin keamanan sistem. Jaminan tersebut juga harus menjamin ketika sistem gagal, masih ada mekanisme perlindungan alternatif yang tidak menggunakan perangkat lunak

## Redundancy and Diversity

Bug, glitch dan kesalahan merupakan keniscayaan dalam suatu sistem. Oleh karena itu, sistem harus mampu menangani kegagalan tersebut agar tidak memengaruhi seluruh sistem. Pendekatannya melalui redundansi dan kegagalan

* Redundansi dapat digambarkan sebagai pemain cadangan yang menggantikan perangkat keras/lunak yang gagal
* Keragaman berarti komponen redundan memiliki jenis yang berbeda, sehingga mencegah kegagalan yang sama, dan memengaruhi seluruh sistem
  Selain itu juga dapat memberikan kode pengecekan yang menangani potensi kegagalan yang ada. 

Redundansi sering digunakan pada sistem yang memiliki ketersediaan sebagai persyaratan utama. Ada juga pendekatan redundansi dengan menggunakan sistem operasi lain. 

Redundansi juga dapat diimplementasikan dalam proses desain. Redundansi dapat berupa seperti pencegahan kesalahan dalam sistem, validasi, inspeksi, analisis, testing, dsb. Pendekatan ini dapat memberikan perspektif berbeda terhadap sistem

Redundansi menambahkan kompleksitas, yang berisiko terhadap potensi kesalahan yang tidak terdeteksi. Oleh karena itu sebagian pendekatan pengembangan menghindari redundansi dan variasi secara penuh, dan meingkatkan verifikasi dan validasi. 

## Dependable Processes

Proses yang dapat diandalkan akan menghasilkan perangkat lunak yang diandalkan. Caranya adalah dengan 

1. Software harus mudah dipahami
1. Software harus redundan atau divalidasi dengan benar
1. Dokumentasi yang baik
1. Tahan terhadap potensi kegagalan
1. Terstandar

Dengan proses yang dapat diandalkan, kita dapat memastikan kepada regulator bahwa standar standar telah dipenuhi. 
Proses harus didokumentasi dengan baik, dan menggunakan model yang benar 
Proses harus dapat diulang pada lingkungan yang berbeda, agar proses tersebut betul-betul sistematis dan dapat diandalkan

Pendekatan redundansi maupun verifikasi dapat digunakan secara bersama sama agar dapat menemukan lebih banyak kesalahan yang ada 

Hal yang dapat dilakukan untuk menganalisa apakah proses dapat diandalkan adalah

1. Peninjauan persyaratan
1. Manajemen Persyaratan, dan pengelolaan perubahan persyaratan
1. Spesifikasi formal (model matematika perangkat lunak)
1. Pemodelan sistem (UML)
1. Desain dan inspeksi oleh tim khusus
1. Analisis kode program
1. Pengelolaan pengujian secara komprehensif

Proses harus juga dilengkapi dengan manajemen kualitas dan perubahan yang baik. Selain itu juga reliabilitas proses bergantung pada tiap organisasi. Namun kebutuhan atas kualitas dan manajemen perubahan bersifat universal.

Sistem yang kritis pun juga tidak dipungkiri mulai menggunakan sistem agile, karena lebih cepat. Pendekatannya menggunakan sertifikasi, analisis persyaratan, analisis perubahan formal, dan pengecekan persyaratan yang bertentangan. 

Teknik agile tidak selamanya ngebut, namun suatu teknik dapat dikatakan agile ketika mneggunakan pengembangan berulang, user testing, uji pertama. Hal tersebut telah memenuhi hakikat proses agile

## Formal Methods and Dependability

Metode formal yang dimaksud adalah **pendekatan matematis** terhadap pengembangan software yang digunakan untuk mencari kesalahan dan ketidakkonsistenan. 

Caranya adalah dengan menggunakan bukti matematika. Spesifikasi formal dikembangkan yang merupakan basis konjektur yang akan dibuktikan. Kemudian dibuktikan dengan software maupun secara manual, tergantung kompleksitas software.

[TDD](PERT%206.md#test-driven-development) merupakan alternatif dari pembuktian tersebut, dimana pembuktian direpresentasikan sebagai proses testing dalam software. 

Selain itu juga dapat dilakukan pendekatan pemeriksaan model, dimana model akan diuji atas properti yang merupakan persyaratan sistem. Pemodelan ini mengetes apakah sistem memenuhi persyaratan dalam bentuk model matematika. 

Kesalahan yang dapat ditemukan dalam pemodelan ini adalah

* Kesalahan pada spesifikasi dan desain (yang mungkin tidak terdeteksi dalam testing)
* Ketidakkonsistenan spesifikasi dengan program

Pada pemodelan ini perlu membuat model sistem matematika yang ditransformasi menjadi semantik bahasa formal matematika. Spesifikasi ini akan menghindari potensi kesalahpahaman terhadap sistem, yang dapat terjadi pada spesifikasi bahasa manusia. 

Kelebihan spesifikasi ini adalah

* Pemahaman yang mendalam dan terperinci, sehingga masalah dapat dideteksi dengan awal
* Dapat langsung melakukan validasi terhadap potensi kesalahan
* Spesifikasi dapat langsung diubah menjadi urutan transformasi
* Biaya pengujian yang berkurang
  Kekurangannya adalah 
* Jarang orang memahami spesifikasi tersebut
* Sulit menentukan potensi penghematan biaya dari metode tersebut
* Sulit untuk diimplementasi
* Keterbatasan alat yang ada
* Tidak kompartibel dengan Agile SDLC
