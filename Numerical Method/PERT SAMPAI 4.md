\#galat #deret-taylor #floating-point

# PERT1 DERET TAYLOR

## Deret Taylor

Taylor series adalah deret yang dapat digunakan untuk memperkirakan terhadap suatu fungsi analitis dalam interval $\[a,b\]$

Rumus Taylor Series (Derajat $n$):

$$ f(x) \approx f(x\_{0}) + \frac{(x- x\_{0})}{1!}f^{'}(x\_{0}) + \frac{(x- x\_{0})^{2}}{2!}f^{''}(x\_{0}) + ...  + \frac{(x- x\_{0})^{n}}{n!}f^{n}(x\_{0}) \tag{1.1}$$

Atau secara sederhana dalam notasi sigma:
$$f(x) \approx \sum\_{i=0}^{n}\frac{f^{(i)}(x\_{0})(x-x\_{0})^{i}}{i!} \tag{1.2}$$

Untuk Deret Taylor penuh (Ingat tanda sama dengannya) :
$$f(x) = \sum\_{i=0}^{\infty}\frac{f^{(i)}(x\_{0})(x-x\_{0})^{i}}{i!} \tag{1.3}$$
infinite sum dari semua deret taylor 

 > 
 > \[!note\]
 > Deret Taylor dengan $x_0 = 0$ dinamakan **Deret Maclaurin**, Digunakan pada metode [Newton Raphson](PERT%202.md#metode-newton-raphson) 

Deret Maclaurin memiliki rumus berikut
$$
f(x) \approx f(0) + \frac{x}{1!}f^{'}(0) + \frac{x^{2}}{2!}f^{''}(0) + ...  + \frac{x^{n}}{n!}f^{n}(0) \tag{1.1.1}
$$
Dan notasi sigmanya adalah :
$$
f(x) = \sum\_{i=0}^{\infty}\frac{x^{i}}{i!}f^{(i)}(0) \tag{1.3}
$$

Karena secara praktis tidak dapat menghitung deret taylor secara tak hingga, maka kita menghitung deret Taylor terpotong yang berupa:
$$f(x) =P\_{n}(x) + R\_{n}(x) \tag{1.4}$$
dimana $P\_{n}(x)$ adalah deret taylor derajat $n$ dan $R\_{n}(x)$ adalah berikut: 
$$ R\_{n}(x) = \frac{(x-x\_{0})^{(n+1)}}{(n+1)!}f^{(n+1)}(c) \tag{1.5}$$
dimana $x\_{0} \< c \< x$ 
\>\[!note\]
\>Jika kita perhatikan, $R_n$ nyaris sama persis dengan suku ke $n+1$ dalam Deret Taylor. Hanya saja $x_0$ diganti dengan $c$ yang merupakan nilai diantara $x_0$ dan $x$

### Order Approximation

Tetapi umumnya dalam literatur $R\_{n}(x)$ tidak dihitung namun disimbolkan dengan tingkat ketelitian simbol Big O yaitu $O(h^{n})$ dimana $n$ adalah orde deret Taylor sehingga :
$$f(x) =P\_{n}(x) + O(h^{n}) \tag{1.6}$$

Deret Taylor digunakan oleh komputer agar dapat memperkirakan fungsi fungsi yang seperti $sin(x)$, $cos(x)$, $e^{x}$, $ln(x)$, $tanh(x)$, dsb hanya dengan menggunakan `+ -  * \`

Dalam Python, ada library yang bernama `sympy` yang dapat digunakan untuk menghitung deret Taylor terpotong

Implementasi rumus taylor series dalam `sympy`

Note : Sematkan `import sympy` terlebih dahulu 

````python
def taylorEq(f,x0,upperBound,symbol=x):
	taylorSeries = 0
	for i in range(0,upperBound+1):
		fdiff = sympy.diff(f,symbol,i).subs(symbol,x0)
		taylorFrac = (symbol-x0)**i/sympy.factorial(i)
		taylorSeries += fdiff*taylorFrac
	return taylorSeries
````

Fungsi ini mengaplikasikan rumus Taylor series dan menghitung deret Taylor terpotong. `f` sebagai fungsi, `x0` sebagai $x\_{0}$, `upperBound` sebagai derajat Deret Taylor, dan `symbol` sebagai variabel yang akan diturunkan, jika multi-variabel, atau tidak menggunakan variabel $x$

 > 
 > \[!warning\]
 > **INGAT: HANYA [DERET TAYLOR TERPOTONG](PERT%20SAMPAI%204.md#0c74e8) YANG MEMBUTUHKAN $R\_{n}(x)$ DALAM BENTUK PERSAMAAN (5) DERET TAYLOR BIASA TIDAK MEMBUTUHKANNYA** 

## Analisis Error dan Sumber Utama Error

Error adalah kemelencengan akan nilai yang diperkirakan dengan nilai sejati. Error disimbolkan dengan $\epsilon$

$$\epsilon = \alpha - \hat{\alpha} \tag{1.7}$$

Error relatif adalah $\epsilon\_{r} = {\epsilon}/{\alpha}$ dan error relatif hampiran adalah $\epsilon\_{ra} = {\epsilon}/{\hat{\alpha}}$. $\epsilon\_{ra}$ digunakan agar dapat menentukan apakah error cukup kecil (dibawah nilai toleransi) agar dapat digunakan dalam penghitungan.

Error relatif juga dapat dihitung dengan cara berikut :
$$\epsilon\_{ra} =\left| \frac{x\_{r+1}-x\_{r}}{x\_{r+1}} \right| \tag{1.8}$$
\>\[!note\]
\>Error relatif $e\_{ra}$ sering digunakan dalam perhitungan error dalam metode [Newton Raphson](PERT%202.md#metode-newton-raphson), Metode bagi dua (bisection), dsb

Error pemotongan maximum adalah error terbesar yang akan diberikan oleh deret Taylor pada nilai yang di input kepada deret Taylor tersebut

$$R_n(x) = \frac{f^{n+1}(x)}{(n+1)!}(x-a)^{n+1} \tag{1.9}$$

dimana $a = x_0$ pada sesuai dengan Persamaan (1.1),(1.2), maupun (1.3)

Error pembulatan adalah error yang terjadi karena suatu nilai dibulatkan. Nilai terbesar error pembulatan adalah $10^{-(nilai,presisi)}$

Angka penting adalah angka yang dianggap relevan dalam suatu nilai. Angka penting memiliki perhitungan sebagai berikut

* Angka selain 0 adalah angka penting Contoh : **123**
* Angka 0 diantara angka selain 0 adalah angka penting Contoh : 1**0**2
* Angka 0 yang berada disebelah kiri (trailing zeroes) adalah angka penting Contoh : 12300 dan 12,34**00**
* Angka 0 yang berada disebelah kanan (leading zeroes) **bukan** angka penting Contoh : ~~000~~134 dan ~~0.00~~234

## Floating Point Numbers

Komputer menyimpan bilangan desimal dengan format floating point, yang dimana merupakan suatu representasi notasi saintifik dalam bilangan biner. Format dari bilangan floating point adalah

$$a = \pm mB^p = \pm 0.d_1d_2d_3d_4\cdots d_n \cdot B^n \tag{1.10}$$
dimana n merupakan tingkat presisi dari standar floating point (IEEE 754 maupun format lainnya) dan $B$ adalah basis dari angka floating point yang hampir selalu $2$ 

Contoh floating point format dengan tipedata C (berlaku untuk mayoritas bahasa pemograman dengan arsitektur x86 maupun ARM)

* `float` memiliki nilai $p = 24$ dan $n = 8$
* `double` memiliki nilai $p = 53$ dan $n = 11$
* `long double` memiliki nilai $p = 64$ dan $n = 15$

# PERT 1-2 Perambatan Error

## Error Floating Point

Misal $a$ dan $b$ adalah suatu nilai yang direpresentasikan dalam floating point sebagai $\hat{a}$ dan $\hat{b}$ . Maka hubungan antara nilai dan bentuk floating pointnya dapat digambarkan sebagai berikut

$$\begin{flalign}
&a = \hat{a} + \epsilon_a \tag{1}\\
&b = \hat{b} + \epsilon_b \tag{2}\\
&a+b = \hat{a} + \hat{b} + \epsilon_a + \epsilon_b \tag{3}\\
&\sum\_{i=1}^{n} a_i = \sum\_{i=1}^n \hat{a_i} + \sum\_{i=1}^n \epsilon_i \tag{4}
\\end{flalign}
$$
dimana $\epsilon_a$ dan $\epsilon_b$ adalah error floating point untuk $a$ dan $b$ 

### Kondisi Buruk

Suatu persoalan metode numerik berkondisi buruk jika perubahan data yang kecil akan merubah jawaban secara drastis (butterfly effect). Contohnya pada teori chaos, sistem dinamis, dan polinom nonlinear

## Metode Pencarian Akar

Ada 2 metode pencarian akar yaitu

* Metode Tertutup (Bracketing Method)
* Metode Terbuka (Bisection Method) dan Regula falsi

Bracketing method bergantung akan produk antara suatu fungsi antara 2 interval, jika $f(a)f(b) \< 0$ maka **pasti** ada 1 atau lebih akar dalam interval fungsi tersebut, tetapi ada kemungkinan jika $f(a)f(b) > 0$ maka **masih ada** akar yang ada dalam interval tersebut

Metode bisection menggunakan teknik bracketing method, namun berdasarkan nilai terhadap $f(a)f(c)$, dengan $c$ adalah titik tengah maka prosedur tersebut kembali dijalankan secara rekursif

````python
#TODO proteksi infinite loop
def bisectionIterative(func, leftGuess, rightGuess, errorTreshold)
    mid = (leftGuess+rightGuess)/2
    leftBound = func(leftGuess)
    rightBound = func(rightGuess)
    if leftBound > 0 and rightBound > 0 \
    or leftBound < 0 and rightBound < 0 :
        return 
    else:
        while math.fabs(func(mid)) > errorTreshold:
            mid = (leftGuess + rightGuess)/2
            if func(mid) * func(leftGuess) < 0:
                rightGuess = mid
            else:
                leftGuess = mid
        return mid
````

### Metode *Regular falsi*

Metode ini hampir identik dengan metode bisection, namun dengan perbedaan mencolok dalam perhitungan titik tengahnya yaitu
$$c = \frac{af(b) - bf(a)}{f(b)-f(a)} \tag{5}$$
Dalam Python maka perbedaannya hanya pada perhitungan `mid` yang menggunakan persamaan (5) sebagai berikut

````python
def regularFalsiMid(func,leftGuess,rightGuess):
	return (a*func(b) - b*func(a))/ (func(b) - func(a))
````

dan diaplikasikan pada `bisectionIterative` sebagai berikut

````python
mid = regularFalsiMid(func,leftGuess,rightGuess)
````

\#galat #root-finding

## Metode Leleran (Iterasi)

Misalkan ada suatu polinom $P(x)$ dengan bentuk umum:
$$P(x) = a_0x^n + a_1x^{n-1} + a_2x^{n-2} + \cdots + a\_{n-1}x + a_n \tag{2.1}$$
Maka cara memperhitungkan akar $P(x)$ secara iteratif dapat dilakukan sebagai berikut :
$$x_i = g(x\_{i-1}) \tag{2.2} $$
dimana 
$$\begin{align}
&P(x) = 0 \\
&a_0x^n + a_1x^{n-1} + a_2x^{n-2} + \cdots + a\_{n-1}x + a_n = 0 \tag{dari 2.1} \\
&a_0x^n = -(a_1x^{n-1} + a_2x^{n-2} + \cdots + a\_{n-1}x + a_n) \\
&x^n = \frac{-(a_1x^{n-1} + a_2x^{n-2} + \cdots + a\_{n-1}x + a_n)}{a_0} \\
&x = \sqrt\[n\]{\frac{-(a_1x^{n-1} + a_2x^{n-2} + \cdots + a\_{n-1}x + a_n)}{a_0}} \tag{2.3}
\\end{align}$$
Persamaan (2.3) adalah bentuk umum dan penuh dari Persamaan (2.2)
Perhitungan ini dilakukan secara rekursif sampai nilai error lebih kecil dari yang ditentukan berdasarkan [error maupun error relatif](PERT%201.md#analisis-error-dan-sumber-utama-error)
Note : 

* konvergen absolut adalah dimana nilai hampiran secara monoton mendekat nilai sejati
* konvergen berosiliasi adalah dimana nilai hampiran dapat naik turun dengan nilai amplitudo yang semakin mengecil menuju nilai sejati

## Metode Newton - Raphson

Misalkan sebuah garis singgung pada sebuah fungsi, dan kita ingin mengetahui akar dari garis singgung tersebut
$$\begin{align}
&f(x) + (x\_{i-1}-x_i)f'(x) = 0\\
&x_i - x\_{i-1} = -\frac{f(x_i)}{f'(x_i)} \\
& x_i = x\_{i-1}+ \frac{f(x_i)}{f'(x_i)} \tag{2.4}
\\end{align}$$
Untuk 2 variabel penurunannya cukup kompleks, dan rumusnya adalah
$$x\_{i+1} = x_i - \frac{p_iD_y(q_i) + q_iD_y(p_i)}{D_x(p_i)D_y(q_i) - D_y(p_i)D_x(q_i)} \tag{2.5.1} $$ dan
$$y\_{i+1} = y_i - \frac{p_iD_x(q_i) + q_iD_x(p_i)}{D_x(p_i)D_y(q_i) - D_y(p_i)D_x(q_i)} \tag{2.5.2} $$
dimana $D_x(f(x,y))$ adalah turunan $f(x,y)$ berdasarkan variabel $x$ atau $\frac{\partial f}{\partial x}$

### Orde Konvergensi

Menggunakan [deret Taylor derajat ke 2 ](PERT%201.md#deret-taylor) metode Orde Konvergensi dapat mencapai akar dari suatu fungsi dengan jauh lebih cepat. Bentuk Orde Konvergensi adalah sebagai berikut 
$$x\_{i+1} = x_r - \frac{f(x_i)(x_i-x\_{i-1})}{f(x_i) - f(x\_{i-1})} \tag{2.6} $$

### Metode Secant

Menghitung gradien dengan menghitung rasio antara $\Delta y$ dan $\Delta x$ karena, $\frac{\Delta y}{\Delta x}$ akan semakin mendekati $f'(x)$ pada nilai yang semakin kecil
Bentuk ini juga memiliki rumus akhir sama dengan [Persamaan (2.6)](PERT%20SAMPAI%204.md#orde-konvergensi)

## Akar Polinom

## Akar ganda

Terjadi ketika fungsi menyinggung sumbu x, dan ketika difaktorisasi, tampak memiliki lebih dari satu $(x-a)$ 

### Metode Horner

````
t
	| an an-1 an-2 --- a1 a0
	|    bn   bn-1 --- b2 b1
	========================
	  an an-1+bn an-2+bn-1 a1+b2 a0+b1
````

Catatan : Ketika $a_0 + b_1 = 0$ maka $(x-t)$ adalah akar dari polinom tersebut, jika tidak maka $a_0+b_1 = P(t)$

### Mencari perkiraan akar terbesar dan terkecil

Untuk akar terbesar dari $P(x)$ adalah :
$$\frac{- \text{ koefisien untuk suku kedua}}{\text{korefisien untuk suku pertama}}  $$
Sedangkan akar terkecil adalah :
$$\frac{-\text{ koefisien untuk suku sebelum suku terakhir}}{\text{koefisien untuk suku terakhir}}$$

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
 > $\text{rank}(A\_{nn})$ ditentukan dengan mencari bentuk [Row Echelon Form](PERT%20SAMPAI%204.md#gaussian-elimination), dan menghitung jumlah baris yang tidak seluruhnya 0

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

Untuk mendapatkan $U$ digunakan metode [Gaussian Elimination](PERT%20SAMPAI%204.md#gaussian-elimination) secara biasa
$L$ dapat didapat dengan mengikuti proses [Gaussian Elimination](PERT%20SAMPAI%204.md#gaussian-elimination), dan ketika angka pada pivot (diagonal) sudah 1, maka dapat menyalin angka-angka dibawahnya untuk untuk barisan dalam $L$
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

# PERT 4

# Regresi

Regresi adalah analisis antara hubungan antara variabel, apakah berkorelasi atau tidak, dan juga mempresiksi nilai sebuah fungsi matematika berdasarkan nilai-nilai sebelumnya.

Regresi banyak digunakan pada Machine Learning dan AI, karena prediksi berdasarkan dataset adalah **hakikat** dari "kecerdasan" pada AI

Regresi juga digunakan untuk menggambarkan seberapa keterikatan suatu variabel dalam penelitian, apakah peningkatan $A$ akan menaikkan $B$ atau menurunkan $B$, **secara konsisten**

## Regresi Linier

$\hat{Y} = a+bx$ 

dimana 
$$
a = \frac{(\sum(y)-b(\sum(x))}{n} \tag{5.1}
$$
dan 
$$
b = \frac{n\sum(xy) - \sum(x)\sum(y)}{n\sum(x^2) - \sum(x)^2}  \tag{5.2}
$$
%% THANKX PAK CEVI!!!!!!!!!!! %%

## Pelinieran

Adalah proses untuk menggambarkan titik titik yang ada dalam dataset sebagai sebuah model linier (fungsi $\hat{Y}$)

Ada berbagai pendekatan dari fungsi nonlinier yang dapat membantu dalam pelinieran yaitu :
$$
\\begin{align}
y = Cx^b \tag{5.3.1}\\ y = Ce^{bx} \tag{5.3.2} \\ y = \frac{Cx}{d+x} \tag{5.3.3}
\\end{align}
$$
Contoh Pelinieran dari $(5.3.1)$  adalah  berikut
$$
\\begin{align}
&y = Cx^b \\
&\ln(y) = \ln(C) + b\ln(x) \\
&Y = \ln(x), a = \ln(C), X = \ln(x) \\
&\therefore Y = a + bX
\\end{align}
$$
Cara melakukannya adalah dengan mengubah titik titik $(x_i,y_i)$ menjadi $(\ln(x_i),\ln(y_i))$ dan hitung $a$ dan $b$ seperti teknik regresi linier, dan untuk memodelkannya kembali berdasar $(5.3.1)$ kita menggunakan hubungan $C = e^a$ sehingga $(5.3.1)$ berubah menjadi

$$ 
y = e^ax^b \tag{5.4}
$$
Cara menemukan $a$ dan $b$ adalah  untuk menyelesaikan SPL Matriks berikut

# $$
\\begin{bmatrix}
n & \sum x \\
\\sum x & \sum x^2
\\end{bmatrix}
\\begin{bmatrix}
a\\
b
\\end{bmatrix}

\\begin{bmatrix}
\\sum y\\
\\sum xy
\\end{bmatrix}
\\tag{5.5}
$$

# PERT 4

# Interpolasi

## Interpolasi Polinom

Diberikan suatu fungsi yang akan kita perkirakan yaitu $f(x)$, kita membuat suatu polinom dengan menggunakan sebuah himpunan dari $n+1$ titik yang berbentuk $(x_i,f(x_i))$ dimana $0\leq i \leq n+1$. Polinom yang dibuat dari himpunan titik tersebut akan mengaproksimasi dari fungsi $f(x)$ tersebut

 > 
 > \[!note\]
 > Interpolasi adalah dimana suatu nilai diperkirakan dengan fungsi lain, sedangkan ekstrapolasi adalah nilai yang direpresentasikan oleh fungsi yang melakukan interpolasi

## Interpolasi Linier

Interpolasi ini adalah bentuk khusus dari [Interpolasi Polinom](PERT%20SAMPAI%204.md#interpolasi-polinom) dimana $n = 1$ , dan membuat sebuah fungsi linier umum $p_1(x) = a_0+a_1x$. Kita dapat membayangkan fungsi ini sebagai fungsi generik yang menghasilkan sistem persamaan fungsi lainnya.

Kita dapat memodelkan fungsi yang diinterpolasi dengan $p(x)$ yaitu dengan :
$$
\\begin{cases}
y_0 = a_0 + a_1x_0\\
y_1 = a_0 + a_1x_1
\\end{cases}
$$
Menyelesaikan fungsi ini secara eliminasi menghasilkan
$$
a_0 = \frac{y_1-y_0}{x_1-x_0}, a_1 = \frac{x_1y_0 - x_0y_1}{x_1-x_0}
$$

## Interpolasi Kuadrat

Hampir sama dengan [Interpolasi Linier](PERT%20SAMPAI%204.md#interpolasi-linier) kecuali $n = 2$ sehingga $p_2(x) = a_0+a_1x + a_2x^2$, sehingga dapat dibuat SPLTV berikut:
$$
\\begin{cases}
y_0 = a_0 + a_1x_0 + a_2x_0^2\\
y_1 = a_0 + a_1x_1 + a_2x_1^2\\
y_2 = a_0 + a_1x_2 + a_2x_2^2
\\end{cases}
$$
Selesaikan dengan substitusi eliminasi, Gauss Jordan, Gauss, LU, dsb

## Interpolasi Kubik

Hampir sama dengan [Interpolasi Linier](PERT%20SAMPAI%204.md#interpolasi-linier) kecuali $n = 3$ sehingga $p_3(x) = a_0+a_1x + a_2x^2 + a_3x^3$, sehingga dapat dibuat SPL berikut:
$$
\\begin{cases}
y_0 = a_0 + a_1x_0 + a_2x_0^2 + a_3x_0^3\\
y_1 = a_0 + a_1x_1 + a_2x_1^2 + a_3x_1^3\\
y_2 = a_0 + a_1x_2 + a_2x_2^2 + a_3x_2^3\\
y_3 = a_0 + a_1x_3 + a_2x_3^2 + a_3x_3^3\\
\\end{cases}
$$
Selesaikan dengan substitusi eliminasi, Gauss Jordan, Gauss, LU, dsb

## Polinom Lagrange

Merupakan teknik lain untuk membuat polinom yang menginterpolasi $f(x)$
$$
P_n(x) = \sum^n\_{i=1} f(x_i)L_i(x)
$$
dimana $L_i(x)$ adalah.
$$
L_i(x) = \prod^n\_{\begin{align} j = 0 \\ j \neq i \end{align}} 
\\frac{x-x_j}{x_i-x_j}
$$
Kita dapat melihat $P_n(x)$ sebagai berikut
![Pasted image 20231103182512.png](..\Software%20Engineering\Pasted%20image%2020231103182512.png)
Contoh kasus untuk $n = 2$ adalah
![Pasted image 20231103182728.png](..\Software%20Engineering\Pasted%20image%2020231103182728.png)

 > 
 > \[!note\]
 > Tampak pada contoh diatas, tidak ada suku dimana $x_i = x_j$ untuk menghindari pembagian dengan 0

 > 
 > \[!info\]
 > $\prod$ sama saja dengan $\sum$ namun menggunakan perkalian
