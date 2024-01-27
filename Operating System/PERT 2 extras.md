# PERT2 extra

OS menyediakan 3 hal ke user yaitu :

* Services (syscall)
* Interface (terminal/gui)
* Komponen (Driver)

## OS Services

Services yang ada dalam OS dapat berupa

* UI (CLI,GUI,Shell Script)
* Program execution
* IO Execution
* Filesystem communication (read, write, delete, search, list, permission management)
* Memory, IO and Network Communication
* Error detection and debugging

Services yang dilakukan dalam internal kernel OS adalah :

* Resource allocation (cpu time, memory allocation, IO operation)
* Accounting (Memanajemen penggunaan resources dalam bentuk statistik)

 > 
 > Dalam makna literal, accounting dapat digunakan untuk membilling pengguna terhadap penggunaan resource seperti di Cloud

* Protection and security (Menjaga keamanan terhadap jaringan dan sistem terhadap hal-hal yang tak diharapkan)

OS awal seperti DOS hanya dapat menjalankan 1 program (bukan proses) dalam satu waktu. program diload kedalam memory secara langsung

## Program

OS modern memiliki kemampuan multitasking dengan menggunakan **proses**. Contoh pada linux yaitu adalah menggunakan `fork()` untuk membuat proses dan `exec()` untuk menjalankannya.

Jika exit code program 0 maka proses berjalan normal, dan selain itu merupakan error code dari sistem

## System Program

Os memberikan environment untuk menjalankan dan mengembangkan program maupun memroses file

Sistem dapat memberikan informasi terhadap apa yang sedang terjadi dalam bentuk log, debug info, logcat, dsb

Komunikasi yang dapat dilakukan dengan antar hardware, user maupun sistem 

 > 
 > Contohnya dapat berupa : share screen, browsing internet, keyboard input, dsb

Umumnya services dijalankan secara background, dinamakan daemon. Daemon digunakan untuk membantu OS untuk melakukan utilitas seperti disk checking, error logging, scheduling, dsb.

contohnya dalam task manager: svchost.exe merupakan services, sedangkan System adalah kernel yang dijalankan

## Desain dan implementasi OS

OS memiliki desain yang berdasarkan kegunaannya. Goals dari OS adalah :

* User goals -> memudahkan User untuk berinteraksi dengan hardware
* System goals -> Meemiliki sistem yang fleksibel, robust, dan efisien

OS akan menjadi sangat fleksibel ketika mekanisme (cara) dipisah dari tugasnya.

OS awalnya dijalankan pada bahasa mesin, kemudian berkembang menggunakan bahasa program seperti C, C++ dan Rust.

### Client-server / Microkernel

Sistem client server sesungguhnya merupakan sistem mikrokernel. dimana kernel dipindahkan ke user space, dan menggunakan message passing untuk komunikasinya.

Sistem mikrokernel jauh lebih fleksibel dan mudah untuk dikembangkan secara lanjut

### Modular Approach (OOP)

Dalam konsep OOP, kernel dipecah menjadi berbagai kernel module.

* Kernel module merupakan suatu Objek OOP yang terpisah
* Komunikasi menggunakan Interface
* Dapat diload secara ad hoc

### Hybrid System

Menggabungkan berbagai jenis kernel design untuk mencapai tujuannya.

Contoh : 

* linux => monolihtik + modular 
* Windows => monolihtik + mikrokernel

### Android

Kasus spesial untuk Android adalah desainnya yang sangat developer friendly. 

Android memiliki dalvik vm yang memproses aplikasi dalam Java

Android juga memiliki sistem web (Android System Webview), SQLite, multimedia, dan libc yang kecil

## Performance Tuning

Dilakukan dengan Task Manager atau `top` untuk Linux, untuk meningkatkan performa dengan mengkill program yang tidak berguna

Selain itu, overclocking dan undervolting juga dapat dilakukan untuk performance tuning dalam sisi hardware

## Dtrace

Memonitor CPU dan event yang terjadi dalam satu atau beberapa proses yang ada dalam OS family Linux, BSD dan Mac

## Booting

Booting dimulai dengan proses berikut :

* Menjalankan kode booting dalam firmware
* Menjalankan bootloader 
* Memulai kernel
* Kernel memulai proses pada OS

## VM

VM memiliki beberapa fungsi seperti berikut :

* Testing OS
* Virtual Client PC
* Container aman untuk eksperimentasi dalam sistem
* Container untuk testing software
* Menjalankan clent program dalam suatu server
