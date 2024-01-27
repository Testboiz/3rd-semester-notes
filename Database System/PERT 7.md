# PERT 7

# `JOIN`

`JOIN` adalah cara untuk melink tabel yang sudah dipecah setelah [normalisasi](PERT%207.md#normalisasi) menggunakan `PRIMARY KEY` dan `FOREIGN KEY` yang ada

Contoh Kueri

````sql
SELECT t1.col1,t1,col2,...,t2.col1,t2.col2,...
FROM first_table_name AS t1
[type] JOIN second_table_name AS t2 
ON t1.PRIMARY_KEY_COLUMN = t2.FOREIGN_KEY_COLUMN
;
````

Kita dapat menggambarkan `JOIN` sebagai berikut

Misal $A$ adalah himpunan yang mewakili `first_table_name` dam $B$ adalah himpunan yang mewakili `second_table_name`

Maka `JOIN` dapat digambarkan secara teori himpunan sebagai berikut

* `LEFT JOIN` $= A$ 
* `RIGHT JOIN` $= B$ 
* `INNER JOIN` $= A\cap B$
* `FULL OUTER JOIN` $= A \cup B$
* `LEFT JOIN EXCLUDING INNER JOIN` $A \cup B^c$
* `RIGHT JOIN EXCLUDING INNER JOIN` $A^c \cup B$
* `OUTER JOIN EXCLUDING INNER JOIN` $A^c \cup B^c = (A \cap B)^c$ (De Morgan) 
  Untuk `EXCLUDING INNER JOIN` kueri diatas dapat dimodifikasi menjadi berikut

````sql
SELECT t1.col1,t1,col2,...,t2.col1,t2.col2,...
FROM first_table_name AS t1
[type] JOIN second_table_name AS t2 
ON t1.PRIMARY_KEY_COLUMN = t2.FOREIGN_KEY_COLUMN
WHERE t1.FOREIGN_KEY_COLUMN = NULL --untuk LEFT JOIN EXCLUDING INNER JOIN
--atau
[
WHERE t2.FOREIGN_KEY_COLUMN = NULL --untuk RIGHT JOIN EXCLUDING INNER JOIN
]
--atau
[
--untuk OUTER JOIN EXCLUDING INNER JOIN
WHERE t1.FOREIGN_KEY_COLUMN = NULL OR t2.FOREIGN_KEY_COLUMN = NULL
]
;
````

$$
A = \text{LEFT JOIN}
$$

````tikz
\begin{document}
\begin{tikzpicture}
\scope % A \cap B
\fill[red] (0,0) circle (1);
\endscope
% outline
\draw (0,0) circle (1)
      (1,0) circle (1);
\end{tikzpicture}
\end{document}
````

$$B = \text{RIGHT JOIN}$$

````tikz
\begin{document}
\begin{tikzpicture}
\scope % A \cap B
\fill[red] (1,0) circle (1);
\endscope
% outline
\draw (0,0) circle (1)
      (1,0) circle (1);
\end{tikzpicture}
\end{document}
````

$$
A\cap B = \text{INNER JOIN}
$$

````tikz
\begin{document}
\begin{tikzpicture}
\scope % A \cap B
\clip (0,0) circle (1);
\fill[red] (1,0) circle (1);
\endscope
% outline
\draw (0,0) circle (1)
      (1,0) circle (1);
\end{tikzpicture}
\end{document}
````

$$
A \cup B^c = \text{LEFT JOIN EXCLUDING INNER JOIN}
$$

````tikz
\begin{document}
\begin{tikzpicture}
\scope
\clip (-2,-2) rectangle (2,2)
      (1,0) circle (1);
\fill[red] (0,0) circle (1);
\endscope
% outline
\draw (0,0) circle (1)
      (1,0) circle (1);
\end{tikzpicture}
\end{document}
````

$$
A^c \cup B = \text{RIGHT JOIN EXCLUDING INNER JOIN}
$$

````tikz
\begin{document}
\begin{tikzpicture}
\scope
\clip (-2,-2) rectangle (2,2)
      (0,0) circle (1);
\fill[red] (1,0) circle (1);
\endscope
% outline
\draw (0,0) circle (1)
      (1,0) circle (1);
\end{tikzpicture}
\end{document}
````

$$
A^c \cup B^c = (A \cap B)^c = \text{OUTER JOIN EXCLUDING INNER JOIN}
$$

````tikz
\begin{document}
\begin{tikzpicture}
\scope
\clip (-2,-2) rectangle (2,2)
      (1,0) circle (1);
\fill[red] (0,0) circle (1);
\endscope
\scope
\clip (-2,-2) rectangle (2,2)
      (0,0) circle (1);
\fill[red] (1,0) circle (1);
\endscope
% outline
\draw (0,0) circle (1)
      (1,0) circle (1);
\end{tikzpicture}
\end{document}
````

 > 
 > \[!note\]
 > Konteks terhadap notasi teori himpunan
 > Lingkaran kiri adalah semua baris pada `first_table_name`, dengan `FOREIGN KEY` yang terisi atau `NULL`
 > Lingkaran kanan adalah semua baris pada `second_table_name`, dengan `FOREIGN KEY` yang terisi atau `NULL`
 > Irisan kedua lingkaran tersebut adalah semua baris pada `first_table_name` **dan** `second_table_name` dimana masing-masing baris memiliki `FOREIGN KEY` yang bukan `NULL`
 > Bagian lingkaran yang diluar irisan adalah baris-baris pada `first_table_name` maupun `second_table_name` dimana `FOREIGN KEY`nya `NULL`

Diagram Chen membedakan partisipasi penuh dan partisipasi parsial

Kita dapat menggambarkan partisipasi penuh keduanya, salah satu parsial dan parsial keduanya seperti berikut

* Partisipasi parsial keduanya

````tikz
\begin{document}
\begin{tikzpicture}
% outline
\draw (0,0) circle (1)
      (1,0) circle (1);
\end{tikzpicture}
\end{document}
````

* Partisipasi full sebagian

````tikz
\begin{document}
\begin{tikzpicture}
\scope % A \cap B
\endscope
% outline
\draw (1,0) circle (1)
      (1,0) circle (2);
\end{tikzpicture}
\end{document}
````

* Partisipasi penuh keduanya

````tikz
\begin{document}
\begin{tikzpicture}
% outline
\draw (0,0) circle (1);
\end{tikzpicture}
\end{document}
````

# `UNION`

Menggabungkan beberapa tabel satu dengan tabel lain yang memiliki jumlah kolom sama (ditaruh dibawah)

Contoh kueri

````sql
SELECT col_name
FROM table_name
UNION
SELECT another_col_name
FROM another_table_name
;
````
