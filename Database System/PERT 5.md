# PERT5-1

# SQL

## Pengertian

 > 
 > \[!info\]
 > SQL adalah standar ISO, SQL flavors yaitu MySQL, PostgreSQL, SQLite, NoSQL, dsb

CRUD memiliki elemen DDL (`CREATE`, `ALTER`, dan `DROP`) dan DML (`SELECT`,`UPDATE`,`INSERT INTO`, dan `DELETE` )

Bahasa SQL tidak hanya dapat melakukan CRUD saja namun termasuk :

* Pemrosesan CRUD menjadi data yang diinginkan
* Pemrosesan data dengan fungsi seperti `COUNT()`,`COALSCENCE()`,dan `MAX()`
* Tidak merepotkan DB admin jika ingin mengubah maupun mentansfer kode SQL karena SQL sudah terstandardisasi

## Database dan Tabel

Sebelum tabel dibuat, DB admin perlu membuat sebuah database untuk menampung tabel tabel tersebut dan informasi terkaitnya. Tabel DB dapat dibayangkan seperti `dict` di Python. Umumnya DBMS mewajibkan DB admin untuk login dahulu

Untuk melakukannya, buatlah kueri berikut

````sql
CREATE DATABASE db_name;
````

Untuk membuat tabel, buatlah kueri berikut

````sql
CREATE TABLE table_name
col_1_name DATA_TYPE_1(SIZE) CONSTRAINT1,
col_2_name DATA_TYPE_2(SIZE) CONSTRAINT2,
--more cols
col_N_name DATA_TYPE_N(SIZE) CONSTRAINTN,
;
````

`(SIZE)` biasanya bersifat opsional jika tipedatanya bukan `VARCHAR`,
`CONSTRAINT` dapat berupa `PRIMARY KEY`,`FOREIGN KEY`, maupun `NOT NULL`

# PERT 5-2

# DDL

 > 
 > \[!warning\]
 > Ingat untuk selalu mengakhiri command SQL dengan titik koma `;`

# `CREATE`

`CREATE` dapat digunakan untuk membuat sebuah database maupun tabel

````sql
-- for database
CREATE DATABASE db_name;
-- for table
CREATE TABLE table_name
col_1_name DATA_TYPE_1(SIZE) CONSTRAINT1,
col_2_name DATA_TYPE_2(SIZE) CONSTRAINT2,
--more cols
col_N_name DATA_TYPE_N(SIZE) CONSTRAINTN,
;
````

untuk melihat informasi terhadap tipedata, kolom dan constraint, dapat menggunakan `DESC`, sintaksnya adalah

````sql
DESC table_name;
````

## `ALTER`

`ALTER` dapat digunakan untuk melakukan hal seperti

* menambah kolom
* menghapus kolom

Untuk menambah kolom, gunakan sintaks berikut

````sql
ALTER TABLE table_name
ADD col_name DATA_TYPE(SIZE) CONSTRAINT;
````

Untuk menghapus kolom, gunakan sintaks berikut

````sql
ALTER TABLE table_name
DROP col_name;
````

## `DROP`

`DROP` dapat digunakan untuk hal berikut

* menghapus tabel
* menghapus kolom (dengan `ALTER TABLE`) 

Untuk menghapus tabel, gunakan sintaks berikut

````sql
DROP TABLE table_name;
````

Untuk menghapus kolom, gunakan sintaks berikut

````sql
ALTER TABLE table_name
DROP col_name;
````
