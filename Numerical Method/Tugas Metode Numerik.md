1. Diketahui :

* a. $f(x) = e^{2x}$
* b. $f(x) =\ln(x-1)$
  Ditanya :
  Deret Taylor ordo ke 4
  Jawab :
  Rumus Deret Taylor Ordo ke 4 adalah: 
  $$
  f(x) = \sum^4\_{i=1} \frac{f^{(i)}(a)(x-a)^i}{i!} 
  $$
  atau
  $$
  f(x) = f(x_0) + \frac{(x- x\_{0})}{1!}f^{'}(x\_{0}) + \frac{(x- x\_{0})^{2}}{2!}f^{''}(x\_{0}) + \frac{(x- x\_{0})^{3}}{3!}f^{'''}(x\_{0}) + \frac{(x- x\_{0})^{4}}{4!}f^{''''}(x\_{0})
  $$
  a. Berikut adalah nilai turunan dari $f(x)$
  $$\begin{align}
  f(x) = e^{2x} \\
  f'(x) = 2e^{2x} \\
  f''(x) = 4e^{2x} \\
  f'''(x) = 8e^{2x} \\
  f''''(x) = 16e^{2x}
  \\end{align}
  $$
  (untuk $x_0=0$), maka kita dapat melakukan penyederhanaan berikut :
  $$
  \\begin{align}
  (x-x_0) = (x-0) = x \tag{1.1}\\
  e^{2(0)} = e^{0} = 1 \tag{1.2}
  \\end{align}
  $$
  Deret Taylor dapat dibuat dengan cara berikut dengan menggunakan bantuan rumus $(1.1)$ dan $(1.2)$:
  $$
  \\begin{align}
  &(1) = f(x_0) = e^0 \Rightarrow 1 \\
  &(2) = \frac{(x- x\_{0})}{1!}f^{'}(x\_{0}) \Rightarrow 2x \\
  &(3) = \frac{(x- x\_{0})^{2}}{2!}f^{''}(x\_{0}) = \frac{x^2}{2}(4) \Rightarrow 2x^2 \\
  &(4) = \frac{(x- x\_{0})^{3}}{3!}f^{'''}(x\_{0}) = \frac{x^3}{6}(8) \Rightarrow \frac{4x^3}{3}  \\
  &(5) = \frac{(x- x\_{0})^{4}}{4!}f^{''''}(x\_{0}) = \frac{x^4}{24}(16) \Rightarrow \frac{2x^4}{3} \\
  \\end{align}
  $$
  Sehingga menjadi seperti berikut
  $$
  1 + 2 x + 2 x^{2} + \frac{4 x^{3}}{3} + \frac{2 x^{4}}{3} \tag{1.3}
  $$

b. Berikut adalah nilai turunan dari $f(x)$
$$\begin{align}
&f(x)=\ln{\left(x-1 \right)} \\
&f'(x) = \frac{1}{x-1} \\
&f''(x) = - \frac{1}{\left(x-1\right)^{2}} \\
&f'''(x)=\frac{2}{\left(x-1\right)^{3}} \\
&f''''(x)=- \frac{6}{\left(x-1\right)^{4}} \\
\\end{align}
$$
Kemudian dengan menggunakan $x_0=2$ maka kita dapat menyederhanakan fungsi fungsi diatas menjadi
$$
\\begin{align}
&f(x_0) = 0\\
&f'(x_0) = 1\\
&f''(x_0) = -1\\
&f'''(x_0) = 2\\
&f''''(x_0) = -6\\
\\end{align}
$$
Deret Taylor dapat dibuat dengan cara berikut, dengan mensubstitusikan nilai diatas dan nilai $x_0$ : 

$$
\\begin{align}
&(1) = f(x_0) \Rightarrow   0\\
&(2) = \frac{(x- x\_{0})}{1!}f^{'}(x\_{0}) = (x-2)(1) \Rightarrow x-2 \\
&(3) = \frac{(x- x\_{0})^{2}}{2!}f^{''}(x\_{0}) = \frac{(x-2)^2}{2}(-1) \Rightarrow -\frac{(x-2)^2}{2}  \\
&(4) = \frac{(x- x\_{0})^{3}}{3!}f^{'''}(x\_{0}) = \frac{(x-2)^3}{6}(2) \Rightarrow \frac{(x-2)^3}{3}  \\
&(5) = \frac{(x- x\_{0})^{4}}{4!}f^{''''}(x\_{0}) =  \frac{(x-2)^4}{24}(-6) \Rightarrow -\frac{(x-2)^4}{4} \\
\\end{align}
$$
Maka Deret Taylor untuk $f(x)$ adalah (setelah membagi nilai $f$ dengan $n!$) dan mensubstitusikan $x_0$ dengan 2:
$$
0 + (x-2) - \frac{\left(x-2\right)^{2}}{2} + \frac{\left(x-2\right)^{3}}{3} - \frac{\left(x-2\right)^{4}}{4}    \tag{1.4}
$$

2. Diketahui :

a. $\ln(x-1)$
b. $f(x) = e^x-1$
Ditanya :
a. Buat Deret Taylor ordo ke 4 dimana $x_0=1$ dan cari hampiran $\ln(0.9)$
b. Buat Deret Taylor ordo ke 3 dimana $x_0=0$ dan cari hampiran $f(0.0001)$ dengan 4 angka bena
Jawab :
\>\[!note\]  
Pada nilai $x_0 =1$ maka $\ln(x)=\infty$, dan $\frac{1}{x-1} = \text{undefined}$ sehingga digunakan $x_0 = 2$

a. Berikut adalah nilai turunan dari $f(x)$
$$\begin{align}
&f(x)=\ln{\left(x-1 \right)} \\
&f'(x) = \frac{1}{x-1} \\
&f''(x) = - \frac{1}{\left(x-1\right)^{2}} \\
&f'''(x)=\frac{2}{\left(x-1\right)^{3}} \\
&f''''(x)=- \frac{6}{\left(x-1\right)^{4}} \\
\\end{align}$$
Kemudian dengan menggunakan $x_0=2$ maka kita dapat menyederhanakan fungsi fungsi diatas menjadi
$$
\\begin{align}
&f(x_0) = 0\\
&f'(x_0) = 1\\
&f''(x_0) = -1\\
&f'''(x_0) = 2\\
&f''''(x_0) = -6\\
\\end{align}
$$ 

Deret Taylor dapat dibuat dengan cara berikut, dengan mensubstitusikan nilai diatas dan nilai $x_0$ : 
$$

\\begin{align}
&(1) = f(x_0) \Rightarrow   0\\
&(2) = \frac{(x- x\_{0})}{1!}f^{'}(x\_{0}) = (x-2)(1) \Rightarrow x-2 \\
&(3) = \frac{(x- x\_{0})^{2}}{2!}f^{''}(x\_{0}) = \frac{(x-2)^2}{2}(-1) \Rightarrow -\frac{(x-2)^2}{2}  \\
&(4) = \frac{(x- x\_{0})^{3}}{3!}f^{'''}(x\_{0}) = \frac{(x-2)^3}{6}(2) \Rightarrow \frac{(x-2)^3}{3}  \\
&(5) = \frac{(x- x\_{0})^{4}}{4!}f^{''''}(x\_{0}) =  \frac{(x-2)^4}{24}(-6) \Rightarrow -\frac{(x-2)^4}{4} \\
\\end{align}
$$
Maka Deret Taylor untuk $f(x)$ adalah (setelah membagi nilai $f$ dengan $n!$) dan mensubstitusikan $x_0$ dengan 2:
$$
0 + (x-2) - \frac{\left(x-2\right)^{2}}{2} + \frac{\left(x-2\right)^{3}}{3} - \frac{\left(x-2\right)^{4}}{4}    \tag{2.1}
$$

**Nilai hampiran dari** $\ln{0.9}$ **adalah** = 

$$
\\begin{align}
&0 + (0.9-2) - \frac{\left(0.9-2\right)^{2}}{2} + \frac{\left(0.9-2\right)^{3}}{3} - \frac{\left(0.9-2\right)^{4}}{4}\\
&=0 + (-1.1) - \frac{\left(-1.1\right)^{2}}{2} + \frac{\left(-1.1\right)^{3}}{3} - \frac{\left(-1.1\right)^{4}}{4} \\
&= 0 -1.1 - (1.21)/2 + (-1.331)/3 - (1.4641)/4 \\
&=-2.5147
\\end{align}
$$
b. 
Berikut adalah nilai turunan dari $f(x) = e^x-1$ 
$$
\\begin{align} 
&f(x) =  -1 + e^{ x} \\
&f'(x) =  e^{ x} \\
&f''(x) =  e^{ x} \\
&f'''(x) =  e^{ x} \\
\\end{align}
$$
Dan nilai dari $f(x)$ pada $x=x_0$
$$
\\begin{align} 
&f(x_0) = 0 \\
&f'(x_0) = 1  \\
&f''(x_0) = 1 \\
&f'''(x_0) = 1  \\
\\end{align}
$$
$(x-x_0)$ dapat disederhanakan menjadi $x$ dengan mensubstitusikan $x_0$ dengan 0 sesuai dengan soal
Deret Taylor dapat dibuat dengan cara berikut:
$$
\\begin{align}
&(1) = f(x_0) \Rightarrow 0  \\
&(2) = \frac{(x- x\_{0})}{1!}f^{'}(x\_{0}) = x \Rightarrow x \\
&(3) = \frac{(x- x\_{0})^{2}}{2!}f^{''}(x\_{0}) = \frac{x^2}{2}(1) \Rightarrow \frac{x^2}{2} \\
&(4) = \frac{(x- x\_{0})^{3}}{3!}f^{'''}(x\_{0}) = \frac{x^3}{6}(1) \Rightarrow \frac{x^3}{6} \\
\\end{align}
$$  
Maka hasilnya adalah sebagai berikut
$$
x + \frac{x^{2}}{2} + \frac{ x^{3}}{6} \tag{2.2}
$$
**Maka Nilai hampiran dari** $f(0.0001)$ **adalah (dalam 4 angka bena)**:
Misal 0.0001 = $10^{-4}$, maka deret Taylornya menjadi berikut

