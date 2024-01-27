# PERT 6 - Intergrasi Numerik

## Metode Pias

 > 
 > \[!abstract\] Definisi
 > Integrasi numerik adalah cara untuk menghitung integral tentu dari suatu fungsi secara approksimasi numerik 
 > $$
 > \\int_a^bf(x)dx
 > $$

Metode Pias adalah cara untuk mengintegrasi sebuah fungsi menggunakan teknik seperti

1. Kaidah segiempat (Riemann sum/Rectangle rule)
1. Kaidah trapesium (Trapezoidal rule)
1. Kaidah Titik Tengah (Midpoint rule)
   Komponen-komponen ini akan menjadi komponen penting dalam perhitungan integrasi numerik

$$
\\begin{align}
h = \frac{b-a}{n}\\
x_r = a+rh\\
f_r = f(x_r)
\\end{align}
$$

## Kaidah Segiempat, Trapesium dan Titik Tengah

Kaidah Segiempat
$$
\\int_a^bf(x)dx = h\sum\_{i=1}^n f_i
$$
Kaidah Trapesium
$$
\\int_a^bf(x)dx = \frac{h(f_0+2\sum\_{i=1}^{n-1}f_i+f_n)}{2}
$$
Kaidah Titik tengah
$$
\\int_a^bf(x)dx = h\sum^{n-1}*{i=0}f*{\frac{i+1}{2}}
$$

## Error Metode Pias

Error dapat digambarkan sebagai jumlah luas sisa yang ada pada perhitungan. Semakin banyak pias, semakin kecil errornya, dan akan konvergen ke $F(b)-F(a)$ (FTC 2)

Notasi error dari Metode Pias adalah $O(n^2)$, berdasarkan perhitungan deret taylornya

## Metode Newton Cotes

Gunakan [Interpolasi Polinom](PERT%204-2.md#interpolasi-polinom), untuk mengapproksimasikan sebuah integral dari suatu fungsi non polinom dari $f(x)$, Ini bahkan dapat digunakan untuk fungsi yang tidak memiliki antiderivatif elementer.

$$
I = \int_a^bf(x)dx \approx \int_a^bP\_ n(x)dx
$$

## Kaidah Simpson 1/3

Adalah kaidah untuk mengintegrasi sebuah fungsi secara numerik dengan pendekatan sebuah polinom interpolasi (Newton Gregory Polynomial)

Kemudian dengan fungsi yang terinterpolasi, kita integralkan fungsi tersebut.

Kaidah Simpson 1/3 adalah bentuk khusus dari Metode Newton Cotes

Rumusnya adalah
$$
\\int_a^b f(x) dx \approx \frac{h}{3}\left(f_0 + 4 \left( \sum^{n-1}*{i = 1,3,\cdots} f_i \right) + 2 \left(\sum^{n-2}*{i = 2,4,\cdots}f_i \right) + f_n\right)
$$

## Kaidah Simpson 3/8

Menggunakan polinom interpolasi Newton Gregory derajat lebih tinggi untuk menghasilkan rumus yang lebih presisi

Rumusnya adalah
$$
\\int_a^b f(x) dx \approx \frac{3h}{8} \left(f_0 +2\left( \sum^{n-1}*{i = 3,6,\cdots} f_i \right) + 3\left( \sum^{n-1}*{i \ne 3,6,\cdots} f_i \right) + f_n \right)
$$

## Singularitas

Jika sebuah fungsi memiliki nilai $\frac10$ pada selang integral tersebut, gunakan integrasi substitusi untuk menghilangkan titik $\frac10$ tersebut

## Penggunaan Ekstrapolasi untuk Integrasi

Menggunakan Extrapolasi Richardson yang ada dalam Turunan Numerik, kita juga dapat mengaplikasikannya dalam integral, untuk meningkatkan akurasi dari perhitungannya

## Integral Ganda

Integrasi ganda adalah integral tentu yang ganda pada fungsi multivariabel. Contohnya adalah
$$
\\int\int f(x,y)dxdy = \int_a^b\int_c^df(x,y) dxdy
$$
Pada Integrasi ganda, penghitungannya secara numerik adalah untuk menghitung integral dalamnya terlebih dahulu, lalu menghitung integral luarnya
$$
\\int_a^b\int_c^df(x,y) dxdy = \int_a^b Fdy
$$
dimana $F = \int_c^df(x,y) dx$

Hitunglah integrasi $F$ terlebih dahulu secara numerik, lalu lakukan integral luarnya.

Jika diberikan tabel nilai dari fungsi tersebut, gunakan nilai-nilai dari fungsi tersebut mengikuti kaidah kaidah integrasi yang telah diketahui dengan menjumlahkan **kolom kiri ke kolom kanan**

|1|2|3|4|
|-|-|-|-|
|1st|2nd|3rd|4th|
|1st|2nd|3rd|4th|
|1st|2nd|3rd|4th|
|1st|2nd|3rd|4th|

Pada intinya integral ganda numerik dapat digambarkan sebagai berikut
$$
\\int_a^b\int_c^df(x,y) dxdy = \sum\_{i=0}^n \int_c^df(x,y_i)dx
$$

Integrasi dimensi lebih tinggi dapat dilakukan dengan pengulangan kaidah yang sama

## Kuadrat Gauss

Kuadrat Gauss adalah cara untuk mengkonversikan sebuah integral tentu biasa menjadi berikut
$$
\\int_a^b f(x)dx = \int_i^if(x) dx
$$
Hal ini dilakukan agar dapat mengurangi error dari perhitungan. 

## CHEATSHEET

1. Kaidah Segiempat

$$
h\sum f_i
$$
jumlah tengah
2. Kaidah Trapesium
$$
\\frac{h}{2}(f_0 +\sum f_i+ f_n)
$$
kiri + 2 * tengah + kanan

3. Kaidah Titik Tengah
   $$
   h\sum f\_{i/2}
   $$
   Hampir sama dengan kaidah segiempat, hanya saja offsetnya berbeda

3. Newton Cotes
   $$
   \\int_b^a f(x) dx = \int_a^b P(x) dx
   $$
   dimana $P(x)$ adalah polinom interpolasi,

Gunakan ini sebagai step intremediet untuk mempermudah perhitungan dengan kaidah kaidah lainnya
5. Kaidah Simpson 1/3
$$
\\frac{h}{3}(f_0 +4\sum f\_{\text{ganjil}} + 2\sum f\_{\text{genap}}+ f_n)
$$
6. Kaidah Simpson 3/8
$$
\\frac{h}{3}(f_0 +2\sum f\_{\text{kelipatan 3}} + 3\sum f\_{\text{bukan kelipatan 3}}+ f_n)
$$
