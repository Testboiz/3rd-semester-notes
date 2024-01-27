# PERT 3

# Pemodelan Sistem

## Model Konteks

 > 
 > \[! abstract\] Definisi
 > Yaitu hubungan akan beberapa sistem otomatis lainnya

Sistem Eksternal menggunakan input maupun output dari sistem, secara fisik terintegrasi secara hardware atau tidak. Hal ini perlu diperhatikan

Model konteks didesain untuk dapat berinteraksi dengan model lainnya

$\Huge \bullet$  merupakan START dan END dari suatu model konteks
$\square$ menandakan kegiatan yang dilakukan, dan berisi objek
$\rightarrow$ menandakan aliran kerja dari kegiatan satu dan kegiatan lainnya
Jika $\rightarrow$ mengarah ke $\framebox{;}$ maka aktifitas ini harus diselesaikan sebelum dilanjutkan
Jika aliran tersebut mengarah ke sejumlah aktifitas, maka dapat dilakukan secara bersamaan
$\Rightarrow$ menandakan bahwa aliran baru dapat dilakukan setelah selesainya proses
\[$\rightarrow$\] dapat menggambarkan kapan aliran diikuti

Context Diagram menggambarkan interaksi antar sistem
DFD level 1,2,3... akan menggambarkan bagaimana data akan diproses secara semakin detil
![DFD Level 0.png](DFD%20Level%200.png)
![Pasted image 20231025103822.png](Pasted%20image%2020231025103822.png)

## Model Interaksi

 > 
 > \[!abstract\] Definisi
 > Adalah suatu model yang menggambarkan interaksi antar komponen komponen (sistem, aktor dan database) dalam hal seperti gambaran bagaimana sistem dapat digunakan, dan bagaimana sistem bekerja

Hal yang dapat dimodelkan dalam interaksi ini adalah interaksi antar pengguna, interaksi antar sistem, dan interaksi antar mekanisme dalam sistem

Model Interaksi berupa Use Case Diagram dan Diagram Sekuensial

## Use Case Diagram

Use case dapat dimodelkan dalam bentuk 
$$\enclose{circle}{\text{use case}}$$
Aktor dapat dimodelkan dengan bentuk *stickman*

Aktor dapat berupa manusia, sistem maupun database. Diagram ini dapat digambarkan lebih spesifik sesuai kegunaan.

 > 
 > \[!note\]
 > Jangan menggunakan $\rightarrow$ di Use Case diagram, karena dalam UML  karena  simbol tersebut memiliki makna aliran pesan (data)

Gambaran Use Case Diagram harus diperkaya dengan penjelasan dalam  bentuk tabel, deskripsi maupun diagram lainnya yang mendukung

Diagram Use Case komposit adalah diagram Use Case yang digunakan untuk menggambarkan berbagai aktor dalam suatu sistem. Walau demikian desain ini tidak direkomendasikan, karena akan membuat diagram terlalu sulit untuk dimengerti

Gambaran Umum Use Case Diagram
![Use Case 1.png](Use%20Case%201.png)
![Use Case 2.png](Use%20Case%202.png)

### Sequence Diagram

**Sequence Diagram adalah penggambaran interaksi antar objek**
![Pasted image 20231025100452.png](Pasted%20image%2020231025100452.png)

Sequence Diagram menggambarkan hal yang terjadi *didalam* sistem tiap kasus use case. Hal yang terjadi dapat berupa function call, object creation, procedure, dll. 

Objek dan aktor berada di paling atas diagram, dengan entitasnya digambarkan dengan garis putus-putus

$\rightarrow$ menandakan interaksi antar objek
$\framebox\[10\]{;}$ menandakan lifetime dari objek tersebut, pada saat proses apa sajakah objek tersebut dibutuhkan
$\framebox{;;;;;;alt}$  menandakan bagian yang bersifat alternatif dengan menggunakan $\dashrightarrow$

Interaksi dalam diagram tidak perlu disertakan secara penuh, jika digunakan untuk gambaran high level ke pengguna. Lagipula banyak interaksi yang akan ditentukan pada saat implementasi

Activity Diagram adalah gambaran cara kerja sistem secara umum  
![Activity Diagram.png](Activity%20Diagram.png)

## Model Struktural

 > 
 > \[!abstract\] Definisi
 > Yaitu model yang menggambarkan desain suatu sistem pada saat runtime atau compile-time Model ini menggunakan Class Diagram pada UML

### Class Diagram

Class diagram adalah model suatu kelas OOP yang bersifat **language agnostic** yang berarti model ini berlaku untuk semua bahasa OOP

````uml
|--------------|
| ClassName    |
|--------------|
| attr1        |
| attr2        |
| attr3        |
| ...          |
|--------------|
| Meth1        |
| Meth2        |
| Meth3        |
| ...          |
|--------------|
````

Contoh Kode dalam Java

