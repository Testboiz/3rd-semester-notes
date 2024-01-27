# Amdhal law

$S(N)$ adalah speedup yang didapat dari menambahkan jumlah core
$$
S(N) = \frac{1}{T-\frac{1-T}{N}}
$$
dimana $T$ adalah fraksi waktu yang dapat proses secara serial oleh banyak CPU. Dan $N$ adalah jumlah core CPU

Misal kasus dimana 25% dari proses dapat dijalankan secara serial dalam CPU Dual Core
$$
\\begin{align}
\\frac{1}{\frac{1}{4} + \frac{1-\frac{1}{4}}{2}}\\
\\frac{1}{\frac{1}{4} + \frac{\frac{3}{4}}{2}}\\
\\frac{1}{\frac{1}{4} + \frac{3}{8}}\\
\\frac{1}{\frac{5}{8}}\\
\\frac{8}{5} = 1.6
\\end{align}
$$

Ketika $N \rightarrow \infty$ maka 

$$
\\lim\_{N\rightarrow\infty} \frac{1}{T-\frac{1-T}{N}} = \frac{1}{T-\frac{1-T}{\infty}} = \frac{1}{T-(1-T)(0)}= \frac{1}{T}
$$
