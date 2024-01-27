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
Bentuk ini juga memiliki rumus akhir sama dengan [Persamaan (2.6)](PERT%202.md#orde-konvergensi)

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