$$
10^{-4} + \frac{10^{-4(2)}}{2} + \frac{10^{-4(3)}}{6}
$$
$$
10^{-4} + \frac{10^{-8}}{2} + \frac{10^{-12}}{6}
$$
Nilai tersebut memiliki hasil sekitar 0.000100005..., maka dengan 4 angka bena, akan menjadi 0.001
3. Diketahui :
$$
\\begin{cases}
&2.51x_1+1.48x_2+4.53x_3=0.05 \\
&1.48x_1+0.93x_2-1.30x_3=1.03 \\
&2.68x_1+3.04x_2-1.48x_3=-0.53 \\
\\end{cases} 
\\tag{3}
$$

Ditanya :
a. Pecahkan dengan eliminasi Gauss (manual, 3 angka bena)
b. Pecahkan dengan eliminasi Gauss dengan tata ancang pivoting (manual, 3 angka bena)
Jawab :
a.
Pertama, buat matrix augmented untuk memudahkan dalam pemrosesan eliminasi Gauss
$$
\\left\[\\begin{array}{ccc|c}2.51 & 1.48 & 4.53 & 0.05\\1.48 & 0.93 & -1.3 & 1.03\\2.68 & 3.04 & -1.48 & -0.53\end{array}\right\] \tag{3.1}
$$
Kedua, dengan menggunakan operasi baris elementer (OBE), buat matrix augmented diatas menjadi dalam bentuk *upper triangular*. Berikut adalah prosesnya
$$
\\left\[\\begin{array}{ccc|c}2.51 & 1.48 & 4.53 & 0.05\\0 & 0.057 & -3.971 & 1.001\\2.68 & 3.04 & -1.48 & -0.53\end{array}\right\] R_2 + \frac{-1.48}{2.51}R_1
$$
$$
\\left\[\\begin{array}{ccc|c}2.51 & 1.48 & 4.53 & 0.05\\0 & 0.057 & -3.971 & 1.001\\0 & 1.46 & -6.317 & -0.583\end{array}\right\] R_2 + \frac{ -2.68 }{ 2.51 }R\_{ 0 }
$$
$$
\\left\[\\begin{array}{ccc|c}2.51 & 1.48 & 4.53 & 0.05\\0 & 0.057 & -3.971 & 1.001\\0 & 0 & 94.795 & -26.059\end{array}\right\] R_2 + \frac{ -1.46 }{ 0.057 }R\_{ 1 }
$$

