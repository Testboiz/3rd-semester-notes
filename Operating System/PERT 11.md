# PERT 11

# PERT 11 - File System Implementation

## File Concept

File merupakan sebuah blob kontingen (utuh) yang berisi informasi.
File dapat berupa teks, binary, gambar, video, 3d model, dsb

File merupakan sebuah abstraksi dari blok blok tersebut, agar lebih mudah ditangani. File dapat berstruktur atau tidak (blob)

File memiliki attribut berikut

* Nama
* Extension (.txt .exe .so dsb) yang menentukan tipe file
* Type (dideteksi oleh header file / extension)
* Size
* Protection (`rwx` di Linux)
* Metadata

File memiliki operasi berikut

* Buat
* Edit
* Baca
* Pindah
* Hapus
* Syscall `open()` dan `close()`
* Append
* Rename
* Set Attribute
* Get Attribute

File yang telah dibuka akan memiliki file pointer dalam bentuk file deskriptor, 
referensi pada open file count, lokasi dan access rights. File juga dapat dilock 
agar akses dapat diblokir dalam kasus tertentu

## Access Methods

1. Sequential Access 

Akses ini dapat digambarkan seperti membaca pita kaset. Dimana kita jika kita ingin
membaca posisi 5 dan kita berada di posisi 1, kita harus membaca posisi 2,3,4 juga

2. Direct Access

Akses ini memperbolehkan kita untuk mengakses posisi secara acak secara langsung, 
namun akses berupa per blok blok penyimpanan

3. Random Access

Mirip dengan direct access, namun dapat langsung mengakses bit yang spesifik

## Directory Structure

