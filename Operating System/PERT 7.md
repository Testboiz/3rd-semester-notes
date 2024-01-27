# PERT 7 - Deadlock

## System Model

Deadlock terjadi ketika semaphore dari semua thread memiliki nilai 1, sedangkan race condition adalah ketika semua thread memiliki nilai semaphore 0

Contohnya adalah pada simpang tanpa lampu merah yang semrawut, dimana pengendara saling ingin menang sendiri, sehingga kendaraan terkunci dan tidak bisa maju atau bahkan mundur.

## Karakteristik Deadlock

1. Hanya 1 proses dapat menggunakan resource (mutex)
1. Ada lebih dari 1 proses yang ingin menggunakan resource dan harus menunggu
1. Proses hanya baru bisa berhenti menggunakan resource ketika sudah selesai
1. Semua proses menunggu proses lain (stuck/circular wait)

Contoh di dunia nyata

1. Simpang lalulintas
1. Memiliki lampu merah yang seharusnya dipakai
1. Tidak ada percabangan di tengah2 lampu merah
1. Kendaraan-kendaraan tersangkut karena sedang macet

## Deadlock in Multithreaded Application

Kita dapat menvisualisasikannya dengan sebuah **graf resource allocation**.
Misal proses $P_1,P_2,\cdots,P_n$ merupakan node dari proses
dan $R_1,R_2,\cdots,R_n$ adalah node resource yang memiliki batasan semaphore (jumlah titiknya)

Maka Deadlock dapat dideteksi dengan adanya siklus pada graf tersebut jika ada 1 proses per 1 resource.

## Methods for Handling Deadlocks

Cara menangani Deadlock adalah

1. Mencegahnya
1. Memiliki sistem recovery
1. Anggap tidak terjadi (UNIX)

## Deadlock Prevention

Menggunakan mutex (tidak wajib), namun yang paling penting adalah, program harus menunggu jika ada program lain yang mengakses resource **(Hold and wait)**.
Catatannya adalah proses harus merequest resource pada **sebelum** program berjalan, atau pada sebelum ada resource pada proses tersebut. Dapat berisiko starvation jika memiliki penggunaan resource rendah

Dengan **No Preemption**

1. Proses yang memiliki resource harus melepasnya jika ingin merequest resource yang dipakai resource lain
1. Proses akan menunggu pada queue
1. Proses baru bisa berjalan jika dapat kembali mengakses resource lama dan baru

Dengan **Circular Wait**, menggunakan enumerasi terhadap resource dan mewajibkan request pada urutan nilai enumerasi terendah hingga yang tertinggi

## Deadlock Avoidance

Mewajibkan sistem memiliki informasi a priori. Dapat menggunnakan pendekatan berikut

* Mendeklarasikan jumlah maksimum resource yang dapat dipakai untuk setiap tipe resource pada proses
* Menghindari circular wait condition dengan algoritma khusus
* Menggunakan Resource-allocation state yang ditentukan dengan jumlah resource yang tersedia dan teralokasi, dan kebutuhan tiap proses

### Safe State

Safe state adalah situasi dimana sistem dapat memodelkan **graf resource allocation**, dan mengecek apakah ada potensi deadlock, dengan mendeteksi siklus pada graf. Jika ada siklus maka bukan safe state dan berisiko deadlock, dan sebaliknya

Jika resource hanya memiliki nilai semaphore 0 dan 1. Gunakan **graf resource allocation**. Jika lebih, gunakan **algoritma Banker**

#### Resource-Allocation Graph

Graf resource allocation dapat digambarkan sebagai berikut

* Gunakan node biasa untuk memodelkan proses $P_1,P_2,\cdots,P_n$ dan kotak untuk memodelkan $R_1,R_2,\cdots,R_n$ 
* Gunakan $\dashrightarrow$ jika $P_i$ mungkin akan menggunakan $R_i$ 
* Gunakan $\rightarrow$ jika $P_i$ sedang menggunakan $R_i$

Deteksikan siklus yang ada dan tentukan apakah ada dalam safe state atau tidak, berdasarkan garis-garis yang **bukan putus putus**

#### Banker's Algorithm

Misal `n` adalah jumlah proses dan `m` adalah jumlah resource
Ada 4 tipedata yang harus diperhatikan