Ketiga, Subsititusikan nilai variabel yang ada ke dalam SPL
$$
\\begin{align}
& x\_{3} = \frac{-26.059}{94.795} = -0.275 \\
& 0.057 x\_{2} - 3.971 x\_{3} = 1.001 \\
& x\_{2} = \frac{0.091}{0.057} = -1.589 \\
& 2.51 x\_{1} + 1.48 x\_{2} + 4.53 x\_{3} = 0.05 \\
& 2.51 x\_{1} + 4.53 x\_{2} = 2.402 \\
& x\_{1} = \frac{1.453}{2.51} = 1.453 \\
&\therefore x_1, x_2,x_3 = \left\[ 1.453, \  -1.589, \  -0.275\right\] \\
\\end{align}
$$
b. Pertama, buat matrix augmented untuk memudahkan dalam pemrosesan eliminasi Gauss
$$
\\left\[\\begin{array}{ccc|c}2.51 & 1.48 & 4.53 & 0.05\\1.48 & 0.93 & -1.3 & 1.03\\2.68 & 3.04 & -1.48 & -0.53\end{array}\right\] \tag{3.2}
$$
Kedua, dengan menggunakan operasi baris elementer (OBE), buat matrix augmented diatas menjadi dalam bentuk *upper triangular*. 
\>\[!note\]
\>Pivoting berarti kita akan melakukan swap untuk meletakkan nilai koefisien terbesar pada pivot, yaitu pada diagonal (kiri atas ke bawah) dari augmented matrix