File System umumnya memiliki sebuah direktori yang menyimpan sebuah file
Direktori umumnya memiliki operasi operasi file seperti pada [File Concept](PERT%2011.md#file-concept)

Direktori sering disebut folder

Direktori memiliki informasi berikut

* Name
* Path
* Size (length)
* last accessed
* last updated
* owner id
* protection

Direktori dikelola berdasarkan hal berikut

* Secara efisien agar dapat diakses secepat mungkin
* Mudah dikenal dengan nama file
* Grouping (file disimpan dalam kode program)

Direktori dapat disimpan dengan linear list (array), maupun hash table. Linear list simple namun performanya kurang, dan sebaliknya

## File System Structure

File System memiliki beberapa struktur seperti

1. Single level (tidak ada folder)
1. Double level (1 partisi per user, user tidak dapat membuat folder)
1. Tree Structure (struktur berfolder dengan root directory)
1. Acyclic graph (Ada link dan shortcut seperti di Windows ataupun alias di Linux)
1. General Graph (Link tidak memiliki constraint, kita dapat membuat infinite loop dengan link)

## File System Mounting

File System harus dimount pada satu posisi seperti di `/` di Linux/Unix atau `C:\` di Windows

File System external ataupun partisi dari file system dapat dimount di tempat lain seperti
`/mnt` di Linux/Unix maupun `D:\` di Windows

## File System Operation

File sharing dapat dilakukan pada sistem terdistribusi, Network File System, maupun komputer multi user
Perlu ada skema proteksi untuk melindungi akses file. User harus dapat diidentifikasi, siapa dan berasal dari grup mana

Remote file system merupakan akses file system bersifat client server menggunakan Internet. Sering disebut **Cloud Storage**

Dalam Unix menggunakan protokol NFS, dan CIFS untuk Windows

Filesistem tersebut harus dapat menangani potensi kegagalan seperti network error, server error. Jika error tersebut terjadi
maka harus ada penangannanya dengan menggunakan Consistency Schematics. NFS mudah untuk direkoveri, namun kurang secure

Consistency schematics adalah sejenis semaphore (pert 6) dan menangani potensi gangguan sinkronisasi.

Contoh :

* Andrew File System
  
  * Penulisan data terjadi setelah file ditutup
* Unix File System
  
  * Penulisan data sesegera mungkin (mirip Google Docs)
  * File Pointer dishare, sehingga dapat collab

## Protection

Proteksi pada intinya adalah pengelolaan akses sebuah file. Di Linux menggunakan
`ls -la` akan menunjukkan `drwxrwxrwx` pada tiap file dan direktori. String tersebut
menandakan proteksi file dimana 
Group dan User harus dapat diidentifikasikan dengan id unik

1. `rwx` pertama untuk akses owner
1. `rwx` kedua untuk akses group
1. `rwx` ketiga untuk akses publik

Menggunakan perintah `chmod` untuk memodifikasikannya

Group dapat diubah dengan `chgrp`

Proses juga melakukan `SETUID` yang pada intinya memiliki privilige sementara, dengan command `sudo`

Setiap proses dapat diasosiasikan dengan objek yang dapat digunakan. Objek tersebut memiliki capability yang berisi hak akses, pointer objek, jenis objek yang disimpan di kernel dan user space

Windows dapat mengelola akses dengan GUI

## File System Implementation (Extra)

Konsep Filesistem perlu diimplementasikan ke hardware (HDD,SSD,NVME,CD,DVD,Disket,dsb). 

Harus ada fitur fitur seperti space allocation, free space recovery, dan OS Support

Untuk meringankan kerja IO, hardware menyimpan file dengan menggunakan blok. Tiap blok **hanya berisi 1 file** 

Filesystem memudahkan akses ke disk. Filesystem harus dapat menampilkan informasi terhadap file, support operasi file dan visualisasi struktur direktori, serta kemampuan memappingkan file system logical ke hardware

Note. Basic file system mengelola data **didalam** blok tersebut

## Allocation Methods (Extra)

* Contigous Allocation

Semua Blok dialokasikan secara kontingen, mirip dengan segmentation di memori. Digunakan pada disket, dan OS IBM lama

Tantangannya adalah integritas data, pointer ke file dapat berubah. Selain itu juga tantangan yang ada pada pengelolaan segmentasi memori juga ada pada metode ini (first fit, best fit, fragmentasi). Selain itu juga output file dari proses yang tak terduga juga mempersulit alokasi

* Linked Allocation

Blok dikelola dengan linked list, sehingga menghindari fragmentasi external, namun tidak ada support untuk direct access, dan ruang pointer yang kurang efisien

Contohnya adalah FAT32 

Ada satu bagian disk yang berisi entry tiap blok dalam penyimpanan. Tiap entry berisi nomor blok pertama dalam file. Nomor FAT dapat diatur secara berantai untuk mengoptimalkan random access.

* Indexed 

Efektif untuk file besar, menggunakan scheme berikut

Linked Scheme merupakan index blok secara linked list

Multilevel Index merupakan penyimpanan indirect index blok yang berisi blok yang hanya berisikan pointer saja. Dapat memiliki berbagai level agar dapat mengsupport ukuran yang sangat besar

Mixed System (BSD)

12 pointer direct blok ke data
1 pointer indirect untuk level 1 2 dan 3 index blok

## Extra

Efisiensi tergantung pada effisiensi algoritma, dan tipe data dalam direktori. Selain itu juga, dapat melakukan caching, read ahead, write ahead, virtual disk dan ramdisk

Recovery dilakukan ketika ada pengecekan seperti `CHKDSK` atau `fsck` di Linux, dan ketika terjadi korupsi file, menggunakan backup storage untuk restore data

Dalam Floppy, tidak ada partisi, hanya ada root direktori, file dan folder. Dalam penyimpanan lebih modern disupport partisi

Ada Boot Sector dalam FAT yang berisi bootstrap loader (bootloader), byte per sektor, jumlah sektor per blok, tabel partisi, partisi aktif. dll

Ada File Allocation Table yang berisi informasi terhadap disk seperti informasi pemakaian disk, backup, boot disk, entry table, isi entry

Open file dilakukan dengan langkah berikut

1. Menggunakan file deskriptor
1. Menggunakan slot kosong pada file table
1. Open direktori
1. Ambil nomor awal dari FAT dan mulai akses file
