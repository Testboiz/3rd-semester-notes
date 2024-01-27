### Unit Test Cases

Testing cukup memakan waktu, sehingga kasus pengujian harus efektif, yaitu mewakili seluruh komponen yang teruji melalui kasus uji pada SOP (partisi), dan potensi masalah lainnya (pedoman).

Data dapat digambarkan dengan operasi himpunan berikut $\mathbb{Z} \rightarrow \mathbb{Z}$ alias input dan output bertipe sama. Oleh karena itu, ada sistematika testing dimana kita memantau jenis output yang ada, dan apakah konsisten dengan input, berdasarkan konsep partisi dan himpunan 

Ada kemungkinan setiap input dapat terpetakan satu satu ke output (fungsi yang menambah angka dengan 1), namun dalam kenyataannya fungsi dapat mengoutput seperti `null` ketika ada hal yang tidak beres terjadi (input tak valid).

Kemudian pada testing dipilih nilai yang berada pada kasus normal, dan nilai-nilai yang berpotensi error, umumnya `null`,`0`, maupun bilangan negatif dihindari karena potensi errornya.

SRS umumnya sudah memberikan batasan batasan testing untuk memudahkan kita melakukannya, pengetes hanya perlu mengetes nilai pada batasan himpunan dan tengah himpunan, Nilai pada batasan himpunan umumnya adalah sumber utama error.

Jika kita sekadar mengecek kekonsistenan input output hal tersebut dinamakan *black box testing*, namun jika kita juga memperhatikan kode program, dinamakan *white box testing*.

Program akan disesuaikan agar dapat menolak input yang berpotensi bermasalah, karena input yang berada pada ujung partisi.

Pedoman testing membantu kita dalam menguji secara sistematis, contohnya dengan array :

* Pass array dengan panjang 1
* Cek dengan array yang memiliki panjang berbeda beda
* Cek pengaksesan elemen pertama, tengah dan terakhir
  Selain itu (Whittaker 2009) juga menambahkan untuk pedoman umum :
* Paksakan error dengan input bermasalah
* Jadikan buffer offerflow
* Ulangi testing beberapa kali
* Paksakan output tidak valid
* Paksakan output menjadi terlalu besar/kecil
  Pengalaman akan membantu kita membuat pedoman yang lebih baik

### Component Testing

 > 
 > \[!abstract\] Definition
 > Yaitu pengetesan dimana beberapa objek berinteraksi satu sama lain.

