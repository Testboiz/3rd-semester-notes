# PERT 10 - IO SYSTEMS

## IO Hardware + Overview

Skema / Hireaki komputer dapat digambarkan seperti berikut

* CPU (ALU, CU, Register)
* Input (Keyboard, Scanner, Mouse, camera. recognition device, modem, dll)
* Secondary storage
* Output (monitor, printer, ploter,dll)

BUS digunakan sebagai channel transportasi informasi dari berbagai sistem IO seperti

* CD Player
* HDD / SSD controller
* PCIE
* Keyboard Mouse (PS/2)
* Monitor
* GPU
* **USB**

`insert gambar`

IO Hardware tersebut pada umumnya memiliki

* Port (konektor ke dunia luar)
* Bus (Komunikator ke OS)
* Controller (CPU IO)

BUS juga memiliki kontroller tersendiri yang menangani aliran bit sesuai standar. 

Jenis jenis bus adalah

* Bus arbiter (BUS scheduler)
* Bus ISA (standar lama)
* Bus EISA (pengembangan ISA untuk bus multiple)
* Bus PCIE (penghubung ke bus bus ISA)

Device Controller dapat berupa sebuah kartu adapter yang memperbolehkan akses perangkat sejenis atau tidak seperti USB HUB

IO dapat dimap dalam memori pada address khusus

Ada 2 cara untuk menunggu event dari IO yaitu Polling dan Interrupt

Polling dapat digambarkan sebagai berikut 

````
while (! io_response()){
    // do nothing
    // also called busy waiting
}
````

Sedangkan Interrupt adalah dengan memberikan sejenis `Event` ke CPU untuk menangani IO. CPU memiliki Interrupt handler untuk menangani ini

* Programmed IO (async)
* Interupt driven (event)
* DMA

`insert gambar dari ppt bpk 25`

Ada berbagai opersi sistem IO yaitu

`insert gambar`

DMA (Direct Memory Access) digunakan untuk menghindari penggunaan IO untuk pemindahan data besar, membutuhkan DMA Controller yang dapat menggantikan CPU

`insert gambar`

## Application IO Interface

Tiap IO memberikan API/Library yang memudahkan programmer dalam menggunakan IO.

Tiap device memiliki karakteristik seperti berikut

* Menggunakan stream (Keyboard) / blok (HDD)
* Sequential (Tape) / Random Access (SSD)
* Sharable (Monitor) / Dedicated (Accelerator)
* Speed (Kbps, IOps, dsb)
* Read write, read only, write only (CD RW, CD, CDR-)

Kita dapat membayangkan blok dan karakter seperti berikut:

* Blok merupakan struktur data yang mengelompokan data menjadi kumpulan struktur data. Umum di penyimpanan
* Karakter merupakan struktur data lebih sederhana yang memiliki fleksibilitas untuk mencari (seek) seperti Printer

Network Device memiliki karakteristik seperti memiliki blok/karakter, pipa, FIFO, stream, queue, mailbox, dsb

Clock dan Timer secara IO tersedia, di UNIX/Linux tersedia `ioctl`

Blocking IO menggunakan Busy Waiting, Nonblocking IO menggunakan Multiprocessing, Asynchronous menggunakan sistem async khusus untuk melakukan IO sambil mengerjakan proses di CPU

Namun, async akan mengembalikan data ketika proses IO **selesai**, sedangkan nonblocking dapat mengembalikan data **kapan saja**

## Kernel IO Subsystem

Kernel memberikan layanan sepertiu Scheduling yang mirip dengan [CPU Scheduling](PERT%2010.md#cpu-scheduling), dan juga Buffering yaitu penyimpanan data di memori secara sementara untuk menangani perbedaan speed, transfer size dan juga integritas data

OS dapat mentrack status IO dalam **Device Status Table**

`insert gambar`

Caching adalah menyimpan data secara sementara untuk meningkatkan performa

Spooling adalah menahan output dalam device jika IO hanya dapat menghandle 1 proses dalam 1 waktu seperti Printer

Device reservation (OS membooking IO untuk proses tertentu dengan memperhatikan deadlock)

Kegagalan IO dapat dicek dengan error codenya, namun terkadang kegagalan IO kritikal menyebabkan BSOD

Proteksi IO digunakan dengan menggunakan akun Administrator atau `sudo` di Linux/UNIX, maupun dengan menggunakan syscall

`insert gambar`

Device Status Table, Open file table, network connections, device state, dll merupakan struktur data yang digunakan OS untuk menangani IO, dapat menggunakan paradigma OOP

## Transforming IO Request to Hardware Operations

insert gambar

## Streams

STREAMS adalah komunikasi channel dengan proses dan IO dalam Unix System V keatas yang memiliki

* stream head interface
* modul modul read queue dan write queue
* driver end

Menggunakan message passing tiap queue

## Performance

Performa merupakan faktor penting dalam IO. Hal hal yang memengaruhi performa contohnya adalah

* CPU mengerjakan device driver dan kernel IO code
* Context switch
* Data copy
* Network traffic (faktor luar)

Tips meningkatkan performa

* Kurangi context switch, data copy
* Minimalisir interrupt dengan large transfer, smart controller, polling
* Pakai DMA
* Balance load CPU, memory, bus dan IO

`insert gambar`

## EXTRAS

### Modul dan fungsi modul

Interface antara CPU, memori dan periferal lainnya

Fungsinya adalah

* Control, timing, communication
* Interface communcation
* Buffering
* Error detection

Penanganan IO dilakukan dengan berikut

* Cek status IO
* Jika ready transfer data
* Proses pengambilan data dari IO
* IO mentransfer data ke CPU

### Interfacing IO

Berfungsi untuk

* Menyediakan status IO dan operasi
* Integrasi DMA
* Transfer instruksi CPU
* Bufer data
* Pengujian, encoding dan decoding 

Interface dapat dependen dan independen dari device. Berupa Register / BUS

General Purpose Computer menggunakan banyak DMA, 1 CPU dan berjalan paarallel untuk menangani IO secara khusus dalam IO Channel
