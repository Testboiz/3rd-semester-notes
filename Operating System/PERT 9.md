# PERT 9 - Virtual Memory

## Demand Paging

Virtual memory adalah bagian dari penyimpanan sekunder yang digunakan sebagaimana memori. Implementatinya melalui Demand paging maupun Demand segmentation

Virtual Memory dapat berkali kali lipat lebih besar daripada main memory. Program dapat memanggil library yang tersimpan dalam penyimpanan sekunder yang merupakan implementasi virtual memory

Kelebihannya adalah 

1. Mengurangi IO
1. Mengurangi konsumsi memori
1. Respon Cepat
1. Support multi user lebih baik

Ketika sebuah page dalam virtual memory dibutuhkan, maka dapat dipindahkan ke memory. Jika swap hanya dilakukan ketika diperlukan ini dinamakan **lazy swapper**

Demand paging menggunakan lazy swapper untuk mengswap page ke penyimpanan sekunder ketika dibutuhkan. Ada valid invalid bit yang menentukan apakah sebuah frame ada dalam memori atau tidak. Valid Invalid bit digunakan juga untuk menandakan apakah page tidak ada dalam memori

Interrupt akan diberikan kepada sistem ketika ada referensi kepada sebuah page. Page fault adalah kejadian dimana pointer page belum ada pada memori fisik

$$
\\text{EAT} = (1-p) * (\text{memory access}) + p(\text{page fault overhead} + \text{swap page out} + \text{swap page in} + \text{restart overhead})
$$

dimana $p$ adalah peluang page fault

## Copy On Write

Salah satu mamfaat Virtual Memory adalah Copy on Write. CoW memperbolehkan proses parent dan child untuk menggunakan shared memory, hanya mengcopy ketika ada modifikasi. Hal ini meningkatkan efisiensi memori. 

## Page Replacement

Page Replacement adalah proses swapping yang dilakukan ketika bagian dari memori dianggap jarang dipakai. Page replacement mendeteksi apakah file yang diubah memiliki modify bit yang tepat. Membantu dalam pemisahan akan memori logikal dan fisik

Page replacement dilakukan ketika alokasi memori terlalu tinggi, dimana semua page telah dipakai, lalu pindahkan swapkan ke virtual memory

Algoritma yang dapat dipakai adalah

* FIFO 
* LRU (Least Recently Used)
* Counting Algorithm (LFU dan MFU)

## Allocation of Frames

Tiap program memiliki kebutuhan page (memori) minimum. Alokasinya dapat dilakukan dengan Fixed Allocation dan Priority Allocation

Fixed allocation memiliki beberapa cara alokasi yaitu :

1. Equal allocation => frame per proses => free frame / jumlah proses
1. Propotional allocation
   $$
   a_i = \frac{s_i}{\sum s_i}m
   $$
   dimana 

* $a_i$ adalah jumlah frame pada proses ke $i$
* $s_i$ adalah ukuran proses ke $i$
* $m$ adalah jumlah frame

Priority allocation menggunakan proportional allocation, dimana ketika page fault terjadi, pilih proses dengan prioritas yang lebih rendah

Allokasi dapat bersifat lokal (mengambil frame dari proses sendiri), maupun global (dapat mengambil frame dari proses lain)

## Trashing

Ketika memori lagi penuh / lemot, hal tersebut dapat menyebabkan trashing, yaitu kejadian dimana page sering diswap. Locality model adalah kelompok page (memori) yang digunakan. Program dapat memiliki beberapa locality karena shared memory.

Working set model

Memory mapped files adalah file yang 100% berada di RAM, yang biasanya ada pada file yang diload pada program untuk meringankan IO

## Allocating Kernel Memory

Kernel juga dapat meminta memory dari free memory pool secara kontingen. Memory dialokasikan per $2^n$ byte chunk

Slab allocator adalah menggunakan page kontingen dimana :

1. Ketika slab dialokasikan masih dianggap `free`
1. Ketika objek program telah menggunakannya, di mark `used`
1. Jika slab penuh, alokasikan slab baru

Metode ini menghindari fragmentasi dan cepat 

Prepaging adalah proses mengalokasikan page sebelum direferensi. Hal ini menghindari page fault, namun boros memori dan IO

Selain itu, juga perlu memperhatikan fragmentasi, ukuran tabel, overhead IO, lokalitas

IO interlock dilakukan ketika memori diasosiasikan dengan IO, sehingga tidak boleh sembarangan di swap dengan page replacement algorithm

Implementasinya di Windows XP menggunakan demand paging dengan clustering. Dimana ada minimal dan maksimum page yang dijamin. Ketika memori mulai minim, maka nimimum page akan dikurangi, dan proses yang melebihi minimum akan diswap 

Solaris menggunakan list of free pages dan mengscan dengan parameter parameter tertentu yang menentukan rate swapping
