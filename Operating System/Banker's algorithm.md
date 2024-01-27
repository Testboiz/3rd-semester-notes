Diketahui : 
Available = {3,3,2} dan total resource = {10,5,7}

|Allocated|A|B|C|
|---------|-|-|-|
|P0|0|1|0|
|P1|2|0|0|
|P2|3|0|2|
|P3|2|1|1|
|P4|0|0|2|
|dan||||

|Max|A|B|C|
|---|-|-|-|
|P0|7|5|4|
|P1|3|2|2|
|P2|9|0|2|
|P3|2|2|2|
|P4|4|3|3|
|||||
|Ditanya :||||
|Apakah terjadi Deadlock atau tidak||||
|Jika tidak tunjukkan safe statenya||||

Jawab :
Kita dapat anggap Allocated dan Max sebagai sebuah Matriks

$$
A =
\\begin{pmatrix}
0 &1 &0\\
2 &0 &0\\
3 &0 &2\\
2 &1 &1\\
0 &0 &2\\
\\end{pmatrix}
, M =
\\begin{pmatrix}
7 &5 &4\\
3 &2 &2\\
9 &0 &2\\
2 &2 &2\\
4 &3 &3\\
\\end{pmatrix}
$$
Need Matrix kita dapat anggap sebagai $N = M - A$

Need Matrix kita menjadi
$$
N = \begin{pmatrix}
7 &4 &4\\
1 &2 &2\\
6 &0 &0\\
0 &1 &1\\
4 &3 &1\\
\\end{pmatrix}
$$
Kita misalkan sebuah vektor namanya adalah $W$, dimana $W = Available$ = {3,3,2}

Lalu kita melakukan looping 

Iterasi pertama

Baris pertama dari Matrix Need (P0) kita bandingkan dengan $W$ 
$$
\\begin{pmatrix}
7\\
4\\
4
\\end{pmatrix}
\\nless
\\begin{pmatrix}
3\\
3\\
2
\\end{pmatrix}
$$
Jadi kita tidak dapat menjalankan P0, karena kebutuhan P0 lebih besar daripada ketersediaan resource

Iterasi kedua

Baris kedua dari Matrix Need (P1) kita bandingkan dengan $W$ 
$$
\\begin{pmatrix}
1\\
2\\
2
\\end{pmatrix}
\\lt
\\begin{pmatrix}
3\\
3\\
2
\\end{pmatrix}
$$
Karena kebutuhan P1 lebih kecil daripada $W$ maka kita dapat mengerjakannya

Lalu $W$ kita update dengan baris kedua dari $A$ yaitu
$$
\\begin{pmatrix}
2\\
0\\
0
\\end{pmatrix}

* 

# \\begin{pmatrix}
3\\
3\\
2
\\end{pmatrix}

\\begin{pmatrix}
5\\
3\\
2
\\end{pmatrix}
$$
Iterasi Ketiga

Baris ketiga dari Matrix Need (P2) kita bandingkan dengan $W$ 
$$
\\begin{pmatrix}
6\\
0\\
0
\\end{pmatrix}
\\nless
\\begin{pmatrix}
5\\
3\\
2
\\end{pmatrix}
$$
Jadi kita tidak dapat menjalankan P2, karena kebutuhan P3 lebih besar daripada ketersediaan resource

Iterasi keempat

Baris keempat dari Matrix Need (P3) kita bandingkan dengan $W$ 
$$
\\begin{pmatrix}
0\\
1\\
1
\\end{pmatrix}
\\lt
\\begin{pmatrix}
5\\
3\\
2
\\end{pmatrix}
$$
Karena kebutuhan P3 lebih kecil daripada $W$ maka kita dapat mengerjakannya

Lalu $W$ kita update dengan baris keempat dari $A$ yaitu
$$
\\begin{pmatrix}
2\\
1\\
1
\\end{pmatrix}

* 

# \\begin{pmatrix}
5\\
3\\
2
\\end{pmatrix}

\\begin{pmatrix}
7\\
4\\
3
\\end{pmatrix}
$$

Iterasi kelima

Baris kelima dari Matrix Need (P4) kita bandingkan dengan $W$ 
$$
\\begin{pmatrix}
4\\
3\\
1
\\end{pmatrix}
\\lt
\\begin{pmatrix}
7\\
4\\
3
\\end{pmatrix}
$$
Karena kebutuhan P4 lebih kecil daripada $W$ maka kita dapat mengerjakannya
Lalu $W$ kita update dengan baris kelima dari $A$ yaitu
$$
\\begin{pmatrix}
0\\
0\\
2
\\end{pmatrix}

* 

# \\begin{pmatrix}
7\\
4\\
3
\\end{pmatrix}

\\begin{pmatrix}
7\\
4\\
5
\\end{pmatrix}
$$

Iterasi keenam 

Baris pertama dari Matrix Need (P0) kita bandingkan dengan $W$ 
$$
\\begin{pmatrix}
7\\
4\\
5
\\end{pmatrix}
\\lt
\\begin{pmatrix}
6\\
6\\
7
\\end{pmatrix}
$$
Karena kebutuhan P0 lebih besar daripada $W$ maka kita tidak dapat mengerjakannya

Iterasi ketujuh
Baris ketiga dari Matrix Need (P2) kita bandingkan dengan $W$ 
$$

\\begin{pmatrix}
6\\
0\\
2
\\end{pmatrix}
\\lt
\\begin{pmatrix}
7\\
4\\
5
\\end{pmatrix}
$$
Lalu $W$ kita update dengan baris ketiga dari $A$ yaitu
$$
\\begin{pmatrix}
3\\
0\\
2
\\end{pmatrix}

* 

# \\begin{pmatrix}
7\\
4\\
5
\\end{pmatrix}

\\begin{pmatrix}
10\\
5\\
7
\\end{pmatrix}
$$
