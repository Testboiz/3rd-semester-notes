# PERT 3

# RELATIONAL DATA MODEL

## Terminologi

* Relasi => Tabel
* Atribut -> Kolom
* Domain -> Nilai Atribut
* Tuple -> Array nilai 
* Degree -> Jumlah atribut
* Kardinalitas -> Jumlah tuple
* RDB -> database yang menggunakan tabel

## DB Relations

* **Relation schema**, Relasi dari atribut dan domain
* **RDB Schema**, Himpunan Relation schema

Relation memiliki nama yang unik, dan tiap sel memiliki 1 nilai

Atribut memiliki nama yang distinct tiap tabel, dan nilanya dalam domain tabel

Tuple adalah distinct, dan urutan atribut/tuple tidak perlu diperhatikan

Superkey adalah atribut yang unik dan **dipakai** untuk mengidentifikasi tabel

Candidate Key adalah adalah `PRIMARY KEY`, `FOREIGN KEY`, dsb

Candidate Key adalah 

* Kolom yang dapat menjadi superkey
* Subset Superkey unik

`PRIMARY KEY` adalah key yang paling **tepat** untuk mengidentifikasikan tabel

`ALTERNATE KEY` adalah key yang tidak dipilih

`COMPOSITE KEY` adalah subset tabel (kolom) yang unik dan dapat menjadi KEY

`FOREIGN KEY` adalah `PRIMARY KEY` dari tabel lain yang dipakai di tabek tersebut

Non Prime attribute adalah atribut selain `PRIMARY KEY` 

## Integritas Relasional

`NULL` adalah nilai yang dianggap tidak ada, tidak siap, error

`PRIMARY KEY` tidak boleh `NULL`

`FOREIGN KEY` harus mengidentifikasi `CANDIDATE KEY` dari relasi aslinya atau `NULL`

Menentukan Constraint dari relasinya

## View

Base Relation adalah relasi yang berkorespondensi dengan entitas dalam Conceptual schema dimana tuple disimpan secara fisik

View adalah hasil `SELECT` yang menggambarkan relasi baru, yang dibuat dari kueri tersebut. 

Perubahan relasi akan langsung memengaruhi View

View membantu dalam information hiding karena hanya menampilkan database yang penting penting saja, dan memperbolehkan user untuk mengakses data secara custom

Ada batasan dari modifikasi View yaitu

* Update diperbolehkan jika kueri memiliki base relation dan mengandung candidate keynya
* Tidak diperbolehkan jika menggunakan banyak base relation, agregrasi maupun grouping

Jenis View adalah :

* tidak dapat diupdate secara teoretis
* tidak dapat diupdate
* dapat diupdate secara parsial
