# PHP

## Pengantar

PHP yang memiliki arti PHP Hypertext Processor adalah bahasa pemograman yang merupakan pemroses HTML. 

Projek PHP disimpan disini 

````
C:\xampp\htdocs\nama_folder
````

dan diakses dengan 

````
localhost/nama_folder/nama_file.php
````

atau

````
127.0.0.1/nama_folder/nama_file.php
````

## PHP Extras

Learn more here * Learn PHP in Y Minutes*

PHP ditulis dalam tagnya tersendiri yaitu 

````php
<?php 
	//PHP code
?>
````

Variabel harus dimulai dengan $ atau kalau tidak maka akan diangap konstan. PHP bersifat dynamically typed. Statement PHP harus diakhiri dengan titik koma (;)

PHP `echo` adalah perintah yang sangat powerful di PHP. Perintah ini akan memprint ke `stdout` ataupun HTML tergantung dengan cara esekusinya. 

`date()` adalah fungsi yang dapat mengoutput tanggal dan waktu dengan banyak format Formatnya dapat berupa
`d m y` => dd mm yy dst

|Format|Deskripsi|
|------|---------|
|d|01-31 (day)|
|j|1-31 (day)|
|D|Sun-Sat|
|l|Sunday-Saturday|
|z|0-365 (hari)|
|m|01-12 (bulan)|
|n|1-12 (bulan)|
|F|January-December|
|t|Jumlah hari (28-31)|
|Y|yyyy|
|y|yy|

Variabel superglobal adalah variabel yang dapat diakses di **semua** bagian kode **tanpa kecuali**
Contohnya adalah

````php
$GLOBALS //diakses dengan $GLOBALS['varname']
$_SERVER 
/*
['SERVER_NAME'] Nama host server
['HTTP_HOST'] host header
['HTTP_REFERER'] url lengkap dari halaman
['REQUEST_METHOD'] GET atau POST
*/
$_REQUEST // data dari form setelah request 
// diakses dengan $_REQUEST['form-name'] dari attribut name 
$_GET // for forms that do method="get"
// GET akan memberikan data ke URL, namun tidak pada POST
$_POST // for forms that do method="post"
$_FILES // files sent on the form 
// gunakan enctype="multipart/form-data" pada form
$_SESSION //session stuff
$_COOKIE //cookies that all we know
//dalam setcookie(nama,nilai,batas)
//akan diakses dengan $_COOKIE[nama]
````
