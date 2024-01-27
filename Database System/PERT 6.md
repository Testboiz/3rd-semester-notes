# PERT 6

# Kueri Lanjutan

## Data Sorting

Mirip dengan mengklik ikon $\uparrow\downarrow$ pada UI tabel, kita dapat melakukannya di SQL dengan kueri ini

````sql
SELECT * FROM table_name
WHERE col_name = condition
ORDER BY col_name = ASC --[or DESC]
````

condition can be something like expressions on C/C++ like `x>y` 

## Data Grouping

Dengan `GROUP BY` kita dapat mengelompokan `SELECT` yang menggunakan fungsi-fungsi yang ada pada SQL.

 > 
 > \[!warn\]
 > `GROUP BY` esensial dalam melakukan `SELECT` jika menggunakan fungsi sepert `SUM()`,`COUNT()`,`MAX()`, dsb, agar mendapatkan kolom mana yang dilakukan fungsi tersebut

Sintaksnya adalah

````sql
SELECT col_1, col_2, ... ,FUNC_1(input1),FUNC_2(input2),...
FROM table_name
GROUP BY col_1, col_2, ...
;
````

## Aggregrate Function

Fungsi seperti `SUM()`,`COUNT()`,`MAX()`, dsb juga dapat digunakan sendiri tanpa `SELECT` kolom lainnya.
Contoh Kueri

````sql
SELECT MAX(col_name) AS maxvalue FROM table_name;
````

Ini akan mengembalikan 1 tabel dengan kolom bernama `maxvalue` dengan isi `MAX(col_name)`

## `HAVING`

`HAVING` mirip dengan `WHERE`, hanya saja digunakan dengan `GROUP BY`
Sintaksnya adalah

````sql
SELECT col_1, col_2, ... ,FUNC_1(input1),FUNC_2(input2),...
FROM table_name
GROUP BY col_1, col_2, ...
HAVING condition
````