Terkadang integrasi komponen yang kurang tepat dapat menyebabkan error yang tidak dapat dideteksi pada fase [Unit Test Cases](PERT%206.md#unit-test-cases). 

Interface yang dapat dites dalam fase ini adalah :

1. **Parameter interface**, yaitu data return maupun input yang dipassing ke objek lain
1. **Shared memory interface**, yaitu data pada memory yang diakses oleh bebrapa objek sekaligus. Terkadang sistem asinkron maupun objek komposit dapat memiliki interface ini
1. **Procedural interface**, yaitu fungsi fungsi yang menjalankan fungsi-fungsi lain sebagai bentuk abstraksi seperti contohnya fungsi `buildUI()`
1. **Message passing interface**, dimana pesan pesan dalam bentuk POST, GET, TCP, IP, dsb dikirimkan dan diterima pada arsitektur klien server.

Kesalahan yang umum terjadi pada interface ini ialah :

1. **Interface misuse**, dimana penggunaan interface tidak semestinya Contoh :

* Passing parameter bertipe salah
* Urutan parameter/prosedur salah
* Header POST yang salah, dsb
* Menshare data yang salah ke thread lainnya

2. **Interface misunderstanding**, yaitu penggunaan komponen yang salah. Contoh :

* Pemanggilan prosedur yang salah
* Parameter yang tidak sesuai standar SOP
* Tipedata yang salah
* API key/website yang salah

3. **Timing error**, dimana sistem memiliki penghitungan waktu yang tidak tepat. Dapat menggunakan data yang kadarluasa. Contoh :

* Merequest data pada proses yang kurang tepat
* Thread synchronization, dan masalah pada promises
* Timing yang salah pada sistem real time

Penentuan kesalahan ini umumnya cukup sulit, karena terkadang kesalahan dapat terjadi karena kondisi yang tidak diharapkan. Umumnya masalah ini baru dapat dideteksi dengan memaksakan error.

Seringkali kesalalahan baru terdeteksi jika komponen malfungsi memberikan output yang salah, sehingga sering dianggap menjadi masalah pada interface yang salah/unit testing, atau bahkan tidak terdeteksi.

Pedoman umum pada fase ini ialah :

* Cek kode secara manual
* Buat reference `null`
* Paksakan error
* Buat stress testing untuk client server
* Gunakan asumsi yang berbeda-beda dalam manajemen memori

 > 
 > \[!note\]
 > Inspeksi umumnya dapat menangkap masalah masalah pada component testing secara lebih efektif

### Systems testing

 > 
 > \[!abstract\] Definisi
 > Yaitu pengetesan antar komponen yang membentuk 1 sistem utuh.

Pengujian ini menemukan bug yang ada pada integrasi komponen pada sistem. 

Use case based testing digunakan pada fase ini, kita menguji use case terhadap sistem, dan memastikan program bebas dari kesalahan. 

Kita akan mengetes aksi yang kita petakan pada use case maupun sequence secara SOP atau edge case untuk menentukan error.

Pengujian ini paling sulit untuk diotomatisir karena output sulit diprediksi

## Test Driven Development

 > 
 > \[!abstract\] Definisi
 > Yaitu pendekatan pengembangan dimana setiap step pengembangan akan langsung dites. Pengembangan tidak akan dilanjutkan sampai kode pass testing. 

Banyak digunakan pada agile SDLC maupun plan based SDLC. Langkah-langkahnya adalah

1. Identifikasi upgrade fungsionalitas
1. Tes fungsionalitas tersebut
1. Review dan refactor potensi kesalahan
1. Jika berhasil, ulangi step 1

Lingkungan pengujian otomatis sangat membantu dalam TDD, Contohnya JUnit. Hal ini membantu untuk mengetes dengan cepat. 

Pemahaman potensi error penting karena, meskipun dibantu dengan lingkungan tes, jika tida memerhatikan potensi error, maka potensi error tersebur tidak ditangani

Mamfaat dari TDD adalah :

1. Error dapat terdeteksi seawal mungkin
1. Regresi pengujian membantu dalam increment fungsionalitas, dan memercepat proses development
1. Tidak perlu sering sering debugging

Pengujian regresi ini cukup mahal, karena itu TDD membuat pengujian ini jauh lebih murah dan streamlined. 

TDD efektif untuk projek baru yang menggunakan standard library, namun kurang efektif pada sistem multithread.

TDD tidak menghilangkan Component Testing dan System Testing. 

TDD juga populer pada banyak developer

## Release Testing

 > 
 > \[!abstract\] Definisi
 > Yaitu pengujian setelah software dirilis, umumnya oleh user maupun tim khusus

Pada saat release testing, validasi yang dilakukan adalah validasi akan kebutuhan yang ada, memastikan software memenuhinya.

Release testing menggunakan black box. 

### Requirement based Testing

 > 
 > \[!abstract\] Definisi
 > Yaitu dimana persyararatan harus dapat diuji dalam fase testing

Pengetesan ini lebih mengarah ke validasi daripada menemukan bug. 

### Scenario Testing

 > 
 > \[!abstract\] Definisi
 > Yaitu pendekatan dimana kita mendesain skenario akan bagaimana software akan digunakan.

Skenario harus merepresentasikan SOP dari software, Skenario dapat berupa narasi agar dapat dipahami berbagai pemangku kepentingan (Kaner 2003)

### Performance Testing

 > 
 > \[!abstract\] Definisi
 > Yaitu pengetesan untuk menguji apakah software memenuhi kemampuan/performa yang diharapkan

Umumnya dilakukan dengan stress testing, yaitu pengujian dengan menjalankan sistem diluar batasan performa sistem.

Stress test membantu dalam menentukan bagaimana sistem akan gagal dimana apakah akan membahayakan data atau tidak. Selain itu juga dapat menemukan bug yang tak terdeteksi pada load standar

## User Testing

 > 
 > \[!abstract\] Definisi
 > Pengguna yang merupakan penguji, dan akan memberikan masukan dan saran. Pengguna dapat berekperimen ataupun menggunakan software dalam SOP

Lebih umum daripada tidak, bug dan error masih bisa selip dan menggangu user, Oleh karena itu ada berbagai testing yang dapat dilakukan yaitu

1. **Alpha**, pengguna bekerja sama dengan developer secara langsung
1. **Beta**, pengguna yang lebih besar dan umumnya testing secara remote
1. ***Acceptance Testing***, pengujian apakah sistem dapat diterima atau tidak

Proses Acceptance Testing ialah :

1. **Define Acceptance Criteria**, menentukan kriteria bagaimana software akan diterima oleh klien
1. **Plan Acceptance Testing**, kita akan merencanakan bagaimana Acceptance Testing harus dijalankan
1. **Derive Acceptance Testing**, desain bagaimana tes harus dijalankan, mengikuti requirement yang ada
1. **Run acceptance Testing**, Lakukan desain di lapangan dan simulasikan kondisinya. 
1. **NEGOTIATE TEST RESULT**, lebih sering daripada tidak, ketidaksetujuan akan hasil tes harus dinegosiasikan, agar kesepakatan dapat dicapai.
1. **Reject/Accept system**, pada akhirnya sistem akan disetujui atau ditolak oleh klien, jika penolakan maka dinegosiasikan apakah tahap testing dapat diulang

Hasil negosiasi dapat menjadi persyaratan dari sistem, hal tersebut memungkinkan developer untuk update software dan kirimkan ke user.

Dalam sistem agile, semua jenis user testing digabung jadi 1, pengguna adalah penguji Alpha yang memberikan user stories yang berupa cerita bagaimana menggunakan software

Pengguna pada sistem agile dianggap sebagai user yang akan menggunakan sistem sebagaimana klien.

Terkadang acceptance testing belum tentu mencerminkan kondisi nyata apalagi dalam sistem agile dimana testing dilakukan secara **otomatis**.

Pengujian otomatis ini sering kurang ideal, sehingga sering SDLC agile digabung dengan elemen tradisional yaitu **Acceptance Testing**
