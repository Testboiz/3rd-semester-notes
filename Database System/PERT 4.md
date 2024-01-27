# PERT 4

# NORMALISASI

 > 
 > Digunakan untuk membuat data agar dapat direpresentasikan lebih baik dalam database, meminimalkan redundansi, ukuran DB,dsb

Sebuah data yang redundan dapat berisiko mengalami Update Anomalies, dimana data menjadi tidak konsisten setelah diupdate. 

Adapun sifat dari loseless join dan Dependenct Preservation yaitu

* Loseless Join dapat membuat kita menemukan relasi dari elemen elemen yang ada dalam relasi yang lebih kecil
* Dependency Preservation Property membuat kita dapat membuat constraint dari relasi induk dengan membuat constraint pada relasi anaknya

## Dependensi Fungsional

 > 
 > Definisi. Yaitu menggambarkan hubungan antara atribut dan relasi. Jika A dan B berelasi dengan R maka B dependen dengan A yang dinotasikan B $\rightarrow$ A dimana tiap nilai A di R diasosiasikan dengna nilai B di R

Secara Diagram, simbol $\rightarrow$ juga digunakan, dan ketika hubungan tersebut tidak dependen secara fungsional maka digunakan simbol $\not\rightarrow$ 

Sifat dari dependensi fungsional adalah 

* memiliki hubungan one to one dengan tiap atribut
* Valid sepanjang waktu
* tidak trivial

Dependensi fungsional bisa cukup kompleks.

Selain itu juga perlu mengidentifikasi himpunan dari dependensi fungsional $X$ dimana $X \subset Y$ dan $X \rightarrow Y$ ($X$ implikasi $Y$) dimana dinotasikan sebagai $X^+$

Aksioma Amstrong adalah aturan akan bagaimana dependensi fungsional baru dapat diambil dari yang sudah ada

Misal $A$, $B$ dan $C$ merupakan subset dari $R$.($A \subset R, B \subset R, C \subset R$)  Maka :

* Jika $B \subset A$ maka $A \rightarrow B$ (Refleksif)
* Jika $A \rightarrow B$ maka $AC \rightarrow BC $ (Augmentasi)
* Jika $A \rightarrow B, B \rightarrow C$ maka $A \rightarrow C$ (Transitif)

Seiring data semakin normal, maka hubungan akan data akan semakin terbatas dan risiko anomali update semakin berkurang

## Bentuk Normal Form

* Unnormalized Normal Form (tabel data asli yang memiliki banyak duplikat)
* Bentuk Normal Pertama (tabel dengan `PRIMARY KEY`, yang menghindari entri duplikat)
* Bentuk Normal Kedua (1NF dimana atribut tanpa `PRIMARY KEY` dependen dengannya)
  Didapat dengan menghapus dependensi parsial pada `PRIMARY KEY` dan menaruhnya ke relasi baru dengan salinan deterrminannya. 2NF dependen dengan `CANDIDATE KEY`
* Bentuk Normal Ketiga (Tidak ada atribut yang dependen secara transitif ke `PRIMARY KEY` )
  Didapat dengan menghapus dependensi pada `PRIMARY KEY` dan membuat relasi baru dari salinan determinannya.  2NF dependen secara **transitif** dengan `CANDIDATE KEY`
* Bentuk Normal Boyce Codd (BCNF) (Tiap determinan adalah  `CANDIDATE KEY`)
  Penyimpangan BCNF terjadi jika 
  * Memiliki 2 atau lebih composite `CANDIDATE KEY`
  * `CANDIDATE KEY` yang ada memiliki atribut yang sama

Synopsis 
$$
UNF \subset 1NF \subset 2NF \subset 3NF \subset BCNF \subset \cdots \text{Higher Normal Form}
$$

* UNF adalah data kotor dalam database
* 1NF adalah data yang diorganisir dengan `PRIMARY KEY`
* 2NF adalah data dimana tiap kolomnya berikatan dengan `PRIMARY KEY`
* 3NF adalah data dimana tiap kolomnya berikatan dengan `PRIMARY KEY` **secara transitif**
* BCNF adalah data dimana kolom kolomnya dapat diidentifikasi dengan superkey, alias **tiap entry database selalu dapat dicari dalam tabel lain di database**
