![Untitled.jpg](..\Software%20Engineering\Untitled.jpg)

Jawab :
Untuk Turunan Numerik, kita tinggal mencari  rumus rumus yang relevan berdasarkan metodenya dan juga $O(H)$ nya 
a. Hampiran selisih pusat, $O(H^2)$, $h=0.1$ 
$$
f'(x) = \frac{f_1-f\_{-1}}{2h}+ O(h^2)
$$
\>\[!note\] Ingat
\>$f\_{\pm i} = f(x \pm ih)$
\>Contoh
\>$f_3 = f(x+3h)$
\>$f\_{-2} = f(x-2h)$
\>$f_0 = f(x)$

kita tinggal masukkan saja angka2nya berdasarkan tabel ke rumus. Masukkan nilai $h$ dan juga $x$ kedalam rumus

$$
\\begin{align}
f'(x) = \frac{f(x+h)-f(x-h)}{2h}\\
f'(x) = \frac{(e^{-0.4 + 0.1} -2) -(e^{-0.4 - 0.1} -2) }{2(0.1)}\\
f'(x) = \frac{(e^{-0.3} -2) -(e^{-0.5} -2) }{0.2}
\\end{align}
$$
Selesaikan dengan kalkulator
b. 
Hampiran selisih pusat, $O(H^2)$, $h=0.2$ 
Hampir sama dengan cara diatas, hanya saja $h = 0.2$
$$
\\begin{align}
f'(x) = \frac{f(x+h)-f(x-h)}{2h}\\
f'(x) = \frac{(e^{-0.4 + 0.2} -2) -(e^{-0.4 - 0.2} -2) }{2(0.1)}\\
f'(x) = \frac{(e^{-0.2} -2) -(e^{-0.6} -2) }{0.2}
\\end{align}
$$
Selesaikan dengan kalkulator
c. 
Bandingkan jawaban (a) dan (b) dengan nilai yang tertera pada soal

![Untitled 1.jpg](..\Software%20Engineering\Untitled%201.jpg)
Kasus NIM Ganjil
$a = 4, h = \frac{4}{8} \rightarrow h = \frac{1}{2}$ maka soal tersebut menjadi
$$
\\int_0^4x^2+8x
$$
Metode Trapesium =
$$
\\int_a^bf(x) = \frac{h}{2}(f(a) + 2\sum f(x_i) +f(b))
$$
yang menjadi
$$
\\int_0^4f(x) = \frac{1}{4}(f(0) + 2\sum^{n-1}\_{i=1} f(x_i) +f(4))
$$

 > 
 > \[!note\] Ingat
 > $$
 > \\begin{align}
 > h = \frac{b-a}{n}\\
 > x_i = a+ih\\
 > x\_{i+1} = h + x_i
 > \\end{align}
 > $$

Karena kita telah mengetahui nilai dari $h$, oleh karena itu, kita tinggal menghitung $x_r$ 

|$i$|$x_i$|$f(x_i)$|
|---|-----|--------|
|0|0|0|
|1|0.5|4,25|
|2|1|9|
|3|1,5|14,25|
|4|2|20|
|5|2,5|26,25|
|6|3|33|
|7|3,5|40,25|
|8|4|48|
|Dan kita jumlahkan semuanya berdasarkan metode Trapesium menjadi|||
|$$|||
|\\frac{h}{2} (0 + 2\*( 4,25+9+14,25 + 20 +26,25 + 33 + 40,25) + 48) = \frac{195h}{2}  = 48,75|||
|$$|||
|\>\[!question\] Tugas|||
|\>Kerjakan untuk versi NIM Genap|||

![Untitled 2.jpg](..\Software%20Engineering\Untitled%202.jpg)
Ingat, Deret Taylor Orde ke 2 berupa berikut
$$
f(x) = f(x_0) + \frac{(x- x\_{0})}{1!}f^{'}(x\_{0}) + \frac{(x- x\_{0})^{2}}{2!}f^{''}(x\_{0})
$$
Maka kita perlu menurunkan $\frac{dy}{dx}$ sebanyak **2 kali**, seperti berikut
$$
\\begin{align}
f(x) = \hbox{y} \tag{1}\\
f' = \frac{dy}{dx} = 2x^2-y \tag{2}\\
f'' = \frac{d^2y}{dx^2}= 4x-\frac{dy}{dx}\\
f'' = 4x-2x^2+y\tag{3}
\\end{align}
$$

 > 
 > \[!note\]
 > $\frac{dy}{dx}$ adalah cara untuk menggambarkan persamaan differensial pada soal, yang berarti turunan pertama

Kemudian kita substitusikan $(1),(2),(3)$ ke dalam Deret Taylor, dimana berdasarkan yang diketahui $y(0) = 1$ , dapat diketahui bahwa $x_0 =0$  
$$
f(x) = y(0) + hf'(0) + \frac{h^2}{2!}f''(0)
$$
Kemudian dapat disederhanakan dengan $h=1$ lagi menjadi
$$
f(x) = y(0) + f'(0) + \frac{1}{2}f''(0)
$$
Kita mulai lakukan substitusi, Metode Deret Taylor membuat kita dapat mengetahui nilai $x_i$ dengan hasil dari bentuk deret taylor.

Iterasi Pertama

$$
\\begin{align}
y(1) = y(0) + f'(0) + \frac{1}{2}f''(0)\\
y(1) = y(0) + (2*0^2 + y(0)) + \frac{(4(0) - 2(0)^2 +y(0))}{2}\\
y(1) = 1 + (0 + 1) + \frac{0-0+1}{2}\\
y(1) = \frac{5}{2}
\\end{align}
$$
Iterasi Kedua
$$
\\begin{align}
y(2) = y(1) + f'(1) + \frac{1}{2}f''(1)\\
y(2) = y(1) + (2*1^2 + y(1)) + \frac{(4(1) - 2(1)^2 +y(1))}{2}\\
y(2) = \frac{5}{2} + (2 + \frac{5}{2}) + \frac{4-4+\frac{5}{2}}{2}\\
y(2) = \frac{33}{4}
\\end{align}
$$

Iterasi Ketiga
$$
\\begin{align}
y(3) = y(2) + f'(2) + \frac{1}{2}f''(2)\\
y(3) = y(2) + (2\*2^2 + y(2)) + \frac{(4(2) - 2(2)^2 +y(2))}{2}\\
y(3) = \frac{33}{4} + (8 + \frac{33}{4}) + \frac{8-8+\frac{33}{4}}{2}\\
y(3) = \frac{33}{2}+ \frac{33}{8} = \frac{165}{8}
\\end{align}
$$
Maka kita menemukan nilai $y(3) = \frac{165}{8}$

 > 
 > \[!question\] Tugas
 > Verifikasi Jawaban Ini

## Extras

![Pasted image 20240112183603.png](..\Software%20Engineering\Pasted%20image%2020240112183603.png)
![Pasted image 20240112183633.png](..\Software%20Engineering\Pasted%20image%2020240112183633.png)
![Pasted image 20240112183714.png](..\Software%20Engineering\Pasted%20image%2020240112183714.png)

Metode Simpson 1/3 memiliki versi yang mirip sekali dengan versi trapesium, namun dengan

* koefisien 4 untuk suku ganjil 
* koefisien 2 untuk suku genap
* Kecuali untuk suku pertama dan terakhir
  dan koefisien $h/2$ diganti dengan $h/3$

Metode Euler 
![Pasted image 20240112184403.png](..\Software%20Engineering\Pasted%20image%2020240112184403.png)
