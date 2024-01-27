# PERT 4

# Interpolasi

## Interpolasi Polinom

Diberikan suatu fungsi yang akan kita perkirakan yaitu $f(x)$, kita membuat suatu polinom dengan menggunakan sebuah himpunan dari $n+1$ titik yang berbentuk $(x_i,f(x_i))$ dimana $0\leq i \leq n+1$. Polinom yang dibuat dari himpunan titik tersebut akan mengaproksimasi dari fungsi $f(x)$ tersebut

 > 
 > \[!note\]
 > Interpolasi adalah dimana suatu nilai diperkirakan dengan fungsi lain, sedangkan ekstrapolasi adalah nilai yang direpresentasikan oleh fungsi yang melakukan interpolasi

## Interpolasi Linier

Interpolasi ini adalah bentuk khusus dari [Interpolasi Polinom](PERT%204-2.md#interpolasi-polinom) dimana $n = 1$ , dan membuat sebuah fungsi linier umum $p_1(x) = a_0+a_1x$. Kita dapat membayangkan fungsi ini sebagai fungsi generik yang menghasilkan sistem persamaan fungsi lainnya.

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

Hampir sama dengan [Interpolasi Linier](PERT%204-2.md#interpolasi-linier) kecuali $n = 2$ sehingga $p_2(x) = a_0+a_1x + a_2x^2$, sehingga dapat dibuat SPLTV berikut:
$$
\\begin{cases}
y_0 = a_0 + a_1x_0 + a_2x_0^2\\
y_1 = a_0 + a_1x_1 + a_2x_1^2\\
y_2 = a_0 + a_1x_2 + a_2x_2^2
\\end{cases}
$$
Selesaikan dengan substitusi eliminasi, Gauss Jordan, Gauss, LU, dsb

## Interpolasi Kubik

Hampir sama dengan [Interpolasi Linier](PERT%204-2.md#interpolasi-linier) kecuali $n = 3$ sehingga $p_3(x) = a_0+a_1x + a_2x^2 + a_3x^3$, sehingga dapat dibuat SPL berikut:
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
