# PERT 8 Software Reuse

## Lanskap Reuse

Reuse baru booming pada abad ke 21 karena pengembangan software semakin mahal. Reuse menghindari pengembangan ulang software yang merupakan fase termahal. Contoh reuse adalah :

1. Reuse sistem (menggunakan sistem yang dikonfig berbeda)
1. Reuse aplikasi (menggunakan aplikasi lama di tim/organisasi baru)
1. Reuse komponen (menggunakan library?API yang sudah ada )
1. Reuse objek / fungsi (mengambil objek/fungsi yang ada dan menganggapnya sebagai library)

Perlu diperhatikan bahwa software yang sangat kompleks dan spesialis akan semakin sulit untuk di reuse, sehingga reuse juga sering diadaptasi dalam proses rekayasa. Jadinya rekayasa menggunakan ulang persyaratan dan desain yang ada. Hal ini juga dapat mengurangi biaya pengembangan karena testing, verification, dan validation dapat diskip

Keuntungan lainnya adalah

1. Lebih cepat dan murah untuk didevelop
1. Software kian handal
1. Risiko berkurang
   Kekurangannya adalah
1. Pengembangan library menjadi mahal
1. Programmer mungkin kesulitan menentukan komponen yang tepat
1. Maintainance semakin mahal dengan faktor library
1. Support reuse terbatas
1. Sindrom [Not Invented Here](https://xkcd.com/927/)

Lanskap Reuse merupakan teknik teknik yang digunakan untuk membuat software yang dapat direuse. Hal tersebut berupa berikut

![Screenshot 2023-11-23 at 18-44-57 Slide 1 - PB11MAT_TIF08 - 10 - P 18.pdf.png](Screenshot%202023-11-23%20at%2018-44-57%20Slide%201%20-%20PB11MAT_TIF08%20-%2010%20-%20P%2018.pdf.png)
![Pasted image 20231123184537.png](Pasted%20image%2020231123184537.png)
Hal yang perlu diperhatikan dalam reuse adalah

1. Waktu, Gunakan reuse sistem ketika waktu mepet, dan reuse komponen jika tidak
1. Masa pakai, fokus ke maintainance jika perlu tahan lama
1. Kemampuan tim, memastikan tim memahami komponen dengan baik
1. Kekritisan perangkat lunak dan persyaratan non fungsional, perhatikan faktor regulasi dan keamanan
1. Domain aplikasi, aplikasi tertentu mungkin lebih reusable
1. Platform sistem yang dijalankan, OS maupun framework yang bekerja

## Application Frameworks

OOP sangat efektif dalam membuat kelas yang dapat di reuse, namun umumnya reuse sangat terbatas. Menurut Schmidt dkk framework adalah

 > 
 > sebuah keterintegrasian set artefak software (seperti kelas, objek dan komponen) yang berkolaborasi untuk menyediakan arsitektur dapat digunakan kembali untuk keluarga aplikasi yang terkait

Framework menekankan reuse berdasarkan OOP, banyak bahasa pemograman populer memilikinya. Framework bahkan dapat didevelop dengan framework lainnya. Framework sering dibuat untuk membuat aplikasi web dan mobile. 

MVC adalah arsitektur yang memisahkan GUI, DB dan BL dari suatu aplikasi. Perubahan pada satu bagian tidak akan memengaruhi bagian lainnya. Berbagai kerangka kerja dapat dipilih dalam pengembangan MVC seperti pengamat, strategi dan komposit. Tiap komponen MVC memiliki event loopnya tersendiri

MVC umumnya mendukung fitur berikut :

1. Security WAF
1. Dynamic Web Pages
1. Database Integration
1. Session Management Class
1. UI/UX

Kelas framework lainnya adalah

1. System Infrastructure Framework (membantu dalam komunikasi, layout dan jaringan)
1. Middleware Integration Framework (.NET dan Netbeans)
1. Enterprise Application Framework (membantu mengembangkan aplikasi untuk dipakai langsung oleh end user)

Aplikasi dengan framework dapat dikembangkan lebih lanjut menjadi Product Line Application, melalui penulisan kelas dan method ke kerangka kerja. Kerangka kerja ini sangat efektif, namun sulit dibuat dan perlu pemahaman tinggi

## Software Product LInes

Product Lines dapat digambarkan seperti aplikasi rooting, serupa namun tidak sama karena kebutuhan platform yang berbeda beda

Product Line adalah software yang memiliki tujuan dan arsitektur sama, namun dengan perbedaan deployment

Pengembangannya sangat murah karena perubahan yang ada bersifat konfigurasi, dan testing dapat dikurangi secara signifikan, dengan fokus pada isu isu deployment

Ada 3 lapisan komponen dari product line software 

1. Komponen inti (logic utama aplikasi yang memenuhi kebutuhan non deployment)
1. Komponen yang dapat dikonfigurasi (memudahkan developer untuk deployment secara parametrik )
1. Komponen khusus yang harus didevelop tiap platform baru

Dalam OOP, Interface, Inheritance dan Polymorfisme sangat berperan dalam membentuk komponen diatas, Desain product line identik dengan aplikasi umum, perbedaan hanya ada pada konfigurasi deployment

Contoh : [ Layered Architecture](PERT%204.md#layered-architecture), kita dapat menggangap tiap layer sebagai sebuah komponen

Spesialisasi yang dapat dicapai oleh product line software adalah

* Platform
* Environment
* Functional
* Process

Inti dari product line software adalah **KONFIGURASI**, konfigurasi ini daapt dilakukan pada saat design time (hard code / config file) maupun deployment time (menggunakan setting). Tingkat config yang dapat dilakukan adalah

1. Penentuan komponen yang akan diconfig
1. Menentukan cara kerja dari aplikasi
1. Menentukan parameter yang baru dan teradaptasi

Konfigurasi cukup kompleks juga, terkadang ini memerlukan testing yang cukup lama dan mahal. Namun testing config jauh lebih mudah untuk diotomatisasikan

## Application System Reuse

Mayoritas software yang ada di dunia adalah aplikasi (software yang didesain dengan penekanan end user). Kebanyakan didesain untuk orang banyak, bukan pelanggan khusus

Terkadang aplikasi menggunakan komponen open source, dan umumnya komponen ini jarang dimodifikasi. Konfigurasi umumnya dilakukan secara built in berdasarkan kebutuhan yang ada

Reuse dalam aplikasi memiliki dampak berikut

* Sistem lebih andal
* Lebih memahami aplikasi yang ada
* Minimalisir risiko
* Biaya dapat dihemat
* Aplikasi dapat menghandle perubahan secara mandiri
  Kekurangannya adalah
* Persyaratan yang lebih kompleks
* Proses SOP harus dimodifikasi
* Belum tentu aplikasi tepat digunakan
* Kurangnya talent yang memadai
* Vendor memiliki power yang besar terhadap aplikasi

Sistem aplikasi adalah 2 atau lebih aplikasi yang diconfig untuk menjadi ssitem terintegrasi,  menggabungkan berbagai komponen dan konfigurasi untuk memenuhi persyaratan dengan prinsip reuse.

![Pasted image 20231123195327.png](Pasted%20image%2020231123195327.png)

 > 
 > \[!note\]
 > Terkadang, kita tidak menyadari fleksibilitas dari suatu aplikasi, aplikasi penjadwalan dokter, dapat digunakan di hotel dengan config config yang disediakan

Terkadang kita melihat aplikasi generik/template yang sangat mudah untuk diconfig untuk kebutuhan kita Contohnya adalah teks editor [`neovim`](https://neovim.io),

Pada kasus aplikasi generik, terkadang aplikasi entreprise seperti ERP dapat diconfig untuk use case organisasi tertentu berdasarkan kebutuhan. Pengkonfigurasian aplikasi generik menjadi spesialis meliputi hal berikut

1. Menentukan modul yang dibutuhkan
1. Menyesuaikan dengan kebutuhan
1. Menyiapkan DB dan config komponen yang dibutuhkan
   Setelah itu kita tetap perlu testing. Kesulitannya adalah testing dalam aplikasi generik yang menggunakan integrasi aplikasi lain adalah interaksinya yang berbeda, dan juga otomatisasi sulit tanpa middleware

Prinsip prinsip OOP dapat memudahkan kita dalam mengenkapsulasi aplikasi-aplikasi yang berbeda dan mengkoneksikannya dengan adaptor (middleware), hal ini membuat aplikasi tersebut dapat dianggap sebagai sebuah komponen

Integrasi aplikasi memiliki prinsip-prinsip mirip prinsipnya dengan CBSE, namun interfacenya yang akan menghandle interaksi interaksi yang jauh berbeda (Boehm dan Abs 1999). Masalahnya dalam integrasi aplikasi adalah

1. Kurangnya kendali atas fungsionalitas, evolusi sistem, dan kinerja
1. Interoperabilitas (mungkin butuh middleware)
1. Support dari vendor
1. Biaya pemeliharaan tinggi
