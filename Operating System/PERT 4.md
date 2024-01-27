# PERT 4

## Gambaran Umum

Thread adalah suatu penjalan dari proses. Proses dapat dijalankan dengan beberapa thread agar dapat lebih responsif, efisien dan sclalable.

Thread dapat dibayangkan sebagai suatu aksi yang running dalam aplikasi seperti API call, spellcheck, update display, dll. Threading lebih efisien daripada proses baru

## Multicore Programming

Thread library telah disupport oleh banyak bahasa pemograman seperti C, C++, Python, Java, dsb. Ada juga library POSIX dan WIN32Api. Threading telah disupport oleh OS NT dan Unix like dalam bentuk **kernel thread**

Tantangan dari Multicore Programming adalah :

* Task switch
* Thread communication and dependency
* Testing dan debugging

 > 
 > Paralel adalah sistem yang menjalankan lebih dari 1 task. Contoh Rendering 

 > 
 > Konkurent adalah sistem yang mendukung lebih dalam 1 task dalam 1 thread. Contoh threading module

Data Parallelism adalah data yang dishare oleh berbagai thread. Task Parallelism adalah task yang dijalankan oleh berbagai thread seperti pada algoritma Divide and Conquer

Banyak CPU modern memiliki banyak core dan thread. Contoh R7 dapat memiliki 8 core dan 16 thread

Hukum Amdhal :

$$
\\text{speedup} \leq \frac{1}{S + \frac{1-S}{N}} \tag{1}
$$

dimana $S$ adalah persen program yang bersifat serial, dan $N$ adalah jumlah core yang dipakai

## Multithreading Models

### One to One

Model thread ini merupakan abstraksi penuh dari satu kernel thread. Disupport pada Windows NT sebelum XP, Linux dan Solaris 9 keatas

### One to Many

Merupakan bentuk umum threading saat ini, dimana thread kernel menggunakan time sharing untuk menghandle user thread dari thread library. 

 > 
 > Multithreading library menggunakan threading ini. Proses tetap single threaded namun dapat menjalankan beberapa fungsi secara sekaligus

### Many to Many

Yaitu bentuk yang direfine dari one to one, yang menggabungkan one to one dengan one to many. Ini lebih dikenal sebagai multiprocessing library. Program inilah yang menggunakan beberapa CPU core sekaligus

### Two Level Model

Mirip dengan Many to Many, namun ada implementasi one to one, dan one to many secara **terpisah**

## Thread Library

`fork()` menghandle thread dan `exec()` menghandle proses. 

Thread dapat dicancel dengan asynchronous interrupt (CTRL+C/Esc), OS juga dapat mengcek apakah thread boleh dihentikan atau tidak 

Dalam pthread dapat menggunakan `pthread.cancel(tid)` untuk membatalkan thread. 

Thread juga dapat dimatikan agar tidak menerima sinyal

Thread secara default dicancel menggunakan cancellation point seperti `pthread_testcancel()` dan memanggil cleanup handler

## Implicit Threading

Thread ini dibuat pada saat runtime program, bukan pada source code 

Contoh Implicit Thread adalah

* thread pools
* OpenMP
* Grand Central Dispatch
* `java.util.concurrent`

Pool thread adalah kumpulan thrad yang menunggu esekusi. Hal ini meningkatkan performa karena dapat menggunakan thread yang sudah ada. Task dijalankan dalam suatu periode

Contoh di Win32api

````cpp
DWORD WINAPI PoolFunction (Avoid Param){
    // do something
}
````

Contoh di OpenMP

````c
#include <omp.h> //header OpenMP
#pragma omp parallel // thread sebanyak core
#pragma omp parallel for
for (int i = 0 ; i < N; i++){
    int j = i;
} //menjalankan for secara parallel

````

Grand Central Dispatch digunakan pada iOS dan macOS yang merupakan exension pada bahasa C dan C++

Implementasinya adalah  `^ˆ{ printf("I am a block"); }`
Akan kembali ke thread pool setelah selesai dijalankan

Dispatch menggunakan Queue serial (pop satu per satu) maupu priority queue yang dapat melakukan pop berbagai thread

````c
dispatch.queue.t queue = dispatch.get.global.queue(DISPATCH.QUEUE.PRIORITY.DEFAULT, 0);

dispatch.async(queue, ^{printf("Hello World!");});

````

## Signal Handling

UNIX menggunakan sinyal untuk mengkomunikasikan event. Signal handler memroses sinyal berikut :

* Sinyal bahwa suatu event terjadi
* Sinyal dikirim ke suatu proses
* Sinyal bahwa sinyal telah dihanle secara default atau user defined

User defined signal handler mengoverride default signal handler. Untuk proses single threaded, sinyal dideliver ke proses

Untuk multi threaded sinyal dapat dideliver ke 

* thread klien
* semua thread bekerja
* sebagain thread
* thread tertentu

## Pthread

Pthread tersedia dalam kernel dan user level. Pthread tersedia dalam POSIX (IEEE 1003.1c) yang merupakan library yang dapat dikembangkan lebih lanjut oleh flavor UNIX lainnya

## Java Thread

Java Thread dijalankan oleh JVM dengan mengextend kelas `Thread` maupun mengimplemen Interface `Runnable`

````java
public class RunThread implements Runnable{
    @Override
    public void run(){/*do something*/}
}
````

dan 

````java
public class ThreadInherit extends Thread{
    @Override
    public void run(){/*do something*/}
}
````

## Thread Local Storage (TLS)

TLS merupakan penyimpanan untuk tiap thread yang digunakan pada thread pool. Sifatnya seperti `static` di Java. TLS ada selama thread aktif

## Scheduler Activation

Many to Many dan Two level menggunakan komunikasi thread menggunakan LWP yang merupakan suatu struktur data. Aktifasi scheduler memberikan upcall yang dihandle dengan upcall handler agar memastikan jumlah kernel threads tepat

## Windows Threads

Windows Threads mengunakan `win32api` yang menggunakan one to one threading dengan fitur TLS DLL stack user dan kernel terpisah, register set dan thread id

Ada struktur data  berikut :

* ETHREAD yang berupa pointer ke proses di KTHREAD dalam kernel
* KTHREAD merupakan info scheduling, synchronization, TEB pointer dalam kernel
* TEB yang merupakan thread user dalam user space

## Linux Threads

Linux menggunakan syscall `clone()` untuk menghasilkan thread. task (thread) memiliki address space yang sama dengan parent process. Struktur datanya adalah `struct task_struct`