$$
\\begin{align}
& \left\[\\begin{array}{ccc|c}2.68 & 3.04 & -1.48 & -0.53\\1.48 & 0.93 & -1.3 & 1.03\\2.51 & 1.48 & 4.53 & 0.05\end{array}\right\] R\_{ 0 }\leftrightarrow R\_{ 2 }\\
& \left\[\\begin{array}{ccc|c}2.68 & 3.04 & -1.48 & -0.53\\0 & -0.749 & -0.483 & 1.323\\2.51 & 1.48 & 4.53 & 0.05\end{array}\right\] R_1 + \frac{ -1.48 }{ 2.68 }R\_{ 0 }\\
& \left\[\\begin{array}{ccc|c}2.68 & 3.04 & -1.48 & -0.53\\0 & -0.749 & -0.483 & 1.323\\0 & -1.367 & 5.916 & 0.546\end{array}\right\] R_2 + \frac{ -2.51 }{ 2.68 }R\_{ 0 }\\
& \left\[\\begin{array}{ccc|c}2.68 & 3.04 & -1.48 & -0.53\\0 & -1.367 & 5.916 & 0.546\\0 & -0.749 & -0.483 & 1.323\end{array}\right\] R\_{ 1 }\leftrightarrow R\_{ 2 }\\
& \left\[\\begin{array}{ccc|c}2.68 & 3.04 & -1.48 & -0.53\\0 & -1.367 & 5.916 & 0.546\\0 & 0 & -3.723 & 1.023\end{array}\right\] R_2 + \frac{ 0.749 }{ -1.37 }R\_{ 1 }\\
& \left\[\\begin{array}{ccc|c}2.68 & 3.04 & -1.48 & -0.53\\0 & -1.367 & 5.916 & 0.546\\0 & 0 & -3.723 & 1.023\end{array}\right\] R\_{ 2 }\leftrightarrow R\_{ 2 }\\
\\end{align}
$$
Ketiga, substitusikan nilai variabel ke SPL
$$
\\begin{align}
& x\_{3} = \frac{1.023}{-3.723} = -0.275 \\
& 1.367 x\_{2} - 5.916 x\_{3} = -0.546 \\
& x\_{2} =\frac{-2.173}{1.367} = -1.589 \\
& 2.68 x\_{1} + 3.04 x\_{2} - 1.48 x\_{3} = -0.53 \\
& 2.68 x\_{1} - 1.48 x\_{2} = 4.301 \\
& x\_{1} =\frac{3.894}{2.68} = 1.453 \\
&\therefore x_1, x_2,x_3 = \left\[ 1.453, \  -1.589, \  -0.275\right\] \\\\
\\end{align}
$$
4. Diketahui : SPL matrix $Ax = b$ dengan $A$ dan $b$ sebagai berikut
$$
A= 
\\begin{bmatrix}
1 & 2 & 3 & -1 \\
2 & 5 & 4 & 8 \\
4 & 2 & 2 & 1 \\
6 & 4 & -1 & -2\\
\\end{bmatrix}
, b= 
\\begin{bmatrix}
10 \\
8 \\
-2 \\
4
\\end{bmatrix}
\\tag{4}
$$
Ditanya :
a. Solusinya dengan eliminasi Gauss
b. Determinan dari $A$
c. Solusinya dengan eliminasi Gauss Jordan
d. Solusinya dengan invers matrix
e. Solusinya dengan dekomposisi LU
Jawab :
a. Pertama buat augmented Matrix seperti di soal ke 3 yang berupa:
$$
\\left\[
\\begin{array}{cccc|c}
1 & 2 & 3 & -1 & 10 \\
2 & 5 & 4 & 8 & 8\\
4 & 2 & 2 & 1 & -2\\
6 & 4 & -1 & -2 & 4\\
\\end{array}
\\right\]
\\tag{4.1}
$$
Kedua, lakukan eliminasi Gauss hingga tercapai row echelon form
$$
\\begin{align}
& \left\[\\begin{array}{cccc|c}1 & 2 & 3 & -1 & 10\\0 & 1 & -2 & 10 & -12\\4 & 2 & 2 & 1 & -2\\6 & 4 & -1 & -2 & 4\end{array}\right\] R_1 + \frac{ -2 }{ 1 }R\_{ 0 }\\
& \left\[\\begin{array}{cccc|c}1 & 2 & 3 & -1 & 10\\0 & 1 & -2 & 10 & -12\\0 & -6 & -10 & 5 & -42\\6 & 4 & -1 & -2 & 4\end{array}\right\] R_2 + \frac{ -4 }{ 1 }R\_{ 0 }\\
& \left\[\\begin{array}{cccc|c}1 & 2 & 3 & -1 & 10\\0 & 1 & -2 & 10 & -12\\0 & -6 & -10 & 5 & -42\\0 & -8 & -19 & 4 & -56\end{array}\right\] R_3 + \frac{ -6 }{ 1 }R\_{ 0 }\\
& \left\[\\begin{array}{cccc|c}1 & 2 & 3 & -1 & 10\\0 & 1 & -2 & 10 & -12\\0 & 0 & -22 & 65 & -114\\0 & -8 & -19 & 4 & -56\end{array}\right\] R_2 + \frac{ 6 }{ 1 }R\_{ 1 }\\
& \left\[\\begin{array}{cccc|c}1 & 2 & 3 & -1 & 10\\0 & 1 & -2 & 10 & -12\\0 & 0 & -22 & 65 & -114\\0 & 0 & -35 & 84 & -152\end{array}\right\] R_3 + \frac{ 8 }{ 1 }R\_{ 1 }\\
& \left\[\\begin{array}{cccc|c}1 & 2 & 3 & -1 & 10\\0 & 1 & -2 & 10 & -12\\0 & 0 & -22 & 65 & -114\\0 & 0 & 0 & - \frac{427}{22} & \frac{323}{11}\end{array}\right\] R_3 + \frac{ 35 }{ -22 }R\_{ 2 }\\
\\end{align}
$$
Ketiga, lakukan substitusi nilai pada SPL ke variabel variabelnya
$$\begin{align}
& a\_{3}  =- \frac{646}{427} \\
& 22 a\_{2} - 65 a\_{3} = 114 \\
& a\_{2} = \frac{304}{427} \\
& a\_{1} - 2 a\_{2} + 10 a\_{3} = -12 \\
& a\_{1} + 10 a\_{3} = - \frac{4516}{427} \\
& a\_{1} = \frac{1944}{427} \\
& a\_{0} + 2 a\_{1} + 3 a\_{2} - a\_{3} = 10 \\
& a\_{0} + 3 a\_{2} - a\_{3} = \frac{382}{427} \\
& a\_{0} - a\_{3} = - \frac{530}{427} \\
& a\_{0} = - \frac{168}{61} \\
\\end{align}
$$

Sehingga ditemukan 

$$
x = \begin{bmatrix}

* \\frac{168}{61}  \\
  \\frac{1944}{427} \\
  \\frac{304}{427} \\
* \\frac{646}{427}
  \\end{bmatrix}

$$
b. Determinan dapat ditentukan dengan mengalikan seluruh nilai diagonal pada bentuk row echelon form dari matrix $A$ yaitu
$$
\\left\[\\begin{matrix}1 & 2 & 3 & -1\\0 & 1 & -2 & 10\\0 & 0 & -22 & 65\\0 & 0 & 0 & - \frac{427}{22}\end{matrix}\right\] \tag{4.2}
$$
Nilai determinannya adalah $(1)(1)(-22)(\frac{427}{22}) = 427$ 

