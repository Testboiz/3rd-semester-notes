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
