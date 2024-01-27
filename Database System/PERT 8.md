# PERT 8

# Subquery

## Single Row Subquery

Fungsi pada SQl dapat dimamfaatkan mirip dengan pada bahasa pemograman lainnya. Cara mengaplikasikannya adalah dengan menggunakan subquery

Contoh query

````sql
SELECT col_name FROM table_name
WHERE another_col_name = (SELECT MAX(other_col_name) FROM table_name)
;
````

## Nested Subquery

Ketika kueri semakin kompleks, dapat menambahkan kueri didalam kueri seperti berikut

Single Row Subquery dalam Single Row subquery secara rekursif dimanakan [Nested Subquery](PERT%208.md#nested-subquery)

````sql
SELECT col_name FROM table_name
WHERE another_col_name = (SELECT MAX(other_col_name) FROM table_name
WHERE one_more_category = SELECT MAX(one_more_other_col_name) FROM table_name) 
;
````