````java
public class className{
	int attr1;
	char attr2;
	double attr3
	//and more
	public void Meth1(){};
	public void Meth2(){};
	public void Meth3(){};
	//and more
}
````

#### Generalisasi

Digunakan untuk memodelkan Inheritance dengan tanda panah mengarah ke parent class
Contoh UML

````uml
|-----|
|Hewan|
|-----|
   ^
   |
   |
|-----|
|Kucing|
|-----|
````

Contoh Kode dalam Java :

````java
//Parent Class
public class Hewan {
    void makan(){
        System.out.println("nyam nyam");
    }
}
//Child Class
class Kucing extends Hewan {
    @Override
    void makan(){
        System.out.println("nyam nyam miaw");
    }
}
````

#### Aggregation

Aggregation adalah kasus dimana suatu kelas dapat memiliki 1 atau lebih dari kelas lainnya

Aggregation menggunakan notasi kardinalitas yaitu

* `1..1` yaitu 1 kelas memiliki 1 kelas yang terikat Contoh (WNI dan KTP)
* `1..*` yaitu 1 kelas memiliki banyak kelas yang terikat Contoh (Siswa dengan Kelas)
* `*..*` yaitu banyak kelas terikat dengan banyak kelas lain Contoh (Siswa dengan Eskul) 

````uml
|-----|
|ShelterKucing|
|-----|
   <> 1..*
   |
   |
|-----|
|Kucing|
|-----|
````

````java
public class ShelterKucing {
    Kucing[] meong;
}
````

![Pasted image 20231025101439.png](Pasted%20image%2020231025101439.png)

## Model Perilaku

 > 
 > \[!abstract\] Definisi
 > Merupakan gambaran sistem secara runtime

Model perilaku memodelkan kasus seperti kegiatan pemrosesan data. Dapat dimodelkan dalam Aggregation, Data Driven Modelling, Event Driven Modelling, dan Model Driven Engineering.

### Aggregation

Memodelkan dengan gambaran aksi yang dilakukan dengan data dari input sampai output.
Untuk sistem real time, gambaran aksi yang dilakukan adalah berdasarkan peristiwa, bukan pemrosesan data

### Data Driven Modelling

 > 
 > \[!abstract\] Definisi
 > Menggambarkan urutan interaksi data dalam sistem dari fase input hingga output

Pemodelan ini digunakan pada perangkat lunak grafis pertama. Model ini memudahkan dokumentasi terhadap fase fase yang terjadi pada suatu sistem, dan juga pemahaman pada pihak pihak lainnya yang belum tentu mengerti kode program, termasuk klien.

Objek direpresentasikan dengan $\framebox{seperti ini}$ 
Sedangkan Aktivitas direpresentasikan dengan $(\overline{\underline{\text{seperti ini}}})$

![Data Driven Modelling.png](Data%20Driven%20Modelling.png)

Secara alternatif, dapat menggunakan diagram sekuensial langsung dari UML. Metode ini tidak direkomendasikan karena lebih bersifat preferensi

### Event Driven Modelling

 > 
 > \[!abstract\] Definisi
 > Memodelkan sistem dalam bentuk respons terhadap suatu event. Diasumsikan bahwa sistem adalah suatu Finite State Machine

 > 
 > \[!note\]
 > Finite State Machine dapat digambarkan sebagai suatu Mode dalam suatu perabot listrik

UML mendukung pemodelan ini dengan State Diagram. State Diagram hanya fokus terhadap aliran informasi yang disalurkan pada tiap State

State digambarkan dengan $(\overline{\underline{\text{seperti ini}}})$ dan diberikan deskripsi
$\underset{\text{trigger}}{\rightarrow}$    menandakan pemicu State yang berupa $\text{trigger}$ 

Superstate adalah gabungan state yang dapat bekerja menjadi suatu state.

State diagram juga harus dirincikan lebih dalam menggunakan tabel

### Model Driven Engineering

Pendekatan ini digunakan dimana model yang dihasilkan dari suatu pengembangan. Model akan menghasilkan perangkat lunak secara langsung. Metode ini membuat software engineer tidak perlu lagi untuk membuat program untuk menghasilkan perangkat lunak.

## Rekayasa Model Driven

Ada 3 model sistem abstrak yang harus diproduksi yaitu :

1. **CIM (Computational Independent Model)** yang juga disebut **model domain**. 
1. **PIM (Platform Independent Model)**, yaitu model yang tidak terpengaruhi dengan platform. Contoh : Java dan Python
1. **PSM (Platform Specific Module)**, yaitu model yang dapat menambahkan detil khusus platform dalam model PIM. Contoh : GCC  dan JVM. 

MDA (Model Driven Architecture) adalah pandangan bahwa software dapat menghasilkan program yang spesifik. Contohnya adalah program no code, dan Virtual Machine Intrepreter untuk beberapa bahasa pemograman seperti Python dan Java