c. Buat augmented Matrix dari seperti pada (a)
$$
\\left\[
\\begin{array}{cccc|c}
1 & 2 & 3 & -1 & 10 \\
2 & 5 & 4 & 8 & 8\\
4 & 2 & 2 & 1 & -2\\
6 & 4 & -1 & -2 & 4\\
\\end{array}
\\right\]
$$
Lalu lakukan eliminasi Gauss Jordan ke augmented matrix tersebut
$$
\\begin{align}
& \left\[\\begin{array}{cccc|c}1 & 2 & 3 & -1 & 10\\0 & 1 & -2 & 10 & -12\\4 & 2 & 2 & 1 & -2\\6 & 4 & -1 & -2 & 4\end{array}\right\] R_1 + \frac{ -2 }{ 1 }R\_{ 0 }\\
& \left\[\\begin{array}{cccc|c}1 & 2 & 3 & -1 & 10\\0 & 1 & -2 & 10 & -12\\0 & -6 & -10 & 5 & -42\\6 & 4 & -1 & -2 & 4\end{array}\right\] R_2 + \frac{ -4 }{ 1 }R\_{ 0 }\\
& \left\[\\begin{array}{cccc|c}1 & 2 & 3 & -1 & 10\\0 & 1 & -2 & 10 & -12\\0 & -6 & -10 & 5 & -42\\0 & -8 & -19 & 4 & -56\end{array}\right\] R_3 + \frac{ -6 }{ 1 }R\_{ 0 }\\
& \left\[\\begin{array}{cccc|c}1 & 2 & 3 & -1 & 10\\0 & 1 & -2 & 10 & -12\\0 & 0 & -22 & 65 & -114\\0 & -8 & -19 & 4 & -56\end{array}\right\] R_2 + \frac{ 6 }{ 1 }R\_{ 1 }\\
& \left\[\\begin{array}{cccc|c}1 & 2 & 3 & -1 & 10\\0 & 1 & -2 & 10 & -12\\0 & 0 & -22 & 65 & -114\\0 & 0 & -35 & 84 & -152\end{array}\right\] R_3 + \frac{ 8 }{ 1 }R\_{ 1 }\\
& \left\[\\begin{array}{cccc|c}1 & 2 & 3 & -1 & 10\\0 & 1 & -2 & 10 & -12\\0 & 0 & -22 & 65 & -114\\0 & 0 & 0 & - \frac{427}{22} & \frac{323}{11}\end{array}\right\] R_3 + \frac{ 35 }{ -22 }R\_{ 2 }\\
& \left\[\\begin{array}{cccc|c}1 & 0 & 7 & -21 & 34\\0 & 1 & -2 & 10 & -12\\0 & 0 & -22 & 65 & -114\\0 & 0 & 0 & - \frac{427}{22} & \frac{323}{11}\end{array}\right\] R_0 + \frac{ -2 }{ 1 3 }R\_{ 1 }\\
& \left\[\\begin{array}{cccc|c}1 & 0 & 0 & - \frac{7}{22} & - \frac{25}{11}\\0 & 1 & -2 & 10 & -12\\0 & 0 & -22 & 65 & -114\\0 & 0 & 0 & - \frac{427}{22} & \frac{323}{11}\end{array}\right\] R_0 + \frac{ -7 }{ -22 3 }R\_{ 2 }\\
& \left\[\\begin{array}{cccc|c}1 & 0 & 0 & - \frac{7}{22} & - \frac{25}{11}\\0 & 1 & 0 & \frac{45}{11} & - \frac{18}{11}\\0 & 0 & -22 & 65 & -114\\0 & 0 & 0 & - \frac{427}{22} & \frac{323}{11}\end{array}\right\] R_1 + \frac{ 2 }{ -22 3 }R\_{ 2 }\\
& \left\[\\begin{array}{cccc|c}1 & 0 & 0 & 0 & - \frac{168}{61}\\0 & 1 & 0 & \frac{45}{11} & - \frac{18}{11}\\0 & 0 & -22 & 65 & -114\\0 & 0 & 0 & - \frac{427}{22} & \frac{323}{11}\end{array}\right\] R_0 + \frac{ 7/22 }{ -427/22 3 }R\_{ 3 }\\
& \left\[\\begin{array}{cccc|c}1 & 0 & 0 & 0 & - \frac{168}{61}\\0 & 1 & 0 & 0 & \frac{1944}{427}\\0 & 0 & -22 & 65 & -114\\0 & 0 & 0 & - \frac{427}{22} & \frac{323}{11}\end{array}\right\] R_1 + \frac{ -45/11 }{ -427/22 3 }R\_{ 3 }\\
& \left\[\\begin{array}{cccc|c}1 & 0 & 0 & 0 & - \frac{168}{61}\\0 & 1 & 0 & 0 & \frac{1944}{427}\\0 & 0 & -22 & 0 & - \frac{6688}{427}\\0 & 0 & 0 & - \frac{427}{22} & \frac{323}{11}\end{array}\right\] R_2 + \frac{ -65 }{ -427/22 3 }R\_{ 3 }\\
& \left\[\\begin{array}{cccc|c}1 & 0 & 0 & 0 & - \frac{168}{61}\\0 & 1 & 0 & 0 & \frac{1944}{427}\\0 & 0 & 1 & 0 & \frac{304}{427}\\0 & 0 & 0 & - \frac{427}{22} & \frac{323}{11}\end{array}\right\] \frac{R\_{ 2 }}{ -22 }\\
& \left\[\\begin{array}{cccc|c}1 & 0 & 0 & 0 & - \frac{168}{61}\\0 & 1 & 0 & 0 & \frac{1944}{427}\\0 & 0 & 1 & 0 & \frac{304}{427}\\0 & 0 & 0 & 1 & - \frac{646}{427}\end{array}\right\] \frac{R\_{ 3 }}{ -427/22 }\\
\\end{align}
$$
Memecah Matriks  augmented tersebut mendapatkan vektor jawaban yang diharapkan yaitu
$$
x = \begin{bmatrix}

* \\frac{168}{61}  \\
  \\frac{1944}{427} \\
  \\frac{304}{427} \\
