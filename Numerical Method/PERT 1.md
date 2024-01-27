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
 > **INGAT: HANYA [DERET TAYLOR TERPOTONG](PERT%201.md#0c74e8) YANG MEMBUTUHKAN $R\_{n}(x)$ DALAM BENTUK PERSAMAAN (5) DERET TAYLOR BIASA TIDAK MEMBUTUHKANNYA** 

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
