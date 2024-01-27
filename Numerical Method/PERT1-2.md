# PERT 2 Perambatan Error

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