* \\frac{646}{427}
  \\end{bmatrix}
  $$
  d. Melakukan Invers matrix memiliki prosedur mirip dengan Gauss Jordan, dengan satu perbedaan, dimana kita tidak menggabungkan suatu vektor, namun matriks identitas
  $$
  \\begin{align}
  & \left\[\\begin{array}{cccc|cccc}1 & 2 & 3 & -1 & 1 & 0 & 0 & 0\\0 & 1 & -2 & 10 & -2 & 1 & 0 & 0\\4 & 2 & 2 & 1 & 0 & 0 & 1 & 0\\6 & 4 & -1 & -2 & 0 & 0 & 0 & 1\end{array}\right\] R_1 + \frac{ -2 }{ 1 }R\_{ 0 }\\
  & \left\[\\begin{array}{cccc|cccc}1 & 2 & 3 & -1 & 1 & 0 & 0 & 0\\0 & 1 & -2 & 10 & -2 & 1 & 0 & 0\\0 & -6 & -10 & 5 & -4 & 0 & 1 & 0\\6 & 4 & -1 & -2 & 0 & 0 & 0 & 1\end{array}\right\] R_2 + \frac{ -4 }{ 1 }R\_{ 0 }\\
  & \left\[\\begin{array}{cccc|cccc}1 & 2 & 3 & -1 & 1 & 0 & 0 & 0\\0 & 1 & -2 & 10 & -2 & 1 & 0 & 0\\0 & -6 & -10 & 5 & -4 & 0 & 1 & 0\\0 & -8 & -19 & 4 & -6 & 0 & 0 & 1\end{array}\right\] R_3 + \frac{ -6 }{ 1 }R\_{ 0 }\\
  & \left\[\\begin{array}{cccc|cccc}1 & 2 & 3 & -1 & 1 & 0 & 0 & 0\\0 & 1 & -2 & 10 & -2 & 1 & 0 & 0\\0 & 0 & -22 & 65 & -16 & 6 & 1 & 0\\0 & -8 & -19 & 4 & -6 & 0 & 0 & 1\end{array}\right\] R_2 + \frac{ 6 }{ 1 }R\_{ 1 }\\
  & \left\[\\begin{array}{cccc|cccc}1 & 2 & 3 & -1 & 1 & 0 & 0 & 0\\0 & 1 & -2 & 10 & -2 & 1 & 0 & 0\\0 & 0 & -22 & 65 & -16 & 6 & 1 & 0\\0 & 0 & -35 & 84 & -22 & 8 & 0 & 1\end{array}\right\] R_3 + \frac{ 8 }{ 1 }R\_{ 1 }\\
  & \left\[\\begin{array}{cccc|cccc}1 & 2 & 3 & -1 & 1 & 0 & 0 & 0\\0 & 1 & -2 & 10 & -2 & 1 & 0 & 0\\0 & 0 & -22 & 65 & -16 & 6 & 1 & 0\\0 & 0 & 0 & - \frac{427}{22} & \frac{38}{11} & - \frac{17}{11} & - \frac{35}{22} & 1\end{array}\right\] R_3 + \frac{ 35 }{ -22 }R\_{ 2 }\\
  & \left\[\\begin{array}{cccc|cccc}1 & 0 & 7 & -21 & 5 & -2 & 0 & 0\\0 & 1 & -2 & 10 & -2 & 1 & 0 & 0\\0 & 0 & -22 & 65 & -16 & 6 & 1 & 0\\0 & 0 & 0 & - \frac{427}{22} & \frac{38}{11} & - \frac{17}{11} & - \frac{35}{22} & 1\end{array}\right\] R_0 + \frac{ -2 }{ 1 3 }R\_{ 1 }\\
  & \left\[\\begin{array}{cccc|cccc}1 & 0 & 0 & - \frac{7}{22} & - \frac{1}{11} & - \frac{1}{11} & \frac{7}{22} & 0\\0 & 1 & -2 & 10 & -2 & 1 & 0 & 0\\0 & 0 & -22 & 65 & -16 & 6 & 1 & 0\\0 & 0 & 0 & - \frac{427}{22} & \frac{38}{11} & - \frac{17}{11} & - \frac{35}{22} & 1\end{array}\right\] R_0 + \frac{ -7 }{ -22 3 }R\_{ 2 }\\
  & \left\[\\begin{array}{cccc|cccc}1 & 0 & 0 & - \frac{7}{22} & - \frac{1}{11} & - \frac{1}{11} & \frac{7}{22} & 0\\0 & 1 & 0 & \frac{45}{11} & - \frac{6}{11} & \frac{5}{11} & - \frac{1}{11} & 0\\0 & 0 & -22 & 65 & -16 & 6 & 1 & 0\\0 & 0 & 0 & - \frac{427}{22} & \frac{38}{11} & - \frac{17}{11} & - \frac{35}{22} & 1\end{array}\right\] R_1 + \frac{ 2 }{ -22 3 }R\_{ 2 }\\
  & \left\[\\begin{array}{cccc|cccc}1 & 0 & 0 & 0 & - \frac{9}{61} & - \frac{4}{61} & \frac{21}{61} & - \frac{1}{61}\\0 & 1 & 0 & \frac{45}{11} & - \frac{6}{11} & \frac{5}{11} & - \frac{1}{11} & 0\\0 & 0 & -22 & 65 & -16 & 6 & 1 & 0\\0 & 0 & 0 & - \frac{427}{22} & \frac{38}{11} & - \frac{17}{11} & - \frac{35}{22} & 1\end{array}\right\] R_0 + \frac{ 7/22 }{ -427/22 3 }R\_{ 3 }\\
  & \left\[\\begin{array}{cccc|cccc}1 & 0 & 0 & 0 & - \frac{9}{61} & - \frac{4}{61} & \frac{21}{61} & - \frac{1}{61}\\0 & 1 & 0 & 0 & \frac{78}{427} & \frac{55}{427} & - \frac{26}{61} & \frac{90}{427}\\0 & 0 & -22 & 65 & -16 & 6 & 1 & 0\\0 & 0 & 0 & - \frac{427}{22} & \frac{38}{11} & - \frac{17}{11} & - \frac{35}{22} & 1\end{array}\right\] R_1 + \frac{ -45/11 }{ -427/22 3 }R\_{ 3 }\\
  & \left\[\\begin{array}{cccc|cccc}1 & 0 & 0 & 0 & - \frac{9}{61} & - \frac{4}{61} & \frac{21}{61} & - \frac{1}{61}\\0 & 1 & 0 & 0 & \frac{78}{427} & \frac{55}{427} & - \frac{26}{61} & \frac{90}{427}\\0 & 0 & -22 & 0 & - \frac{1892}{427} & \frac{352}{427} & - \frac{264}{61} & \frac{1430}{427}\\0 & 0 & 0 & - \frac{427}{22} & \frac{38}{11} & - \frac{17}{11} & - \frac{35}{22} & 1\end{array}\right\] R_2 + \frac{ -65 }{ -427/22 3 }R\_{ 3 }\\
  & \left\[\\begin{array}{cccc|cccc}1 & 0 & 0 & 0 & - \frac{9}{61} & - \frac{4}{61} & \frac{21}{61} & - \frac{1}{61}\\0 & 1 & 0 & 0 & \frac{78}{427} & \frac{55}{427} & - \frac{26}{61} & \frac{90}{427}\\0 & 0 & 1 & 0 & \frac{86}{427} & - \frac{16}{427} & \frac{12}{61} & - \frac{65}{427}\\0 & 0 & 0 & - \frac{427}{22} & \frac{38}{11} & - \frac{17}{11} & - \frac{35}{22} & 1\end{array}\right\] \frac{R\_{ 2 }}{ -22 }\\
  & \left\[\\begin{array}{cccc|cccc}1 & 0 & 0 & 0 & - \frac{9}{61} & - \frac{4}{61} & \frac{21}{61} & - \frac{1}{61}\\0 & 1 & 0 & 0 & \frac{78}{427} & \frac{55}{427} & - \frac{26}{61} & \frac{90}{427}\\0 & 0 & 1 & 0 & \frac{86}{427} & - \frac{16}{427} & \frac{12}{61} & - \frac{65}{427}\\0 & 0 & 0 & 1 & - \frac{76}{427} & \frac{34}{427} & \frac{5}{61} & - \frac{22}{427}\end{array}\right\] \frac{R\_{ 3 }}{ -427/22 }\\
  \\end{align}
  $$

