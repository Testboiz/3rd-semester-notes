# PERT 5 - JAVASCRIPT

Javascript adalah bahasa pemograman yang digunakan untuk memanage data dalam bentuk DOM. Javascript digunakan untuk scripting logika dari webpage HTML agar dapat interaktif. Javascript membutuhkan runtime environment untuk menampilkan hasil pada javascript dengan menggunakan browser, Node, Express, dsb

Dalam HTML. Javascript dapat digunakan dengan 3 cara yaitu

1. Inline, dengan menggunakan attribut seperti `onclick`, `onload`,dsb. Contohnya adalah `<button onclick="doSomething();"> CLICK ME </button>`. Umumnya hanya untuk pemanggilan fungsi sederhana
1. Internal, untuk script sederhana

````html
<script> 
//insert JS Code
</script>
````

3. Eksternal (tidak terlihat kode pada Inspect Element), untuk script kompleks

````html
<script src="path/to/script.js"></script>
<!-- atau dengan CDN (link web) -->
<script src="http://cdn.scriptsource.com"></script>
````

Tips-tips JS

1. Gunakan Inspect Element -> Console untuk mendebug JS
1. JS memiliki sintaks mirip C++
1. JS tidak mewajibkan statement untuk diakhiri dengan `;`, namun sangat disarankan untuk menghindari bug
1. JS menggunakan `var`,`let`,dan `const` untuk mendeklarasi variabel. Perbedaannya adalah `var` untuk variabel, `let` dan `const` untuk konstanta dengan scoping yang berbeda. `let` memiliki scope pada blok yang memiliki `{}`, sedangkan `const` memiliki scope pada `function` atau global
1. Event, selain dengan menggunakan `elementVariableName.addEventListener()`, juga dapat menggunakan attribut `attr="//JS Code here"` dalam HTML. Attribut event memiliki awalan `on`
1. `new` juga dapat digunakan untuk menginisialisasi array (selain `[]`), objek JS (selain `{}`), dan banyak tipedata non primitif lainnya
1. Tidak ada error untuk mengakses array dengan indeks tak terdefinisi.
1. Objek di Javascript sering didefinisikan tanpa menggunakan kelas. Sintaksnya dinamakan JSON, dan dapat menampung variabel primitif, objek dan bahkan fungsi. sintaks JSON dan objek Javascript mirip dengan sintaks `dict` di Python
1. Gunakan delete untuk menghapus variabel (mirip dengan `del` di Python dan `free()` di C dan juga `~Constructor()` di C++)
1. JSON tidak memiliki fungsi didalamnya, JSON merupakan bentuk teks yang merupakan sintaks valid untuk objek JS
1. Objek JSON digunakan untuk memproses string JSON, dengan `JSON.stringify(obj)` untuk mendapatkan string JSON, dan `JSON.parse(str)` untuk menghasilkan objek dari string JSON
1. AJAX digunakan untuk melakukan `GET`,`POST`,dsb tanpa reload.
1. ECMA adalah bentuk standar Javascript yang sudah tersedia pada browser. Mirip dengan standar ANSI C. Fitur-fitur khusus ECMA seperti `set`,`get`,dan objek `JSON`
1. JQuery merupakan sejenis library Javascript yang sering digunakan pada website. JQuery perlu diload dengan tag `<script src="js/jquery-script-name.js"></script>` di `<head>`
1. JQuery menggunakan selektor dengan sintaks selektor CSS untuk melakukan fungsi yang sama dengan member dari object `document`. Sintaknya adalah `$(*)`, `$(selector)`, dan `$(selector1,selector2,...,selectorN)`
1. Plugin JQuery dapat digunakan untuk memudahkan programmer web untuk menambahkan fungsionalitas suatu elemen pada HTML. Sintaksnya adalah

````js
$(function(){
  $('#idname').pluginName();
});
//atau
$(()=>$('#idname').pluginName());
````
