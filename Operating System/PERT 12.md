# PERT 12 - Security & Protection

## The Security Problem

 > 
 > Info. Security adalah ketahanan sistem terhadap ancaman yang bersifat tak terduga maupun malisius

Contoh serangan yang paling umum adalah

* Malware
* DDOS
* Phising
* Session Hijacking
* Authentication Breach

4 Layer ini harus dilindungi dari serangan 

* Hardware
* Brainware
* OS
* Network (Cyber Security)

*Security Is as weak as the weakest chain*

Adapun kehilangan data dapat disebabkan oleh berikut

* Bencana
* Masalah hardware / software
* Human error

Aspek keamanan sistem adalah

* Kerahasiaan
* Integritas
* Ketersediaan

## Program Threats

Intruder adalah pihak yang menghasilkan threat. Intruder dapat berasal dari keisengan, snooping, hecker, spionase, dll

Ada 4 jenis serangan siber yaitu :

* Interupsi adalah pemblokiran akses ke service melalui DDOS maupun pengrusakan hardware
* Intersepsi adalah pihak yang mengalihkan otentikasi ke sistem lain (phising, authorization breach, dll)
* Fabrikasi adalah menggunakan data palsu untuk mendapat akses
* Modification (mengubah nilai data dari user yang telah terotentikasi)

Contoh serangan secara umum adalah 

* Penyalahgunaan system call dan memori
* Login dengan injeksi spesial karakter
* Hacking sistem
* Social engineering

Malware dapat dipecah menjadi berikut

* Trojan Horse (penyalahgunaan fasilitas framework)
* Trap Door (security breach dalam compiled code)
* Logic Bomb (Infinite loop, resource hogging, dsb)
* Stack/Buffer Overflow (bug exploit yang membuat crash dan DDOS)
* Virus (code injection)

Virus memiliki berbagai struktur, dapat menyerang OS, memori,penyimpanan, dan bahkan boot sector. Virus dapat memiliki taktik tertentu untuk tidak terdeteksi antivirus

Serangan ini dapat menimbulkan kerusakan secara data dan bahkan kerusakan hardware dan sabotase

Antivirus mendeteksi dan mengidentifikasi virus, kemudian menghilangkan virus dengan assembler

Prinsip pengamanan komputer merupakan berikut

* Rancangan terbuka
* Auth Checking
* Just In Time Auth
* Privillige terbatas
* Proteksi sederhana, uniform dan built in
* Mekanisme Ekonomis
* Nyaman digunakan

BIBA menjamin integritas data dengan membatasi penulisan data dengan tingkat keamanan rendah, dan pembacaan objek yang memiliki tingkat keamanan tinggi. 

## System and Network Threats

Malware yang bersebar melalui jaringan komputer adalah sebagai berikut

* Blackmail
* Worm (Virus yang dapat menyebar melalui network)
* Port Scanning (mencari port yang tersedia)
* DDOS (Server overload yang menyebabkan Denial of Service)

## Cryptography as a Security Tool

Kriptografi adalah standar yang digunakan oleh internet untuk mengamankan data

Kriptografi menggunakan key, yang membatasi siapa yang mampu mengerti apa data yang diberikan

### Algoritma Enkripsi

Tiap algoritma memiliki hal hal berikut

* ${K}$ key
* ${M}$ pesan
* ${C}$ cipher
* Fungsi $E(K,M) \rightarrow C$ yang mengenskripsi pesan menjadi cipher (encryptor)
* Fungsi $D(K,C) \rightarrow M$ yang mendekripsikan cipher menjadi pesan (decryptor)

Sifat dari algoritma enkripsi adalah 

* Cipher tidak memiliki pola yang dapat di reverse enggineer
* Decryptor harus mampu mengencrypt juga

Contoh algoritma Enkripsi adalah

* Enkripsi simetris (key untuk enkripsi dan dekripsi sama) Contoh : DES,AES,RC4
* Enkripsi asimetris (ada public key untuk enkripsi dan private key untuk dekripsi) Contoh : RSA yang menggunakan prime factorization dari $pq$ dimana $p$ dan $q$ adalah bilangan prima besar. Dengan memiliki encryptor-pun tetap tidak dapat mengkonstruksi decryptor

Enkripsi asimetris sangat intensif dalam komputasi, sehingga hanya digunakan untuk data tertentu 

Kunci Enkripsi simetris mudah ditrace, kunci asimetris juga dapat ditrace menggunakan man in middle attack

### Otentikasi

Algoritma otentikasi sesungguhnya mirip dengan enkripsi, dengan cipher merupakan otentikator dalam otentikasi

Ada juga fungsi yang menghasilkan otentikasi dan juga fungsi verifikator yang memverifikasikan pesan

Mirip dengan encryptor dan decryptor, setiap otentikasi harus mampu memiliki fungsi verifikator agar dapat memverifikasi pesan

Fungsi otentikator tidak boleh memiliki pola fungsi verifikator

Fungsi hash digunakan untuk menghasilkan fungsi otentikator dan verifikator. Hash colision nharus diperhatikan. Hash value menandakan kesamaan dari sebuah data. Secara ideal, setiap data memiliki korespondensi 1 1 dengan hash

Adapun pendekatin lainnya adalah

* MAC (Message Authentication Code)
* Digital Signature 
* RSA Digital Signature

Otentikasi lebih sederhana daripada enkripsi, sehingga untuk data yang tidak memiliki kebutuhan security tinggi, maka dapat menggunakan otentikasi

Contoh otentikasi klasik adalah username password. Adapun contoh lainnya adalah OAuth dan biometrik.

Pembatasan dari otentikasi dapat berupa berikut

* Pembatasan waktu login
* Pembatasan jumlah login
* Simple login
* DB login

### Digital Certificates

Merupakan bukti kepemilikan public key, yang memastikan keamanan data

## Implementing Security Defenses

* Menggunakan lapisan keamanan pada tiap layer (OS,Hardware,User,Network)
* Intrusion Detection (signature based detection, anomaly detection)
* Antivirus
* Audit, accounting, logging
* Firewall

Firewall dapat memblokir akses koneksi yang tak terpecaya, firewall dapat memblokir situs situs yang dianggap berbahaya maupun berdampak buruk ke user. Contoh Internet Positif 

## Principles of Protection

Ada 4 level proteksi menurut U.S. Departement of Defense

* A menggunakan formal design dan teknik verifikasi
* B Auditing dan dengan memperhatikan sensitifitas data
* C Auditing
* D Minimal Security