Dan hasil Invers matrixnya adalah 

# $$
\\left\[\\begin{matrix}- \frac{9}{61} & - \frac{4}{61} & \frac{21}{61} & - \frac{1}{61}\\\frac{78}{427} & \frac{55}{427} & - \frac{26}{61} & \frac{90}{427}\\\frac{86}{427} & - \frac{16}{427} & \frac{12}{61} & - \frac{65}{427}\\- \frac{76}{427} & \frac{34}{427} & \frac{5}{61} & - \frac{22}{427}\end{matrix}\right\]
$$
Hasil perkalian dari $A^{-1}b$ akan menjadi $x$ 
$$
\\left\[\\begin{matrix}- \frac{9}{61} & - \frac{4}{61} & \frac{21}{61} & - \frac{1}{61}\\\frac{78}{427} & \frac{55}{427} & - \frac{26}{61} & \frac{90}{427}\\\frac{86}{427} & - \frac{16}{427} & \frac{12}{61} & - \frac{65}{427}\\- \frac{76}{427} & \frac{34}{427} & \frac{5}{61} & - \frac{22}{427}\end{matrix}\right\]
\\begin{bmatrix}
10 \\
8 \\
-2 \\
4
\\end{bmatrix}

\\begin{bmatrix}

* \\frac{168}{61}  \\
  \\frac{1944}{427} \\
  \\frac{304}{427} \\
* \\frac{646}{427}
  \\end{bmatrix}
  $$

d. Mendekomposisi $A$ menjadi $L$ dan $U$ dapat dilakukan dengan dengan cara Eliminasi Gaussian yang dimodifikasi