`Available` yaitu vektor dengan panjang `m` yang menandakan jumlah instans $R_j$ yang dapat dipenuhi
`Max` adalah matrix dengan ukuran `n`x`m` dimana `Max[i][j]` menandakan maksimal jumlah request dari $P_i$ untuk $R_j$
`Allocation` adalah matrix dengan ukuran `n`x`m` dimana `Allocation[i][j]` menandakan jumlah request dari $P_i$ untuk $R_j$ yang **sedang ada**
`Need` adalah matrix dengan ukuran `n`x`m` dimana `Need[i][j]` menandakan jumlah request dari $P_i$ untuk $R_j$ yang **dibutuhkan untuk menyelesaikan tugasnya** dimana `Need[i][j] = Max[i][j] - Allocation[i][j]`

#### Algoritma Safety

Dengan menggunakan tipedata pada algoritma Banker tambahkan tipedata berikut

`Work` adalah vektor dengan panjang `m` dimana `Work == Available`
`Finish` adalah vektor dengan panjang `n` dengan tipedata `bool`

Jika ada `finish[i] == false ` dan `Need[i] <= Work` maka

````python
for i in range(Work):
	Work[i] += Allocation[i]
Finish[i] = True
````

Safe state ditentukan dengan apakah semua nilai pada `Finish` adalah `True`

Contoh [Banker's algorithm dan Safety algorithm](https://www.geeksforgeeks.org/bankers-algorithm-in-operating-system-2/) dalam Python

````python
# Banker's Algorithm
 
# Driver code:
if __name__=="__main__":
     
    # P0, P1, P2, P3, P4 are the Process names here
    n = 5 # Number of processes
    m = 3 # Number of resources
     
    # Allocation Matrix
    alloc = [[0, 1, 0 ],[ 2, 0, 0 ],
            [3, 0, 2 ],[2, 1, 1] ,[ 0, 0, 2]]
     
    # MAX Matrix 
    max = [[7, 5, 3 ],[3, 2, 2 ],
            [ 9, 0, 2 ],[2, 2, 2],[4, 3, 3]]
     
    avail = [3, 3, 2] # Available Resources
     
    f = [0]*n
    ans = [0]*n
    ind = 0 # index 
    # initializing the boolean flags
    for k in range(n):
        f[k] = 0

	# Initializing the need matrix
    need = [[ 0 for i in range(m)]for i in range(n)]
    for i in range(n):
        for j in range(m):
            need[i][j] = max[i][j] - alloc[i][j]
    y = 0 # another index var
    # Safety Algorithm
    for k in range(n):
        for i in range(n):
            if (f[i] == 0):
                flag = 0
                for j in range(m):
                    if (need[i][j] > avail[j]):
                        flag = 1
                        break
                 
                if (flag == 0):
                    ans[ind] = i
                    ind += 1
                    for y in range(m):
                        avail[y] += alloc[i][y]
                    f[i] = 1

	# printing the graph
    print("Following is the SAFE Sequence")
     
    for i in range(n - 1):
        print(" P", ans[i], " ->", sep="", end="")
    print(" P", ans[n - 1], sep="")
 
# This code is contributed by SHUBHAMSINGH10
````

## Deadlock Detection

Mekanisme ini memperbolehkan deadlock, dan juga deadlock perlu dideteksi dan recover dari deadlock

Jika menggunakan [Resource-Allocation Graph](PERT%207.md#resource-allocation-graph), gunakan algoritma untuk mendeteksi siklus

Jika tidak, gunakan algoritma deteksi berikut

Siapkan tipedata
`Available` yaitu vektor dengan panjang `m` yang menandakan jumlah resource dari tiap tipe
`Allocation` yaitu matrix `n`x`m` yang menandakan jumlah resource yang dialkoasi dalam tiap proses
`Request` yaitu matrix `n`x`m` yang menandakan jumlah resource yang direquest oleh tiap proses

Dengan algortima yang mirip dengan [Algoritma Safety](PERT%207.md#algoritma-safety) tentukan apakah ada member vektor yang `false`, jika iya maka sebagian dari proses yang ada sedang mengalami deadlock

Tidak selamanya deteksi deadlock dapat menentukan proses yang menyebabkan deadlock. Maka algoritma ini dijalankan berdasarkan pertimbangan frekuensi deadlock dan jumlah proses yang dirollback

## Recovery From Deadlock

Ada 2 cara yaitu

1. Process Termination
1. Resource preemption

Untuk Process termination, hentikan 1 proses sampai deadlock berhenti. Prioritasnya adalah

1. Prioritas proses
1. Umur proses dan lama pengerjaannya
1. Jumlah resource
1. Kebutuhan Resource
1. Jumlah proses 
1. Interactive atau batch

Untuk Resource preemption, pilih salah 1 proses dengan cost (dampak rollback) terendah. Lalu lakukan rollback, Ingat untuk mempertimbangkan jumlah rollback dalam cost untuk menghindari starvation
