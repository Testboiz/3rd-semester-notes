# PERT 3

## Bentuk Umum Persamaan Linier

SPL memiliki bentuk sebagai berikut

# $$
\\begin{cases}
&a\_{11}x_1+a\_{12}x_2+\cdots+a\_{1n}x_n = b_1\\
&a\_{21}x_1+a\_{22}x_2+\cdots+a\_{2n}x_n = b_2\\
&\cdots \\
&a\_{m1}x_1+a\_{m2}x_2+\cdots+a\_{mn}x_n = b_m \tag{3.1}\\
\\end{cases}
$$
Bentuk Matrixnya adalah
$$
\\begin{pmatrix}
a\_{11} & a\_{12} & a\_{13} & \cdots & a\_{1n} \\
a\_{21} & a\_{22} & a\_{23} & \cdots & a\_{2n} \\
a\_{31} & a\_{22} & a\_{33} & \cdots & a\_{3n} \\
\\vdots & \vdots & \vdots & \ddots & \vdots \\
a\_{n1} & a\_{n2} & a\_{n3} & \cdots & a\_{nn} \\
\\end{pmatrix}
\\begin{pmatrix}
x_1\\
x_2\\
x_3\\
\\vdots\\
x_n
\\end{pmatrix}

\\begin{pmatrix}
b_1\\
b_2\\
b_3\\
\\vdots\\
b_n
\\end{pmatrix}
\\tag{3.2}
$$

Dapat disederhanakan menjadi $A\pmb{x} = b$ 

## Gaussian Elimination

# Buat Bentuk Matrix $(3.2)$  menjadi seperti berikut menggunakan operasi basis elementer :
$$
\\begin{pmatrix}
a\_{11} & a\_{12} & a\_{13} & \cdots & a\_{1n} \\
0 & a\_{22} & a\_{23} & \cdots & a\_{2n} \\
0 & 0 & a\_{33} & \cdots & a\_{3n} \\
\\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & a\_{nn} \\
\\end{pmatrix}
\\begin{pmatrix}
x_1\\
x_2\\
x_3\\
\\vdots\\
x_n
\\end{pmatrix}

\\begin{pmatrix}
b_1\\
b_2\\
b_3\\
\\vdots\\
b_n
\\end{pmatrix}
\\tag{3.3}
$$
Bentuk $(3.3)$ dinamakan *Row Echelon Form*

### Modified Gaussian Elimination

Ketika kita sedang mengerjakan proses eliminasi Gaussian, terkadang kita menukar baris satu dengan baris lainnya. Ketika hal ini dilakukan, maka teknik ini sudah termasuk **Modified Gaussian Elimination**. Sekilas teknik ini hampir sama dengan Gaussian Elimination biasa, namun teknik ini sangat berbeda dalam implementasi algoritmiknya. Metode ini juga memiliki error yang jauh lebih kecil

## Scaling

Memperhatikan pembulatan yang dapat terjadi dalam suatu sistem komputer. Ada kemungkinan bahwa suatu SPL memiliki mangnitudo yang terlalu besar, dan pembulatan membuat penghitungan menjadi error. 
Contohnya : 
$$
\\begin{align}
&2x_1 + 100000x_2 = 100000 \tag{A} \\
&x_1 + x_2 = 2 \tag{B}
\\end{align}
\\tag{3.3}
$$
Jika menggunakan akurasi desimal yang terlalu rendah, maka Operasi $\frac12 (\text{A}) - (\text{B})$ dapat menghasilkan $-50000x_2=-50000$, Substitusi $x_2 = 1$ di $(\text{A})$ menghasilkan $x_1 = 0$ yang merupakan jawaban yang salah.

Oleh karena itu. Penskalaan digunakan untuk menghindari hal tersebut. Persamaan $(\text{A})$ dapat dibagi dengan nilai koefisien terbesar sehingga koefisien terbesar adalah 1

Hal ini dapat dilakukan terus menerus untuk semua persamaan, sehingga semua persamaan memiliki koefisien terbesar yaitu 1

## Eksistensi Solusi SPL

