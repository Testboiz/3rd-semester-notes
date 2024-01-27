# PERT 7 - Persamaan Differensial Biasa

## Persamaan Differensial Biasa Orde Satu

Misal $y = f(x)$, dan $y' = f'(x) = \frac{df}{dx}$, maka Persamaan differensial biasa orde satu adalah sebuah persamaan yang memiliki paling tidak 1 suku $y'$ 

Contoh 

* $y' = x^2$
* $y'^2 - 2y' +1=0$ 
* $y' + x^2y - y^2 = 0$

Persamaan differensial biasa orde ke $n$ adalah persamaan differensial biasa yang memiliki turunan tertinggi dari $y$ ke $n$

Pada kenyataannya, metode numerik merupakan satu satunya cara untuk menemukan solusi dari mayoritas persamaan numerik. 

## Metode Euler

Kita akan memisalkan hal hal berikut

$$
\\begin{align}
& \frac{dy}{dt} = f(x,y) \tag{7.1.1} \\
& y(t_0) = y_0 \tag{7.1.2} \\
& x_r = x_0 + rh,;; r = 0,1,\cdots,n \tag{7.1.3} \\
\\end{align}
$$
Dengan nilai $h$ diset secara menual, berdasarkan kebutuhan presisi yang diinginkan, kita dapat mengetahui nilai dari persamaan differensial tersebut pada 1 titik, yaitu

$$
y(x\_{r+1}) = y(x_r) + hf(x_r,y_r)) \tag{7.2}
$$
Penurunan rumus tersebut tersedia [disini](https://tutorial.math.lamar.edu/classes/de/eulersmethod.aspx)

## Metode Heun

Metode Heun adalah metode Euler yang ditingkatkan. Berdasarkan referensi dalam link [diatas](https://tutorial.math.lamar.edu/classes/de/eulersmethod.aspx), Metode Euler kesulitan dalam memperkirakan nilai fungsi differensial yang memiliki perubahan yang besar, dan akurasinya menurun seiring jarak fungsi meningkat

Metode Euler digunakan sebagai Predictor, sedangkan Metode Heun digunakan sebagai corrector.

Metode Heun memiliki rumus berikut
$$
y(x\_{r+1}) = y_r + \frac{h}{2}\left( f(x_r,y_r)+f(x\_{r+1},y\_{r+1}) \right) \tag{7.3}
$$
Menggunakan 2 titik interpolasi meningkatkan akurasi dari Metode Euler yang menggunakan 1 titik saja. Lihat grafiknya [disini](http://calculuslab.deltacollege.edu/ODE/7-C-2/7-C-2-h.html)

## Metode Deret Taylor

Mengingat [ Deret Taylor](PERT%201.md#deret-taylor) pada Persamaan $(1.3)$, kita dapat merubah persamaan tersebut dengan mengubah $(x-x_0)$ menjadi $h$, dan kita dapat menghitung hampiran dari persamaan differensial tersebut

$$
f(x) \approx \sum\_{i=0}^{n}\frac{f^{(i)}(x\_{0})h^{i}}{i!} \tag{7.4}
$$
Fungsi tersebut dapat disederhanakan menjadi 
$$
\\begin{align}
& y^{(k)} = P^{(k-1)}f(x,y) \tag{7.5.1} \\
& P = \left(\frac{\partial}{\partial x} + f \frac{\partial}{\partial y} \right) \tag{7.5.2} \\
\\end{align}
$$
dimana $\frac{\partial}{\partial x}$ adalah turunan fungsi $f(x,y)$ dan menganggap $y$ sebagai variabel konstan, dan sebaliknya

Komputasikan iterasi berikutnya dengan menghitung nilai deret taylornya

## Metode Runge - Kutta

Metode Runge - Kutta merupakan metode yang menghitung nilai dari persamaan differensial biasa berdasarkan 4 titik gradien yaitu

1. $k_1$ adalah gradien di awal interval (Metode Euler)
1. $k_2$ adalah gradien diantara median dengan awal interval
1. $k_3$ adalah gradien di median interval
1. $k_4$ adalah gradien di akhir interval

Rumus Gradiennya adalah
$$
\\begin{align}
& k_1 = f(t_n,y_n)\tag{7.6.1} \\
& k_2 = f(t_n + \frac{h}{2}, y_n + \frac{hk_1}{2}) \tag{7.6.2} \\
& k_3 = f(t_n + \frac{h}{2}, y_n + \frac{hk_2}{2}) \tag{7.6.3} \\
& k_4 = f(t_n + h, y_n + hk_3) \tag{7.6.4} \\
\\end{align}
$$
dan nilai $y\_{r+1}$ adalah
$$
y\_{r+1} = y_r + \frac16(k_1+2k_2+2k_3+k_4) \tag{7.7}
$$

## Metode Banyak Langkah

Metode ini menghitung berdasarkan algoritma sebelumnya, namun secara rekursif, selain itu juga menggunakan predictor dan corrector seperti di [Metode Heun](PERT%207.md#metode-heun), yaitu

predictor : Metode Banyak Langkah rekursif
corrector : Memperbaiki nilai dari predictor
