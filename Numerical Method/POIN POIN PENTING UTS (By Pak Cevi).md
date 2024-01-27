## Gauss Jordan

Soal 

$$
\\begin{cases}
2x+3y-z = 10\\
4x-2y+5z=5\\
x+2y+3z+15
\\end{cases}
$$
Ditanya :
Nilai $(x,y,z)$ 
Jawab:

$$
\\begin{align}
\\left\[\\begin{array}{ccc|c}2 & 3 & -1 & 10\\4 & -2 & 5 & 5\\1 & 2 & 3 & 15\end{array}\right\]
\\rightarrow
& \left\[\\begin{array}{ccc|c}2 & 3 & -1 & 10\\0 & -8 & 7 & -15\\1 & 2 & 3 & 15\end{array}\right\] R_1 + \frac{ -4.00 }{ 2.00 }R\_{ 0 }\\  
& \left\[\\begin{array}{ccc|c}2 & 3 & -1 & 10\\0 & -8 & 7 & -15\\0 & \frac{1}{2} & \frac{7}{2} & 10\end{array}\right\] R_2 + \frac{ -1.00 }{ 2.00 }R\_{ 0 }\\
& \left\[\\begin{array}{ccc|c}2 & 3 & -1 & 10\\0 & -8 & 7 & -15\\0 & 0 & \frac{63}{16} & \frac{145}{16}\end{array}\right\] R_2 + \frac{ -0.500 }{ -8.00 }R\_{ 1 }\\
& \left\[\\begin{array}{ccc|c}2 & 0 & \frac{13}{8} & \frac{35}{8}\\0 & -8 & 7 & -15\\0 & 0 & \frac{63}{16} & \frac{145}{16}\end{array}\right\] R_0 + \frac{ -3 }{ -8 3 }R\_{ 1 }\\
& \left\[\\begin{array}{ccc|c}2 & 0 & 0 & \frac{40}{63}\\0 & -8 & 7 & -15\\0 & 0 & \frac{63}{16} & \frac{145}{16}\end{array}\right\] R_0 + \frac{ -13/8 }{ 63/16 3 }R\_{ 2 }\\
& \left\[\\begin{array}{ccc|c}2 & 0 & 0 & \frac{40}{63}\\0 & -8 & 0 & - \frac{280}{9}\\0 & 0 & \frac{63}{16} & \frac{145}{16}\end{array}\right\] R_1 + \frac{ -7 }{ 63/16 3 }R\_{ 2 }\\
& \left\[\\begin{array}{ccc|c}1 & 0 & 0 & \frac{20}{63}\\0 & -8 & 0 & - \frac{280}{9}\\0 & 0 & \frac{63}{16} & \frac{145}{16}\end{array}\right\] \frac{R\_{ 0 }}{ 2 }\\
& \left\[\\begin{array}{ccc|c}1 & 0 & 0 & \frac{20}{63}\\0 & 1 & 0 & \frac{35}{9}\\0 & 0 & \frac{63}{16} & \frac{145}{16}\end{array}\right\] \frac{R\_{ 1 }}{ -8 }\\
& \left\[\\begin{array}{ccc|c}1 & 0 & 0 & \frac{20}{63}\\0 & 1 & 0 & \frac{35}{9}\\0 & 0 & 1 & \frac{145}{63}\end{array}\right\] \frac{R\_{ 2 }}{ 63/16 }\\
\\end{align}
$$

## Interpolasi Linear

Dik :
$\ln(2)$ = 0.6931 dan $\ln(8)$ = 2.0794 
Dit :
$\ln(6)$ dengan interpolasi linier
Jawab :
Kita dapat membayangkan suatu interpolasi dengan membuat sebuah persamaan garis lurus dengan menggunakan persamaan berikut

$$
\\frac{y-y_0}{y_1-y_0} = \frac{x-x_0}{x_1-x_0} 
$$
Lalu pindah ruas dan menjadi berikut
$$
\\frac{y-y_0}{y_1-y_0} - \frac{x-x_0}{x_1-x_0} = 0
$$
Kalikan dengan $(y_1-y_0)$ sehingga menjadi berikut
$$
y-y_0 - \frac{(x-x_0)(y_1-y_0)}{(x_1-x_0)} = 0
$$
Dengan memindahkan hampir semua bagian persamaan, kecuali $y$ kita telah membuat fungsi dalam bentuk $y=f(x)$ yang berupa
$$
y = y_0 + \frac{(x-x_0)(y_1-y_0)}{(x_1-x_0)}
$$
Disini $f(x)$ akan memodelkan $\ln(x)$ maka $f(x)\approx\ln(x)$ sehingga $y = \ln(x)$ 
Maka kita tinggal substitusikan $x = 6$. Sedangkan
$$
\\begin{align}
y_0 = 0.691 && x_0 = 2\\
y_1 = 2.0794 && x_1 = 8
\\end{align}
$$
Sehingga setelah kita mensubstitusikannya ke persamaan (kalkulator) maka didapat hasil
$$
\\ln(6) \approx 1.612
$$

