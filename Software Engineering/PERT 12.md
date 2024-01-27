# PERT 12 - Real Time Software Engineering

## Rancangan Sistem Embedded

Sistem embedded umumnya bersifat real time, yang berarti sedikit/tidak ada toleransi jika operasi berjalan tidak sebagai semestinya, dan jika hal tersebut tidak memenuhi, sistem dianggap gagal.

 > 
 > \[!tip\]
 > Hal hal yang bersifat real time umumnya adalah sistem yang membutuhkan respons cepat seperti keyboard, maupun yang bertanggung jawab terhadap nyawa manusia seperti sistem pengereman

Sistem real time dapat menggunakan stimulus. Contohnya adalah pada keyboard dimana stimulus merupakan pemencetan tombolnya.

Stimulus dapat dicek secara berkala menggunakan listener, maupun secara periodik yaitu seperti interrupt IO. Stimulus periodik lebih sulit untuk ditangani daripada stimulus berkala.

Stimulus kemudian ditangani oleh Real Time Control System untuk memilih actuator yang harus bekerja
![Pasted image 20240120095705.png](Pasted%20image%2020240120095705.png)
Desain ini membuat sistem mampu menangani pengumpulan data yang ada, daripada langsung menyalakan actuator. Tiap sensor dan Actuator mungkin memiliki controller masing masing, untuk meringankan kerja sistem control.

Kompleksitas sistem yang ada membuat terkadang menangani berbagai sensor dan actuator menggunakan program menjadi tidak praktis, sehingga dapat menggunakan sistem operasi waktu nyata (RTOS).

Proses desain sistem real time meliputi

1. Memilih Platform
1. Menentukan stimulus
1. Menganalisis durasi/waktu
1. Desain proses, algoritma dan data
1. Menjadwalkan proses

Dalam proses desain mungkin kita akan merombak arsitektur dan menganalisisnya lagi.

### Pemodelan Sistem Waktu Nyata

Kita dapat menggunakan UML state diagram untuk memodelkan sistem waktu nyata. Sistem akan selalu berada pada salah satu state yang ada. Stimulus akan membuat state sistem berubah, dan dapat melakukan aksi aksi yang tersedia.

### Pemograman Waktu Nyata

Pada sistem dengan kebutuhan waktu nyata yang tinggi (mission critical), bahasa assembly masih digunakan. Untuk sistem real time biasa dapat menggunakan bahasa C. Pemilihan bahasa ini dilakukan karena bahasa-bahasa tersebut dapat mengakses hardware secara langsung dengan cepat, karena tidak memiliki banyak lapisan abstraksi yang meningkatkan overhead.

Dalam RTOS, maka manajemen konkurensi dan sumber daya dilakukan melalui system call. Walaupun terlihat memudahkan, namun pemilihan syscall yang salah dapat mempersulit optimalisasi dari sistem real time. 

## Pola Pola Arsitektural untuk Real-Time Software

Pola-pola arsitektur untuk sistem real time jelas berbeda daripada sistem biasa, karena batasan waktu sangat diperhatikan, maka lebih bersifat prosedural daripada objek maupun komponen. Ada 3 pola arsitektural umum dari sistem real time yaitu 

1. Observe and React 
   Sistem ini akan menganalisis proses dari nilai-nilai sensor yang didapat secara berkala. Kemudian jika kondisi dipenuhi maka akan menimbulkan operasi actuator. Pola ini digunakan untuk soft real time yang tidak memiliki batasan waktu yang terlalu ketat. Contohnya adalah alarm
1. Environmental Control 
   Mirip dengan Observe and React, namun sistem ini dapat menyesuaikan dan memodifikasikan keadaan yang ada. Sistem ini lebih bersifat mengontrol seperti kontrol AC maupun sistem rem.
1. Process Pipeline 
   Arsitektur yang ada merupakan arsitektur producer consumer dimana

