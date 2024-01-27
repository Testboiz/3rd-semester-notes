# PERT 2

## Komponen Sistem

### Manajemen Proses

Proses adalah program yang dijalankan. Hal yang dapat dilakukan adalah :

* create and kill task
* start and pause
* sync and comm
* deadlock

### Manajemen Memori dan penyimpanan

Memori adalah "array" yang fleksibel, yang dapat diakses secara cepat. Setiap variabel dalam program berada pada memori 

Memory management dilakukan dalam program, umumnya dalam bahasa low level seperti C dan C++. Contohnya adalah `malloc()`, `calloc()`, `dealloc()` dan `free()`

Penyimpanan adalah tempat untuk menyimpan data secara permanen / non volatile.

Hal yang dilakukan dalam emmori dapat berupa : 

* alokasi penyimpanan
* membersihkan file tak berguna

### Manajemen file

File adalah informasi yang tersimpan dalam penyimpanan. File tersimpan dalam sistem direktori komputer `C:\` di Windows dan `/` di UNIX/Linux.

 > 
 > Direktori (folder) adalah sebuah file yang menampung direktori atau file lainnya

Hal yang dilakukan saat manajemen file :

* pembuatan, penghapusan dan backup file maupun direktori
* manipulasi file dan direktori

### Manajemen IO

IO dimanajemen dengan driver sebagai perantara antar hardware dan softwarenya. 

Hal yang dimanajemen adalah :

* Buffer/caching
* Scheduling (spooling) IO
* IO Processsing

### Sistem Distribusi

Sistem ini menggunakan protokol untuk menghubungkan beberapa CPU dan memori untuk bekerja menjadi satu kesatuan

 > 
 > Superkomputer, server dan render farm menggunakan sistem distribusi untuk melakukan proses komputasi secara parallel dan cepat

### Sistem Proteksi

Memberikan keamanan terhadap penjalanan malware, code injection, dsb. Software seperti bootloader lock, antivirus,  dan secure boot melindungi perangkat dari malware. Selain itu juga dapat membatasi sideloading maupun networking

### Command Intrepreter

Berupa terminal emulator maupun command prompt dapat menjalankan command command dalam suatu OS :

 > 
 > Secara teknis OS dapat bekerja **hanya** dengan Command Intrepreter seperti pada DOS dan Linux. Pada praktiknya, dalam Linux Command Intepreter (terminal) adalah program yang sangat **esensial** dalam menggunakan Linux.

### GUI Interface

Kebanyakan sistem operasi sekarang menggunakan GUI (desktop) karena lebih mudah untuk digunakan, namun  CLI tetap disediakan ketika ingin digunakan

## OS Services

OS melakukan proses-proses yang berkaitan dalam interaksi hardware dan software. Pengguna tidak mengakses operasi tersebut secara langsung, namun dengan menggunakan system call yang berupa [`syscall` (linux)](https://blog.rchapman.org/posts/Linux_System_Call_Table_for_x86_64/) dalam bahasa Assembly. Untuk memahami lebih dalam terhadap syscall klik link yang ada.

Syscall juga bergantung terhadap OS yang ada di linux dinamakan `syscall` dan dalam Windows dinamakan `Windows API`

Diawali dengan user space request 

````
; program untuk exit program
mov rax, 60
xor rdi, rdi
syscall
````

Kemudian setelah syscall dilakukan, maka `rax` dan `rdi` dibaca untuk menentukan `syscall` yang dilakukan dalam mode kernel

Mode kernel akan menjalankan code system call tersebut, dan menghandle result dari system call tersebut.

Setelah result didapat, maka akan kembali ke user space (code assembly)

 > 
 > Hal ini tidak perlu begitu didalami ketika kita tidak memfokuskan terhadap hal low level, namun berguna untuk lebih memahami hardware yang ada

 > 
 > \[!note\] In A Nutshell
 > Setiap melakukan syscall, maka komputer akan switch ke kernel mode, dimana kernel akan bertanggung jawab atas komputasi, dan bukan user.

## System Call

System call mirip dengan function call dalam library, perbedaannya adalah bahwa system call akan memproses dalam kernel mode, dimana akan banyak terjadi pemrosesan secara hardware, tidak hanya pemrosesan software

Syscall membutuhkan passing parameter ke register yang ada. Parameter dapat berupa nilai (`word` atau `byte`) maupun pointer. Selain itu juga, program dapat melakukannya secara otomatis

System call memiliki fitur seperti SISGEV (kontrol proses), informasi terhadap hardware, dan komunikasi antar hardware/software.

## Sistem Program

Program memiliki scope yang lebih terbatas, karena hanya berinteraksi dengan hardware menggunakan system call, sisanya adalah pemrosesan yang bersifat internal seperti :

* manipulasi file dan memori
* esekusi dan komunikasi dengan program maupun sistem
* debugging

## Arsitektur OS

### Sistem Monolihtik

Sistem ini memiliki satu kernel yang bertanggungjawab untuk menjalankan suatu prosedur dalam bentuk service procedure (syscall)

Utility procedure dilakukan oleh service procedure dalam syscall tersebut untuk berkomunikasi terhadap sistem dan program

### Sistem Berlapis

Merupakan metode abstraksi terhadap sistem hardware, kernel terhadap program. 

Semakin rendah level abstraksinya, semakin sedikit user controlnya, karena sifatnya kritikal

Layer Layer Sistem berlapis dapat berupa :

* Layer 6 : Program
* Layer 5 : driver / scheduler
* Layer 4 : memory 
* Layer 3 : I/O channel
* Layer 2 : CPU scheduler
* Layer 1 : Instruction intepreter (assembly/binary)
* Layer 0 : hardware

### Sistem client server

Client server memisahkan kernel dengan aplikasi yang berjalan dalam suatu os dengan membatasi interaksi dalam bentuk suatu pesan

### Sistem Virtual Machine

Virtual machine mensimulasikan suatu OS lengkap dengan proses, kernel dan hardware yang dijakankan dalam suatu program untuk dijalankan dalam suatu kernel/hypervisor. 

Virtual Machine mensimulasikan hardware dengan spooling, CPU scheduling dan time sharing terminal. Namun sebagian virtual machine yang bersifat abstrak, mengunakan konsep ini untuk menjalankan program secara kernel agnostik

Contoh : vmware, virtualbox dan WSL

### Sistem Berorientasi Objek

Yaitu OS yang didesain dengan paradigma OOP dalam source codenya. OS moderen umumnya didevelop dengan sistem ini.

## Implementasi

OS mempermudah user untuk berinteraksi dengan hardware dari OS . 

OS juga membuat sistem lebih secure karena membatasi interaksi yang akan dilakukan pada hardware, dan mencegah tindakan malicious oleh program tak bertanggung jawab