Jika Bentuk Row Echelon Form memiliki $\text{rank}(A\_{nn}) \< n$ yang bermakna bahwa ada barisan yang dipenuhi angka 0, maka SPL dapat memiliki solusi tak hingga atau tidak ada sama sekali, jika tidak konsisten

 > 
 > \[!note\]
 > $\text{rank}(A\_{nn})$ ditentukan dengan mencari bentuk [Row Echelon Form](PERT%203.md#gaussian-elimination), dan menghitung jumlah baris yang tidak seluruhnya 0

More in Linear Algebra %% i did not catat :( %%

## Gauss Jordan

Hampir sama dengan Gauss, namun matrix $A$ harus menjadi matrix identitas $I\_{nn}$ dari 
$$
\\left(\hspace{0pt}\begin{array}{ccccc|c}
x\_{11} & x\_{12} & x\_{13} & x\_{14} & \cdots & b_1\\
x\_{21} & x\_{22} & x\_{23} & x\_{24} & \cdots & b_2\\
x\_{31} & x\_{32} & x\_{33} & x\_{34} & \cdots & b_3\\
\\vdots & \vdots & \vdots & \vdots & \ddots & \vdots\\
x\_{n1} & x\_{n2} & x\_{n3} & x\_{n4} & \cdots & b_n\\
\\end{array}\hspace{0pt}\right)
\\tag{3.4}
$$
yang merupakan bentuk gabungan $A\vec{x} = \vec{b}$
menjadi
$$
\\left(\hspace{0pt}\begin{array}{ccccc|c}
1 & 0 & 0 & 0 & \cdots & b_1\\
0 & 1 & 0 & 0 & \cdots & b_2\\
0 & 0 & 1 & 0 & \cdots & b_3\\
\\vdots & \vdots & \vdots & \vdots & \ddots & \vdots\\
1 & 0 & 0 & 0 & \cdots & b_n\\
\\end{array}\hspace{0pt}\right)
\\tag{3.5}
$$

## Metode Invers

Dengan menggunakan persamaan matrix $A\vec{x} = \vec{b}$ kita dapat memanipulasinya menjadi $\pmb{x} = A^{-1}\pmb{b}$ 

# Teknik perhitungan Invers adalah seperti berikut
2x2
$$
\\begin{pmatrix}
a & b \\
c & d
\\end{pmatrix} ^{-1}

\\frac{1}{\det(A)} 
\\begin{pmatrix}
-d & c \\
b & -a 
\\end{pmatrix}
\\tag{3.6}
$$
Untuk matrix 3x3
Pada Matrix berikut dapat ditentukan inversnya dengan berikut
$$
\\begin{pmatrix}
a & b & c \\
d & e & f \\
g & h & i
\\end{pmatrix}
\\tag{3.7}
$$
Pertama mencari determinannya terlebih dahulu

* Menggunakan Metode Sarrus 
  $$
  \\det(A) = abc + bfg + cdh - gec - hfa - idb
  \\tag{3.8}
  $$
* Menggunakan [Metode Kofaktor](https://byjus.com/maths/cofactor/) 
* Menggunakan Metode Gauss yang dimodifikasi

Lalu menggunakan rumus berikut
$$
A^{-1} = \frac{\text{adj}(A)}{\det(A)} \tag{3.9}
$$
Untuk matrix 4x4 keatas juga sama dengan 3x3
Pertama mencari determinan terlebih dahulu

* Menggunakan  [Metode Kofaktor](https://byjus.com/maths/cofactor/) 
* Menggunakan Metode Gauss yang dimodifikasi

Modifikasi Metode Gauss yang dimaksud adalah menggunakan bentuk $(3.2)$ dimana 
$$\det(A) = \prod\_{i=1}^nx\_{ii} \tag{3.10}$$
Dimana notasi $\Pi$ adalah bentuk notasi Sigma, namun untuk perkalian
Dan menggunakan rumus $(3.9)$ kembali
\>\[!note\]
\>Row echelon form (yang dimana kita membagi diagonalnya menjadi 1, dan juga diatasnya adalah 0) juga dinamakan Reduced Row Echelon form. 

## Dekomposisi LU

# Semua Matrix dengan determinan bukan 0 dapat didekomposisi menjadi LU yaitu $A = LU$ dimana
$$
\\begin{pmatrix}
a\_{11} & a\_{12} & a\_{13} & \cdots & a\_{1n} \\
a\_{21} & a\_{22} & a\_{23} & \cdots & a\_{2n} \\
a\_{31} & a\_{22} & a\_{33} & \cdots & a\_{3n} \\
\\vdots & \vdots & \vdots & \ddots & \vdots \\
a\_{n1} & a\_{n2} & a\_{n3} & \cdots & a\_{nn} \\
\\end{pmatrix}

\\begin{pmatrix}
1 & 0 & 0  & \cdots & 0\\
L\_{21} & 1 & 0  & \cdots & 0\\
L\_{31} & L\_{32} & 1  & \cdots & 0\\
\\vdots & \vdots & \vdots & \ddots & \vdots\\
L\_{n1} & L\_{n2} & L\_{n3} & \cdots & 1\\
\\end{pmatrix}
\\begin{pmatrix}
U\_{11} & U\_{12} & U\_{13} & \cdots & U\_{1n} \\
0 & U\_{22} & U\_{23} & \cdots & U\_{2n} \\
0 & 0 & U\_{33} & \cdots & U\_{3n} \\
\\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & U\_{nn} \\
\\end{pmatrix}
\\tag{3.11}
$$

Untuk mendapatkan $U$ digunakan metode [Gaussian Elimination](PERT%203.md#gaussian-elimination) secara biasa
$L$ dapat didapat dengan mengikuti proses [Gaussian Elimination](PERT%203.md#gaussian-elimination), dan ketika angka pada pivot (diagonal) sudah 1, maka dapat menyalin angka-angka dibawahnya untuk untuk barisan dalam $L$
Setelah $LU$ sudah tercapai, maka Lakukan Substitusi dalam bentuk $U\pmb{x} = \pmb{y}$  dan $L\pmb{y}=\pmb{b}$ 
$$
\\begin{align}
A\pmb{x} = \pmb{b} \\
L(U\pmb{x}) = \pmb{b} \\
L\pmb{y} = \pmb{b}\\
U\pmb{x} = \pmb{y}
\\end{align}
\\tag{3.12}
$$
Ingat $U\pmb{x}$ tinggal melakukan  substitusi saja, sehingga menjadi sangat mudah