* Producer merupakan sensor dan pemroses data, pemrosesan harus cepat agar menghindari hasil yang terpecah-pecah/terputus
* Buffer merupakan tempat penyimpanan data sementara untuk dipakai consumer
* Consumer akan mengoutput data yang diproses
  Contoh : radio dan kamera.

Pola pola ini merupakan titik awal dari sistem, sistem harus dioptimalisasi dengan meminimalkan proses.

## Timing Analysis

Untuk sistem yang memproses stimulus yang periodik maupun aperiodik akan menjadi sangat sulit. Maka kita terkadang terpaksa untuk membuat asumsi terhadap kemungkinan terjadinya stimlus. Ada 3 faktor terhadap menganalisis timing yaitu

1. Batasan Waktu
1. Frekuensi proses
1. Waktu esekusi
   Analisis waktu dapat menggunakan pendekatan worst case scenario untuk meminimalisir potensi dan dampak kegagalan. Kita juga harus membayangkan apa yang akan terjadi dan bagaimana kejadian diproses untuk melakukan analisis waktu. 

Setelah melakukan analisis, maka kita dapat membuat diagram UML untuk memodelkannya. Diagram ini akan menjadi basis dalam desain proses penjadwalan untuk memastikan akan memenuhi tenggat waktu.

Jika menggunakan RTOS maka manajemen prioritas proses perlu dilakukan untuk mengoptimalkan waktu pemrosesan dari proses.

## Sistem Operasi Real Time

 > 
 > \[!abstract\] Definisi
 > Merupakan sistem operasi yang didesain untuk menjalankan operasi secara real time, dengan hanya menyediakan layanan esekusi proses, manajemen sumber daya, dan penjadwalan proses. Oleh karena itu sering disebut sistem *bare metal*

Dalam RTOS ada komponen berikut

1. Jam waktu nyata untuk penjadwalan
1. Pengangan interrupt
1. Scheduler (memilih penjadwalan)
1. Manajer sumber daya
1. Dispatcher (mengesekusi proses)
   Komponen dapat ditambah maupun dikurangi berdasar kebutuhan

### Manajemen Proses

Karena sistem real time wajib menjalankan proses secara cepat dan memenuhi tenggat waktu maka memerlukan alokasi sumber daya yang cepat juga. RTOS memiliki manajer proses untuk menangani itu semua, dengan memperhatikan ransangan, prioritas, urutan dan batas waktu yang ada. 

Jenis interrupt yang ada meliputi Clock Level untuk proses periodik dengan prioritas rendah, dan Interrupt level untuk prioritas tertinggi. Proses prioritas rendah dijalankan di background sambil menunggu kapasitas CPU.

Untuk proses periodik RTOS, konfigurasi pada RTOS dapat digunakan untuk melaksanakan proses tersebut dan memilik proses yang akan dijalankan. Yang perlu diperhatikan adalah

* Prioritas
* Periode
* Waktu eksekusi
* Deadline
  Jika tiba tiba ada 2 proses yang dijalankan pada waktu yang sama, 1 proses akan ditunda, umumnya dengan memperhatikan deadline.

Proses asinkron dapat berinteraksi dengan CPU menggunakan interrupt. Interrupt ini membuat sistem akan langsung otomatis mengerjakan operasi. Pada saat pemrosesan stimulus prioritas tertinggi, CPU akan mengabaikan interrupt yang lain dan menyimpannya di buffer.

Ada 2 kategori algoritma scheduling yang digunakan dalam mengimplementasikan kebijakan interrupsi yaitu

1. Preemptive scheduling (CPU dapat mengerjakan proses lain jika ada interrupt)
1. Non Preemptive scheduling (CPU mengabaikan interrupt selama mengerjakan proses)
   Berbagai algoritma yang dapat digunakan adalah FIFO, Priority, Round Robin, dsb

Informasi proses yang akan dikerjakan akan diproses pada resource manager dan memasukkannya ke ready queue, agar dapat diesekusikan oleh CPU
