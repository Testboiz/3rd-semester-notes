# PERT 8 - Main Memory

## Contingous Memory Allocation

Memori adalah tempat data disimpan dalam sebuah program yang sedang **berjalan**, semua hal seperti variabel, kode program dan juga pointer disimpan disini.

CPU hanya dapat mengakses data dari register. Data yang ada dapat berupa nilai pada register tersebut, ataupun **alamat lokasi memori (pointer)**. Pengaksesan data dari memori dengan pointer tidak secepat register. Sistem ini harus dijaga dengan baik karena kritikal terhadap bekerjanya komputer

Pointer data dapat dilink dengan instruksi pada saat kompilasi (hard coded addresses), loading program (pointer allocation), maupun secara eksekusi (dynamic memory allocation).

 > 
 > \[!info\]
 > Dalam kebanyakan bahasa pemograman, umumnya library akan melakukan linking tersebut pada saat esekusi, dengan ekspresi `new ObjectName()`

CPU dapat membuat logical address yang dapat diakses pada kode program. Alamat memori ini akan diterjemahkan menjadi alamat memori fisik menggunakan MMU (Memory Management Unit)

Adapun juga dalam sistem modern, tidak semua function/objek akan diload dalam memori untuk mengurangi penggunaan memori pada program.

Dalam Windows, ada file .dll (.so di Linux) yang merupakan library yang dapat diload ketika program berjalan, hal ini juga menghemat penggunaan memori

## Swapping

Ketika program kehabisan memori, maka untuk sementara data yang dimiliki program dapat dipindahkan ke penyimpanan sekunder untuk mengurangi utilisasi memori.

Ada 2 strategi swapping yaitu

1. Backing Store, yaitu sejenis backup yang digunakan oleh disk yang cukup besar yang dapat segera digunakan ketika memori habis
1. Roll out, roll in, yaitu metode swap berdasarkan prioritas (priority schedulling untuk swapping)

Swapping perlu memperhatikan overhead (waktu untuk memindahkan data) untuk memaksimalkan performa. Ready queue juga harus mengsupport program yang sedang berjalan dalam disk

Memori dari suatu program umumnya diload secara kontingen (1 blok utuh) kedalam memori. CPU memiliki **Relocation Register** untuk mengecek apakah daerah memori tersebut benar benar kosong atau tidak

Terkadang swapping memiliki risiko dimana ketika sebuah proses sedang sibuk, kita melakukan swap pada program, dan koneksi IO ternyata terputus dan menggangu jalannya program

Maka tipsnya adalah untuk tidak mengswap program yang sedang melakukan IO

Illustrasi memori kosong dan loading memori ke 1 program
![Pasted image 20231121124340.png](..\Software%20Engineering\Pasted%20image%2020231121124340.png)

Ruang kosong (abu abu) dapat diisi dengan blok blok yang merupakan representasi memori dari suatu program

Ada 3 strategi yaitu

1. First Fit (mengalokasikan lubang yang paling pertama yang muat)
1. Best Fit (mengalokasikan lubang terkecil yang perlu dicari dahulu)
1. Worst Fit (mengalokasikan lubang terbesar)

First Fit dan Best fit lebih digunakan karena kecepatan dan effisiensi

Fragmentasi memori ada dalam bentuk berikut :

1. Fragmentasi eksternal yaitu, banyak lubang lubang kecil yang tidak dapat digunakan untuk memasukan program baru
1. Fragmentasi internal yaitu proses dapat memiliki konsumsi memori yang lebih besar karena ada internal memori dalam partisi yang tidak dipakai

Compaction adalah proses untuk menghilangkan fragmentasi eksternal dengan menggabungkan blok blok memori menjadi 1 blok besar. Compaction dapat dilakukan ketika relokasi bersifat dinamis pada saat runtime

Kelebihan Segmentasi dan Paging

1. Dapat dishare (blok tidak dapat)
1. Skema proteksi tersedia
1. Menghindari fragmentasi (spillover tercontain di excess space dari page)
1. Alokasi cepat dan mudah
1. Customizable
1. Overhead kecil

Perbedaan Segmentasi dan paging

|Segmentasi|Paging|
|----------|------|
|Programmer harus pahami|Programmer tidak perlu pahami|
|Kompilasi terpisah|Kompilasi tergabung|
|Proteksi terpisah|Proteksi digabung|
|Fitur Shared code|Tidak Tersedia|
|Banyak ruang alamat linier|1 ruang alamat linier|

