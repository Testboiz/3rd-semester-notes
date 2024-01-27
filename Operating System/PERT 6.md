# PERT 6

# Synchronization

## Critical Section Problem

 > 
 > \[!abstract\] Definisi
 > Dimana kondisi dimana proses sedang memanipulasi shared data 

OS harus menjamin proses tidak dapat memengaruhi proses lain. Namun jika proses perlu melakukan hal tersebut maka dinamakan Cooperating Process. Contohnya adalah 

* DB
* Parallelization
* Modularity

Tantangannya adalah konsistensi data dan koordinasi

Multithreading dan multiprocessing dapat menyebabkan inkonsistensi data. Hal ini menjadi suatu tantangan besar untuk menjamin reliabilitas dari suatu sistem yang memiliki fitur tersebut.

Salah satu strateginya adalah pada sistem klien server dimana sistem akan track berapa banyak jumlah buffer penuh yang berada dalam `queue`. Jika ada buffer baru maka jumlah buffer dinaikan 1 dan jika buffer telah diberikan ke klien maka jumlah buffer dikurangi 1. Komunikasi tersebut dinamakan IPC, dan memorinya adalah shared buffer. Buffer dapat berupa bounded atau tidak

Race Conditiion adalah keadaan dimana update data bergantung dengan urutan CPU time. Hal ini menyebabkan inkonsistensi data. 

## Mutex Lock

 > 
 > \[!abstract\] Definisi
 > Mutual Exclusion (mutex) adalah suatu state dimana ketika suatu proses sedang menjalankan sesi kritikalnya, proses lain tidak boleh melakukan sesi kritikal mereka

Proses tidak dibolehkan untuk menunggu dalam mutex lock terlalu lama(Progress). Mutex juga harus memberikan batasan jumlah proses yang boleh masuk sesi kritikal ketika proses memberikan request sebelum diberikan akses

## Solusi Peterson

2 proses akan diberikan variabel `turn` dan `flag[2]` dimana variabel `turn` menandakan proses mana yang dijalankan dan `flag[2]` menandakan state dari proses (berjalan/tidak)

````
//Petersib Solution
while (true) {
    flag[i] = TRUE;
    turn = j;
    while ( flag[j] && turn == j);
        //CRITICAL SECTION
        flag[i] = FALSE;
        //REMAINDER SECTION
}
````

Asumsikan `LOAD` dan `STORE` bersifat atomik (tidak ada sub langkah)

## Hardware Support

Hardware modern semuanya memiliki support ini. Pada CPU single core dapat menghentikan interrupt, dan CPU multicore dapat memberikan instruksi atomic yang khusus.

Sistem uniprosesor kurang scalable karena kode tidak preemptif, namun sistem modern menggunakan sistem atomic yang dapat swap memori atau isi memori

## Semaphore

 > 
 > Definisi. Semaphore adalah alat yang tidak menuntut proses untuk menunggu selama sibuk

Semaphore memiliki variabel `int s;`. Variabel ini didecrement ketika sedang menunggu, dan ditambah jika ada sinyal yang didapat

Semaphore yang memiliki `s` sebagai boolean adalah [Mutex Lock](PERT%206.md#mutex-lock) 

Semaphore diimplementasikan dimana `wait()` dan `signal()` tidak dapat diesekusi pada semaphore secara sekaligus, sehingga `wait()` dan `signal()` call diletakkan pada critical section. Alternatifnya adalah dengan menggunakan busy waiting jika implementation code dapat dijalankan dengan cepat

Namun hindari strategi semaphore jika aplikasi membutuhkan waktu lama pada critical section

Jika Semaphore tidak mengimplementasikan busy waiting, maka alternatifnya adalah membuat queue berupa linked list yang memiliki method `block` yang push operasi ke waiting queue dajn `wakeup` yang akan mengpop operasi dari waiting queue dan push ke ready queue.

 > 
 > \[!warning\] 
 > Deadlock dapat terjadi jika proses menunggu terlalu lama %%sampai tahun jebot%% untuk event pada proses yang sedang ada pada waiting queue.

 > 
 > \[!Warning\]
 > Starvation adalah proses yang tidak dapat diremove dari queue yang sedang berhenti

## Masalah Klasik Semaphore

* Bounded Buffer Problem
* Reader-Writers Problem (Race Condition)
* Dining-Philosophers Problem (Deadlock)

Solusinya dapat diimplementasikan dengan operasi semaphore `wait(S)` dan `signal(S)`, dimana operasi operasi tersebut akan menyembunyikan implementasi synchronization agar dilakukan oleh sistem.

Selain itu juga dapat menggunakan monitor. Monitor umumnya adalah suatu objek dalam bahasa pemograman tertentu yang aakan menghandle sinkronisasi dengan memberikan kontrol kepada programmer

## Monitor

 > 
 > \[!abstract\] Definisi
 > Yaitu abstraksi akan mekanisme sinkronisasi program Contohnya adalah threading library yang ada dalam banyak bahasa pemograman high level seperti Java, Python, dsb

Monitor akan memberikan informasi seperti kondisi program dsb, program juga dapat dimanipulasikan dengan `.wait()` dan `.signal()`. dimana

* `.wait()` adalah proses suspensi program ketika ada pemanggilan `.signal()`
* `.signal()` adalah proses resume 1 proses yang sedang melakukan `.wait()`

Jika tidak ada proses yang disuspend, `signal()` tidak berpengaruhi sama sekali