$U$ adalah bentuk row echelon form dari matrix $A$, sehingga caranya merupakan berikut
Pertama buat augmented Matrix seperti di soal ke 3 yang berupa:
$$
\\left\[
\\begin{array}{cccc|c}
1 & 2 & 3 & -1 & 10 \\
2 & 5 & 4 & 8 & 8\\
4 & 2 & 2 & 1 & -2\\
6 & 4 & -1 & -2 & 4\\
\\end{array}
\\tag{A}
\\right\]
$$
Kedua, lakukan eliminasi Gauss hingga tercapai row echelon form
$$
\\begin{align}
& \left\[\\begin{array}{cccc|c}1 & 2 & 3 & -1 & 10\\0 & 1 & -2 & 10 & -12\\4 & 2 & 2 & 1 & -2\\6 & 4 & -1 & -2 & 4\end{array}\right\] R_1 + \frac{ -2 }{ 1 }R\_{ 0 }\\
& \left\[\\begin{array}{cccc|c}1 & 2 & 3 & -1 & 10\\0 & 1 & -2 & 10 & -12\\0 & -6 & -10 & 5 & -42\\6 & 4 & -1 & -2 & 4\end{array}\right\] R_2 + \frac{ -4 }{ 1 }R\_{ 0 }\\
& \left\[\\begin{array}{cccc|c}1 & 2 & 3 & -1 & 10\\0 & 1 & -2 & 10 & -12\\0 & -6 & -10 & 5 & -42\\0 & -8 & -19 & 4 & -56\end{array}\right\] R_3 + \frac{ -6 }{ 1 }R\_{ 0 } \tag{B}\\
& \left\[\\begin{array}{cccc|c}1 & 2 & 3 & -1 & 10\\0 & 1 & -2 & 10 & -12\\0 & 0 & -22 & 65 & -114\\0 & -8 & -19 & 4 & -56\end{array}\right\] R_2 + \frac{ 6 }{ 1 }R\_{ 1 }\\
& \left\[\\begin{array}{cccc|c}1 & 2 & 3 & -1 & 10\\0 & 1 & -2 & 10 & -12\\0 & 0 & -22 & 65 & -114\\0 & 0 & -35 & 84 & -152\end{array}\right\] R_3 + \frac{ 8 }{ 1 }R\_{ 1 }  \tag{C} \\
& \left\[\\begin{array}{cccc|c}1 & 2 & 3 & -1 & 10\\0 & 1 & -2 & 10 & -12\\0 & 0 & -22 & 65 & -114\\0 & 0 & 0 & - \frac{427}{22} & \frac{323}{11}\end{array}\right\] R_3 + \frac{ 35 }{ -22 }R\_{ 2 }\\
\\end{align}
$$
Bentuk Row Echelon Form, atau Matrix $U$ adalah berikut 
$$
U =  \left\[\\begin{matrix}1 & 2 & 3 & -1\\0 & 1 & -2 & 10\\0 & 0 & -22 & 65\\0 & 0 & 0 & - \frac{427}{22}\end{matrix}\right\]
$$
Untuk menentukan $L$ dapat dilakukan dengan langkah-langkah berikut :
Pertama, buat matriks identitas dengan ukuran yang sama dengan $U$
$$
\\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\\end{bmatrix}
$$
Kemudian untuk menentukan nilai 0 yang ada dibawah angka 1, maka perhatikan matriks $(A),(B)$ dan $(C)$ pada proses menentukan matriks $U$ dengan eliminasi Gaussian
$$
\\left\[
\\begin{array}{cccc|c}
1 & 2 & 3 & -1 & 10 \\
2 & 5 & 4 & 8 & 8\\
4 & 2 & 2 & 1 & -2\\
6 & 4 & -1 & -2 & 4\\
\\end{array}
\\tag{A}
\\right\]
$$
Kita cukup ambil nilai yang ada dibawah dari nilai pivot yang dikotakkan (nilai diagonal)
$$
L =
\\begin{bmatrix}
1 & 0 & 0 & 0 \\
2 & 1 & 0 & 0 \\
4 & 0 & 1 & 0 \\
6 & 0 & 0 & 1 \\
\\end{bmatrix}
$$
Langkah berikutnya adalah lanjutkan proses eliminasi Gaussian sampai mencapai Matrix $(B)$
$$
\\left\[\\begin{matrix}1 & 2 & 3 & -1 & 10\\0 & \framebox{1} & -2 & 10 & -12\\0 & -6 & -10 & 5 & -42\\0 & -8 & -19 & 4 & -56\end{matrix}\right\] \tag{B}
$$
Tampak bahwa nilai pivot kembali lagi 1, maka kita kembali ambil nilai yang dibawah pivot untuk menjadi nilai $L$, sehingga
$$
L =
\\begin{bmatrix}
1 & 0 & 0 & 0 \\
2 & 1 & 0 & 0 \\
4 & -6 & 1 & 0 \\
6 & -8 & 0 & 1 \\
\\end{bmatrix}
$$
Kembali lakukan langkah yang sama, hingga mencapai Matrix $(C)$.
$$
\\left\[\\begin{matrix}1 & 2 & 3 & -1 & 10\\0 & 1 & -2 & 10 & -12\\0 & 0 & \framebox{-22} & 65 & -114\\0 & 0 & -35 & 84 & -152\end{matrix}\right\] \tag{C} 
$$
Tampak kali ini nilai pivot bukanlah 1. Tenang saja, karena untuk menentukan nilai pada kolom $L$ cukup **bagi nilai dibawah pivot dengan nilai pivot**

Sehingga Matrix $L$ menjadi berikut
$$
L =
\\begin{bmatrix}
1 & 0 & 0 & 0 \\
2 & 1 & 0 & 0 \\
4 & -6 & 1 & 0 \\
6 & -8 & \frac{35}{22} & 1 \\
\\end{bmatrix}
$$

Kemudian untuk menentukan nilai $x$ kita perlu menggunakan langkah berikut
$$
\\begin{align}
&Ax = b\\
&LUx = b\\
&\text{misal } Ux = y \\
&\text{selesaikan } Ly = b\\
&\text{dan selesaikan juga } Ux = y\\
\\end{align}
$$
Maka kita akan mendapat nilai dari $x$. Langkah-langkahnya untuk $Ly =b$ adalah :
$$
\\begin{align}
& a\_{0} = 10 \\
& a\_{1} = -12 \\
& 6 a\_{1} - a\_{2} = 42 \\
& a\_{2} = -114 \\
& - 176 a\_{1} + 35 a\_{2} + 22 a\_{3} = -1232 \\
& 35 a\_{2} + 22 a\_{3} = -3344 \\
& a\_{3} = \frac{323}{11} \\
\\end{align}
$$
Dan langkah-langkahnya untuk $Ux = y$ adalah :
$$
\\begin{align}
& a\_{3} = - \frac{646}{427} \\
& 22 a\_{2} - 65 a\_{3} = 114 \\
& a\_{2} = \frac{304}{427} \\
& a\_{1} - 2 a\_{2} + 10 a\_{3} = -12 \\
& a\_{1} + 10 a\_{3} = - \frac{4516}{427} \\
& a\_{1} = \frac{1944}{427} \\
& a\_{0} + 2 a\_{1} + 3 a\_{2} - a\_{3} = 10 \\
& a\_{0} + 3 a\_{2} - a\_{3} = \frac{382}{427} \\
& a\_{0} - a\_{3} = - \frac{530}{427} \\
& a\_{0} = - \frac{168}{61} \\
\\end{align}
$$
Sehingga ditemukan 
$$
x = \begin{bmatrix}

* \\frac{168}{61}  \\
  \\frac{1944}{427} \\
  \\frac{304}{427} \\
* \\frac{646}{427}
  \\end{bmatrix}

$$
