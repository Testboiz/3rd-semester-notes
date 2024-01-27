# PERT 5

# CPU Scheduling

## Konsep

 > 
 > CPU dan IO memiliki keterbatasan atas performan dan kemampuan, sehingga CPU scheduling dibutuhkan, apalagi pada sistem low end

CPU melakukan burst untuk mengoperasi IO maupun init/stop esekusi. Burst umumnya cukup singkat. CPU scheduler adalah proses untuk menentukan suatu proses yang dapat diesekusi terlebih dahulu, agar waktu CPU dapat digunakan seefisien mungkin. Dispatcher adalah modul yang memberi CPU kontrol untuk :

* switch konteks
* switch user mode
* menjalankan program 
* restart program
* memindakan proses ke short term scheduler
* memindahkan data register ke PCB proses

CPU Scheduling ada berbagai jenis penjadwalan yaitu

* Short Term Scheduling (seleksi proses yang ready untuk dijalankan)
* Medium Term Scheduling (melakukan swap memori RAM ke disk\[HDD/SSD/NVME\] )

## Kriteria Scheduing

Berdasarkan faktor tersebut :

* **Keadilan**, yaitu semua proses akan dilayani, dengan waktu yang pantas
* **Efisiensi**, yaitu menggunakan CPU Time seoptimal mungkin (tidak pernah idle)
* **Response Time**, yaitu mempercepat waktu respons secepat mungkin
* Waktu tunnggu antara process switching dan pada scheduler seminimum mungkin
* Memiliki throughput tinggi (jumlah proses selesai )

## Algoritma Scheduling

Scheduling bertujuan agar CPU dapat mengelola waktu, sumber daya, dan throughput seefisien mungkin. CPU scheduling memanfaatkan multiprogramming. Beberapa jenis scheduling yang dapat dilakukan adalah :

* First come First Served
* Shortest Job First
* Priority Scheduling
* Round Robin
* Multilevel Queue
* Multilevel Feedback Queue
* Penjadwalan Multiple Processor

### FCFS (FIFO)

Merupakan algoritma paling sederhana (stack). Memiliki banyak kekurangan karena waktunya kurang efisien. Job yang penting harus menunggu job yang kurang penting, dan job cepat harus menunggu job lama

FIFO digunakan pada batch processing, namun tidak digunakan pada sistem interaktif dan real time

### SJF

 > 
 > \[!Note\] 
 > Shortest Job First memiliki skema preemtif (dapat diinterupsi dengan job yang lebih singkat) maupun tidak (non preemptif)

Shortest Job first lebih efisien daripada First Come First Served, dan Shortest Job First preemptif dinamakan **Shortest Remaining Time First**

Ada teknik yang dapat memperkirakan  lama burst CPU adalah :

$$\tau\_{n+1} = \alpha\tau_n + \sum^{n+1}*{i=1}(1-\alpha)^i\alpha\tau*{n-i} \tag{1}$$

* $\tau_n$ adalah waktu pemrosesan ke i (sebelumnya)
* $\tau\_{n+1}$ adalah waktu pemrosesan yang diprediksi
* $\alpha$ adalah suatu konstan yang ditentukan secara arbitrary

 > 
 > \[!fail\]
 > SJF memiliki kekurangan bahwa meskipun telah ada rumusnya, tetap sulit untuk memprediksi waktu running secara efektif. Dan proses yang penting tidak diprioritaskan kalau lama

### Priority Scheduling

Priority scheduling menggunakan priortias sebagai weight dari proses, bukan waktu. Prioritas meningkat kalau waktunya makin lama.

 > 
 > \[!Warning\]
 > Program starvation dapat terjadi ketika program prioritas rendarh tidak pernah teresekusi. Sering terjadi setelah deadlock

Solusinya adalah process aging yaitu meningkatkan prioritas pada proses yang sudah lama tidak diproses

Keputusan scheduling dilakukan saat proses switch dari state waiting, ready, running maupun proses berhenti

### Round Robin (RR)

Round robin melakukan switching yang sering untuk mencapai keseragaman waktu. Switching dapat dikurangi jika periode ditingkatkan. Queue harus memiliki quantum yang besar agar memiliki performa seperti FIFO, kalau tidak akan memiliki overhead terlalu tinggi

### Multilevel Queue

Menggunakan beberapa jenis queue RR maupun FCFS/FIFO/stack yang memisahkan proses batch dengan interaktif/real time. Prioritasnya semuanya adalah sama. Tiap queue memiliki algoritma scheduling tersendiri

### Multilevel Feedback Queue

Merupakan perkembangan dari multilevel queue dimana proses dapat pindah queue dengan faktor berikut :

* jumlah antrian
* algoritma penjadwalan tersebut
* meningkatkan / menurunkan antrian proses
* prioritas dari job
  Menggunakan time quantum, yaitu satuan unit waktu yang ditentukan oleh CPU dalam ms. Time quantum memudahkan CPU untuk mengerjakan proses cepat tanpa overhead. 

 > 
 > \[!warning\]
 > Namun time quantum yang terlalu lama akan membuat pemrosesan seperti FIFO, dan waktu yang terlalu singkat akan memiliki overhead tinggi

Contoh :

* Queue 0 memiliki waktu processing 8ms, dan semua proses masuk kesini
* Queue 1 memiliki waktu processing 16ms, untuk proses yang terlalu lama di queue 0. Berjalan ketika queue 0 kosong
* Queue 2 untuk proses yang terlalu lama dalam queue 1, menggunakan algoritma FCFS. Queue 2 hanya dijalankan ketika queue 1 dan 0 kosong

### Penjadwalan Multiple Processor

Pada CPU modern yang memiliki 2 atau lebih CPU, menggunakan penjadwalan multi processor yang memiliki load sharing. Selain itu juga menggunakan *asymmetric multiprocessing* dimana ada CPU yang mengelola pemrosesan dan CPU lain menjalankannya. *symmetric processing* adalah pendekatan dimana tiap CPU bertanggung jawab atas scheduling mereka sendiri

### EXTRA : Real Time Scheduling

Mission Critical adalah sistem real time yang akan gagal jika gagal menyelesaikan proses dalam waktu yang diberikan. 

Real time (soft real time) memiliki dampak yang lebih kecil ketika terjadi kegagalan, namun tetap menuntut respons cepat
