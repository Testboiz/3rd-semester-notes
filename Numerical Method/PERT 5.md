# PERT 5 - Turunan Numerik

## Pendekatan Menghitung Turunan Numerik

Turunan numerik digunakan agar komputer dapat memperkirakan nilai turunan dengan menggunakan sistem diskret bit.

Turunan ini digunakan dalam komputer grafis, fotogrametri,  dan citra digital

Turunan numerik dicari dengan menghitung langsung rumus turunan tanpa limit
$$
f'(x_0) = \frac{f(x_0+h)-f(x_0)}{h} \tag{5.1}
$$
dimana $h$ ditentukan berdasarkan seberapa presisi kita ingin menghitung turunannya

Pendekatannya adalah berikut
Misal $f(x_0-h) = f_1$ dan $f(x_0) = f_0$. Maka ada 3 pendekatan yaitu

1. Hampiran selisih maju yaitu 
   $$
   f'(x_0) = \frac{f(x_0+h)-f(x_0)}{h} \tag{5.2}
   $$
1. Hampiran selisih mundur yaitu 
   $$
   f'(x_0) = \frac{f(x_0)-f(x_0-h)}{h} \tag{5.3}
   $$
1. Hampiran selisih pusat yaitu  
   $$
   f'(x_0) = \frac{f(x_0+h)-f(x_0-h)}{2h} \tag{5.4}
   $$

## Turunan Numerik Dengan Deret Taylor

Dengan kumpulan titik-titik fungsi yang ada, gunakan 3 hampiran yang sudah ada untuk menghitung nilai turunan, dengan catatan, $f_i = f(x_i)$

1. Hampiran selisih maju yaitu $\frac{f\_{i+1}-f_1}{h}$ 
1. Hampiran selisih mundur yaitu  $\frac{f_1-f\_{i-1}}{h}$ 
1. Hampiran selisih pusat yaitu  $\frac{f\_{i+1}-f\_{i-1}}{2h}$ 

Untuk turunan kedua, rumusnya sedikit berbeda %%why?%%

1. Hampiran selisih maju yaitu $\frac{f\_{i+2} - 2f\_{i+1}-f_i}{h^2}$ 
1. Hampiran selisih mundur yaitu  $\frac{f\_{i-2}-2f\_{i-1}+f_i}{h^2}$ 
1. Hampiran selisih pusat yaitu  $\frac{f\_{i+1}-2f_i+f\_{i-1}}{h^2}$ 

## Turunan Numerik Dengan Polinom Interpolasi

%% mtk hapal mati %%
Merupakan generalisasi dari hampiran sebelumnya
Gunakan metode ini untuk menghitung turunan derajat ke $n$ secara numerik dengan 2 pendekatan

1. Hampiran selisih maju
   $$
   \\begin{align}
   f''(x) = f^{(2)}(x) = \frac{f'(x+h)-f'(x)}{h}\\
   = \frac{\frac{f(x+h+h)-f(x+h)}{h} -\frac{f(x+h)+f(x)}{h}}{h}\\
   = \frac{f(x+2h)-2f(x+h)+f(x)}{h^2}\\
   = \frac{\frac{f(x+3h)-f(x+2h)}{h}-2(\frac{f(x+2h)-f(x+h)}{h})+\frac{f(x+h)-f(x)}{h}} {h^2} \\
   = \frac{f(x+3h)-f(x+2h)-2f(x+2h) + 2f(x+h)+f(x+h)-f(x)}{h^3} \\
   = \frac{f(x+3h)-3f(x+2h)+3f(x+h)-f(x) }{h^2} \\
   f^{(i)}(x)= \frac{1}{h^i}\sum^n\_{i=0}(-1)^{n-i}{n \choose i}f(x+ih) \tag{5.5}
   \\end{align}
   $$

1. Hampiran selisih mundur
   Melakukan penurunan seperti pada persamaan $(5.4)$ menghasilkan rumus berikut
   $$
   f^{(i)}(x) = \frac{1}{h^i}\sum^n\_{i=0}(-1)^i{n \choose i}f(x-ih) 
   \\tag{5.5}
   $$

1. Hampiran selisih pusat
   Melakukan penurunan seperti pada persamaan $(5.4)$ menghasilkan rumus berikut

$$
f^{(i)}(x) = \frac{1}{h^i}\sum^n\_{i=0}(-1)^i{n \choose i}f\left(x+(\frac{n}{2}-i)h\right)  \tag{5.6}
$$
Orde error dari turunan tersebut adalah berikut, dengan $i$ adalah ordo turunan

1. Selisih maju = $O(h)$
1. Selisih mundur = $O(h)$
1. Selisih pusat = $O(h^2)$ 

Perhitungannya dilakukan dengan perhitungan taylor dari tiap fungsi dari hampiran selisih selisih tersebut. Illustrasi yang memudahkan perhitungan tersebut tersedia [disini](https://math.stackexchange.com/a/3385554)
![Pasted image 20231124161044.png](..\Software%20Engineering\Pasted%20image%2020231124161044.png)

## Ekstrapolasi Richardson

Misal $D(h)=f'(x_0)$ dengan hampiran sebesar $h$, dan $D(2h)$ untuk hampiran sebesar $2h$. Gunakan Ekstrapolasi Richardson untuk meningkatkan presisinya 
$$
\\begin{align}
D(h) = \frac{f(x+h)-f(x-h)}{2h}\\
D(2h) = \frac{f(x+2h)-f(x-2h)}{4h}
\\end{align}
$$
$$
f'\_0 = D(h) + \frac{D(h) - D(2h)}{2^n-1} \tag{5.7}
$$
