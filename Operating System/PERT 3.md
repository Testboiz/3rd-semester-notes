# PERT 3

## Process Concept

Process adalah suatu program yang berjalan secara batch maupun time shared. Proses memiliki stack, data dan counter program (PID)

Stack dan heap dimanage dengan menggunakan memori alokasi terhadap objek seperti `malloc()` dan `new`

State dari suatu proses :

* New (proses baru dibuat)
* running (berjalan)
* waiting (menunggu `Event`)
* ready (menunggu data)
* terminated (berhenti)

PCB (Process Control Block) adalah blok di memori yang memberikan informasi terhadap suatu proses yaitu

* Process \[state\] 
* Pointer to next instruction dalam assembly
* CPU register data
* CPU scheduling info
* Memory management info
* Accounting info (taskmgr)
* IO status

`thread` adalah suatu bagian proses yang bertanggung jawab untuk menjalankan kode. Suatu program dapat menjadi multithread sehingga dapat menjalankan 2 task sekaligus

Multiprogramming dan time sharing digunakan pada saat CPU masih terbatas hanya dapat melakukan 1 task, namun dapat mengschedule waktu agar dapat digunakan efisien, dan seolah olah melakukan multitasking. Hal tersebut dicapati dengan process scheduler dan queue

Di Linux, prosecces direpresentasi dengan `struct task_struct`

````c
 struct task_struct {
      volatile long state;    /* -1 unrunnable, 0 runnable, >0 stopped */
      void *stack;
      atomic_t usage;
      unsigned int flags; /* per process flags, defined below */
      unsigned int ptrace;
      //and more
 }

````

Dalam Queue, tiap program yang ready mereka akan diletakan di ready queue

## Process Schedule

Scheduler bertanggung jawab untuk mengelola process queue

short term scheduler mengelola waktu CPU sedangkan long term scheduler mengelola proses yang berjalan

IO bound proses membutuhkan CPU burst/overload dan CPU bound sebaliknya. 

Medium term scheduling adalah pengelola proses yang dapat menulis dan menghapus data di penyimpanan sekuder

Dalam Android dan IOS dikenal foreground process yang sedang tampil di GUI dan background process yang tidak

Context switch menyimpan info PCB (Process Control Block) agar dapat dengan mudah melakukan switch ke proses lain

## Operating On process

Process berupa suatu tree dimana PID child node selalu lebih besar daripada parent node, dengan init PID selalu 1

Proses dapat selesai secara konkuren, atau menunggu child node untuk selesai

Proses dibuat dengan menciptakan suatu child process node (`fork()`), dan load program (`exec()`)

Proses dapat dihentiukan ketika perintah terakhir diesekusi yaitu `exit()` call, yang akan mengembalikan status ke parent processs node, dan dealokasi proses.

Selain itu dapat menggunakan `abort()` ketika OS menganggap program tidak dibutuhkan maupun menggunakan resource secara berlebihan

Ketika parent process sudah berhenti OS akan menghentikan proses pada child node. Ketika child node berhenti dahulu, maka parent process akan mendapatkan PIDnya dengan system call `wait()`.

Program zombie adalah program yang tidak memanggil `wait()`, dan program orphan berhenti tanpa `wait()`

Browser menggunakan proses yang baru ketika membuka tab baru (oleh karena itu sangat banyak proses yang dibuat dari browser)

## Interprocess Communication

Process dapat share data dengan cooperating yaitu dengan shared memory atau message parsing (log file) atau buffer

Keuntungannya adalah modularitas, performa yang baik, dan kemudahan

Menggunakan shared memory membuat tiap proses dapat mengakses variabel variabel yang ada dalam program. Tantangannya adalah sinkronisasi data

Menggunakan message parsing memiliki tantangan dimana jauh lebih kompleks karena harus memperhatikan infratsruktur yang akan dibuat dan kompleksitasnya

Direct communication adalah cara untuk mengirim message secara langsung ke proses lain. Sifatnya unidirectional dan hanya ada 1 link tiap proses

Indirect communication menggunakan port TCP IP. Sifatnya adlah link terkoneksi ke port dan dapat diakses banyak proses dan memiliki banyak komuniasi. Sifanya lebih fleksibel daripada direct communication

Message yang synchronous adalah message yang blocking (menghentikan esekusi) sehingga integritas data dan variabel terjamin

Message yang asynchronous terjadi ketika message tidak bersifat blocking karena disimpan dalam queue of messages

## Contoh sistem IPC

### POSIX

Menggunakan POSIX shared memory yang membuat memory segment (alokasi pointer), lalu menyetel ukurannya (alokasi memori) baru dapat menulisnya 

### macOS

Syscall adalah pesan ke kernel atau notify. Port digunakan untuk mendapatkan message tersebut, sehingga syscall menjadi fleksibel

Ketika port penuh, maka sistem menunggu data, mereturnnya atau mengcachenya

### Windows

Menggunakan advanced Local Procedure Call yang menggunakan sistem port yang lokal

Connection port dibuka dan klien mengirimkan request. Kemudian server memberikan port komunikasi yang digunakan untuk saling komunikasi

Tiga jenis buffer yaiu

1. Zero capacity (sender harus menunggu)
1. Bounded capacity (sender perlu tunggu jika buffer penuh)
1. Unbounded capacity (sender tidak perlu tunggu)

## Komunikasi Client server

Socket digunakan untuk komunikasi akan port.

192.168.1.1:25565 adalah port ke 25565 untuk IP 192.168.1.1

Jenis socket adalah TCP UDP dan MulticastSocket

### Remote procedure call (Java)

Remote procedure call adalah call prosedur dalam bentuk pesan klien server

Stub adalah proksi untuk memanggil prosedur dalam klien maupun server. 

Stub klien mencari server dan memberikan parameter

Stub server mendapatkan pesanya dan melakukn prosedurnya

Risiko failure sangat besar dan data hanya dikirim 1 kali

### Pipe

Adalah perantara komunikasi. Jenis pipe adalah

Pipe ordinary adalah pipe yang hanya dapat diakses parent dan child

Pipe ordinary bersifat unidirectional karena sifatnya adalah klien server. Dinamakan anonymous pipe di Windows

Named pipe dapat diakses proses lain

Komunikasinya bersifat bidireksional dan digunakan oleh proses lain. Tersedia di UNIX dan Windows
