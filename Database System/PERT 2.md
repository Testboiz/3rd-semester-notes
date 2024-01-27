# PERT 2

## Conceptual Data Model

Conceptual data model mewakili objek dunia nyata, untuk memudahkan suatu bisnis untuk menggambarkan objek yang akan dihandle dalam bentuk database

Ada desain logical dan physical dalam desain data model :

Logical design -> desain DBMS -> Physical design -> Sistem DBMS

Struktur Conceptual Data Model :

* Conceptual Model
* Entity
* Attribute
* Relasi

Top down -> Conceptual dulu

Bottom Up -> Attribut dulu

Jika kita menggambarkan Conceptual Data Model dalam sebuah Relational Data model maka :

* Entity adalah tabel dalam Database
* Attribute adalah kolom dari tabel tersebut
* Relasi adalah hubungan antar tabel seperti `PRIMARY KEY`, `FOREIGN KEY`, dsb

### Network Model

Network model adalah model yang merepresentasikan data sebagai himpunan. Model ini harus diembed dalam bahasa pemograman. 

Network model DBMS dikembangkan oleh Honeywell pada 1964-65 dalam IDS System dan dipopulerkan oleh CODASYL.

DBMS ini diimplementasikan dalam IDMS, DMS 1100, IMAGE, VAX -DBMS, dsb

Kelebihan :

* Dapat memodelkan kebanyakan jenis record
* Menggambarkan skematik dari hubungan tiap dat
* Menggunakan bahasa navigasional seperti `FIND`, `FIND NEXT within set`, `GET`, dsb

Kekurangan :

* Proses navigasional juga memiliki masalah tersendiri
* Banyak array pointer yang sulit untuk di optimize

### Hierachical Data Model

Merepresentasikan data dalam bentuk tree. Sistem ini tidak memiliki bahasa yang standar

Kelebihan :

* Simple untuk dibuat dan diproses
* Berkoresporensi dengan baik dengan sifat data yang terstruktur

Kekurangan :

* Sistem pemrosesan yang juga navigasional
* Database masih digambarkan secara linear
* Sulit untuk dioptimize

### Object Oriented Data Model

Merepresentasikan data dalam bentuk `class` atau `object`. Tiap `class` diorganisir dengan struktur hireaki. Operasi yang ada dalam tiap `class` dinamakan `method`.

Sistem DB ini digunakan untuk menggambarkan struktur logika pada bahasa pemograman seperti C++, Java, dll

Sistem DB yang menggunakan konsep ini adalah O2, ORION, IRIS. Dan standar-standarnya adalah ODMG-93, ODMG-Version 2.0 dan ODMG-Version 3.0

### Relational Model

Model ini membuat record data dapat disimpan dalam sebuah tabel tabel terpisah. Umumnya dimanajemen oleh SQL. Model ini diproposalkan oleh [E.F. Codd (IBM)](#) Pada tahun 1970, dan sistem pertama dibuat tahun 1982. 

Implementasinya ada pada sistem sistem seperti DB2, ORACLE, MS SQL Server, SYSBASE, INFORMIX, MySQL, dan PostgreSQL

Standar yang dibuat untuk database adalah SQL-89, SQL-92, SQL-99, dsb

### Object Oriented Relational Model

Model ini menginkoporasikan konsep Object Oriented dengan Relational Model

Sistem Oracle-10i, DB2 dan SQL server terbaru telah memiliki fitur ini

## Entity

Entity adalah data yang memiliki property yang sama dan memiliki keberadaan yang independen.

Kita dapat membayangkan Entitas sebagai tabel dalam DB

* Entity Occurence adalah jumlah objek dari tipe entity

* Strong Entity tidak secara *existence dependent* dengan tipe entity lainnya

* Weak Entity bersifat *Existence dependent* dengan tipe entity lainnya

Weak Entity bergantung pada Strong Entity. Contoh : Mahasiswa dan *Orang tua* (weak). Ketika entitas yang strong dihapus, maka entias lemah (*Orang tua*) akan hilang.

Dan hubungan relasi ke entitas weak akan menjadi weak juga

-> Mahasiswa - \<\<Memiliki>> *Orang Tua*

Maka relasi `Memiliki` itu juga weak

![Gambar Entity](#)

## Attribute

Attribut adalah properti dari entity / tipe relasi

Simple Attribute adalah atribut yang memiliki single component yang independen. Dapat digambarkan sebagai tipedata primitif, seperti `int`, `VARCHAR`, dsb.  Contoh : Nama orang, ~~gender~~

Composite Attribute adalah atribut yang memiliki banyak komponen. Dapat digambarkan sebagai Object OOP

Contoh Composite Attribute adalah `DATE` karena dapat dipisah menjadi `DAY`,`MONTH`, dan `YEAR`

Key attribute adalah attribut yang bersifat KEY seperti `PRIMARY KEY` di SQL atau seperti NIM atau NIK

Multi Valued Attribute adalah attribut yang memiliki banyak nilai tiap sebuah tipe entity. Dapat digambarkan sebagai sebuah Array Contoh : email address

Derived Attribute adalah attribute yang menggambarkan nilai yang dapat diturunkan dari tipe entitas lainnya. Umumnya dihitung dengan fungsi dalam DBMS tersebut. Contoh : IPK dapat dihitung dari IPS

## Relationship

Relationship type adalah himpunan atas hubungan antara entitas

Relationship Occurence adalah jumlah Relationship dalam tiap entitas

General Relationship adalah relationship untuk entitas yang sama

Identifying Relationship adalah relationship untuk entitas yang berbeda

Recursive Relationship adalah relationship untuk tipe entitas yang sama namun memiliki lebih dari satu peran

Relationship dapat diberikan nama peran untuk menggambarkan kegunaan dalam tiap jenis entitas 

## Cardinality

Cardinality adalah derajat hubungan dalam tiap entitas

Jenis kardinalitas adalah :

* 1 : 1 Contoh 1 Orang 1 KTP
* 1 : M Contoh 1 Mahasiswa M Matkul
* M : 1 Contoh Banyak Mhs dalam 1 Kelas
* M : N Contoh 1 Mhs bisa punya banyak UKM dan 1 UKM dapat memiliki banyak Mhs

## Constraint

Range dari jumlah okkurensi terhadap sebuah entitas dalam sebuah hubungan yang ada.

Menggambarkan Constraint dengan notasi \[m...n\] dengan m,n 0-x dimana x adalah bilangan bulat atau * yang menandakannya opsional

## Participation

$-$ adalah partial participation. Contoh Mahasiswa dapat mengikuti UKM namun tidak diwajibkan

$=$ adalah full participation. Contoh : Setiap WNI memiliki NIK

````flow
st=>start: Start
op=>operation: Your Operation
cond=>condition: Yes or No?
e=>end

st->op->cond
cond(yes)->e
cond(no)->op
````