## Regresi Linear

Dik :

|Hari|Volume Perdagangan $(x)$|Harga Saham $(y)$|
|----|------------------------|-----------------|
|1|25|100|
|2|30|110|
|3|40|130|
|4|35|115|
|5|50|150|
|6|45|140|
|7|60|175|
|8|55|160|
|9|70|200|
|10|65|190|
|11|80|240|
|12|75|220|
|13|90|270|
|14|85|250|
|15|100|300|
|16|95|280|
|17|110|330|
|18|105|310|
|19|120|360|
|20|115|340|

Dit : 
a. Model regresi linier sederhana
b. Persamaan Regresi Linier
c. Prediksi harga saham dengan volume perdagangan 125 ribu lembar saham
d. Hitung R squared

a. Model Regresi Linier Sederhana
$\hat{Y} = a+bx$ 
b. Persamaan Regresi Linier
$$
a = \frac{(\sum(y)-b(\sum(x))}{n}
$$
$$
b = \frac{n(\sum((xy)) - (\sum(x)\sum(y)))}{n(\sum(x^2)) - (\sum(x)^2)} 
$$
Pertama buat tabel untuk mengtrack nilai dari **jumlah** $x,y,xy,x^2,y^2$ 

|n|$x$|$y$|$x^2$|$y^2$|$xy$|
|-|---|---|-----|-----|----|
|1|25|100|625|10000|2500|
|2|30|110|900|12100|3300|
|3|40|130|1600|16900|5200|
|4|35|115|1225|13225|4025|
|5|50|150|2500|22500|7500|
|6|45|140|2025|19600|6300|
|7|60|175|3600|30625|10500|
|8|55|160|3025|25600|8800|
|9|70|200|4900|40000|14000|
|10|65|190|4225|36100|12350|
|11|80|240|6400|57600|19200|
|12|75|220|5625|48400|16500|
|13|90|270|8100|72900|24300|
|14|85|250|7225|62500|21250|
|15|100|300|10000|90000|30000|
|16|95|380|9025|144400|36100|
|17|110|330|12100|108900|36300|
|18|105|310|11025|96100|32550|
|19|120|360|14400|129600|43200|
|20|115|340|13225|115600|39100|

Kemudian jumlahnya adalah

|n|$\sum x$|$\sum y$|$\sum x^2$|$\sum y^2$|$\sum xy$|
|-|--------|--------|----------|----------|---------|
|20|1450|4470|121750|1152650|372975|

Setelah dikalkulasikan dengan kalkulator didapat

$a$ = 10,252  dan $b$ = 2,941

$$
a = \frac{\sum(y)-b(\sum(x)}{n}
$$
$$
b = \frac{n\sum(xy) - \sum(x)\sum(y)}{n\sum(x^2) - \sum(x)^2} 
$$

Sehingga persamaan regresinya adalah
$$
\\hat{Y} = 10.252 + 2.941x
$$
c. Memprediksikan harga saham dengan volume perdagangan 125 ribu saham dapat dilakukan dengan mensubsitusikan 125 ke persamaan diatas dan menghitung $\hat{Y}$

$$
\\hat{Y} = 10.252 + 2.941(125)
$$
$$
\\hat{Y} = 377.877
$$
d. Menghitung R squared sangat mirip dengan menghitung koefisien $b$ dalam regresi. 
$$
\\text{R squared} = \frac{n(\sum((xy)) - (\sum(x)\sum(y)))}{\sqrt{n(\sum(x^2)) - (\sum(x)^2)}}.\frac{1}{\sqrt{n(\sum(y^2)) - (\sum(y)^2)}} 
$$
Jika kalian lihat, suku kiri sama saja dengan $b$, hanya saja penyebutnya diakarkan. Dan juga suku di kanan hampir sama dengan penyebut di suku kiri. Hanya saja menggunakan jumlah untuk $y$ 

Hitung hasil R squared dengan kalkulator

## Deret Taylor

Dik : 
$$
f(x) = 2 - \frac{1}{e^x}
$$
Dit :
Buat deret taylor derajat ke 2 dan gunakan metode Newton Raphson untuk mencari akar dari deret taylor tersebut
Gunakan $x_0 = 0$ dan error  $10^{-3}$  
Jawab :
%%
monmaap cursed
%%
Pertama kita lihat bagaimana bentuk Deret Taylor derajat ke2 seperti apa

$$
\\text{taylor-derajat-dua}(x) = f(x_0) + \frac{(x- x\_{0})}{1!}f^{'}(x\_{0}) + \frac{(x- x\_{0})^{2}}{2!}f^{''}(x\_{0}) 
$$

Tampak kita perlu menurunkan fungsi tersebut sebanyak 2 kali
$$
\\begin{align}
f(x) = 2-e^{-x}\\
f'(x) = e^{-x}\\
f''(x) = -e^{-x}
\\end{align}
$$

Lalu kita substitusikan $x = x_0 = 0$ pada fungsi tersebut

$$
\\begin{align}
f(x_0) = 2-e^{0} = 1\\
f'(x_0) = e^{0} = 1\\
f''(x_0) = -e^{0} = -1
\\end{align}
$$

Kini kita dapat mensubstitusikan fungsi diatas ke $\text{taylor-derajat-dua}(x)$ 

$$
1 + \frac{(x- x\_{0})}{1!} - \frac{(x- x\_{0})^{2}}{2!}
$$

Kemudian $(x-x_0) = (x-0) = x$ 
Maka $\text{taylor-derajat-dua}(x)$ menjadi

$$
1+\frac{x}{1!} - \frac{x^2}{2!}
$$

Sederhanakan faktorialnya dan pecahannya

$$
1 + \frac{x}{1} - \frac{x^2}{2\*1}
$$

Menjadi

$$
1+x-\frac{x^2}{2}
$$

Kemudian kita persiapkan Metode Newton Raphson

$$
x\_{t+1} = x\_{t} - \frac{f(x)}{f'(x)}
$$

dimana $f(x) = \text{taylor-derajat-dua}(x)$
Turunan dari $\text{taylor-derajat-dua}(x)$ adalah

$$
\\begin{align}
&=(1+x-\frac{x^2}{2})'\\
&=1'+x'-(\frac{x^2}{2})'\\
&=0 + 1 - 2\*\\frac{x^{2-1}}{2}\\
&=1-x
\\end{align}
$$

Maka bentuk Newton Raphsonnya adalah

$$
x\_{t+1} = x_t - \frac{1+x_t-\frac{x_t^2}{2}}{1-x_t}
$$

Kemudian tinggal iterasikan sampai errornya sesuai standar

|$t$|$x_t$|
|---|-----|
|0|0|
|1|-1|
|2|-0.75|
|3|-0.7321428571|
|4|-0.73205081|
|5|-0.7320508076|

Lalu kita tentukan perambatan errornya

$$
e\_{ra} = |\frac{x\_{i+1}-x_i}{x\_{i+1}}|
$$

Tampak pada iterasi ke 4, digit ke 3 yang menandakan $10^{-3}$ sudah tidak berubah
Maka jawabannya adalah -0.732

|$t$|$x_t$|$e\_{ra}$|
|---|-----|--------|
|0|0||
|1|-1|1|
|2|-0.75|0.3333333333|
|3|-0.7321428571|0.02439024396|
|4|-0.73205081|0.0001257386765|
|5|-0.7320508076|0.000000003278461089|

## Bisection

Dik : Sebuah fungsi $f(x) = x^2-x-200$ memiliki akar $x=5$ dengan bisection sebanyak 4 iterasi dengan selang $\[4,n\]$ dengan error sebesar 0.0001
Dit : 
Tentukan Nilai $n$
Jawab : 
Setelah diverifikasi dengan [Desmos](https://www.desmos.com/calculator/9gnmcuvova) Tampak akar dari fungsi tersebut bukan 5

Namun secara logikal, kita tidak perlu memerhatikan fungsi dan errornya, yang paling penting adalah sesungguhnya membayangkan algoritma tersebut secara terbalik

Kondisi awal
![diagram-20231101.png](..\Software%20Engineering\diagram-20231101.png)
Iterasi ke 4
![diagram-20231101(1).png](..\Software%20Engineering\diagram-20231101%281%29.png)
Iterasi ke 3
![diagram-20231101(2).png](..\Software%20Engineering\diagram-20231101%282%29.png)
Iterasi ke 2
![diagram-20231101(3).png](..\Software%20Engineering\diagram-20231101%283%29.png)
Iterasi ke 1
![diagram-20231101(4).png](..\Software%20Engineering\diagram-20231101%284%29.png)
Tampak nilai $n$ adalah 20