## Paging

Paging adalah cara OS untuk mengelola memori yang ada dalam bentuk sebuah file, 1 page logikal berkorespondensi dengan 1 frame fisik. 1 page dapat berukuran 512KB - 8192KB. Page mirip dengan blok pada penyimpanan sekunder, Page merupakan unit terkecil dari suatu memori yang dapat dialokasikan ke dalam suatu program

Page dapat digambarkan sebagai sebuah array yang berisi bit bit memori dalam RAM. Suatu address memori dapat direpresentasikan sebagai berikut. (`word` $\approx$ `unsigned int`)

````
	word bits = page[number][offset];
````

Ketika ada proses baru yang akan diesekusi, maka OS akan menganalisa kebutuhan memorinya dalam jumlah page dan mencari kumpulan page kontingen yang memiliki ukuran yang cukup

## Structure of the Page Table

Ada tabel page di memori yang berisi pointer seperti PTBR dan PRLR, PTBR adalah pointer ke page yang dituju dan PTLR merupakan ukuran dari page tersebut. Hal ini membutuhkan 2 akses memori, Untuk mempercepatnya digunakan cache maupun TLB. TLB memiliki fitur proteksi dengan address space identifier (ASID) terhadap ancaman address space

Dengan TLB, akan ada penyimpanan khusus yang menyimpan lokasi page dan frame. Jika tidak ditemukan lokasi page dalam TLB, maka perlu mencarinya di page table

Waktu akses efektif dari memori adalah $2t + \epsilon - \alpha$, dimana $t$ adalah waktu clock memori, $\epsilon$ adalah waktu lookup, dan $\alpha$ adalah hit rate (persen dari page yang dapat ditemukan oleh associative register)

Tiap page memiliki skema proteksinya sendiri seperti **valid invalid**, yaitu bit boolean yang menandakan bahwa sebuah page itu ada dalam proses tersebut atau tidak

Page dapat dishare untuk beberapa program dengan kode khusus yang memperbolehkannya. Lokasi address page harus dipastikan sama untuk mencegah masalah sinkronisasi. Adapun untuk data yang tidak dishare, dapat disimpan di tempat lain

Ada beberapa cara untuk mengelola jumlah page yang besar dalam memori yaitu

1. Hierarchical Paging
1. Hashed page tables
1. Inverted page tables

Hierarchical paging adalah cara untuk mengelola page dengan sebuah hireaki. Hireaki ini dapat digambarkan sebagai matrix multidimensi.

````
// 2 level
word bits = page[first_level][second_level][offset];
// 3 level
word bits = page[first_level][second_level][third_level][offset];
````

Ada alternatif dari paging 2 level yang menggunakan `second_level` sebagai offset dari nested page table

Hashed page table adalah cara mengorganisir page pada sistem yang modern (32 bit / lebih). Page number yang dihash dinamakan virtual page number, virtual page number inilah yang diorganisir dan dicari oleh sistem untuk mengalokasikan memori

Inverted page table adalah "page table" yang berisikan kepemilikan dari semua proses yang berada pada segmen memori tersebut. Jadinya 1 page hanya perlu mencatat berapa banyak bagian page yang dipakai oleh tiap program, dan bukan seluruh bit dari page. 

Teknik ini membuat page table lebih kecil, namun butuh lebih banyak waktu untuk mencari data dalam page table. Hash table digunakan untuk membuat searching lebih cepat 

## Contoh

Sebuah program memiliki komponen komponen berikut yang harus diload pada memori

1. Main Program
1. Function, procedure
1. Variabel, konstanta, array
1. Objek, atribut, method
1. Stack dan symbol table
   Kumpulan dari semua objek tersebut dinamakan segmentation

 > 
 > \[!note\]
 > `Segmentation fault core dumped` terjadi karena program mengakses memori yang tidak dialokasikan pada program tersebut

Segment disimpan dalam segment table yang berisikan informasi dalam bentuk tuple berikut `(base,limit)` dimana `base` adalah lokasi memori, dan `limit` adalah panjangnya. Segment table base register (STBR) merupakan pointer ke tabel tersebut ke memori, dan Segment table length register merupakan informasi terhadap jumlah segmen yang dipakai program, apakah legal atau `Segmentation fault`

Segmen menggunakan bit yang menandakan apakah segmen tersebut dapat dilakukan `rwx`. Bit ini ada pada setiap segmen
